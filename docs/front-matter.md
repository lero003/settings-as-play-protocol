# Optional Front Matter

SaPP is Markdown-first. Visible sections carry the setting; YAML metadata is optional for an ordinary card. Add only the keys you need. The [canonical Core Skill](../spec/skills/sapp-core.skill.md) defines optional revision tracking.

The [OKF v0.2 bundle profile](okf-template.md) requires parseable front matter with a non-empty `type` on concept documents. This requirement applies only to that profile.

## Minimal Revision Example

```yaml
---
sapp_version: "0.6"
card_id: "hazakura-lab/rain-lighthouse"
card_revision: "r2"
---
```

`sapp_version` identifies the format; `card_revision` identifies this card's content. A name change preserves the same `card_id`. A new derivative gets a new ID. Revision labels are author-chosen strings, not globally ordered versions. No Git account, UUID, or central registry is required.

For a derivative, add only what is known:

```yaml
derived_from: "../versioned/lighthouse-r1.md"
derived_from_revision: "r1"
```

Keep the source revision fixed when the original advances to r2. The visible Derived From field should link to the same snapshot. See the [r1 source](../examples/versioned/lighthouse-r1.md), [r2 source](../examples/versioned/lighthouse-r2.md), and [derivative that retains r1](../examples/versioned/lighthouse-derivative-r1.md).

## Optional Keys

| Key | Meaning |
|---|---|
| `sapp_version` | Format version; old v0.5 cards remain valid |
| `card_id` | Stable identity of this card; recommended author namespace |
| `card_revision` | This card's revision; requires `card_id` |
| `derived_from` | Identified source card, link, or setting |
| `derived_from_revision` | Source revision; requires `derived_from` |
| `card_type` | `core`, `module`, `derivation`, `asset`, or a local type |
| `sapp_status` | SaPP document lifecycle: `draft`, `public-draft`, `released`, `archived` |
| `language`, `name` | Primary language and human-readable name |
| `canonical_status` | Position in the setting: e.g. `canonical`, `public sample`, `derivative`, `non-canonical visual reference` |
| `original_by`, `license`, `cultural_agreement` | Authorship, legal permission, and cultural agreement; distinct facts |
| `public_range`, `non_public_range` | Reusable range and excluded material |

Omit unused keys rather than filling a template with nulls. Quote revision values so YAML does not turn them into numbers. `card_revision` and `derived_from_revision` must be non-empty strings when present. For multiple sources, record each known revision beside its visible source link instead of squeezing them into one scalar.

## Reading And Compatibility

- Metadata supports discovery and tooling; it does not replace visible Core or credit information.
- If metadata and visible text disagree, report the conflict and resolve it before reuse; do not silently merge permission claims.
- `canonical_status`, document lifecycle, and permission are separate. None proves either of the others.
- Preserve unknown metadata when copying or updating a card.
- Outside OKF bundles, legacy SaPP `status` remains accepted as a lifecycle alias. New cards should use `sapp_status`; conflicting legacy/new values need correction.
- In OKF v0.2 bundles, `status` belongs to OKF (`draft`, `stable`, `deprecated`). SaPP lifecycle uses `sapp_status`. The [profile mapping](okf-template.md#lifecycle-mapping) explains their independent meanings.
- Missing IDs or revisions do not invalidate an old card. Never manufacture source revisions or infer permission from metadata alone.
