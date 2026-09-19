# Reusable prompt: codebase audit

Copy-paste the block below into any AI coding agent to audit a codebase
across architecture, quality, and maintainability dimensions with 0-10
scores and a prioritized refactoring roadmap.

---

Audit this repo as a senior software architect. Rate 0–10 for overall code quality, architecture, maintainability, modularity, cohesion/coupling, separation of concerns, duplication, technical debt, testing, documentation, error handling, security, performance, scalability, and production readiness.

Specifically identify:

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

For each major issue give severity, evidence, impact, and recommended fix. Finish with an overall architecture score, top 10 problems, and a prioritized refactoring roadmap. Do not modify code.
