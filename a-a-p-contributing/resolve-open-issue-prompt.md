# Reusable prompt: resolve an open issue

Copy-paste the block below into any AI coding agent to take an open issue in
this repository from reading the ticket to a mergeable pull request.

---

Help me complete the issue I point you at in this `awesome-ai-prompts`
repository and land it as a pull request a maintainer will merge. This is a
catalog of copy-paste prompts, so most issues are about wiring, wording, or new
prompts - read the conventions before changing anything.

## Steps

1. **Understand the ticket** - Read the issue and the files it touches.
   Restate the ask in one sentence and list the files you expect to change.
   Ask me before proceeding if anything is ambiguous.
2. **Reproduce or show the before-state** - For a bug, broken link, or failing
   check, reproduce the failure first and show me the actual output. For a
   feature or new prompt, show me the current state before proposing a change.
3. **Read the conventions** - `CONTRIBUTING.md`, `.github/PROMPT_TEMPLATE.md`,
   and a neighboring prompt when the issue is about prompts.
4. **Scope the change** - State precisely what will change: for prompt work,
   one new file in a category folder, one README entry plus a Contents count
   bump, and one `## [Unreleased]` CHANGELOG entry. Keep it minimal.
5. **Implement** - Make the smallest change that resolves the issue. Follow the
   repo's rules: tool-agnostic, verification-first, no em dashes, one PR per
   logical change.
6. **Update the derived artifacts** - README entry and Contents count, plus a
   CHANGELOG entry under `[Unreleased]`, exactly when prompts are added,
   renamed, or moved.
7. **Verify** - Run `bash scripts/check-links.sh` and
   `bash scripts/check-consistency.sh`, and `npx --yes markdownlint-cli2@0.17.2`
   on the changed files. Paste the outputs.
8. **Commit and PR** - One conventional commit, reference the issue (for
   example `Closes #N` when it truly resolves it), and open the PR with the
   verification output in the description.

## Rules

- Never change a prompt's substance to satisfy a check; if a check conflicts,
  stop and ask.
- Never claim the issue is resolved unless the failing behavior is gone or the
  missing feature demonstrably exists.
- Keep unrelated files untouched.

## Verification

Confirm the reproduction or before-state from step 2, then the check outputs
from step 7. For a broken link or script, show that the fix catches the old
failure.
