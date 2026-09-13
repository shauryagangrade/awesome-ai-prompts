# Reusable prompt: git history surgery

Copy-paste the block below into any AI coding agent to perform tricky git
operations safely - clean history, find the culprit commit, or rescue lost
work without damaging the repo.

---

Help me with the git operation I describe in this repository. Work carefully:
git history surgery can destroy work. Verify your commands before running
them and prefer non-destructive operations.

## Ground rules

1. **Understand before acting** - Show me what the current state is
   (`git status`, `git log --oneline --graph`, relevant branches) and explain
   what the operation will do before you run anything irreversible.
2. **Never rewrite published history** - No `rebase`/`filter-branch`/force-push
   on commits that exist on the remote, unless I explicitly confirm I know the
   consequences. Prefer `revert` for committed-then-pushed mistakes.
3. **For local-only history** - Use `git rebase -i`, `git reset --soft`,
   `git commit --amend`, and `git reflog` to tidy local commits. Before a
   rebase, make sure my working tree is clean (or stash first) and show me
   the plan.
4. **Finding things** - Use `git bisect` to find the commit that introduced a
   bug (give me the good/bad start points and let me run each step if you
   need my input), `git blame` for line provenance, `git log -S/-G` for when a
   string changed, and `git reflog` to recover seemingly lost commits/branches.
5. **Recovery** - If work appears lost, check the reflog and dangling commits
   (`git fsck --lost-found`) before concluding it's gone. Never recreate work
   from memory when the original can be recovered.

## Rules

- Never force-push unless I explicitly ask.
- Never use `filter-branch` to scrub secrets from history on a shared repo -
  advise rotating the secret and using GitHub's secret-scanning/removal
  tooling instead.
- After any surgery, verify the result (`git log`, `git status`, tests) and
  show me the diff of what changed.
