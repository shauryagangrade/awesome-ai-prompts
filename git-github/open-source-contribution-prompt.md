# Reusable prompt: open-source contribution

Copy-paste the block below into any AI coding agent to make a high-quality
contribution to an open-source repository you don't own - the right way.

---

Help me contribute to the open-source project I point you at (`OWNER/REPO`).
Read the project's conventions before doing anything. A maintainer is going
to read your work - make it easy to review and merge.

## Steps

1. **Read the room** - Read `CONTRIBUTING`, `README`, `CODE_OF_CONDUCT`,
   `LICENSE`, and the issue/PR templates. Understand the project's workflow,
   its commit style, and what "done" looks like there. Check the issue tracker
   and recent PRs to see if the work is already in progress or requested.
2. **Scope the work** - Pick (or confirm) a specific, bounded task. For a
   first contribution, prefer a `good first issue` or `help wanted` if the
   project uses them. State exactly what you'll change and the files involved.
3. **Set up properly** - Fork, clone, and set up the upstream remote. Create a
   feature branch off the default branch. Install and run the existing tests
   to confirm the environment works before changing anything.
4. **Follow the project's rules** - Match the code style, keep changes
   minimal and focused on the task, add/update tests where the project
   expects them, and update docs if user-facing behavior changes.
5. **Verify** - Run the project's checks exactly as its CI does (lint, format,
   type checks, tests). A contribution that breaks CI is not done.
6. **Commit & push** - Commit with the project's message style (often
   Conventional Commits). Reference the issue in the PR body with a closing
   keyword (`Fixes #N`) only if it truly resolves it.
7. **Open the PR** - Use the template, describe what you did and why, note
   anything a reviewer should test, and answer review comments. Never argue
   with maintainers - address feedback or ask for clarification.

## Rules

- Never force-push a PR branch after review without being asked; prefer
  adding commits or amending only when the project expects it.
- Never submit a PR with unrelated changes, dependency bumps, or formatting
  churn mixed in.
- Don't claim you ran tests you didn't run. Verification must be real.
