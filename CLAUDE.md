# Hedoria

A fantasy worldbuilding project. The world is called Hedoria; the game/setting is called Voyage.

## Repo files

- `full_def.json` — full system/game definition
- `ludion_format_and_inspiration.json` — An external project that we can get schema and inspiration from.
- `canon` dir contains established elements of the world
- `candidates` dir contains suggestions and not yet accepted content
- `build` dir contains built combined files

## Schema

- `ludion_format_and_inspiration.json` is the **validated** schema source. Always consult it for the correct field names and shape before writing any canon-bound content. There is no validation harness, so schema discipline matters.
- Existing files in `canon/` are also reliable references — they've already been adapted to Hedoria — but ludion is the source of truth when in doubt.

## Candidate workflow

All new or revised content goes through `candidates/`:

1. **Never write to `canon/` directly.** Write to `candidates/` only.
2. **Candidate files mirror canon block shape.** Top-level keys are canon block names (`npcTypes`, `npcs`, `factions`, etc.). Multiple blocks in one file is fine — the file is just a change batch.
3. **Updates and additions are the same operation.** Both are entries keyed by name; the merger overwrites or inserts by key. Don't invent wrapper keys like `npcTypeUpdates`.
4. **No invented fields.** Every field on every entry must exist in the ludion schema. No `_comment`, no ad-hoc metadata. If you need to leave a note for the reviewer, put it in your reply, not in the file.
5. **Block → canon file** is resolved by `canon/_map.json`. Most blocks have one home. Two blocks split across files (see `_split` in the map):
   - `npcTypes`: race/profession types → `npcTypes.json`; creatures (beasts, trolls, demonic remnants, magical beasts, greater monsters) → `bestiary.json`.
   - `worldLore`: general lore → `worldLore.json`; creature-lore prose → `bestiary.json`.
6. **Filenames in `candidates/`** are freeform — files get reviewed, merged into canon, and deleted, so naming is just for human readability.

## Build

`build/full_def.json` is the merged output of all canon files. It's generated; don't edit it directly.

## Google Drive source documents

All lore lives in Google Drive. The canonical folder is **Hedoria** (id: `1877tORqPaxTRAj9uGHgfj358FAVz_AUV`). Use the Google Drive MCP tool to read any of these by file ID.

### World overview & history

| Document         | Drive file ID                                  |
| ---------------- | ---------------------------------------------- |
| worldDescription | `1JqXc5FX92A3mbJ9FmaWSHbfHwsJWP95kbEZY_sDzaQM` |
| Ensoulment       | `1tfZWe34SvOnrcGZQrJp5y0gfndUJZWVNj6pNob8yQ08` |
| Wartide          | `1OAs9jPvvslR900uuP3D4vQZRDxS20DPqJW-padqph-w` |
| The next Wartide | `1N5ulwRy89FFPkbdIGaBR6hoA02d4hW8OYK5E2kbQvY0` |
| Magic            | `1R3fCR9DCQMO6SYlpiPZ7tIdZPfMNa1-7CAbys5VvIeA` |

### Races

| Document         | Drive file ID                                  |
| ---------------- | ---------------------------------------------- |
| races (overview) | `1woJMIjkhiOTjBaRQYzdYZUBYFy4FOD4jVoSgEILzzs0` |
| Humans           | `1NsfconIh78Am9JRPF9LDqrJElf08AtTlA0FSxvjHdmM` |
| Threshi          | `1CqjR2Q44MmDqloP5mxtH9nEWlVeLVBsIHKrWLpuYMAw` |
| Hofnar           | `1T1jHjVeNy1_GUewZJ38OBy51sso2cGDxDxTG3_A63JQ` |
| Cephalen         | `1YvEvtya5lK9XUW_lpKdxWUPFwIOZGJlswtx2wJxl64A` |
| Draklid          | `1CbUk_oZ9a26iOmTyPELiuhAgb4iJLczis6mspoJ-0xI` |
| Primes           | `1QCXIluzsHggfbWAYXSG20R7pQco2o-CzCfwuUfsUfNQ` |
| Raknid           | `190YQ_uQaMEf1LNXKQYZVUHtIts_RrfMBuGXtGRlKvno` |
| Vorok            | `11XNeKy9dq1ms1GG7a7Kzx8s_N7LVSKfHWoeElUQHISs` |
| Fernwarg         | `1fpFoc5bZH1HCgDrya7a2cwWPsap3e3FQDIguWj2FjTI` |
| Quelled          | `1caPgrMMmDQlXNe7JZZiMLNuJF_Y6T-DSb8jURHkO7As` |

### Geography & locations

| Document                                    | Drive file ID                                  |
| ------------------------------------------- | ---------------------------------------------- |
| hedoria_regions (continent map & locations) | `1uBfR5ggWuVDbD5ObTJfVgKxw56FmBHqC8_ncpDxUpOs` |
| Avenor (city-state detail)                  | `1-rDOlTek3GWZSONzZ6GvPJQsMCMPZy-wNLHYeMeyO5I` |

### Bestiary & classes

| Document                              | Drive file ID                                  |
| ------------------------------------- | ---------------------------------------------- |
| hedoria_bestiary (all creature tiers) | `1jwrHU3om4LhhswlnqkAJKF2XWhcjq8qOGP67Rvz2mbI` |
| Quell Sorcerer (character class)      | `1x2lZnaXYZATA7eG6XrBaiidS9ze3ARAvmolfSJA02Bk` |

## How to read a document

```
mcp__claude_ai_Google_Drive__read_file_content(file_id: "<id from table above>")
```
