# Changelog

All notable changes to Awesome AI Prompts are documented here.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Fixed

- `git-github/pr-review-prompt.md` renamed from `pr-review.md` and moved to `git-github/` for correct categorization

### Added

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

## [0.1.0] - 2026-08-15

### Added

- Initial public release
- 26 curated copy-paste prompts covering the full development lifecycle: core coding, git & GitHub, code review, testing, docs, security, performance, DevOps, and career
- Prompts grouped into category folders with a categorized README index

---

[Unreleased]: https://github.com/shauryagangrade/awesome-ai-prompts/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/shauryagangrade/awesome-ai-prompts/releases/tag/v0.1.0
