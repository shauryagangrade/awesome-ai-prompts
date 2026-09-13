# Reusable prompt: good-first-issue guard workflow

Copy-paste the block below into any AI coding agent to build the same
good-first-issue enforcement workflow for a different repository.

## Gist: the protected-labels setup

Two labels are reserved for contributors submitting their **first PR** to the
repo: `good first issue` and `help wanted`. Together they cover the explicit
kinds of issues a newcomer can realistically ship - documentation, tests,
small bug fixes, and scoped UI/UX, performance, and devops chores. Any
experienced contributor (≥1 merged PR here) who grabs one is unassigned and
their PR is closed, with a note to pick an **unreserved** issue instead.
First-time assignees get a welcome comment and keep the issue unless their
assignment goes stale (no open PR within 14 days), at which point it's
released back to the pool.

---

Create a GitHub Actions workflow for **this** repository that reserves
starter-labeled issues (`good first issue` and `help wanted`) for first-time
contributors. The workflow must run fully automatically with no manual
approval, and enforce the rules below. Do not ask the user which repo - use
the current one.

## Output

A single workflow file at `.github/workflows/good-first-issue.yml`, written
in bash using the GitHub CLI (`gh`), with **no third-party actions and no
`checkout` step** anywhere. Three jobs: a per-assignment guard, a per-PR
guard, and a periodic on-demand sweep that enforces the policy
retroactively.

## Configurable policy (use these defaults unless told otherwise)

- Labels to protect (reserved for first-timers): `good first issue` and
  `help wanted`
- Experienced contributors should be redirected to any **unreserved** issue
  (the old "pick a help wanted issue instead" advice no longer applies -
  `help wanted` is itself reserved)
- "First-time contributor" = has **0 merged PRs** authored by them in this
  repo (query via `gh pr list --state merged --author "<login>" --limit 1`;
  beware the `commits?author=` API 422ing for users with no GitHub activity
  - don't use it)
- Exempt from enforcement: repo owner and anyone with collaborator access
  (use `author_association` if available on the event, else the collaborators
  API `repos/{owner}/{repo}/collaborators/{login}` → 204 means exempt)
- Staleness window `GFI_STALE_DAYS`, default **14 days**: a first-time
  assignee who has no open PR referencing the issue after that long is
  unassigned and the issue returns to the pool

## Enforcement behavior

All comments (welcome, policy, close, stale) must spell out the **explicit
kinds of issues** the reserved labels cover - documentation, tests, small
bug fixes, and scoped UI/UX, performance, and devops chores - and, for
experienced contributors, point them at unreserved work (e.g. larger
features, architecture, security hardening, cross-platform/CI overhauls)
instead.

1. **When someone gets assigned to a protected issue** (trigger
   `issues: types: [assigned]`, only if the issue has either protected
   label):
   - Assignee is first-time → post a friendly welcome comment once (dedupe
     with a hidden HTML-comment marker in the comment body).
   - Assignee is experienced → remove them (`DELETE
.../issues/{n}/assignees`), post a polite comment explaining the policy,
     and **close without merging** any PRs authored by that person that
     reference the issue (find them via the issue's timeline
     `cross-referenced` events filtered to PRs and matching author).
2. **When a PR is opened that claims a protected issue** (trigger
   `pull_request_target: types: [opened, reopened]`): parse the PR body for
   claim refs ONLY - regex
   `(close|closes|closed|fix|fixes|fixed|resolve|resolves|resolved)\s+#\d+`
   (case-insensitive) so a `#N` in prose or code fences is ignored. If any
   referenced issue has either protected label and the author is experienced →
   close the PR without merging + comment. Skip owners/members/collaborators.
3. **Periodic sweep** (trigger `schedule: cron: "0 */6 * * *"` **and**
   `workflow_dispatch` so it can be run on demand). It is the backstop that
   catches everything the event triggers miss, so it must do three things:
   - **Assignment enforcement**: search all open protected issues (union of
     both labels - note `gh search issues` ANDs multiple `--label` flags, so
     run one search per label and `sort -u`), and for any assigned to a
     non-exempt experienced contributor, apply the same unassign + comment +
     close-linked-PRs logic. This catches issues labeled after assignment and
     unassign/reassign dodging.
   - **Retroactive PR-claim sweep**: enumerate every open PR, extract claim
     refs from the body (same regex as rule 2), and close any PR by an
     experienced non-exempt author that claims a protected issue. This closes
     PRs opened **before** the workflow existed and authors who became
     "experienced" after opening their PR - the event trigger alone never
     sees either case.
   - **Staleness release**: for a protected issue held by a **first-time**
     assignee, find their last `assigned` timeline event (dedupe by
     assignee), and if it is older than `GFI_STALE_DAYS` **and** they have no
     **open** PR referencing the issue, unassign them (comment with a
     `good-first-issue-stale` marker) so the issue is freed up. Never release
     an assignee who has an open PR on the issue.

## Hard security constraints (non-negotiable)

- `pull_request_target` runs with a write-scoped token on fork PRs, so the
  workflow **must never checkout or execute code from the PR**. It may only
  read issue/PR metadata and write comments/unassignments/closes. Keep it
  that way and say so in a header comment. This is also why shared logic is
  duplicated inline across jobs instead of being factored into a script file
  that would require a checkout.
- Pass any user-derived values to `gh` via environment variables or shell
  variables - never string-interpolate them into commands that could be
  injected.
- Guard every `gh` write call with `|| true` so a race (already-closed PR,
  already-unassigned) can't fail the job.
- Add `concurrency:` groups (per issue / per PR / one shared sweep group) so
  repeated events can't double-comment.

## Permissions

`permissions: { issues: write, pull-requests: write }` and run with
`GH_TOKEN: ${{ github.token }}`, `GH_REPO: ${{ github.repository }}`.

## Verification (required before finishing)

1. Confirm the YAML parses.
2. Extract each `run:` block and syntax-check with `bash -n`.
3. Dry-run the read-only logic against the real repo to confirm: the
   merged-PR count query returns `0`/`1` for known users, the claim-ref
   regex extracts the right issue numbers from real PR bodies, the timeline
   cross-reference query works, and the sweep searches (both labels, plus the
   open-PR enumeration) return results. Do NOT perform any write operations
   during verification.
4. Confirm commit-message style follows the repo's conventions
   (Conventional Commits) if committing.
