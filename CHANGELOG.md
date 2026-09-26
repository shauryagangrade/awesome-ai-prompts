# Changelog

All notable changes to Awesome AI Prompts are documented here.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added

- `docs/demo.gif` - README demo GIF: a one-line prompt gets a shrug, then a repo prompt drives a real opencode run that cites file:line
- `.github/workflows/auto-contributors.yml` - append every merged prompt PR author to `CONTRIBUTORS.md` automatically
- `.github/workflows/auto-label.yml` - label PRs by category folder and close referenced good-first-issue tickets on merge
- `docs/usage-stories/TEMPLATE.md` - template for real before/after usage stories per category
- `docs/usage-stories/ucip-elderly-indicator-removal.md` - reviewing the removal of an invalid data indicator that cascaded across 83 files, using `code-review/secure-code-review-prompt.md`
- `docs/usage-stories/tourneyradar-api-ipv6-ratelimit.md` - a before/after record of an IPv6 rate-limit bypass fix; no prompt from this repo was used, so it is a case study rather than prompt evidence
- `core-coding/error-handling-strategy-prompt.md` - one coherent error policy: typed errors, context-rich logs, retry vs surface, proven by failure injection
- `security-performance/memory-leak-hunting-prompt.md` - find and remove a leak from measurements: baseline, reproduced growth, diffed snapshots, and a flat after-curve
- `core-coding/regular-expressions-prompt.md` - write or repair a regex with a stated purpose, a test corpus, and a check that it cannot hang on adversarial input
- `scripts/check-external-links.py` + `.github/workflows/url-rot-check.yml` - weekly external-link rot check (manual dispatch too) that fails on dead URLs in the README or any prompt
- `mobile-dev/mobile-ui-audit-prompt.md` **[spec]** - audit a mobile UI against platform conventions: touch targets, safe areas, accessibility, states, theming, with file:line fixes
- `mobile-dev/mobile-ui-overhaul-prompt.md` **[spec]** - overhaul a mobile UI end-to-end: target design spec, token layer, reimplemented screens, with before/after proof on every platform
- `mobile-dev/website-to-mobile-app-prompt.md` **[spec]** - turn a website into a mobile app, choosing the adaptation strategy from the site's actual architecture: wrapper vs shared-logic vs native
- `a-a-p-contributing/one-pager-schema-prompt.md` - the repo's one-pager format as a schema: field contract, size budget, and checks for authoring quick-task prompts
- `a-a-p-contributing/spec-prompt-schema-prompt.md` **[spec]** - the repo's spec format as a schema: what earns the badge, the mandatory field contract, and evidence-gated verification
- `git-github/issue-resolving-prompt.md` - resolve a GitHub issue end-to-end: reproduce the failure, prove the root cause, land a minimal fix with a regression test, and verify against the project's checks
- `code-review/architecture-review-prompt.md` **[spec]** - audit architecture as a senior architect: evidence-backed 0-10 scorecard, file:line findings with severity/impact/fix, and a prioritized refactoring roadmap, read-only
- `code-review/codebase-audit-prompt.md` **[spec]** - audit a codebase as a senior architect: evidence-backed 0-10 scores, structural smell identification, and a prioritized refactoring roadmap
- `scripts/build-all.py` + `vercel.json` - deterministic builder for `ALL_PROMPTS.html`, a single printable page with a linked mini-TOC and per-prompt copy buttons; committed for static hosting (served at the root by Vercel) and verified in sync by CI with `--check`

### Changed

- CONTRIBUTING.md - community rules: no unsolicited paid pitches or paid third-party actions in issues and PRs
- CONTRIBUTING.md - review policy: 48h response SLA for external PRs, merge-first with maintainer nit-fixing
- README.md - recent contributors strip, star-to-contribute handshake, and a "PR in under 10 minutes" contribution CTA
- `.github/workflows/thanks.yml` - limit the thank-you to a contributor's first merged PR
- `.gitignore` - ignore local launch drafts (`drafts/`) that are pasted from your own accounts, not part of the repo

### Fixed

---

## [0.4.0] - 2026-09-17

### Added

- `a-a-p-contributing/new-prompt-contribution-prompt.md` - author a new prompt for this repo: read conventions, confirm the idea is new, draft, sync index, run gates, open a PR
- `a-a-p-contributing/prompt-pr-review-prompt.md` - review a prompt-contribution PR against the repo's gates with an explicit verdict
- `a-a-p-contributing/resolve-open-issue-prompt.md` - take an open issue end-to-end from ticket to a mergeable PR
- `a-a-p-contributing/fix-reported-bug-prompt.md` - fix a reported bug with reproduction, root cause, and proof
- `core-coding/cli-tool-build-prompt.md` - build a well-behaved CLI: documented flags, typed exit codes, safe pipe and TTY handling, testable core
- `core-coding/agent-codebase-onboarding-prompt.md` **[spec]** - onboard an agent into an unfamiliar repo with no human in the loop: a token-budgeted reading protocol, a compact in-context model, and hard verification gates
- `core-coding/human-codebase-onboarding-prompt.md` **[spec]** - renamed from `codebase-onboarding-prompt.md`; understand an unfamiliar repo at verification depth: stack, architecture, data flow, conventions, gotchas, with file:line evidence
- `data-ai/ai-agent-build-prompt.md` **[spec]** - design and build an LLM agent: tool contracts, context strategy, guardrails, eval set, cost and latency budget
- `mobile-dev/mobile-app-develop-prompt.md` **[spec]** - build a mobile feature and prove it works on both platforms: offline, permissions, deep links, lifecycle, with a platform verification matrix
- `mobile-dev/mobile-performance-prompt.md` - find and fix mobile performance from measurements: startup, frame rate, app size, memory, network
- New `mobile-dev/` category for mobile-specific prompts
- `career-learning/conference-talk-proposal-prep-prompt.md` - write a competitive CFP and rehearse the talk: hook, takeaway, timed outline, demo fallbacks
- `git-github/open-source-maintainer-survival-prompt.md` - harden maintenance practices: guidelines, automation, kind declines, bus factor, handoff
- `frontend-ui/design-handoff-prompt.md` - turn a mockup into token-aligned, responsive code with a screenshot comparison loop
- `scripts/check-prettier.sh` - Prettier gate verifying markdown, JSON/JSONC, YAML, and CSS files match repo formatting, wired into CI

## [0.3.0] - 2026-09-09

### Fixed

- `git-github/pr-review-prompt.md` renamed from `pr-review.md` and moved to `git-github/` for correct categorization

### Added

- `docs/media/prompt-in-action.gif` - above-the-fold demo GIF showing a bug-finder [spec] prompt driving an agent to verified bug findings; captured live from an openvidstudio-driven terminal with Aceternity components
- `bug-finder-prompt.md` **[spec]** - sweep a codebase across correctness factors and surface a clear, evidence-backed, priority-ordered list of bugs
- `bug-finder-with-docs-prompt.md` **[spec]** - find bugs and leave a durable bug ledger (BUGS.md + README pointer) without touching code
- `ui-audit-prompt.md` **[spec]** - audit UI for visual consistency, design system adherence, spacing, typography, and responsive behavior with concrete fixes and file:line evidence
- `codebase-onboarding-prompt.md` **[spec]** - understand an unfamiliar repo at verification depth: stack, architecture, data flow, conventions, gotchas, with file:line evidence
- `issue-triage-for-maintainers-prompt.md` - triage a backlog into labeled, prioritized, answerable queues
- `responsible-web-scraping-prompt.md` - scrape within robots.txt/ToS, resilient selectors, checkpointed crawls
- `datetime-timezone-correctness-prompt.md` - UTC storage, DST handling, safe parsing, calendar/duration math
- `csv-spreadsheet-wrangling-prompt.md` - clean messy CSV/spreadsheet exports with encoding detection, explicit type overrides, and a validation report
- `api-design-prompt.md` - design a well-structured REST API with OpenAPI spec
- `database-design-prompt.md` - model a relational schema from requirements
- `environment-setup-prompt.md` - bootstrap a dev environment from scratch
- `code-migration-prompt.md` **[spec]** - migrate code between frameworks/languages with behavior parity
- `performance-review-prompt.md` - review code for performance anti-patterns
- `accessibility-review-prompt.md` - audit UI code for WCAG compliance
- `ui-audit-prompt.md` - audit UI for visual consistency, design system adherence, spacing, typography, and responsive behavior
- `e2e-test-scaffold-prompt.md` - scaffold end-to-end/integration tests
- `mutation-testing-prompt.md` - validate test quality with mutation testing
- `api-documentation-prompt.md` - generate OpenAPI docs from existing code
- `readme-builder-prompt.md` - build a comprehensive README from scratch
- `inline-documentation-prompt.md` - add JSDoc/docstrings to existing code
- `secrets-management-prompt.md` - audit and remediate hardcoded secrets
- `load-testing-prompt.md` - design and run load/stress tests
- `dependency-audit-prompt.md` - audit dependencies for vulnerabilities and staleness
- `monitoring-observability-prompt.md` - set up logging, metrics, and alerting
- `incident-response-prompt.md` - debug incidents and write post-mortems
- `git-bisect-debug-prompt.md` - find the commit that introduced a bug with git bisect
- `release-automation-prompt.md` - automate versioning, tagging, and publishing
- `commit-checklist-prompt.md` - build consistency gates for derived artifacts
- `resume-review-prompt.md` - review a technical resume
- `tech-blog-writer-prompt.md` - turn a project into a blog post
- `component-build-prompt.md` - build a reusable, accessible UI component
- `responsive-design-prompt.md` - audit and implement responsive layouts
- New `frontend-ui/` category for UI-specific prompts
- `system-design-prompt.md` **[spec]** - design a scalable system end-to-end
- `adr-writing-prompt.md` - record a technical decision as an ADR
- `technical-debt-triage-prompt.md` - inventory and prioritize tech debt
- `concurrency-debugging-prompt.md` - debug race conditions and deadlocks
- `caching-strategy-prompt.md` - add caching with designed invalidation
- `data-pipeline-prompt.md` - build idempotent, validated ETL pipelines
- `sql-query-optimization-prompt.md` - optimize slow queries with plan evidence
- `rag-pipeline-prompt.md` - build grounded, cited RAG features with evals
- `llm-feature-eval-prompt.md` - evaluate LLM features against held-out test sets
- `threat-modeling-prompt.md` - STRIDE threat modeling ranked by real risk
- `auth-implementation-prompt.md` - implement authn/authz safely
- `contract-testing-prompt.md` - consumer-driven contract tests in CI
- `chaos-resilience-prompt.md` - failure injection and resilience fixes
- `state-management-prompt.md` - one home per piece of client state
- `web-performance-vitals-prompt.md` - Core Web Vitals optimization with proof
- `i18n-localization-prompt.md` - internationalization done properly
- `kubernetes-deployment-prompt.md` - secure, zero-downtime K8s deploys
- `feature-flag-rollout-prompt.md` - progressive delivery with kill switches
- `backup-disaster-recovery-prompt.md` - restore-proven backups and DR runbooks
- `learning-roadmap-prompt.md` - project-based learning plans with checkpoints
- `website-seo-prompt.md` - technical SEO audit with verification
- `instagram-carousel-prompt.md` - turn a repo into a branded Instagram carousel of HTML slides
- New `system-design/` category for architecture-level prompts
- New `data-ai/` category for data engineering and AI/LLM prompts
- `commit-checklist.yml` workflow enforcing PR gates: listed prompts, changelog coverage, folder/section sync, Contents counts, Conventional Commits titles
- `scripts/check-consistency.sh` for running the consistency checks locally
- Prompt counts in the README Contents list

---

## [0.2.0] - 2026-09-05

### Added

- 50 new prompts, bringing the catalog from 26 to 76 across 11 categories
- New `frontend-ui/` category for UI-specific prompts (ui-audit, component-build, responsive-design, web-performance-vitals, state-management, i18n-localization)
- New `data-ai/` category for data engineering and AI/LLM prompts (data-pipeline, sql-query-optimization, rag-pipeline, llm-feature-eval)
- New `system-design/` category for architecture-level prompts (system-design, adr-writing, caching-strategy, technical-debt-triage)
- `pr-review-prompt.md` for pull request review in `git-github/`
- `commit-checklist-prompt.md` for building consistency gates, plus the `commit-checklist.yml` workflow enforcing them
- `CONTRIBUTORS.md` and `CITATION.cff`
- CI hardening: markdownlint job, em-dash block in tracked files, LF line endings
- README repositioned around verification-first messaging with a category table of contents
- `ui-audit-prompt.md` and `codebase-onboarding-prompt.md` upgraded to **[spec]** prompts

---

## [0.1.0] - 2026-08-15

### Added

- Initial public release
- 26 curated copy-paste prompts covering the full development lifecycle: core coding, git & GitHub, code review, testing, docs, security, performance, DevOps, and career
- Prompts grouped into category folders with a categorized README index

---

[Unreleased]: https://github.com/shauryagangrade/awesome-ai-prompts/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/shauryagangrade/awesome-ai-prompts/releases/tag/v0.4.0
[0.3.0]: https://github.com/shauryagangrade/awesome-ai-prompts/releases/tag/v0.3.0
[0.2.0]: https://github.com/shauryagangrade/awesome-ai-prompts/releases/tag/v0.2.0
[0.1.0]: https://github.com/shauryagangrade/awesome-ai-prompts/releases/tag/v0.1.0
