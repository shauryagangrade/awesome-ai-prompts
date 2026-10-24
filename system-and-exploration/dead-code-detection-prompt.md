# Reusable prompt: dead code detection

Copy-paste the block below into any AI coding agent to find code that nothing
uses: unused exports, unreferenced files, orphaned configs, and unreachable
branches. It is read-only, and every finding is backed by a search that proves
nothing references it.

Keywords: dead code, unused exports, unreferenced files, orphaned config, unreachable code, cleanup, tree shaking

---

Find the dead code in this repository, read-only. The goal: a list of things
that are provably unused, each with the evidence, plus a safe plan to remove
them. Do not delete, move, or edit anything unless the user asks afterwards.

## Steps

1. **Define the scope** - State what you will scan (the whole repository, one
   package, one directory), the languages and build tools involved, and what you
   will leave out (vendored code, generated files, build output). List the
   entrypoints you know of: `main` fields, CLI commands, route files, scheduled
   jobs, exported public APIs, and test files. Anything reachable from them is
   live.
2. **Run the existing tools first** - Use what the stack already provides:
   `knip` or `ts-prune` for TypeScript, `vulture` for Python, `deadcode` or
   `staticcheck` for Go, compiler or linter unused warnings, coverage output.
   Treat their results as candidates, not as proof. Save the raw output.
3. **Search for references yourself** - For each candidate, search the whole
   repository, including tests, configs, scripts, CI files, docs, and build
   files, for its name and for likely variants: imports and requires, string
   references, re-exports, and path or glob patterns. Record the exact search
   you ran and the number of matches.
4. **Rule out dynamic use** - Check for use that a search cannot see:
   reflection, dynamic `import()` or `require` with a built path, plugin or
   decorator registries, framework conventions (a file name that is a route or
   a migration), configuration that names a class or function, serialized data,
   and anything exported as part of a public package API. Mark each candidate
   **dead**, **probably dead**, or **used dynamically**, and say why.
5. **Report with evidence** - For each finding give the `file:line`, what it is
   (unused export, unreferenced file, orphaned config, unreachable branch,
   unused dependency), the searches that found no references, and the
   confidence level. Group the findings by how safe they are to remove.
6. **Propose a safe removal plan** - Order the removals from safest to riskiest.
   For each batch, say how to verify it afterwards: build, type check, full
   test suite, and a search showing zero references. Recommend removing in
   small commits so one can be reverted alone.

## Verification

- [ ] The scope and the list of entrypoints were stated before scanning.
- [ ] Every finding has a `file:line` and the exact search that found no
      references.
- [ ] Tests, configs, scripts, CI files, and docs were included in each search.
- [ ] Dynamic use and public API exports were checked for each candidate, and
      the result is stated.
- [ ] Each finding has a confidence level of dead, probably dead, or used
      dynamically.
- [ ] No file was changed, deleted, or moved.

## Rules

- Never delete or edit anything while detecting; this is a read-only task.
- Never call something dead because a tool flagged it; confirm it with your own
  search.
- Never mark an exported symbol of a published package or library as dead
  without checking whether outside code can import it.
- Never skip tests, configs, or build scripts when searching for references.
- If you cannot tell whether something is used, report it as unknown instead of
  guessing.
