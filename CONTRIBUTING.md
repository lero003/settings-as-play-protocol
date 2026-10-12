# Contributing to SaPP

Thank you for your interest in Settings as Play Protocol.

SaPP is a **v0.6 public draft**. Names, fields, modules, examples, and operating style may change. Existing v0.5 cards remain valid.

The canonical specification is defined in [SaPP Skill Documents](spec/skills/README.md). Templates, examples, and guides are supporting materials for authors and contributors.

## Good First Contributions

- Improve wording in templates
- Improve canonical Skill Documents
- Add small examples
- Report confusing terms
- Suggest optional modules
- Point out license or credit ambiguities
- Clarify public and non-public boundaries in examples

## Before Adding Examples

Please make sure that:

- You have the right to share the setting
- Public and non-public ranges are clear
- Source names and links are kept when possible
- Legal license and cultural agreement are separated
- AI-generated assets are marked as non-canonical unless they are intended to be canonical

## Contribution Style

Small proposals are welcome. You do not need to submit a perfect specification.

Prefer one-screen cards and compact credit blocks. Add optional revision metadata or modules only when useful; do not expand every example to fill every template heading.

When suggesting changes, please describe:

- What is confusing or missing
- Which file or template is affected
- Whether the change is wording, structure, example content, or policy

## Pull Request Checklist

For examples, templates, and policy wording, check the relevant items before submitting:

- You have the right to share the setting or example.
- Public Range is clear.
- Non-public Range is clear.
- Original source and author are credited where practical.
- Legal License / Permission is written.
- Cultural Agreement is not confused with legal license.
- AI-generated assets are marked as canonical or non-canonical.

## Repository License Compatibility

Examples merged into this repository should be compatible with the repository license, CC BY 4.0, unless a different license is explicitly discussed and clearly marked.

If an example uses CC BY-NC, All rights reserved, 個別許諾, or another non-CC-BY permission, prefer linking to it as an external SaPP card rather than copying it into this repository.

## Local Checks

Use an isolated environment; the only check dependency is pinned in `requirements-dev.txt`:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/check-docs.py
git diff --check
```

Checks cover documentation links/style, safe YAML structure, revision metadata, and the included OKF profile. They do not perform the advisory semantic or rights review defined by SaPP's Validator Skill.

## Legal Note

By contributing, you agree that your contribution may be included in this repository under the repository license unless otherwise discussed.

The current repository license is [CC BY 4.0](LICENSE.md).
