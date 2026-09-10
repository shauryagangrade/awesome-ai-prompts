# Reusable prompt: fix a reported bug

Copy-paste the block below into any AI coding agent to fix a bug reported in
an issue in this repository, with proof, in the smallest possible change.

---

Fix the bug in issue `#N` in this `awesome-ai-prompts` repository. Do not
start coding until the bug is reproduced and the root cause is proven. A fix
without a reproduced failure is not a fix - it is a guess.

## Steps

1. **Reproduce** - Read the issue, then read the files it implicates. Run the
   failing command or state exactly how the behavior is wrong, and capture the
   actual output versus the expected output.
2. **Root-cause** - Explain the mechanism precisely: which file and line,
   which check or script, which README entry. Use `git log` and `git blame` on
   the relevant file to see when the behavior appeared. Prove the cause before
   touching anything.
3. **Minimal fix** - Make the smallest change that removes the failure. Do not
   refactor, reword, or reformat unrelated content in the same edit.
4. **Prove it** - Re-run the original failing reproduction and show before and
   after. Run the repo gates: `bash scripts/check-links.sh` and
   `bash scripts/check-consistency.sh`, markdownlint on the changed files, and
   `bash -n` on any changed shell script.
5. **Guard against regression** - Where the repo allows it, add the check that
   would have caught this bug (for example a script assertion or a stricter
   README convention). If nothing reasonable can be added, say why.
6. **Commit and PR** - One conventional `fix:` commit referencing the issue,
   and a PR description showing the reproduced failure, the root cause, and the
   verification output.

## Rules

- No claim of a fix without the reproduced failure and the passed checks shown.
- No unrelated edits and no silent convention changes.
- If the reported bug cannot be reproduced, say so and ask instead of
  inventing a fix.

## Verification

The after-state of the reproduction no longer fails, and every gate named in
step 4 passed with its output shown.
