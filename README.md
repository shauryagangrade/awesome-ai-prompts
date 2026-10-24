# awesome-ai-prompts

![Build](https://github.com/shauryagangrade/awesome-ai-prompts/actions/workflows/ci.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Stars](https://img.shields.io/github/stars/shauryagangrade/awesome-ai-prompts?style=social)](https://github.com/shauryagangrade/awesome-ai-prompts)

A curated list of copy-paste AI prompts for **any developer who uses AI coding
agents**. Unlike most prompt lists, these aren't one-off hacks - they're
disciplined, **senior-engineer workflows that verify, don't guess**: read the
code before editing, small confirmed steps, and tests as guardrails. Paste one
into Claude, ChatGPT, Copilot, Cursor, opencode, or any agent and it takes
over.

Most list agents will happily _hallucinate_ a solution. These prompts are built
to stop that: every one demands evidence, the repo's own tooling, and a
verifiable result before it calls the work done.

**[★ Star on GitHub](https://github.com/shauryagangrade/awesome-ai-prompts)**

![Asking an AI coding agent to "explain this repo to me" and getting a shrug. Then a prompt from this repo is copied and pasted into opencode, which reads the code and reports every claim with file:line evidence](docs/demo.gif)

_The opening chat is staged. The rest is the real opencode run from [prompt-in-action.mp4](docs/media/prompt-in-action.mp4), sped up in places. Made with [openvidstudio](https://github.com/AnayDhawan/openvidstudio)._

[![Contributors](https://contrib.rocks/image?repo=shauryagangrade/awesome-ai-prompts&t=20261024)](https://github.com/shauryagangrade/awesome-ai-prompts/graphs/contributors)

Starring is the hello; a merged PR is the handshake. Every merged prompt PR
auto-appends its author to [CONTRIBUTORS.md](CONTRIBUTORS.md) - the avatars
above are the people who shaped this list.

Want it in video form? [Download the MP4](docs/media/prompt-in-action.mp4).

## Why these are different {#quality-standards}

- **Tool-agnostic** - works with Claude, ChatGPT, Copilot, Cursor, opencode,
  and anything else that reads a prompt. Nothing is tied to one vendor.
- **Verification-first** - "never guess; run the commands and prove it." A
  prompt's whole job is to keep the agent honest.
- **Two formats** - focused one-pagers for quick tasks, plus multi-section
  **[spec]** prompts with hard constraints and required verification for
  big, risky work. Spec prompts carry a light-blue badge in the index so you can
  spot them at a glance.
- **Self-contained** - everything you need is in one copy-paste block.

## Quick Start

1. Browse a category below and pick a prompt.
2. Open its `*-prompt.md`, then copy everything after the `---` divider.
3. Paste it into your AI coding agent along with your task - it handles the rest.

That's it. Here's the shape of it (from
[`feature-implementation-prompt.md`](core-coding/feature-implementation-prompt.md)):

```text
You are implementing a feature in this repository. Work end-to-end ...
1. Understand - Read the code this touches. Ask questions if ambiguous.
2. Plan - State your plan before writing code. Do not start until agreed.
3. Design to fit - Follow existing patterns. Prefer the boring option.
4. Implement - Smallest change that satisfies the requirement.
5. Test - Add tests that assert real behavior. Run the full suite.
6-8. Verify, document, self-review.
Rules: Never modify unrelated code. Verify before claiming. Small commits.
```

The agent handles the rest: reading code, planning, testing, and holding itself
accountable at every step.

## Staying in sync

Star this repo to get notified when new prompts land. Each addition goes under
[Unreleased](CHANGELOG.md) in the changelog and ships in a tagged release, so a
star is how you find out the list grew rather than a tip.

```bash
git clone https://github.com/shauryagangrade/awesome-ai-prompts.git
cd awesome-ai-prompts && git pull
```

If you already have the GitHub CLI authenticated, `gh repo clone shauryagangrade/awesome-ai-prompts` does the same in one step.

## Contributing

Contributions welcome. This catalog stays small and disciplined on purpose, so
the highest-value way to help is adding one good prompt to the right place, not
a pile of near-duplicates. Most contributions are new prompts; fixing a broken
link, a stale count, or a prompt whose instructions no longer hold is just as
welcome. AI-assisted contributions are welcome too - provided you (not the
agent) review the output, run the checks, and never let a claim stand without
verification. Full rules live in [CONTRIBUTING.md](CONTRIBUTING.md); the
section below is the same workflow, self-contained.

### What you can contribute

- A new prompt in a category folder that isn't already covered (the default)
- A fix to an existing prompt: clearer instructions, a rule that no longer
  holds, structure that drifted from the repo's conventions
- Repo hygiene: broken relative links, a stale `## [Unreleased]` changelog,
  a mismatched Contents count
- A [bug report](.github/ISSUE_TEMPLATE/bug_report.yml) or
  [feature request](.github/ISSUE_TEMPLATE/feature_request.yml) when something
  here is wrong or missing

Newcomers should start by scanning the
[`good first issue`](https://github.com/shauryagangrade/awesome-ai-prompts/labels/good%20first%20issue)
label. Beyond the raw files, every prompt here is also a workflow you can reuse,
so issues often ask for new prompts, which is the fastest way to see your work
used.

## Usage in the wild

Real projects are the best proof these prompts work, so we collect short
before/after stories from the people who actually used one: the task, the
prompt used, what the agent did, and the verified result. Evidence only, no
testimonials.

- [Removing an invalid data indicator](docs/usage-stories/ucip-elderly-indicator-removal.md) - a data indicator proved to be a district dummy, and removing it cascaded through 83 files. Used `code-review/secure-code-review-prompt.md`.
- [IPv6 rate limiting bypass](docs/usage-stories/tourneyradar-api-ipv6-ratelimit.md) - a rate limiter keyed on the full IPv6 address, so rotating addresses bypassed it. No prompt from this repo was used here, so it is a case study rather than prompt evidence.

See [docs/usage-stories/TEMPLATE.md](docs/usage-stories/TEMPLATE.md)
for the template, and open a PR (or a
[discussion](https://github.com/shauryagangrade/awesome-ai-prompts/discussions))
with your story.

---

## Translations

English is the source of truth and stays the only version that appears in the
[one-page catalog](#printable-one-page-catalog). Translated prompts live under
`i18n/<lang>/`, mirroring the category folders, and each language keeps a
README with its own status table.

- [Spanish](i18n/es/README.md) - not started yet

We do not machine-translate these prompts. A prompt body is a set of
instructions an agent follows literally, not prose: "delete the staging branch"
and "never delete the staging branch" are one word apart and produce opposite
actions, and no gate can tell afterwards that a translation inverted a rule.
Every translation is written and tested by a person. See
[CONTRIBUTING.md](CONTRIBUTING.md#translations) if you want to add one.

---

### Quick start with an AI agent

The four prompts in the [Contributing to this repo](#contributing-to-this-repo)
category encode every rule below. Paste one into your agent and it takes the
work from idea to a mergeable pull request without you memorizing the checklist:

- [new-prompt-contribution-prompt.md](a-a-p-contributing/new-prompt-contribution-prompt.md) -
  draft a new prompt: conventions, index, changelog, gates, PR
- [prompt-pr-review-prompt.md](a-a-p-contributing/prompt-pr-review-prompt.md) -
  review a prompt PR against the real gates before you merge or comment
- [resolve-open-issue-prompt.md](a-a-p-contributing/resolve-open-issue-prompt.md) -
  take an open issue from ticket to mergeable PR
- [fix-reported-bug-prompt.md](a-a-p-contributing/fix-reported-bug-prompt.md) -
  fix a reported bug with reproduction, root cause, and proof

**Want a PR in under 10 minutes?** Pick a
[`good first issue`](https://github.com/shauryagangrade/awesome-ai-prompts/labels/good%20first%20issue),
then paste
[resolve-open-issue-prompt.md](a-a-p-contributing/resolve-open-issue-prompt.md)
into any agent with the issue number. It runs the whole pipeline itself -
reading the conventions, drafting under the `---` divider, syncing the index
and changelog, and passing every gate - so the PR comes out mergeable on the
first pass. External PRs get a maintainer response within 48 hours.

If you would rather do it by hand, the steps below are the same workflow.

### Adding a new prompt, step by step

1. **Read the room** - Read [CONTRIBUTING.md](CONTRIBUTING.md),
   [.github/PROMPT_TEMPLATE.md](.github/PROMPT_TEMPLATE.md), and two or three
   existing prompts in the category you intend to use. Note the exact shape: an
   H1 title, a short copy-paste usage note, a `---` divider, then the prompt
   body.
2. **Confirm the idea is new** - Search the catalog and README for the closest
   existing prompts and say how yours differs. A contribution that duplicates
   an existing prompt will be bounced; bring a gap, not a copy.
3. **Fork and branch** - Fork the repo, clone, and create a feature branch off
   the default branch such as `git checkout -b docs/add-my-prompt`.
4. **Write the file** - Name it `kebab-case-action-prompt.md` and place it in
   the matching category folder (never the repo root). Structure:

   ```text
   # Reusable prompt: <short action title>

   One or two lines explaining what to paste this into.

   ---

   The prompt body itself: numbered ## Steps with bold lead-ins, a ## Rules
   list, and a ## Verification section that names actual commands. Every
   claim must be checkable - "verify, don't guess".
   ```

   Style rules: tool-agnostic (Claude, ChatGPT, Copilot, Cursor, opencode, and
   others); self-contained (everything the user pastes lives below the
   divider); ASCII hyphens only - no em dashes anywhere in the file.

5. **Sync the index** - Add a one-line entry in the matching README category
   section, format `<name>.md` link followed by a hyphen and a short
   description ending in a period. Bump that category's count in the
   [Contents](#contents) list. Add the same one-line entry to that folder's
   own `README.md` (every category folder has one). If the prompt takes on a
   big, risky task, mark its entry with the violet [spec] badge
   (`<img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">`) and bump the
   spec-count badge on the category's Contents line.
6. **Add a changelog entry** - Under `## [Unreleased]` in
   [CHANGELOG.md](CHANGELOG.md), add a line naming the file in backticks, then
   a hyphen, then a short description.
7. **Run the gates locally** - All three must pass before you push:

   ```bash
   bash scripts/check-links.sh
   bash scripts/check-consistency.sh
   npx --yes markdownlint-cli2@0.17.2 <changed-files>
   ```

   The em-dash scan must also be clean:

   ```bash
   EM="$(python3 -c 'print("\u2014")')"
   git grep -I -l "$EM"
   ```

   Empty output means no em dashes. Actually run these and look at the output;
   saying "it passes" without running it is exactly the failure mode these
   prompts exist to stop.

8. **Commit and open a PR** - Commit with a conventional message, for example
   `docs: add <name> prompt`, push the branch, and open a pull request against
   `main` using [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md).
   Fill in the checklist honestly; the commit-checklist workflow checks it
   either way.

### What CI enforces

One workflow, [ci.yml](.github/workflows/ci.yml), runs on every push to `main`
and every pull request, split into parallel jobs: markdownlint + prettier, docs
structure and em-dash checks, README/CHANGELOG consistency, typos +
editorconfig, shellcheck + ruff, actionlint + zizmor, gitleaks secret scan,
cffconvert validation, unit tests, and a PR-only check of newly added external
links. The full gate list with the exact commands is in
[CONTRIBUTING.md](CONTRIBUTING.md#automated-gates).

The `Commit checklist` workflow separately enforces that the PR title follows
[Conventional Commits](https://www.conventionalcommits.org/).

CI runs the same scripts you run locally, so a green local pass means a green
CI pass.

### Printable one-page catalog

For workshops, printing, or browsing the whole corpus on one page, open
[website/index.html](website/index.html) - every prompt, a linked mini-TOC,
and a one-click copy button on each card. The same build generates the whole
[awesome-ai-prompts.vercel.app](https://awesome-ai-prompts.vercel.app) site in
[website/](website/), one folder holding everything that gets deployed:

- `website/index.html` - the full catalog, served at the site root.
- `website/category/<cat>.html` - one index page per category, at
  `/category/<cat>`.
- `website/prompt/<cat>/<slug>.html` - one page per prompt, at
  `/prompt/<cat>/<slug>`, with the intro and the full prompt block behind a
  copy button.
- `website/sitemap.xml`, `website/robots.txt`, and `website/llms.txt` - crawler
  and agent entry points (llms.txt is a Markdown index of the catalog per the
  llmstxt.org convention).

Every page carries a unique title, meta description, canonical URL, Open
Graph and Twitter card tags, and JSON-LD structured data. To regenerate the
whole site after the catalog changes:

```bash
python3 scripts/build-all.py
```

All pages are committed so static hosts can serve them directly - the repo's
[vercel.json](vercel.json) rewrites the clean public URLs onto the files in
`website/`. CI runs `python3 scripts/build-all.py --check`, which fails if the
builder becomes non-deterministic or any committed page drifts out of sync.

### Guidelines

- One logical change per PR: one prompt, one fix, or one rename. Reviews stay
  reviewable and reverts stay simple.
- Never claim a check passed without running it and seeing the output. These
  prompts are built on verified work, not asserted work.
- Keep changes minimal: no unrelated wording edits, formatting churn, or
  dependency bumps mixed into a contribution.
- If a rule is ambiguous, ask in the issue or PR instead of guessing.
- Questions and discussion happen in
  [GitHub Discussions](https://github.com/shauryagangrade/awesome-ai-prompts/discussions).

## Contents

Prompts tagged with the light-blue badge are the heavyweight [spec] prompts
described above.

- [Contributing to this repo](#contributing-to-this-repo) (6) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">
- [Core coding](#core-coding) (20) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">
- [System design](#system-design) (7) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">
- [Git & GitHub](#git--github) (14) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">
- [Code review & quality](#code-review--quality) (6) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">
- [Testing & quality](#testing--quality) (10) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">
- [Docs & delivery](#docs--delivery) (7)
- [Security & performance](#security--performance) (13) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">
- [DevOps & deploy](#devops--deploy) (15)
- [Career & learning](#career--learning) (8)
- [Frontend & UI](#frontend--ui) (13) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">
- [Data & AI](#data--ai) (13) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">
- [Mobile development](#mobile-development) (8) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">
- [System & Exploration](#system--exploration) (4) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">

## Contributing to this repo

- [new-prompt-contribution-prompt.md](a-a-p-contributing/new-prompt-contribution-prompt.md) - add a new prompt to this repo: conventions, draft, index, changelog, gates, PR.
- [prompt-pr-review-prompt.md](a-a-p-contributing/prompt-pr-review-prompt.md) - review a prompt PR against the repo's real gates with an explicit verdict.
- [resolve-open-issue-prompt.md](a-a-p-contributing/resolve-open-issue-prompt.md) - take an open issue from ticket to a mergeable PR.
- [fix-reported-bug-prompt.md](a-a-p-contributing/fix-reported-bug-prompt.md) - fix a reported bug with reproduction, root cause, and proof.
- [one-pager-schema-prompt.md](a-a-p-contributing/one-pager-schema-prompt.md) - the repo's one-pager format as a schema: field contract, size budget, and checks for authoring quick-task prompts.
- [spec-prompt-schema-prompt.md](a-a-p-contributing/spec-prompt-schema-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - the repo's spec format as a schema: what earns the badge, the mandatory field contract, and evidence-gated verification.

## Core coding

- [feature-implementation-prompt.md](core-coding/feature-implementation-prompt.md) - build a feature end-to-end: understand, plan, implement, test, document.
- [pair-programming-session-prompt.md](core-coding/pair-programming-session-prompt.md) - interactive build loop: plan → code → explain → verify, in small confirmed steps.
- [debugging-prompt.md](core-coding/debugging-prompt.md) - systematic debugging: reproduce, isolate, root-cause, minimal fix, regression test.
- [refactoring-prompt.md](core-coding/refactoring-prompt.md) - behavior-preserving refactoring with tests as the safety net.
- [human-codebase-onboarding-prompt.md](core-coding/human-codebase-onboarding-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - understand an unfamiliar repo at verification depth: stack, architecture, data flow, conventions, gotchas, with file:line evidence.
- [agent-codebase-onboarding-prompt.md](core-coding/agent-codebase-onboarding-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - onboard an agent into an unfamiliar repo with no human in the loop: a token-budgeted protocol, a compact in-context model, and required verification.
- [api-integration-prompt.md](core-coding/api-integration-prompt.md) - integrate a REST API with types, error handling, retries, and tests.
- [api-design-prompt.md](core-coding/api-design-prompt.md) - design a well-structured REST API with OpenAPI spec, conventions, and validation.
- [database-design-prompt.md](core-coding/database-design-prompt.md) - model a relational schema from requirements with normalization, indexes, and migration path.
- [environment-setup-prompt.md](core-coding/environment-setup-prompt.md) - bootstrap a dev environment from scratch: deps, tooling, config, first-run verification.
- [code-migration-prompt.md](core-coding/code-migration-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - migrate code between frameworks/languages with behavior parity and incremental verification.
- [cli-tool-build-prompt.md](core-coding/cli-tool-build-prompt.md) - build a well-behaved CLI: documented flags, typed exit codes, safe pipe and TTY handling, testable core.
- [datetime-timezone-correctness-prompt.md](core-coding/datetime-timezone-correctness-prompt.md) - store UTC render local, handle DST, and get calendar/duration math right.
- [error-handling-strategy-prompt.md](core-coding/error-handling-strategy-prompt.md) - one coherent error policy: typed errors, context-rich logs, retry vs surface, proven by failure injection.
- [regular-expressions-prompt.md](core-coding/regular-expressions-prompt.md) - write or repair a regex with a stated purpose, a test corpus, and a check that it cannot hang on adversarial input.
- [file-uploads-media-handling-prompt.md](core-coding/file-uploads-media-handling-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - take uploads that survive hostile files, traversal, and unreliable networks: server-side validation, streaming, safe storage names, resumable transfers.
- [graphql-api-design-prompt.md](core-coding/graphql-api-design-prompt.md) - design a GraphQL schema that scales past the demo: batching over N+1, field-level authz, bounded complexity, stable error shape.
- [websockets-realtime-features-prompt.md](core-coding/websockets-realtime-features-prompt.md) - build realtime that survives disconnects and horizontal scaling: lifecycle, message contract, stated delivery guarantee, slow-client policy.
- [payment-integration-prompt.md](core-coding/payment-integration-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - add payments with money-grade discipline: no raw card data, idempotent mutations, verified webhooks, reconciliation.
- [email-delivery-prompt.md](core-coding/email-delivery-prompt.md) - send transactional mail that lands: domain authentication, code templates, async retries, bounce and complaint handling.

## System design

- [system-design-prompt.md](system-design/system-design-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - design a scalable system end-to-end: requirements, components, tradeoffs, failure modes, phased build.
- [adr-writing-prompt.md](system-design/adr-writing-prompt.md) - record a technical decision as a two-minute ADR: context, options, consequences.
- [technical-debt-triage-prompt.md](system-design/technical-debt-triage-prompt.md) - inventory tech debt with evidence and get a prioritized paydown plan.
- [concurrency-debugging-prompt.md](system-design/concurrency-debugging-prompt.md) - hunt race conditions and deadlocks: prove the interleaving, minimal fix, stress-verified.
- [caching-strategy-prompt.md](system-design/caching-strategy-prompt.md) - add caching that pays for itself: measured wins, invalidation designed up front.
- [message-queues-event-driven-design-prompt.md](system-design/message-queues-event-driven-design-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - design event-driven systems for duplicates, reordering, and replays: versioned contracts, ordering keys, idempotent consumers, DLQ operations.
- [legacy-code-modernization-assessment-prompt.md](system-design/legacy-code-modernization-assessment-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - decide whether to modernize at all: EOL inventory, value-risk map, strangler seams, characterization tests, stop conditions.

## Git & GitHub

- [git-history-surgery-prompt.md](git-github/git-history-surgery-prompt.md) - safe history editing, bisect, blame, and recovery via reflog.
- [open-source-contribution-prompt.md](git-github/open-source-contribution-prompt.md) - contribute to an OSS repo the maintainer-friendly way.
- [ci-cd-workflow-prompt.md](git-github/ci-cd-workflow-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - build a verified, secure GitHub Actions pipeline.
- [dependency-upgrade-prompt.md](git-github/dependency-upgrade-prompt.md) - upgrade a dependency safely: changelog, migration, full verification.
- [good-first-issue-workflow-prompt.md](git-github/good-first-issue-workflow-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - GitHub Actions workflow reserving starter issues for first-time contributors.
- [git-bisect-debug-prompt.md](git-github/git-bisect-debug-prompt.md) - use git bisect to find the exact commit that introduced a bug.
- [release-automation-prompt.md](git-github/release-automation-prompt.md) - automate versioning, tagging, changelogs, and publishing with CI.
- [commit-checklist-prompt.md](git-github/commit-checklist-prompt.md) - build deterministic PR gates that keep indexes, changelogs, and counts in sync.
- [pr-review-prompt.md](git-github/pr-review-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - thorough PR review: verify claims, run checks, clear verdict, merge-ready.
- [issue-triage-for-maintainers-prompt.md](git-github/issue-triage-for-maintainers-prompt.md) - turn an untriaged backlog into labeled, prioritized, answerable queues.
- [issue-resolving-prompt.md](git-github/issue-resolving-prompt.md) - resolve a GitHub issue end-to-end: reproduce the failure, prove the root cause, land a minimal fix with a regression test, and verify against the project's checks.
- [open-source-maintainer-survival-prompt.md](git-github/open-source-maintainer-survival-prompt.md) - harden maintenance practices: guidelines, automation, kind declines, bus factor, handoff.
- [local-pr-cleanup-prompt.md](git-github/local-pr-cleanup-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - full local hygiene after complex PR work: branches, worktrees, stashes, and build artifacts.
- [remote-pr-cleanup-prompt.md](git-github/remote-pr-cleanup-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - full remote hygiene after complex PR work: prune remotes, delete merged PR branches, sync with upstream.

## Code review & quality

- [secure-code-review-prompt.md](code-review/secure-code-review-prompt.md) - security-lens review: injection, authz, data exposure, with evidence.
- [performance-review-prompt.md](code-review/performance-review-prompt.md) - review code for performance anti-patterns with evidence and specific fixes.
- [accessibility-review-prompt.md](code-review/accessibility-review-prompt.md) - audit UI code for WCAG compliance: semantics, keyboard nav, contrast, screen readers.
- [architecture-review-prompt.md](code-review/architecture-review-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - audit architecture with evidence-backed 0-10 scores, file:line findings, and a prioritized refactoring roadmap.
- [codebase-audit-prompt.md](code-review/codebase-audit-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - audit a codebase as a senior architect: evidence-backed 0-10 scores, structural smell identification, and a prioritized refactoring roadmap.
- [data-model-review-prompt.md](code-review/data-model-review-prompt.md) - review schema, migrations, indexes, and integrity with evidence.

## Testing & quality

- [bug-finder-prompt.md](testing-quality/bug-finder-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - sweep a codebase across correctness factors and get a clear, evidence-backed, priority-ordered list of bugs.
- [bug-finder-with-docs-prompt.md](testing-quality/bug-finder-with-docs-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - find bugs and leave a durable bug ledger behind: a priority-ordered report plus BUGS.md and README pointers, with the code untouched.
- [test-writing-prompt.md](testing-quality/test-writing-prompt.md) - write tests that catch regressions, not ones that pad coverage.
- [test-driven-development-prompt.md](testing-quality/test-driven-development-prompt.md) - strict red → green → refactor discipline.
- [code-coverage-gap-prompt.md](testing-quality/code-coverage-gap-prompt.md) - find risky untested paths and cover them meaningfully.
- [e2e-test-scaffold-prompt.md](testing-quality/e2e-test-scaffold-prompt.md) - scaffold end-to-end/integration tests with realistic fixtures and CI integration.
- [mutation-testing-prompt.md](testing-quality/mutation-testing-prompt.md) - run mutation testing to validate that tests actually catch real defects.
- [contract-testing-prompt.md](testing-quality/contract-testing-prompt.md) - consumer-driven contract tests so API drift fails CI, not production.
- [chaos-resilience-prompt.md](testing-quality/chaos-resilience-prompt.md) - inject failures and close the gaps: timeouts, backoff, graceful degradation.
- [property-based-testing-prompt.md](testing-quality/property-based-testing-prompt.md) - write property-based tests with generated inputs and shrink evidence.

## Docs & delivery

- [documentation-writer-prompt.md](docs-delivery/documentation-writer-prompt.md) - accurate, verified docs that match the project's voice.
- [architecture-documentation-prompt.md](docs-delivery/architecture-documentation-prompt.md) - write architecture docs with evidence, tradeoffs, and verification.
- [release-notes-changelog-prompt.md](docs-delivery/release-notes-changelog-prompt.md) - turn git history into a clear, honest changelog.
- [api-documentation-prompt.md](docs-delivery/api-documentation-prompt.md) - generate OpenAPI/Swagger docs from existing code with accurate schemas.
- [readme-builder-prompt.md](docs-delivery/readme-builder-prompt.md) - build a comprehensive README from scratch: purpose, quickstart, examples.
- [inline-documentation-prompt.md](docs-delivery/inline-documentation-prompt.md) - add JSDoc/docstrings to existing code: accurate, concise, non-redundant.
- [migration-guide-prompt.md](docs-delivery/migration-guide-prompt.md) - write a migration guide: preconditions, steps, rollback, verification, common failures.

## Security & performance

- [security-audit-prompt.md](security-performance/security-audit-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - full-repo audit: injection, auth, secrets, dependencies, with verified findings.
- [performance-optimization-prompt.md](security-performance/performance-optimization-prompt.md) - measure-first optimization with before/after proof.
- [secrets-management-prompt.md](security-performance/secrets-management-prompt.md) - audit and remediate hardcoded secrets, set up env-based secret management.
- [load-testing-prompt.md](security-performance/load-testing-prompt.md) - design and run load/stress tests with measurable thresholds.
- [dependency-audit-prompt.md](security-performance/dependency-audit-prompt.md) - audit dependencies for vulnerabilities, license issues, and staleness.
- [threat-modeling-prompt.md](security-performance/threat-modeling-prompt.md) - STRIDE-style threat model ranked by real risk, with verified mitigations.
- [auth-implementation-prompt.md](security-performance/auth-implementation-prompt.md) - implement sessions/OAuth/JWT safely with server-side authorization everywhere.
- [memory-leak-hunting-prompt.md](security-performance/memory-leak-hunting-prompt.md) - find and remove a leak from measurements: baseline, reproduced growth, diffed snapshots, and a flat after-curve.
- [dependency-vuln-triage-prompt.md](security-performance/dependency-vuln-triage-prompt.md) - triage dependency vulnerability reports: reachability proof, exploitability rating, cheapest verified fix.
- [secrets-scanning-response-prompt.md](security-performance/secrets-scanning-response-prompt.md) - respond to a leaked secret: rotate first, find copies, assess misuse, plan cleanup, prevent recurrence.
- [prompt-injection-defense-prompt.md](security-performance/prompt-injection-defense-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - threat-model one attack class: where untrusted text reaches the context, out-of-band tool gating, a red-team suite, honest residual risk.
- [privacy-gdpr-compliance-review-prompt.md](security-performance/privacy-gdpr-compliance-review-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - systematic privacy pass: data inventory with retention, lawful basis, consent withdrawal, user rights flows, processors, ranked minimization.
- [rate-limiting-abuse-prevention-prompt.md](security-performance/rate-limiting-abuse-prevention-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - protect public endpoints: limits tiered by cost, algorithm chosen for the traffic shape, shared counters, load-test proof.

## DevOps & deploy

- [docker-containerization-prompt.md](devops-deploy/docker-containerization-prompt.md) - small, secure, non-root container images.
- [deployment-runbook-prompt.md](devops-deploy/deployment-runbook-prompt.md) - safe deploys with preflight checks and a rollback plan.
- [infrastructure-as-code-prompt.md](devops-deploy/infrastructure-as-code-prompt.md) - Terraform/CDK with least-privilege IAM and state safety.
- [database-schema-migrations-prompt.md](devops-deploy/database-schema-migrations-prompt.md) - backward-compatible schema changes: expand, migrate, contract.
- [monitoring-observability-prompt.md](devops-deploy/monitoring-observability-prompt.md) - set up logging, metrics, and alerting with actionable dashboards.
- [incident-response-prompt.md](devops-deploy/incident-response-prompt.md) - debug a live incident or write a post-mortem with structured triage.
- [kubernetes-deployment-prompt.md](devops-deploy/kubernetes-deployment-prompt.md) - deploy to Kubernetes securely: real probes, zero-downtime rollouts, non-root pods.
- [feature-flag-rollout-prompt.md](devops-deploy/feature-flag-rollout-prompt.md) - ship behind flags with progressive rollout, kill switch, and cleanup plan.
- [backup-disaster-recovery-prompt.md](devops-deploy/backup-disaster-recovery-prompt.md) - backups proven by restore drills plus a scenario-based DR runbook with RTO/RPO.
- [background-jobs-scheduled-tasks-prompt.md](devops-deploy/background-jobs-scheduled-tasks-prompt.md) - async work that survives duplicates and deploys: idempotent handlers, bounded retries, dead-letter path, queue metrics, graceful drain.
- [cloud-cost-optimization-prompt.md](devops-deploy/cloud-cost-optimization-prompt.md) - cut the bill from measurement: ranked offenders, rightsizing off real utilization, lifecycle policies, before/after savings table.
- [capacity-planning-prompt.md](devops-deploy/capacity-planning-prompt.md) - name the wall and the date: headroom per bottleneck, forecast off a product metric, dated scaling options, early alerts.
- [ci-gate-diagnosis-prompt.md](devops-deploy/ci-gate-diagnosis-prompt.md) - diagnose a failing CI gate: read the real log, compare with base branch, recommend one action with evidence.
- [incident-postmortem-prompt.md](devops-deploy/incident-postmortem-prompt.md) - evidence-based postmortem: timeline, contributing factors, action items with owners, lessons.
- [infra-drift-detection-prompt.md](devops-deploy/infra-drift-detection-prompt.md) - find live infrastructure drift vs IaC: refresh-only, classify differences, approve before any apply.

## Career & learning

- [code-interview-practice-prompt.md](career-learning/code-interview-practice-prompt.md) - structured interview coaching with hints on demand.
- [portfolio-project-prompt.md](career-learning/portfolio-project-prompt.md) - shape an idea into a scoped, presentable portfolio project.
- [resume-review-prompt.md](career-learning/resume-review-prompt.md) - review a technical resume: impact bullets, keyword density, honesty.
- [tech-blog-writer-prompt.md](career-learning/tech-blog-writer-prompt.md) - turn a project or technical concept into a clear, engaging blog post.
- [learning-roadmap-prompt.md](career-learning/learning-roadmap-prompt.md) - turn a skill gap into a project-based roadmap with verifiable checkpoints.
- [conference-talk-proposal-prep-prompt.md](career-learning/conference-talk-proposal-prep-prompt.md) - write a competitive CFP and rehearse the talk: hook, takeaway, timed outline, demo fallbacks.
- [mentoring-feedback-prompt.md](career-learning/mentoring-feedback-prompt.md) - give structured, verifiable feedback to a junior engineer with evidence.
- [interview-debugging-drill-prompt.md](career-learning/interview-debugging-drill-prompt.md) - coaching a real debugging session: reproduce, form/test hypotheses, prove root cause, minimal fix, regression test, explain thinking.

## Frontend & UI

- [component-build-prompt.md](frontend-ui/component-build-prompt.md) - build a reusable, accessible UI component with props, variants, and stories.
- [responsive-design-prompt.md](frontend-ui/responsive-design-prompt.md) - audit and implement responsive layouts: breakpoints, fluid grids, mobile-first.
- [state-management-prompt.md](frontend-ui/state-management-prompt.md) - give every piece of client state one home; compute derived data, delete sync bugs.
- [web-performance-vitals-prompt.md](frontend-ui/web-performance-vitals-prompt.md) - fix Core Web Vitals from measurements: LCP, INP, CLS with before/after proof.
- [i18n-localization-prompt.md](frontend-ui/i18n-localization-prompt.md) - internationalize properly: extracted strings, ICU plurals, RTL, pseudo-locale testing.
- [website-seo-prompt.md](frontend-ui/website-seo-prompt.md) - technical SEO audit: crawlability, canonicalization, metadata, structured data, redirects, and speed - with verification at every step.
- [instagram-carousel-prompt.md](frontend-ui/instagram-carousel-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - turn this repo into a branded, swipeable Instagram carousel delivered as self-contained 1080x1080 HTML slides, mirroring the repo's brand identity.
- [ui-audit-prompt.md](frontend-ui/ui-audit-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - audit UI for visual consistency, design system adherence, spacing, typography, and responsive behavior with concrete fixes and file:line evidence.
- [design-handoff-prompt.md](frontend-ui/design-handoff-prompt.md) - turn a mockup into token-aligned, responsive code with a screenshot comparison loop.
- [design-tokens-theming-prompt.md](frontend-ui/design-tokens-theming-prompt.md) - theming that survives dark mode and a rebrand: token taxonomy, primitive to semantic to component layers, per-pair contrast, a migration off hardcoded values.
- [animation-performance-prompt.md](frontend-ui/animation-performance-prompt.md) - motion that stays smooth on a mid-range phone: only transform and opacity, long frames profiled, reduced motion respected, frame rate measured before and after.
- [browser-extension-development-prompt.md](frontend-ui/browser-extension-development-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - build an extension that passes review: manifest v3, minimum permissions, background worker versus content script, CSP and no-remote-code, load-unpacked loop.
- [pwa-offline-support-prompt.md](frontend-ui/pwa-offline-support-prompt.md) - offline-first done explicitly: service worker lifecycle, cache versioning, per-resource caching strategy, queued mutations, update-in-place, Lighthouse proof.

## Mobile development

- [mobile-app-develop-prompt.md](mobile-dev/mobile-app-develop-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - build a mobile feature and prove it works on both platforms: offline, permissions, deep links, lifecycle, with a platform verification matrix.
- [mobile-performance-prompt.md](mobile-dev/mobile-performance-prompt.md) - find and fix mobile performance from measurements: startup, frame rate, app size, memory, network.
- [mobile-ui-audit-prompt.md](mobile-dev/mobile-ui-audit-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - audit a mobile UI against platform conventions: touch targets, safe areas, accessibility, states, theming, with file:line fixes.
- [mobile-ui-audit-fix-prompt.md](mobile-dev/mobile-ui-audit-fix-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - remediate every finding from a mobile UI audit (AUDIT.md) with evidence-backed fixes, verification matrix, and behavior guard.
- [mobile-ui-overhaul-prompt.md](mobile-dev/mobile-ui-overhaul-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - overhaul a mobile UI end-to-end: target design spec, token layer, reimplemented screens, with before/after proof on every platform.
- [website-to-mobile-app-prompt.md](mobile-dev/website-to-mobile-app-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - turn a website into a mobile app, choosing the adaptation strategy from the site's actual architecture: wrapper vs shared-logic vs native.
- [mobile-app-project-setup-prompt.md](mobile-dev/mobile-app-project-setup-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - bootstrap a new mobile app: argued stack choice, feature-based structure, navigation skeleton, both platforms building from a clean clone on CI.
- [push-notifications-deep-links-prompt.md](mobile-dev/push-notifications-deep-links-prompt.md) - implement notifications and deep links with permission and routing verification.

## Data & AI

- [data-pipeline-prompt.md](data-ai/data-pipeline-prompt.md) - build ETL pipelines that fail loudly, resume cleanly, and prove their output.
- [sql-query-optimization-prompt.md](data-ai/sql-query-optimization-prompt.md) - make slow queries fast with plans before/after and justified indexes.
- [rag-pipeline-prompt.md](data-ai/rag-pipeline-prompt.md) - build retrieval-augmented generation with citations and eval numbers before shipping.
- [llm-feature-eval-prompt.md](data-ai/llm-feature-eval-prompt.md) - evaluate LLM features with a held-out test set and pre-committed thresholds.
- [ai-agent-build-prompt.md](data-ai/ai-agent-build-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - design and build an LLM agent: tool contracts, context strategy, guardrails, eval set, cost and latency budget.
- [csv-spreadsheet-wrangling-prompt.md](data-ai/csv-spreadsheet-wrangling-prompt.md) - clean messy CSV/spreadsheet exports with encoding detection, explicit type overrides, and a validation report.
- [responsible-web-scraping-prompt.md](data-ai/responsible-web-scraping-prompt.md) - scrape within robots.txt/ToS with resilient selectors, checkpointed crawls, and politeness budgets.
- [data-visualization-prompt.md](data-ai/data-visualization-prompt.md) - charts that are honest and accessible: type matched to the question, honest axes, color-blind-safe plus a second encoding, checked against source numbers.
- [ab-test-design-analysis-prompt.md](data-ai/ab-test-design-analysis-prompt.md) - experiments you can trust: hypothesis and metric fixed first, power calculation, contamination checks, stopping rules, effect size with intervals.
- [analytics-event-tracking-prompt.md](data-ai/analytics-event-tracking-prompt.md) - instrumentation that does not rot: tracking plan as source of truth, machine-readable schema, pre-send validation, PII minimized, delivery proven.
- [ml-model-deployment-basics-prompt.md](data-ai/ml-model-deployment-basics-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - from notebook to service: versioned artifacts, validated inference API, measured latency, drift triggers, a rehearsed rollback.
- [fine-tune-vs-rag-vs-prompting-decision-prompt.md](data-ai/fine-tune-vs-rag-vs-prompting-decision-prompt.md) - pick the cheapest sufficient LLM technique: requirements first, evidence-backed matrix, eval plan that could disprove it, reversal criteria.
- [data-quality-validation-prompt.md](data-ai/data-quality-validation-prompt.md) - define data contracts, checks, and failure response for pipelines.

## System & Exploration

- [drive-space-investigator-prompt.md](system-and-exploration/drive-space-investigator-prompt.md) <img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - Strictly read-only drive space investigator that scans near-capacity disks, finds largest files and waste/regenerable items, and produces a comprehensive, review-only report.
- [dead-code-detection-prompt.md](system-and-exploration/dead-code-detection-prompt.md) - find dead code with proof: tool output as candidates only, reference search recorded, dynamic use ruled out before deletion.
- [entrypoints-discovery-prompt.md](system-and-exploration/entrypoints-discovery-prompt.md) - discover runtime entrypoints: servers, CLIs, workers, scheduled jobs, environment/config requirements, connection mapping.
- [impact-analysis-prompt.md](system-and-exploration/impact-analysis-prompt.md) - evaluate change impact before applying: scope, affected paths, risk, verification plan, rollback criteria.
