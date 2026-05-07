# Publication Checklist

Use this checklist for public-facing repository work that may not be part of a normal file edit.

## Last Verified

- Date: 2026-05-08
- Verified by: Hazakura Lab
- Scope: GitHub About, topics, v0.4 public draft release, v0.4.1 docs polish release, docs CI

## GitHub About

Recommended description:

> A lightweight protocol for sharing character settings, worldbuilding, prompts, play rules, derivation, and credit in the AI creation era.

Recommended website:

> https://hazakura.dev

Recommended topics:

- ai-creation
- worldbuilding
- character-design
- creative-commons
- prompting
- markdown-template
- commons
- derivation
- creative-protocol

## Release Tags

Create a GitHub Release when the public draft or docs snapshot is ready to be treated as a named version.

Current tags:

- `v0.4-public-draft`
- `v0.4.1-docs-polish`

Release notes should point to:

- README
- CHANGELOG
- COMMONS_AGREEMENT
- templates/sapp-core.md
- templates/derivation-card.md
- examples/minimal/one-screen-setting.md

## Before Publishing

Use this as a manual release-prep checklist. Checked items record the last verification above; re-check them before a new release.

- [x] README explains what SaPP is and is not.
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

## Notes For AI Assistants

- Do not create a public release, edit repository topics, or change external GitHub settings without an explicit instruction for that public action.
- If asked to prepare the release, update files first, verify the diff, then perform external GitHub actions as a separate named step.
