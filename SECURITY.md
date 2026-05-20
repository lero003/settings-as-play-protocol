# Security Policy

Settings as Play Protocol is an AI-readable specification and template
repository. The main security risk is not service compromise; it is poisoned
documentation that changes how humans or AI agents interpret settings,
licenses, provenance, or instructions.

## Supported Scope

Please report security issues that affect the current `main` branch or latest
public draft release, including:

- prompt injection or malicious instructions in `spec/skills/`, `templates/`,
  `modules/`, examples, or docs
- hidden Unicode, bidirectional controls, or invisible text that changes review
  meaning
- misleading license, provenance, or credit guidance
- GitHub Actions or repository supply-chain risks
- examples that encourage unsafe handling of private data or credentials

## Reporting

Open a GitHub security advisory or contact the maintainer privately if the
issue should not be public yet. Do not include real secret values, private
documents, unpublished settings, shell history, cloud credentials, or unrelated
local paths in the report.

Use synthetic SaPP documents when possible.

## Review Boundary

SaPP documents are intended to be read by AI assistants. Treat all incoming
issues, pull requests, examples, and proposed skill documents as untrusted input
until they have been reviewed for instruction injection, hidden text, and
license/provenance ambiguity.
