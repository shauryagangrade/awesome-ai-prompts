# awesome-ai-prompts

![Build](https://github.com/shauryagangrade/awesome-ai-prompts/actions/workflows/ci.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Stars](https://img.shields.io/github/stars/shauryagangrade/awesome-ai-prompts?style=social)](https://github.com/shauryagangrade/awesome-ai-prompts)

A curated list of copy-paste AI prompts for **student developers who use AI
coding agents**. Unlike most prompt lists, these aren't one-off hacks - they're
disciplined, **senior-engineer workflows that verify, don't guess**: read the
code before editing, small confirmed steps, and tests as guardrails. Paste one
into Claude, ChatGPT, Copilot, Cursor, opencode, or any agent and it takes
over.

Most list agents will happily _hallucinate_ a solution. These prompts are built
to stop that: every one demands evidence, the repo's own tooling, and a
verifiable result before it calls the work done.

**[★ Star on GitHub](https://github.com/shauryagangrade/awesome-ai-prompts)**

![Browsing the repo, copying a codebase-onboarding spec prompt, pasting it into opencode, and watching the agent read the codebase with file:line citations](docs/media/prompt-in-action.gif)

Want it in video form? [Download the MP4](docs/media/prompt-in-action.mp4).

## Why these are different {#quality-standards}

- **Tool-agnostic** - works with Claude, ChatGPT, Copilot, Cursor, opencode,
  and anything else that reads a prompt. Nothing is tied to one vendor.
- **Verification-first** - "never guess; run the commands and prove it." A
  prompt's whole job is to keep the agent honest.
- **Two formats** - focused one-pagers for quick tasks, plus multi-section
  **[spec]** prompts with hard constraints and required verification for
  big, risky work.
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
   [Contents](#contents) list. If the prompt takes on a big, risky task, mark
   its entry with `[spec]`.
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

Two workflows run on every push to `main` and every pull request:

- [docs-lint](.github/workflows/ci.yml) - markdown lint on every `*.md`,
  README relative links must resolve, no em dashes in any tracked file, and
  shellcheck on every `*.sh`.
- [commit-checklist](.github/workflows/commit-checklist.yml) - every
  `*-prompt.md` in a category folder must be linked from the README, new
  prompts need a `## [Unreleased]` changelog entry, category folders and
  README sections must stay in sync in both directions, the Contents counts
  must match the files on disk, and the PR title must follow
  [Conventional Commits](https://www.conventionalcommits.org/).

Both run the same scripts you run locally, so a green local pass means a green
CI pass.

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

- [Contributing to this repo](#contributing-to-this-repo) (4)
- [Core coding](#core-coding) (11)
- [System design](#system-design) (5)
- [Git & GitHub](#git--github) (10)
- [Code review & quality](#code-review--quality) (3)
- [Testing & quality](#testing--quality) (9)
- [Docs & delivery](#docs--delivery) (5)
- [Security & performance](#security--performance) (7)
- [DevOps & deploy](#devops--deploy) (9)
- [Career & learning](#career--learning) (5)
- [Frontend & UI](#frontend--ui) (8)
- [Data & AI](#data--ai) (6)

## Contributing to this repo

- [new-prompt-contribution-prompt.md](a-a-p-contributing/new-prompt-contribution-prompt.md) - add a new prompt to this repo: conventions, draft, index, changelog, gates, PR.
- [prompt-pr-review-prompt.md](a-a-p-contributing/prompt-pr-review-prompt.md) - review a prompt PR against the repo's real gates with an explicit verdict.
- [resolve-open-issue-prompt.md](a-a-p-contributing/resolve-open-issue-prompt.md) - take an open issue from ticket to a mergeable PR.
- [fix-reported-bug-prompt.md](a-a-p-contributing/fix-reported-bug-prompt.md) - fix a reported bug with reproduction, root cause, and proof.

## Core coding

- [feature-implementation-prompt.md](core-coding/feature-implementation-prompt.md) - build a feature end-to-end: understand, plan, implement, test, document.
- [pair-programming-session-prompt.md](core-coding/pair-programming-session-prompt.md) - interactive build loop: plan → code → explain → verify, in small confirmed steps.
- [debugging-prompt.md](core-coding/debugging-prompt.md) - systematic debugging: reproduce, isolate, root-cause, minimal fix, regression test.
- [refactoring-prompt.md](core-coding/refactoring-prompt.md) - behavior-preserving refactoring with tests as the safety net.
- [codebase-onboarding-prompt.md](core-coding/codebase-onboarding-prompt.md) **[spec]** - understand an unfamiliar repo at verification depth: stack, architecture, data flow, conventions, gotchas, with file:line evidence.
- [api-integration-prompt.md](core-coding/api-integration-prompt.md) - integrate a REST API with types, error handling, retries, and tests.
- [api-design-prompt.md](core-coding/api-design-prompt.md) - design a well-structured REST API with OpenAPI spec, conventions, and validation.
- [database-design-prompt.md](core-coding/database-design-prompt.md) - model a relational schema from requirements with normalization, indexes, and migration path.
- [environment-setup-prompt.md](core-coding/environment-setup-prompt.md) - bootstrap a dev environment from scratch: deps, tooling, config, first-run verification.
- [code-migration-prompt.md](core-coding/code-migration-prompt.md) **[spec]** - migrate code between frameworks/languages with behavior parity and incremental verification.
- [datetime-timezone-correctness-prompt.md](core-coding/datetime-timezone-correctness-prompt.md) - store UTC render local, handle DST, and get calendar/duration math right.

## System design

- [system-design-prompt.md](system-design/system-design-prompt.md) **[spec]** - design a scalable system end-to-end: requirements, components, tradeoffs, failure modes, phased build.
- [adr-writing-prompt.md](system-design/adr-writing-prompt.md) - record a technical decision as a two-minute ADR: context, options, consequences.
- [technical-debt-triage-prompt.md](system-design/technical-debt-triage-prompt.md) - inventory tech debt with evidence and get a prioritized paydown plan.
- [concurrency-debugging-prompt.md](system-design/concurrency-debugging-prompt.md) - hunt race conditions and deadlocks: prove the interleaving, minimal fix, stress-verified.
- [caching-strategy-prompt.md](system-design/caching-strategy-prompt.md) - add caching that pays for itself: measured wins, invalidation designed up front.

## Git & GitHub

- [git-history-surgery-prompt.md](git-github/git-history-surgery-prompt.md) - safe history editing, bisect, blame, and recovery via reflog.
- [open-source-contribution-prompt.md](git-github/open-source-contribution-prompt.md) - contribute to an OSS repo the maintainer-friendly way.
- [ci-cd-workflow-prompt.md](git-github/ci-cd-workflow-prompt.md) **[spec]** - build a verified, secure GitHub Actions pipeline.
- [dependency-upgrade-prompt.md](git-github/dependency-upgrade-prompt.md) - upgrade a dependency safely: changelog, migration, full verification.
- [good-first-issue-workflow-prompt.md](git-github/good-first-issue-workflow-prompt.md) **[spec]** - GitHub Actions workflow reserving starter issues for first-time contributors.
- [git-bisect-debug-prompt.md](git-github/git-bisect-debug-prompt.md) - use git bisect to find the exact commit that introduced a bug.
- [release-automation-prompt.md](git-github/release-automation-prompt.md) - automate versioning, tagging, changelogs, and publishing with CI.
- [commit-checklist-prompt.md](git-github/commit-checklist-prompt.md) - build deterministic PR gates that keep indexes, changelogs, and counts in sync.
- [pr-review-prompt.md](git-github/pr-review-prompt.md) - thorough PR review: verify claims, run checks, clear verdict, merge-ready.
- [issue-triage-for-maintainers-prompt.md](git-github/issue-triage-for-maintainers-prompt.md) - turn an untriaged backlog into labeled, prioritized, answerable queues.

## Code review & quality

- [secure-code-review-prompt.md](code-review/secure-code-review-prompt.md) - security-lens review: injection, authz, data exposure, with evidence.
- [performance-review-prompt.md](code-review/performance-review-prompt.md) - review code for performance anti-patterns with evidence and specific fixes.
- [accessibility-review-prompt.md](code-review/accessibility-review-prompt.md) - audit UI code for WCAG compliance: semantics, keyboard nav, contrast, screen readers.

## Testing & quality

- [bug-finder-prompt.md](testing-quality/bug-finder-prompt.md) **[spec]** - sweep a codebase across correctness factors and get a clear, evidence-backed, priority-ordered list of bugs.
- [bug-finder-with-docs-prompt.md](testing-quality/bug-finder-with-docs-prompt.md) **[spec]** - find bugs and leave a durable bug ledger behind: a priority-ordered report plus BUGS.md and README pointers, with the code untouched.
- [test-writing-prompt.md](testing-quality/test-writing-prompt.md) - write tests that catch regressions, not ones that pad coverage.
- [test-driven-development-prompt.md](testing-quality/test-driven-development-prompt.md) - strict red → green → refactor discipline.
- [code-coverage-gap-prompt.md](testing-quality/code-coverage-gap-prompt.md) - find risky untested paths and cover them meaningfully.
- [e2e-test-scaffold-prompt.md](testing-quality/e2e-test-scaffold-prompt.md) - scaffold end-to-end/integration tests with realistic fixtures and CI integration.
- [mutation-testing-prompt.md](testing-quality/mutation-testing-prompt.md) - run mutation testing to validate that tests actually catch real defects.
- [contract-testing-prompt.md](testing-quality/contract-testing-prompt.md) - consumer-driven contract tests so API drift fails CI, not production.
- [chaos-resilience-prompt.md](testing-quality/chaos-resilience-prompt.md) - inject failures and close the gaps: timeouts, backoff, graceful degradation.

## Docs & delivery

- [documentation-writer-prompt.md](docs-delivery/documentation-writer-prompt.md) - accurate, verified docs that match the project's voice.
- [release-notes-changelog-prompt.md](docs-delivery/release-notes-changelog-prompt.md) - turn git history into a clear, honest changelog.
- [api-documentation-prompt.md](docs-delivery/api-documentation-prompt.md) - generate OpenAPI/Swagger docs from existing code with accurate schemas.
- [readme-builder-prompt.md](docs-delivery/readme-builder-prompt.md) - build a comprehensive README from scratch: purpose, quickstart, examples.
- [inline-documentation-prompt.md](docs-delivery/inline-documentation-prompt.md) - add JSDoc/docstrings to existing code: accurate, concise, non-redundant.

## Security & performance

- [security-audit-prompt.md](security-performance/security-audit-prompt.md) **[spec]** - full-repo audit: injection, auth, secrets, dependencies, with verified findings.
- [performance-optimization-prompt.md](security-performance/performance-optimization-prompt.md) - measure-first optimization with before/after proof.
- [secrets-management-prompt.md](security-performance/secrets-management-prompt.md) - audit and remediate hardcoded secrets, set up env-based secret management.
- [load-testing-prompt.md](security-performance/load-testing-prompt.md) - design and run load/stress tests with measurable thresholds.
- [dependency-audit-prompt.md](security-performance/dependency-audit-prompt.md) - audit dependencies for vulnerabilities, license issues, and staleness.
- [threat-modeling-prompt.md](security-performance/threat-modeling-prompt.md) - STRIDE-style threat model ranked by real risk, with verified mitigations.
- [auth-implementation-prompt.md](security-performance/auth-implementation-prompt.md) - implement sessions/OAuth/JWT safely with server-side authorization everywhere.

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

## Career & learning

- [code-interview-practice-prompt.md](career-learning/code-interview-practice-prompt.md) - structured interview coaching with hints on demand.
- [portfolio-project-prompt.md](career-learning/portfolio-project-prompt.md) - shape an idea into a scoped, presentable portfolio project.
- [resume-review-prompt.md](career-learning/resume-review-prompt.md) - review a technical resume: impact bullets, keyword density, honesty.
- [tech-blog-writer-prompt.md](career-learning/tech-blog-writer-prompt.md) - turn a project or technical concept into a clear, engaging blog post.
- [learning-roadmap-prompt.md](career-learning/learning-roadmap-prompt.md) - turn a skill gap into a project-based roadmap with verifiable checkpoints.

## Frontend & UI

- [component-build-prompt.md](frontend-ui/component-build-prompt.md) - build a reusable, accessible UI component with props, variants, and stories.
- [responsive-design-prompt.md](frontend-ui/responsive-design-prompt.md) - audit and implement responsive layouts: breakpoints, fluid grids, mobile-first.
- [state-management-prompt.md](frontend-ui/state-management-prompt.md) - give every piece of client state one home; compute derived data, delete sync bugs.
- [web-performance-vitals-prompt.md](frontend-ui/web-performance-vitals-prompt.md) - fix Core Web Vitals from measurements: LCP, INP, CLS with before/after proof.
- [i18n-localization-prompt.md](frontend-ui/i18n-localization-prompt.md) - internationalize properly: extracted strings, ICU plurals, RTL, pseudo-locale testing.
- [website-seo-prompt.md](frontend-ui/website-seo-prompt.md) - technical SEO audit: crawlability, canonicalization, metadata, structured data, redirects, and speed - with verification at every step.
- [instagram-carousel-prompt.md](frontend-ui/instagram-carousel-prompt.md) - turn this repo into a branded, swipeable Instagram carousel delivered as self-contained 1080x1080 HTML slides, mirroring the repo's brand identity.
- [ui-audit-prompt.md](frontend-ui/ui-audit-prompt.md) **[spec]** - audit UI for visual consistency, design system adherence, spacing, typography, and responsive behavior with concrete fixes and file:line evidence.

## Data & AI

- [data-pipeline-prompt.md](data-ai/data-pipeline-prompt.md) - build ETL pipelines that fail loudly, resume cleanly, and prove their output.
- [sql-query-optimization-prompt.md](data-ai/sql-query-optimization-prompt.md) - make slow queries fast with plans before/after and justified indexes.
- [rag-pipeline-prompt.md](data-ai/rag-pipeline-prompt.md) - build retrieval-augmented generation with citations and eval numbers before shipping.
- [llm-feature-eval-prompt.md](data-ai/llm-feature-eval-prompt.md) - evaluate LLM features with a held-out test set and pre-committed thresholds.
- [csv-spreadsheet-wrangling-prompt.md](data-ai/csv-spreadsheet-wrangling-prompt.md) - clean messy CSV/spreadsheet exports with encoding detection, explicit type overrides, and a validation report.
- [responsible-web-scraping-prompt.md](data-ai/responsible-web-scraping-prompt.md) - scrape within robots.txt/ToS with resilient selectors, checkpointed crawls, and politeness budgets.
