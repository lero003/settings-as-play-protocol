# SaPP Core Skill

## Purpose

SaPP Core is the canonical minimum specification for sharing a creative setting between humans and AI assistants.

An AI assistant uses SaPP Core to understand:

- what the setting is
- why it exists
- what must stay stable
- what may change during derivation
- what attribution, permission, and public boundaries apply

SaPP Core is not only a Markdown card. It is an AI-first specification format for creative settings: human-authored, AI-readable, and human-auditable.

## Document Role

This Skill Document is canonical for SaPP Core.

Human-facing templates and examples are supporting materials. If a template omits guidance that is present here, this Skill Document takes precedence.

## Core Fields

A SaPP Core document has seven core fields.

### 1. Name

Status: Required

The setting name.

An AI assistant should treat this as the human-readable identifier for the setting. If the name is missing, the document is invalid as a shareable SaPP Core document. When present, `card_id` identifies the card across name changes and revisions.

### 2. One-liner

Status: Required

A short description of the setting.

An AI assistant should use this to quickly identify the setting's premise. It should be specific enough to distinguish the setting from generic genre labels.

### 3. Intent

Status: Recommended

The creative purpose of the setting.

This may describe the emotion, play pattern, experiment, scene, medium, or experience the author wants to invite.

If Intent is missing, an AI assistant may still parse the document, but should warn when the intended use is ambiguous.

### 4. Context

Status: Recommended

The background needed to understand the setting.

Context may include world, situation, relationships, history, constraints, source assumptions, or social conditions.

If Context is missing, an AI assistant should avoid inventing hidden background as if it were canonical.

### 5. Core Rules

Status: Required

The constraints that preserve the identity of the setting.

An AI assistant should treat Core Rules as high-priority constraints during generation, validation, transformation, and derivation. If a requested change violates Core Rules, the assistant should identify the conflict instead of silently rewriting the setting.

Core Rules should be concrete enough to test against generated outputs.

### 6. Variables

Status: Required

The aspects that may change while the setting remains recognizable.

An AI assistant should use Variables as the preferred space for variation, remixing, adaptation, and module-specific expansion.

Variables should not contradict Core Rules.

### 7. Derivation & Credit

Status: Required when sharing publicly or deriving from others

The origin, authorship, permission, public range, non-public range, license, canonical status, cultural agreement, and credit notes.

An AI assistant should not treat SaPP as a license. It should preserve the distinction between legal permission and cultural agreement.

## Minimum SaPP Card

A private or early draft may be useful with only:

- Name
- One-liner
- Core Rules
- Variables

For public sharing, redistribution, or derivation from existing work, Derivation & Credit must be reviewed.

## Optional Revision Tracking

SaPP v0.6 adds optional `card_id`, `card_revision`, and `derived_from_revision`. The seven core fields and unversioned cards remain valid; v0.5 cards do not need migration.

- `card_id`: a stable, non-empty string for this card. Preserve it when editing the same card; give a new derivative its own ID. An author namespace is recommended; no registry or UUID is required.
- `card_revision`: a non-empty string chosen by the author, such as `"r2"`. Requires `card_id`. Change it when content meaningfully changes; do not reuse a label for different content. It is independent of `sapp_version` and need not use semantic versioning.
- `derived_from_revision`: the source card's actual revision label, not this card's revision. Requires an identified Derived From source. Preserve it when that source later changes; link to an immutable source snapshot where possible.

These values may appear in YAML front matter or a short visible Revision / Source Revision note. In YAML, put dependent fields in the same front matter: `card_revision` with `card_id`, and `derived_from_revision` with `derived_from`. Quote revision strings. Do not invent missing source IDs or revisions; record an unknown revision explicitly in prose. Multiple sources may use a revision note beside each source link instead of the single-source metadata shortcut. IDs and revision labels record identity, not authorship, permission, or canonical status.

## AI Reading Procedure

When reading a SaPP Core document, an AI assistant should:

1. Identify the SaPP version or infer that the document is an unstated draft if no version is present.
2. Extract the seven core fields.
3. Distinguish required, recommended, and conditional fields.
4. Treat Core Rules as identity-preserving constraints.
5. Treat Variables as the allowed change surface.
6. Preserve Derivation & Credit boundaries.
7. Avoid converting unstated assumptions into canonical facts.
8. Report missing or ambiguous fields before using the setting for high-impact generation or publication.
9. Preserve stated card IDs, revisions, and source revisions; do not replace a fixed source with its latest version silently.

## AI Generation Procedure

When creating or improving a SaPP Core document, an AI assistant should:

1. Start from the user's stated creative intent.
2. Fill required fields first.
3. Keep Core Rules short, concrete, and identity-preserving.
4. Keep Variables flexible, usable, and non-contradictory.
5. Ask for permission and credit details when public sharing or derivation is likely.
6. Mark uncertain assumptions as draft notes, not canonical facts.
7. Prefer a small usable card over an encyclopedic setting bible.

## Concise Authoring

Unless the user requests detail, start with a one-screen card, aiming for about 20–30 lines. This is an authoring target, not a validity limit.

- Use one sentence for One-liner, and about three bullets each for Core Rules and Variables.
- Add Intent, Context, and modules only when they resolve a real ambiguity or the user requests them. Do not pad missing fields with invented lore.
- Keep optional revision metadata out of the default draft unless tracking is useful or requested.
- Derivation & Credit may be one compact block, including under `Credit / Permission`, instead of separate subheadings. Preserve every applicable source, permission, public/non-public boundary, canonical status, and credit fact.
- When shortening, preserve negation, unresolved mysteries, and identity rules. Move necessary detail to a linked module rather than dropping constraints. Do not repeat the whole card in a concluding summary.

## Output Expectations

SaPP Core output should be valid Markdown.

Field names should remain recognizable even when translated. Human-readable prose is allowed, but required information should not be hidden inside decorative language.

## Non-Goals

SaPP Core does not:

- replace copyright, license, contract, or platform policy
- force all settings to be freely reusable
- require a dedicated platform
- guarantee automated enforcement
- replace module-specific details when those details are needed
