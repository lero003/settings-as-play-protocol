# Publication Checklist

Use this checklist for public-facing repository work that may not be part of a normal file edit.

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

## v0.4 Public Draft Release

Create a GitHub Release when the public draft is ready to be treated as a named snapshot.

Suggested tag:

> v0.4-public-draft

Release notes should point to:

- README
- CHANGELOG
- COMMONS_AGREEMENT
- templates/sapp-core.md
- templates/derivation-card.md
- examples/minimal/one-screen-setting.md

## Before Publishing

- [x] README explains what SaPP is and is not.
- [x] Minimum SaPP Card is visible.
- [x] Templates distinguish required, recommended, and optional fields.
- [x] Derivation and credit examples are present.
- [x] License / Permission guidance is present.
- [x] GitHub issue and PR templates exist.
- [x] Lightweight docs CI exists.
- [ ] GitHub About description, website, and topics are configured.
- [ ] `v0.4-public-draft` GitHub Release exists.
- [ ] `git diff --check` passes.
- [ ] `python scripts/check-docs.py` passes.

## Notes For AI Assistants

- Do not create a public release, edit repository topics, or change external GitHub settings without an explicit instruction for that public action.
- If asked to prepare the release, update files first, verify the diff, then perform external GitHub actions as a separate named step.
