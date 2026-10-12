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
- Compare concise cards and expanded modules in actual generation/derivation use; collect cases where brevity loses necessary constraints
- Try copied OKF v0.2 bundles with independent consumers before making broader compatibility claims
- Keep released tags immutable

## v0.5 AI-first Public Draft

Status: released as [v0.5-ai-first-public-draft](https://github.com/lero003/settings-as-play-protocol/releases/tag/v0.5-ai-first-public-draft).

### AI-first Canonical Specification

- [x] Define SaPP as an AI-first specification format
- [x] Add canonical SaPP Core Skill Document
- [x] Add canonical SaPP Validator Skill Document
- [x] Add canonical SaPP Derivation Skill Document
- [x] Add canonical module Skill Documents
- [x] Clarify that templates, examples, docs, schemas, and validators are supporting artifacts
- [x] Smoke-check SaPP Validator Skill against `examples/minimal/one-screen-setting.md`

Follow-up validation and optional validator/schema decisions are tracked under `Next`.

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

## v0.6 Portable Settings Public Draft

Status: published as [v0.6-portable-settings-public-draft](https://github.com/lero003/settings-as-play-protocol/releases/tag/v0.6-portable-settings-public-draft). The optional OKF profile remains a public-draft interoperability aid.

- [x] Define optional card ID, card revision, and fixed source revision tracking
- [x] Preserve compatibility with v0.5 and unversioned cards
- [x] Target a pinned OKF v0.2 specification snapshot in a copyable bundle template
- [x] Map OKF structure to SaPP Core without replacing the canonical Skill Documents
- [x] Separate OKF status from SaPP lifecycle and document the v0.1 migration
- [x] Keep standard SaPP front matter optional outside the OKF bundle profile
- [x] Prefer one-screen cards, optional detail, and compact credit blocks
- [x] Add short revision and OKF examples
- [x] Verify YAML / metadata behavior with regression tests and documentation checks
- [x] Document format, permission, and version boundaries

Verification scope:

- Local and CI checks cover documentation, YAML, and the supported revision/profile metadata structures.
- Advisory semantic review, real multi-model creative use, and independent consumer integration are separate follow-ups under `Next`.
- No stable SaPP or future OKF compatibility promise is made by this release.

## Not Yet

- Stable specification
- Governance model
- Dedicated platform
- Required community workflow
- v1.0 compatibility promise
