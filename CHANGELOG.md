# Changelog

All notable changes to Awesome AI Prompts are documented here.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added

- Add `git-github/local-pr-cleanup-prompt.md` - spec prompt for full local hygiene after complex PR work: branches, worktrees, stashes, and build artifacts.
- Add `git-github/remote-pr-cleanup-prompt.md` - spec prompt for full remote hygiene after complex PR work: prune remotes, delete merged PR branches, sync with upstream.
- Add `security-performance/dependency-vuln-triage-prompt.md` - triage dependency vulnerability reports with reachability proof and verified fix.
- Add `security-performance/secrets-scanning-response-prompt.md` - respond to a leaked secret with rotation-first protocol.
- Add `devops-deploy/ci-gate-diagnosis-prompt.md` - diagnose failing CI gates by comparing against base branch.
- Add `devops-deploy/incident-postmortem-prompt.md` - evidence-based postmortem with timeline and action-item verification.
- Add `devops-deploy/infra-drift-detection-prompt.md` - detect live infrastructure drift vs IaC without applying changes.
- Add `system-and-exploration/dead-code-detection-prompt.md` - find dead code with proof, ruling out dynamic use first.
- Add `system-and-exploration/entrypoints-discovery-prompt.md` - discover runtime entrypoints with environment requirements.
- Add `system-and-exploration/impact-analysis-prompt.md` - evaluate change impact before applying.
- Add `career-learning/interview-debugging-drill-prompt.md` - coaching a debugging session with evidence-based fix.
- Add `docs-delivery/migration-guide-prompt.md` - write a verified migration guide with rollback plan.

- Site SEO, with everything deployed now living in a single `website/` folder:
  `scripts/build-all.py` generates `website/index.html` (the former root `ALL_PROMPTS.html`),
  one page per category (`/category/<cat>`), one page per prompt (`/prompt/<cat>/<slug>`),
  plus `website/sitemap.xml` and `website/robots.txt`. Every page carries a unique title,
  meta description, canonical URL, Open Graph and Twitter card tags, and JSON-LD structured
  data. `vercel.json` rewrites the clean public URLs onto the files in `website/`, and
  `--check` now verifies the whole committed site, not just the main page. Internal
  cross-links are emitted root-relative and extensionless (`/prompt/<cat>/<slug>`) so
  they resolve correctly at any page depth.
- Add `website/llms.txt` (llmstxt.org convention): a deterministic Markdown index of the
  catalog for LLM readers, served at `/llms.txt`.
- Add the Google Search Console site-verification file, served at the domain root via a
  `vercel.json` rewrite.
- Broadened positioning from student developers to all developers: README intro, `CITATION.cff`
  keywords, and the brand-voice example in `frontend-ui/instagram-carousel-prompt.md`.
- Promote `git-github/pr-review-prompt.md` and `frontend-ui/instagram-carousel-prompt.md` to spec prompts ([spec] badge) and register both in `SPEC_PROMPTS`.
- Normalize all remaining one-pager prompts onto the contract (`## Steps`, `## Verification`, `## Rules`) with prompt-specific verification content; rewrite or consolidate Rules where needed.
- Trim over-budget one-pagers (≤45 lines / ≤550 words) by tightening steps; cut Rules to 3-5 bullets. Preserve Verification content.
- Regenerate `ALL_PROMPTS.html` via `scripts/build-all.py`.

- `docs-delivery/architecture-documentation-prompt.md` - architecture docs with evidence and tradeoffs.
- `career-learning/mentoring-feedback-prompt.md` - structured, verifiable mentoring feedback.
- `code-review/data-model-review-prompt.md` - schema, migration, and index review with evidence.
- `testing-quality/property-based-testing-prompt.md` - property-based tests with generated inputs.
- `mobile-dev/push-notifications-deep-links-prompt.md` - notifications and deep-link verification.
- `mobile-dev/mobile-ui-audit-fix-prompt.md` - remediate every finding from a mobile UI audit with evidence-backed fixes, verification matrix, and behavior guard.
- `data-ai/data-quality-validation-prompt.md` - data contracts, checks, and failure response.
- Add System & Exploration category and "Drive space investigator (read-only)" prompt
- aligned all 28 spec prompts with the field contract in `spec-prompt-schema-prompt.md`, and added the
  missing `[spec]` H1 suffix to the five prompts registered in `SPEC_PROMPTS` without it.
- trimmed the `Keywords:` lines in `devops-deploy/kubernetes-deployment-prompt.md` and
  `devops-deploy/monitoring-observability-prompt.md` to the 4-7 term range in CONTRIBUTING.md.

## [0.6.0] - 2026-10-01

### Changed

- promoted `ml-model-deployment-basics-prompt.md` to a spec prompt: added the `[spec]` badge,
  `SPEC_PROMPTS` registration, and the spec field contract.
- promoted `browser-extension-development-prompt.md` to a spec prompt: added the `[spec]` badge,
  `SPEC_PROMPTS` registration, and the spec field contract.
- promoted `mobile-app-project-setup-prompt.md` to a spec prompt: added the `[spec]` badge,
  `SPEC_PROMPTS` registration, and the spec field contract.
- promoted `rate-limiting-abuse-prevention-prompt.md` to a spec prompt: added the `[spec]` badge,
  `SPEC_PROMPTS` registration, and the spec field contract.
- promoted `privacy-gdpr-compliance-review-prompt.md` to a spec prompt: added the `[spec]` badge,
  `SPEC_PROMPTS` registration, and the spec field contract.
- promoted `prompt-injection-defense-prompt.md` to a spec prompt: added the `[spec]` badge,
  `SPEC_PROMPTS` registration, and the spec field contract.
- promoted `legacy-code-modernization-assessment-prompt.md` to a spec prompt: added the `[spec]` badge,
  `SPEC_PROMPTS` registration, and the spec field contract.
- promoted `message-queues-event-driven-design-prompt.md` to a spec prompt: added the `[spec]` badge,
  `SPEC_PROMPTS` registration, and the spec field contract.
- promoted `file-uploads-media-handling-prompt.md` to a spec prompt: added the `[spec]` badge,
  `SPEC_PROMPTS` registration, and the spec field contract.
- promoted `payment-integration-prompt.md` to a spec prompt: added the `[spec]` badge,
  `SPEC_PROMPTS` registration, and the spec field contract.

### Added

- `core-coding/file-uploads-media-handling-prompt.md` - accept uploads safely: server-side validation, streaming for large files, generated storage names, malware scanning hooks, and resumable transfers
- `core-coding/graphql-api-design-prompt.md` - design GraphQL past the demo: schema-first types, resolver N+1 batching, field-level authorization, bounded depth and complexity, stable error shape
- `core-coding/websockets-realtime-features-prompt.md` - build realtime features that survive disconnects and horizontal scaling: connection lifecycle, versioned message contracts, an explicit delivery guarantee, and a slow-client policy
- `core-coding/payment-integration-prompt.md` - integrate payments with money-grade discipline: no raw card data, idempotency keys on every mutation, verified webhooks, an order/payment state machine, and reconciliation jobs
- `core-coding/email-delivery-prompt.md` - send transactional email that reaches the inbox: SPF/DKIM/DMARC domain auth, code templates tested across clients, async sending with retry, and bounce/complaint suppression
- `system-design/message-queues-event-driven-design-prompt.md` - design event-driven systems for at-least-once delivery: versioned event contracts, per-key ordering, idempotent consumers, replay and backfill strategy, and DLQ operations
- `system-design/legacy-code-modernization-assessment-prompt.md` - assess whether a legacy system should be modernized at all: EOL and security inventory, a value-versus-risk map per module, strangler-fig seams, a characterization-test plan, and stop conditions
- `security-performance/prompt-injection-defense-prompt.md` - threat-model the prompt-injection attack class specifically: an inventory of where untrusted text reaches the context, instruction/data separation with its limits, out-of-band tool gating, a red-team suite, and documented residual risk
- `security-performance/privacy-gdpr-compliance-review-prompt.md` - run a systematic privacy review: data inventory with storage and retention, lawful basis and consent withdrawal, user rights flows including backups, the third-party processor list, and ranked minimization work
- `security-performance/rate-limiting-abuse-prevention-prompt.md` - protect public endpoints: limits tiered by identity, IP, and route cost, a written rationale for the algorithm, correct 429 and Retry-After semantics, shared-store counters, and a load test proving the limits trip and recover
- `devops-deploy/background-jobs-scheduled-tasks-prompt.md` - add background jobs that survive retries and deploys: idempotent handlers, bounded retries with backoff, dead-letter handling, queue depth and age metrics, and graceful shutdown drains
- `devops-deploy/cloud-cost-optimization-prompt.md` - cut cloud spend from measurement: a cost inventory ranked by service, rightsizing from utilization data, idle-resource cleanup, storage lifecycle policies, and a before/after savings table
- `devops-deploy/capacity-planning-prompt.md` - turn outages into scheduled upgrades: headroom per bottleneck, a forecast tied to a product metric, dated scaling options with cost and lead time, and alerts that fire well before the wall
- `frontend-ui/design-tokens-theming-prompt.md` - build theming structurally: a token taxonomy for color, spacing, radius, and type; primitive to semantic to component layers; per-pair dark mode contrast checks; and a migration path off hardcoded values
- `frontend-ui/animation-performance-prompt.md` - keep motion smooth on mid-range devices: animate only transform and opacity, profile long frames during real interaction, respect reduced motion, use compositor hints sparingly, and measure frame rate before and after
- `frontend-ui/browser-extension-development-prompt.md` - build a browser extension that passes review: manifest v3 structure, minimum permissions, the background worker and content script split, storage and typed messaging, CSP and no-remote-code rules, and a store review checklist
- `frontend-ui/pwa-offline-support-prompt.md` - implement offline support explicitly: service worker lifecycle and cache versioning, a caching strategy per resource type, offline fallbacks with queued mutations, an update-in-place flow, and Lighthouse verification
- `mobile-dev/mobile-app-project-setup-prompt.md` - bootstrap a mobile app: an argued stack choice with the tradeoffs against it, feature-based project structure, a navigation skeleton, iOS and Android builds from a clean clone on CI, and a device testing plan
- `data-ai/data-visualization-prompt.md` - make charts honest and accessible: match chart type to the question and data shape, keep axes honest and everything labeled, use color-blind-safe palettes plus a non-color encoding, handle every state, and verify against the source numbers
- `data-ai/ab-test-design-analysis-prompt.md` - design and read online experiments honestly: hypothesis and primary metric fixed before launch, sample size and power, randomization unit with contamination checks, pre-committed stopping rules, and effect size with confidence intervals
- `data-ai/analytics-event-tracking-prompt.md` - instrument product analytics so it does not rot: a naming convention and property schema, a tracking plan as the source of truth, client-side validation before send, PII minimization, and an end-to-end test that events arrive
- `data-ai/ml-model-deployment-basics-prompt.md` - bridge training artifacts to serving: model artifact versioning and a registry, an inference API with input and output validation, measured latency and batching, drift monitoring with retraining triggers, and a rehearsed rollback
- `data-ai/fine-tune-vs-rag-vs-prompting-decision-prompt.md` - decide between prompting, RAG, and fine-tuning: requirements for freshness, specificity, cost, and latency first; an evidence-backed decision matrix; the cheapest sufficient option; an eval plan that could disprove the choice; and reversal criteria

## [0.5.0] - 2026-09-26

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

### Removed

- `docs/media/prompt-in-action.gif` - unembedded and deleted; `docs/demo.gif` already carries the same real opencode run behind a staged opening, so the README was showing the same footage twice (12.1MB dropped)

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

[Unreleased]: https://github.com/shauryagangrade/awesome-ai-prompts/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/shauryagangrade/awesome-ai-prompts/releases/tag/v0.6.0
[0.5.0]: https://github.com/shauryagangrade/awesome-ai-prompts/releases/tag/v0.5.0
[0.4.0]: https://github.com/shauryagangrade/awesome-ai-prompts/releases/tag/v0.4.0
[0.3.0]: https://github.com/shauryagangrade/awesome-ai-prompts/releases/tag/v0.3.0
[0.2.0]: https://github.com/shauryagangrade/awesome-ai-prompts/releases/tag/v0.2.0
[0.1.0]: https://github.com/shauryagangrade/awesome-ai-prompts/releases/tag/v0.1.0
