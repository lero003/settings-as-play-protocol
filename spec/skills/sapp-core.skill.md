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

An AI assistant should treat this as the primary identifier for the setting. If the name is missing, the document is invalid as a shareable SaPP Core document.

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

## AI Generation Procedure

When creating or improving a SaPP Core document, an AI assistant should:

1. Start from the user's stated creative intent.
2. Fill required fields first.
3. Keep Core Rules short, concrete, and identity-preserving.
4. Keep Variables flexible, usable, and non-contradictory.
5. Ask for permission and credit details when public sharing or derivation is likely.
6. Mark uncertain assumptions as draft notes, not canonical facts.
7. Prefer a small usable card over an encyclopedic setting bible.

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
