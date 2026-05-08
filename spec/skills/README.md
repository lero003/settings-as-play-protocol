# SaPP Skill Documents

This directory is the canonical specification source for Settings as Play Protocol.

SaPP Skill Documents are AI-readable and human-auditable specification documents. They define how an AI assistant should read, validate, transform, and extend SaPP settings while keeping the format understandable to human authors.

## Canonical Documents

- [SaPP Core Skill](sapp-core.skill.md)
- [SaPP Derivation Skill](sapp-derivation.skill.md)
- [SaPP Validator Skill](sapp-validator.skill.md)

## Module Documents

- [Character Module Skill](modules/character.skill.md)
- [Worldbuilding Module Skill](modules/worldbuilding.skill.md)
- [Image Generation Module Skill](modules/image-generation.skill.md)
- [Story / Film Module Skill](modules/story-film.skill.md)
- [Game Module Skill](modules/game.skill.md)

## Supporting Materials

The files under `templates/`, `modules/`, `examples/`, and `docs/` are supporting materials. They help humans author, learn, and publish SaPP documents, but they do not override the Skill Documents in this directory.

JSON Schema files, command-line validators, or other automated checks may be generated from these Skill Documents when useful. They are optional artifacts, not the canonical source.
