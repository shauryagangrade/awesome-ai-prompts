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

Most list agents will happily *hallucinate* a solution. These prompts are built
to stop that: every one demands evidence, the repo's own tooling, and a
verifiable result before it calls the work done.

**[★ Star on GitHub](https://github.com/shauryagangrade/awesome-ai-prompts)**

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

## Contents

- [Core coding](#core-coding) (11)
- [System design](#system-design) (5)
- [Git & GitHub](#git--github) (10)
- [Code review & quality](#code-review--quality) (3)
- [Testing & quality](#testing--quality) (7)
- [Docs & delivery](#docs--delivery) (5)
- [Security & performance](#security--performance) (7)
- [DevOps & deploy](#devops--deploy) (9)
- [Career & learning](#career--learning) (5)
- [Frontend & UI](#frontend--ui) (7)
- [Data & AI](#data--ai) (6)

## Core coding

- [feature-implementation-prompt.md](core-coding/feature-implementation-prompt.md) - build a feature end-to-end: understand, plan, implement, test, document.
- [pair-programming-session-prompt.md](core-coding/pair-programming-session-prompt.md) - interactive build loop: plan → code → explain → verify, in small confirmed steps.
- [debugging-prompt.md](core-coding/debugging-prompt.md) - systematic debugging: reproduce, isolate, root-cause, minimal fix, regression test.
- [refactoring-prompt.md](core-coding/refactoring-prompt.md) - behavior-preserving refactoring with tests as the safety net.
- [codebase-onboarding-prompt.md](core-coding/codebase-onboarding-prompt.md) - quickly understand an unfamiliar repo: stack, architecture, data flow, gotchas.
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

## Data & AI

- [data-pipeline-prompt.md](data-ai/data-pipeline-prompt.md) - build ETL pipelines that fail loudly, resume cleanly, and prove their output.
- [sql-query-optimization-prompt.md](data-ai/sql-query-optimization-prompt.md) - make slow queries fast with plans before/after and justified indexes.
- [rag-pipeline-prompt.md](data-ai/rag-pipeline-prompt.md) - build retrieval-augmented generation with citations and eval numbers before shipping.
- [llm-feature-eval-prompt.md](data-ai/llm-feature-eval-prompt.md) - evaluate LLM features with a held-out test set and pre-committed thresholds.
- [csv-spreadsheet-wrangling-prompt.md](data-ai/csv-spreadsheet-wrangling-prompt.md) - clean messy CSV/spreadsheet exports with encoding detection, explicit type overrides, and a validation report.
- [responsible-web-scraping-prompt.md](data-ai/responsible-web-scraping-prompt.md) - scrape within robots.txt/ToS with resilient selectors, checkpointed crawls, and politeness budgets.

## Contributing

Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add a
prompt, code style, and PR guidelines.

Prompts live in individual `*-prompt.md` files, grouped in a category folder.
Each one is self-contained: an H1 title, a one-line usage note, and the prompt
block separated by `---`. Keep prompts tool-agnostic, prescriptive, and
grounded in verification. Add a one-line entry to the matching category above
(or a new category + folder) when you add a file.
