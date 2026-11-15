# Reusable prompt: dependency graph analysis

Copy-paste the block below into any AI coding agent to build the internal
dependency graph of a codebase. The goal is to map dependencies, detect cycles,
and find layer violations.

Keywords: dependency graph, code analysis, cycles, layer violations, mermaid, architecture

---

Build the internal dependency graph for `[repository name]`. Map dependencies
between modules/components using file imports, references, and runtime coupling.
List edges with file:line references, detect cycles, and identify layer violations.

## Steps

1. **Build the graph** - Map dependencies between modules/components using file
   imports, references, and runtime coupling. List edges with file:line
   references.
2. **Detect cycles** - Identify circular dependencies using topological analysis
   or graph tools. Provide concrete cycle paths with file:line evidence.
3. **Check layer violations** - Verify that higher-level modules do not depend on
   lower-level implementations. Flag violations with file:line evidence.
4. **Suggest minimal fixes** - Recommend minimal, verifiable decoupling
   approaches to resolve cycles and violations, such as interface extraction,
   dependency inversion, or module restructuring.

## Verification

- [ ] The graph is accurate with file:line references for each dependency edge.
- [ ] All circular dependencies are identified with concrete cycle paths.
- [ ] Layer violations are flagged with file:line evidence.
- [ ] Suggested fixes are minimal and verifiable.
- [ ] Output includes a Mermaid diagram of the dependency graph.

## Rules

- Never assume dependencies; use the actual code to build the graph.
- Never skip cycle detection; if no cycles are found, state that clearly.
- Do not invent file:line references; use actual code analysis tools.
- Provide concrete evidence for each finding, not just general statements.
- The Mermaid diagram should be parseable and useful for documentation.
