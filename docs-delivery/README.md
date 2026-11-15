# Docs & delivery

Prompts for explaining code and changes to other people: READMEs, API docs, inline comments, and changelogs.

Back to the [main index](../README.md#docs--delivery) or browse
[every prompt on one page](../website/index.html).

## Prompts

- [documentation-writer-prompt.md](documentation-writer-prompt.md) - accurate, verified docs that match the project's voice.
- [release-notes-changelog-prompt.md](release-notes-changelog-prompt.md) - turn git history into a clear, honest changelog.
- [api-documentation-prompt.md](api-documentation-prompt.md) - generate OpenAPI/Swagger docs from existing code with accurate schemas.
- [readme-builder-prompt.md](readme-builder-prompt.md) - build a comprehensive README from scratch: purpose, quickstart, examples.
- [inline-documentation-prompt.md](inline-documentation-prompt.md) - add JSDoc/docstrings to existing code: accurate, concise, non-redundant.

- [architecture-documentation-prompt.md](architecture-documentation-prompt.md) - write architecture docs with evidence, tradeoffs, and verification.
- [migration-guide-prompt.md](migration-guide-prompt.md) - write a migration guide: preconditions, steps, rollback, verification, common failures.
- [adr-writing-review-prompt.md](adr-writing-review-prompt.md) - draft or review an ADR against a complete checklist: problem statement, alternatives, trade-offs, consequences, actionability.
- [runbook-writing-prompt.md](runbook-writing-prompt.md) - write verifiable incident runbooks: symptoms, diagnosis commands with expected output, mitigation, rollback, escalation.
- [documentation-audit-prompt.md](documentation-audit-prompt.md) - audit docs into a prioritized, actionable fix list: exact locations, concrete edits, verifiable acceptance checks, grouped by type.

## Adding a prompt here

Read [CONTRIBUTING.md](../CONTRIBUTING.md) for the file format and the gates,
model the new file on a neighbor in this folder, and add a one-line entry
above plus a [CHANGELOG.md](../CHANGELOG.md) entry under `[Unreleased]`.
