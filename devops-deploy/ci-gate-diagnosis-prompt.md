# Reusable prompt: CI gate diagnosis

Copy-paste the block below into any AI coding agent when a CI check fails and
you need to know why. It reads the logs, separates a flaky failure from a real
bug, decides whether your change caused it, and tells you whether to retry,
fix the code, or fix the pipeline.

Keywords: ci failing, flaky test, github actions, build failed, red pipeline, pre-existing failure, rerun checks

---

A CI check failed. Diagnose it from the evidence. The goal: find the root
cause, decide whether this change caused it, and recommend the right action,
with the log lines that prove it.

## Steps

1. **Get the failing run** - Identify the failing job and step and fetch its
   full log (for example `gh run view <id> --log-failed`). Note the commit
   under test, the runner, and the time. Work from the real log, never from a
   summary or a guess.
2. **Find the first real error** - Read the log from the top of the failing
   step, not just the last lines. The first error is usually the cause and the
   rest is fallout. Quote the exact lines and say which command produced them.
3. **Classify the failure** - Decide which kind it is: a **genuine bug** (the
   code or a test fails the same way every time), a **flaky failure** (passes
   on retry, depends on timing, ordering, network, or shared state), an
   **environment problem** (tool or dependency version, missing secret,
   runner image, cache), or a **pipeline fault** (the workflow itself is
   wrong).
4. **Check whether this change caused it** - Compare with the same job on the
   base branch and on recent runs (`gh run list --branch main`). If it also
   fails there, it is pre-existing. If it passes there, find the commit in this
   change that introduces it, and name the file and line.
5. **Reproduce it** - Run the failing command locally or in a clean checkout
   with the same versions as CI. If you cannot reproduce it, say so and name
   what differs (OS, version, environment variable, timing).
6. **Recommend one action** - Choose and justify: **retry** (only with
   evidence it is flaky, such as a pass on another run), **fix the code** (name
   the change), or **fix the pipeline** (name the workflow line). Say what to
   do about a flaky test too, instead of just re-running it forever.
7. **Verify the fix** - After the fix, re-run the check and show it green. For
   a flaky test, run it repeatedly (for example 20 times) and report the
   result.

## Verification

- [ ] The diagnosis quotes the first error from the real log, with the step
      name.
- [ ] The failure is classified as bug, flaky, environment, or pipeline, with
      the evidence for that class.
- [ ] The base branch or recent runs were checked to say whether the failure is
      pre-existing.
- [ ] The failing command was reproduced locally, or the reason it could not be
      is stated.
- [ ] The recommended action is one of retry, fix code, or fix pipeline, with
      a reason.
- [ ] The check was re-run after the fix and the result is shown.

## Rules

- Never recommend "just re-run it" without evidence the failure is flaky.
- Never disable, skip, or delete a failing test or check to make CI green.
- Never claim a failure is unrelated to the change without comparing against
  the base branch.
- Never edit workflow files to hide a real failure, for example by adding
  `continue-on-error`.
- If the log is truncated or unavailable, say so and ask for it instead of
  diagnosing from the tail.
