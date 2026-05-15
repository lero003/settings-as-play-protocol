# Roadmap

This is a draft roadmap for SaPP.

## v0.4 Public Draft

Status: released as [v0.4-public-draft](https://github.com/lero003/settings-as-play-protocol/releases/tag/v0.4-public-draft).

- [x] Publish manifesto
- [x] Publish SaPP Core
- [x] Publish templates
- [x] Publish optional modules
- [x] Publish small examples
- [x] Separate legal license and cultural agreement
- [x] Collect feedback

## v0.4.1 Docs Polish

Status: released as [v0.4.1-docs-polish](https://github.com/lero003/settings-as-play-protocol/releases/tag/v0.4.1-docs-polish).

- [x] Align release, main, roadmap, and changelog status wording
- [x] Clarify repository license compatibility for contributed examples
- [x] Clarify SaPP Mini credit / permission wording
- [x] Add tiny example index
- [x] Add front matter delimiter check
- [x] Update docs workflow actions for the Node.js 24 runner transition

## Next

- Collect first-use feedback on the AI-first Skill Documents
- Validate the Skill Documents against real SaPP cards and derivation examples
- Decide whether optional JSON Schema or a CLI validator is worth generating from the Skill Documents
- Review optional front matter after a few real cards use it
- Keep released tags immutable

## v0.5 AI-first Public Draft

Status: tagged as [v0.5-ai-first-public-draft](https://github.com/lero003/settings-as-play-protocol/tree/v0.5-ai-first-public-draft). A GitHub Release has not been created for this tag yet.

### AI-first Canonical Specification

- [x] Define SaPP as an AI-first specification format
- [x] Add canonical SaPP Core Skill Document
- [x] Add canonical SaPP Validator Skill Document
- [x] Add canonical SaPP Derivation Skill Document
- [x] Add canonical module Skill Documents
- [x] Clarify that templates, examples, docs, schemas, and validators are supporting artifacts
- [x] Smoke-check SaPP Validator Skill against `examples/minimal/one-screen-setting.md`
- [ ] Validate the Skill Documents against real SaPP cards and derivation examples
- [ ] Decide whether optional JSON Schema or a CLI validator is worth generating from the Skill Documents

Done when:

- An AI assistant can read the Skill Documents and produce a usable SaPP Core without relying on README prose.
- An AI assistant can validate a SaPP Core and return `Valid`, `Valid with warnings`, or `Invalid` with actionable issues.
- A human reader can audit the same Skill Documents without needing implementation-specific tooling.
- Templates and examples do not contradict the canonical Skill Documents.

### Foundation Already Prepared

- [x] Define Minimum SaPP Card
- [x] Add issue and PR templates
- [x] Add first Derivation Map example
- [x] Add license / permission guide
- [x] Add 5 tiny examples under 30 lines
- [x] Add bad-example / improved-example pairs
- [x] Add optional YAML front matter convention
- [x] Add lightweight docs CI for markdown style, links, image paths, and trailing spaces
- [x] Publish v0.4 release tag

Done when:

- A new user can copy one file and publish a valid SaPP card within 10 minutes.
- A derivative author can identify what changed, what stayed, and how to credit.
- A non-GitHub user can understand SaPP from README alone.
- An AI assistant can identify required fields, optional metadata, public range, non-public range, license, and canonical status from the canonical Skill Documents.

## Not Yet

- Stable specification
- Governance model
- Dedicated platform
- Required community workflow
- v1.0 compatibility promise
