"""
hedoria.py — compile Hedoria AI instructions between markdown and JSON.

The MD source uses `@@@ section.key` markers at the start of a line. Everything
between one marker and the next is raw markdown — that becomes the value for
that key in the JSON. HTML comments are stripped on build, so you can leave
editorial notes in the MD file.

Usage:
  python3 hedoria.py build      # MD -> JSON
  python3 hedoria.py extract    # JSON -> MD (use to bootstrap or re-sync)
"""

import argparse
import json
import re
import sys
from pathlib import Path

MARKER_RE = re.compile(r"^@@@\s+(.+)$", re.MULTILINE)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def compile_md_to_json(md_path: Path, json_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    text = HTML_COMMENT_RE.sub("", text)

    # Find all marker positions
    markers = list(MARKER_RE.finditer(text))
    if not markers:
        raise SystemExit(f"No @@@ markers found in {md_path}")

    instructions: dict = {}

    for i, m in enumerate(markers):
        path = m.group(1).strip()
        content_start = m.end()
        content_end = markers[i + 1].start() if i + 1 < len(markers) else len(text)
        content = text[content_start:content_end].strip()

        parts = path.split(".", 1)
        if len(parts) != 2:
            print(f"Warning: skipping invalid path '{path}' (expected 'section.key')")
            continue
        section, key = parts
        instructions.setdefault(section, {})[key] = content

    result = {"aiInstructions": instructions}
    json_path.write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    # Validate by re-parsing
    json.loads(json_path.read_text(encoding="utf-8"))
    return result


def extract_json_to_md(json_path: Path, md_path: Path) -> None:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    instructions = data["aiInstructions"]

    lines = [
        "<!--",
        "Hedoria AI instructions — source file.",
        "",
        "Edit the content between @@@ markers, then run:",
        "    python3 hedoria.py build",
        "to compile to hedoria_ai_instructions.json.",
        "",
        "Each marker line is `@@@ section.key`. Content runs until the next marker.",
        "HTML comments (like this one) are stripped during compilation, so feel free",
        "to leave editorial notes wherever they help.",
        "-->",
        "",
    ]

    for section, fields in instructions.items():
        lines.append(f"<!-- ===== {section} ===== -->")
        lines.append("")
        for key, value in fields.items():
            lines.append(f"@@@ {section}.{key}")
            lines.append("")
            lines.append(value if value else "")
            lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("build", help="Compile MD to JSON")
    b.add_argument("--md", default="hedoria_ai_instructions.md")
    b.add_argument("--json", default="hedoria_ai_instructions.json")

    e = sub.add_parser("extract", help="Extract MD from JSON")
    e.add_argument("--json", default="hedoria_ai_instructions.json")
    e.add_argument("--md", default="hedoria_ai_instructions.md")

    args = parser.parse_args()

    if args.cmd == "build":
        result = compile_md_to_json(Path(args.md), Path(args.json))
        sections = list(result["aiInstructions"].keys())
        print(f"Compiled {args.md} -> {args.json}")
        print(f"Sections ({len(sections)}):")
        for s in sections:
            n = len(result["aiInstructions"][s])
            print(f"  {s}: {n} field(s)")
    elif args.cmd == "extract":
        extract_json_to_md(Path(args.json), Path(args.md))
        print(f"Extracted {args.json} -> {args.md}")


if __name__ == "__main__":
    main()