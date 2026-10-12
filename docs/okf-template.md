# OKF-compatible SaPP Bundle Profile

The optional [bundle template](../templates/sapp-okf/index.md) targets OKF v0.2 while preserving SaPP Core semantics. Ordinary single-file SaPP and v0.5 cards remain valid. This profile is a public-draft interchange aid, not a promise of stable compatibility with every OKF consumer.

OKF supplies directory discovery, links, and metadata. SaPP supplies creative intent, identity rules, variation, derivation, and reuse boundaries. The [SaPP Skill Documents](../spec/skills/README.md) remain canonical for those meanings.

## Pinned Reference

- Specification: [GoogleCloudPlatform/open-knowledge-format, SPEC.md at ad30107](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md)
- Version: OKF 0.2
- Commit: `ad30107c31c06aec8a7d5636e0d1058118604e6f`
- SPEC.md SHA-256: `26aa5da029278939f914e578107242d9607d4f2dc5fe153272b82f9ed1030101`
- Checked: 2026-10-13

Compatibility refers to this snapshot, not a moving `main` or an assumed future release. Recheck the reference and consumer behavior before changing the profile's OKF version.

## Copy And Fill

```text
sapp-okf/
├── index.md
└── setting.md
```

1. Copy the whole directory. Root `index.md` declares `okf_version: "0.2"` and links to the concept.
2. Fill the visible fields in `setting.md`. Its only required OKF metadata is a non-empty `type`.
3. Add optional metadata only for discovery or tracking you actually need. `title` and `description` can be omitted to avoid repeating Name and One-liner; index summaries should remain aligned with the concept.
4. Rename or add concept files and update the index. Keep `index.md` and `log.md` reserved for OKF navigation/history.

The template starts with compact Core fields and one credit block. Expand Intent, Context, or modules when needed; do not split every character or chapter into a separate file by default. A [filled one-screen bundle](../examples/okf/index.md) demonstrates the profile.

## Lifecycle Mapping

`status` is an OKF field; `sapp_status` is a SaPP field. They describe different axes.

| SaPP `sapp_status` | OKF `status` guidance |
|---|---|
| `draft` | Usually `draft` while the content is incomplete or unreviewed |
| `public-draft` | Usually `draft`; being publicly visible does not mean reviewed |
| `released` | Use `stable` when ready for consumption; release alone does not establish review |
| `archived` | Use `deprecated` if no longer current; a retained historical snapshot may still be `stable` |

This is guidance, not an automatic conversion or a requirement that the two fields match. Set OKF status explicitly: the pinned spec treats its absence as `stable`. Neither `stable`, `released`, nor an OKF `verified` entry makes a creative fact canonical or supplies legal permission; retain SaPP's distinct credit and boundary fields.

## v0.1 Migration

- Change root `okf_version` to `"0.2"` after reviewing the chosen snapshot.
- Move any SaPP lifecycle `status` to `sapp_status`, then choose an explicit OKF `status`. Do not mechanically rename `released` to `stable` without reviewing readiness.
- The upstream spec replaces legacy `timestamp` with `generated.at` and body `# Citations` with `sources`; keep existing attribution when migrating those fields. The earlier SaPP template contained neither.
- Optional `sources`, `generated`, `verified`, and `stale_after` may be added when relevant. Do not fabricate verification records or give timeless fictional rules an arbitrary expiry.
- Keep visible SaPP fields, source revision links, permissions, and canonical status intact. Unknown producer metadata should survive round trips.

## Verification Boundary

Repository checks parse YAML, reject duplicate keys, and inspect revision metadata and the profile structures they support. They do not prove semantic consistency, rights clearance, authorship, canonical adoption, or compatibility with every independent OKF consumer. SaPP's advisory validator and human review remain separate checks.
