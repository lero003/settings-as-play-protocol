# Publication Checklist

Use this checklist for public-facing repository work that may not be part of a normal file edit.

## Last Verified

- Date: 2026-05-08
- Verified by: Hazakura Lab
- Scope: GitHub About, topics, v0.4 public draft release, v0.4.1 docs polish release, v0.5 AI-first public draft tag, docs CI

## GitHub About

Recommended description:

> An AI-first specification format for sharing, validating, transforming, and extending creative settings.

Recommended website:

> https://hazakura.dev

Recommended topics:

- ai-creation
- worldbuilding
- character-design
- creative-commons
- prompting
- ai-specification
- commons
- derivation
- creative-protocol
- markdown

## Release Tags

Create a GitHub Release when the public draft or docs snapshot is ready to be treated as a named version.

Current tags:

- `v0.4-public-draft`
- `v0.4.1-docs-polish`
- `v0.5-ai-first-public-draft`

Release notes should point to:

- README
- CHANGELOG
- COMMONS_AGREEMENT
- spec/skills/README.md
- spec/skills/sapp-core.skill.md
- spec/skills/sapp-validator.skill.md
- spec/skills/sapp-derivation.skill.md
- templates/sapp-core.md
- templates/derivation-card.md
- examples/minimal/one-screen-setting.md

## Before Publishing

Use this as a manual release-prep checklist. Checked items record the last verification above; re-check them before a new release.

- [x] README explains what SaPP is and is not.
- [x] README defines SaPP as an AI-first specification format.
- [x] Canonical Skill Documents exist under `spec/skills/`.
- [x] Templates and modules are marked as supporting human-facing materials.
- [x] SaPP Validator Skill was smoke-checked against `examples/minimal/one-screen-setting.md`.
- [x] Minimum SaPP Card is visible.
- [x] Templates distinguish required, recommended, and optional fields.
- [x] Derivation and credit examples are present.
- [x] License / Permission guidance is present.
- [x] GitHub issue and PR templates exist.
- [x] Lightweight docs CI exists.
- [x] GitHub About description, website, and topics are configured.
- [x] `v0.4-public-draft` GitHub Release exists.
- [x] `v0.4.1-docs-polish` GitHub Release exists.
- [x] `git diff --check` passes.
- [x] `python scripts/check-docs.py` passes.

## v0.5 Release Readiness Decision

Decision: `v0.5-ai-first-public-draft` is tagged and ready for an optional GitHub Release when explicitly requested.

Rationale:

- v0.5 is a documentation and specification redefinition, not a binary or schema-contract release.
- The canonical specification now lives under `spec/skills/`.
- Supporting templates, modules, examples, and guides no longer claim to be the canonical source.
- The minimal example smoke-checks as usable with only expected draft-level warnings for omitted recommended fields.
- Optional JSON Schema or CLI validation can remain post-v0.5 follow-up work.

Release boundary:

- Do not move the existing `v0.4-public-draft` or `v0.4.1-docs-polish` tags.
- Do not move the existing `v0.5-ai-first-public-draft` tag.
- Do not publish a GitHub Release unless the user explicitly asks for that public action.

## Notes For AI Assistants

- Do not create a public release, edit repository topics, or change external GitHub settings without an explicit instruction for that public action.
- If asked to prepare the release, update files first, verify the diff, then perform external GitHub actions as a separate named step.
