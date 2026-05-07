# Optional Front Matter

SaPP is Markdown-first. Human-readable sections are the main format.

For search, tooling, AI review, or derivation-map generation, a SaPP card may add YAML front matter. This metadata is optional and should not be required for a valid SaPP card.

## Example

```md
---
sapp_version: "0.4"
card_type: "core"
status: "draft"
language: "ja"
name: "朝夜で変わる猫耳ちゃん"
canonical_status: "public sample"
license: "CC BY 4.0"
cultural_agreement: "SaPP Commons Agreement"
derived_from: null
original_by: "Hazakura Lab / 葉桜ラボ"
public_range: "SaPP sample"
non_public_range: "No private source material included"
---

# SaPP Core: 朝夜で変わる猫耳ちゃん
```

## Suggested Keys

| Key | Purpose |
|---|---|
| `sapp_version` | SaPP version used by this card |
| `card_type` | `core`, `module`, `derivation`, `asset`, or another local type |
| `status` | Document lifecycle: `draft`, `public-draft`, `released`, or `archived` |
| `language` | Primary language of the card |
| `name` | Setting or card name |
| `canonical_status` | Setting-world position: `canonical`, `public sample`, `non-canonical visual reference`, `derivative`, `fan derivative`, or `experimental` |
| `license` | Legal license or permission label |
| `cultural_agreement` | Cultural credit agreement, if used |
| `derived_from` | Source card or setting, if any |
| `original_by` | Original creator or organization |
| `public_range` | Reusable public range |
| `non_public_range` | Material not included in public reuse |

## Notes For Tools And AI Assistants

- Treat front matter as advisory metadata, not as a replacement for the visible card sections.
- Keep `status` for document lifecycle and `canonical_status` for official or setting-world position.
- If metadata and visible sections disagree, ask for clarification or prefer the visible section until the author resolves the drift.
- Do not infer legal permission from SaPP usage alone.
- Do not treat `public sample` or `non-canonical visual reference` as a promise that hidden source material is reusable.
