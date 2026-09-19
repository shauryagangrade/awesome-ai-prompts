# Reusable prompt: codebase audit [spec]

Copy-paste the block below into any AI coding agent to perform a comprehensive
codebase audit across architecture, quality, and maintainability dimensions with
evidence-backed 0-10 scores and a prioritized refactoring roadmap - the heavy
format, because a flawed audit produces a misguided roadmap.

---

Audit this repo as a senior software architect. Read-only: this produces a
report, never diffs. Every claim must trace to a file:line or measured evidence -
accuracy matters more than volume.

## Define the scope first

State all four before reading any code:

1. **Target** - Whole repo, or a specific module, package, service, or
   directory? If the repo is large, identify the highest-value boundaries to
   audit first and state the boundary.
2. **Platforms & stack** - Language(s), framework(s), runtime, package
   manager, and repo architecture (monorepo, microservices, standalone app, or
   library).
3. **Inputs in scope** - Source files, tests, build configurations, dependency
   manifests, documentation, and CI workflows.
4. **Out of scope** - Modifying code, formatting fixes, functional bug hunting,
   or speculative refactors. Read-only analysis.

## What to produce

1. **Scorecard** - Rate 0-10 for each dimension below, plus an Overall
   Architecture score. Anchor: 9-10 production-grade; 7-8 solid with specific
   weak spots; 5-6 functional but fragile; 3-4 needs rework; 0-2 foundationally
   broken. Every score must carry a file:line or measured justification:

   - Overall code quality
   - Architecture & system structure
   - Maintainability & technical debt
   - Modularity & boundary clarity
   - Cohesion & coupling
   - Separation of concerns
   - Duplication & redundancy
   - Testing & test health
   - Documentation & spec alignment
   - Error handling & resilience
   - Security posture
   - Performance & resource efficiency
   - Scalability
   - Production readiness

2. **Structural smells & boundaries** - Specifically identify:

   - Monoliths and overly large components
   - Systems, subsystems, modules, packages, services, and boundaries
   - Dependency direction and circular dependencies
   - God classes/functions/components
   - Poor abstractions and leaky boundaries
   - Tight coupling and hidden dependencies
   - Duplicated or fragmented functionality
   - Unclear ownership/responsibilities
   - Dead, obsolete, placeholder, or redundant code
   - Architectural inconsistencies and accidental complexity
   - Areas that should be split, merged, relocated, or redesigned

3. **Findings report** - For each major issue give severity (Critical, Major,
   Minor), evidence (file:line citation and reading), impact (what breaks, what
   slows down, or what risk is introduced), and recommended fix (minimal first
   increment).

4. **Top 10 problems** - Ranked list of the top 10 problems across the
   repository, each traceable to a specific finding.

5. **Refactoring roadmap** - Prioritized: fix now (immediate risk or blocker),
   schedule (technical debt with real maintenance cost), accept and document.
   Every item names a concrete first increment. Do not modify code.

## Method

1. **Map boundaries first** - Identify the top-level packages, modules, entry
   points, and dependency graph before evaluating individual files.
2. **Measure before concluding** - Baseline file sizes, function lengths,
   dependency relationships, and test presence. Prefer measured facts over
   impressions.
3. **Trace the code** - For each candidate finding, trace callers and callees
   to confirm coupling, leakage, or duplication.
4. **Verify impact** - Keep only issues with an observable maintenance or
   runtime cost.
5. **Report only** - Log findings with evidence. Do not edit, refactor, or
   delete code.

## Verification

- [ ] Scope (target, stack, inputs, out-of-scope) stated before code was
      inspected.
- [ ] 0-10 scorecard provided for all dimensions, each backed by file:line
      citations or measurements.
- [ ] Structural smells and boundaries evaluated across all 11 target areas.
- [ ] Every major finding uses severity, evidence, impact, and recommended fix
      with concrete file:line evidence.
- [ ] Top 10 problems ranked and tied to documented findings.
- [ ] Refactoring roadmap prioritized with verifiable increments.
- [ ] No code was modified - the audit is strictly read-only.

## Rules

- Never modify, delete, or reformat code - this produces a report only.
- Never report a finding or score without file:line evidence or a verifiable
  trace.
- Never pad findings - verified architectural facts beat speculative lists.
- Never propose big-bang rewrites; fixes must be incremental and verifiable.
- Never accept "done" without satisfying every deliverable in this spec.
