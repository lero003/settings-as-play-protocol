# SaPP Validator Skill

## Purpose

This Skill Document defines the canonical validation behavior for SaPP documents.

Validation is advisory. It helps humans and AI assistants detect missing fields, weak reuse signals, contradictions, unsupported assumptions, and boundary problems. It is not a legal review and does not guarantee safety.

## Validation Result

A validator should return one of:

- Valid
- Valid with warnings
- Invalid

Use `Valid` only when required fields are present, no blocking contradictions are found, and the document is specific enough for the stated use.

Use `Valid with warnings` when the document can be used, but has ambiguity, weak specificity, optional missing context, or non-blocking boundary issues.

Use `Invalid` when required fields are missing, core constraints contradict each other, permission boundaries are unusable for the stated purpose, or the document cannot be safely interpreted as SaPP.

## Issue Format

For each issue, return:

- severity: error / warning / note
- field: the affected field or module section
- reason: why this matters
- suggested fix: the smallest useful correction

## Validation Procedure

1. Confirm the SaPP version when present.
2. Identify whether the document is SaPP Core, a module, a derivation card, or a mixed document.
3. Check required fields.
4. Check conditional fields, especially Derivation & Credit for public sharing or derivation.
5. Check whether each field is specific enough for AI reuse.
6. Detect contradictions between Core Rules and Variables.
7. Detect contradictions between module details and Core Rules.
8. Detect unsupported assumptions that are not stated in the source document.
9. Check public range, non-public range, legal permission, cultural agreement, and canonical status are not confused.
10. Check module-specific constraints.
11. Return a result and issue list.

## Core Field Checks

### Name

Invalid if missing.

Warn if the name is generic enough that multiple settings could share it without distinction.

### One-liner

Invalid if missing.

Warn if it is only a genre label, mood word, or medium name without a specific premise.

### Intent

Warn if missing when the document is intended for generation, adaptation, or publication.

Warn if it conflicts with Core Rules or module constraints.

### Context

Warn if missing when the setting depends on background assumptions.

Warn if the assistant would need to invent hidden setting facts to proceed.

### Core Rules

Invalid if missing.

Invalid if Core Rules are empty, purely decorative, or mutually contradictory.

Warn if rules are too vague to test against generated outputs.

### Variables

Invalid if missing.

Invalid if Variables directly authorize changes forbidden by Core Rules.

Warn if Variables are so narrow that derivation is impossible, unless the document intentionally describes a locked setting.

### Derivation & Credit

Invalid if missing when the document is public, redistributed, or derived from another work.

Warn if legal license and cultural agreement are merged.

Warn if public range and non-public range are unclear.

Warn if canonical status is missing for AI-generated assets or derivative materials.

## Module Checks

When a module is present, validate it against both the module Skill Document and SaPP Core.

Module content should refine the setting, not override Core Rules unless the document explicitly declares a new derivative version.

## Unsupported Assumptions

An unsupported assumption is a claim that an AI assistant adds without evidence from the SaPP document, source material, or user instruction.

Validators should flag unsupported assumptions when they affect:

- authorship
- permission
- public or non-public range
- canonical status
- character identity
- world rules
- sensitive boundaries
- generation constraints

## Severity Guidance

Use `error` when the issue blocks valid use.

Use `warning` when the document can be used, but the issue may cause misinterpretation, unsafe publication, weak derivation, or inconsistent generation.

Use `note` for helpful improvements that do not affect validity.

## Validator Output Template

```markdown
Result: Valid / Valid with warnings / Invalid

Issues:

- severity:
  field:
  reason:
  suggested fix:
```

## Non-Goals

SaPP validation does not:

- determine legal ownership
- approve commercial use
- guarantee factual accuracy outside the document
- enforce platform policy
- replace human review before publication
