# Reusable prompt: impact analysis

Copy-paste the block below into any AI coding agent to trace the blast radius of
a planned change before anything is edited - every module, contract, schema,
config, and test it could affect, each with a file and line as proof.

Keywords: impact analysis, blast radius, dependencies, call sites, change planning, read only

---

Analyze the impact of this planned change before any code is edited:
`[the change: a file, function, type, route, column, config key, or refactor]`.
The goal: a verified list of everything the change can affect, with a
`path:line` citation for each item and a clear split between what breaks and
what only needs a look. Do not edit files, install anything, or run commands
that write.

## Steps

1. **Pin down the change** - Restate it as a precise before and after: which
   symbols change (function, type, route, column, env var, flag, file path) and
   how (renamed, removed, new signature, new default, new behavior). If it is
   vague, ask me before searching.
2. **Find the direct users** - For each changed symbol, search the repo for
   every reference: imports, calls, type uses, re-exports, generated code, and
   plain-text uses such as route strings, event names, config keys, and column
   names. Use the language's own tools where they exist (a type check against a
   scratch rename, `grep -rn`, find-references from the command line) and grep
   for the bare name to catch dynamic use. Record each hit as `path:line` with
   the line of code.
3. **Follow the ripple** - For each direct user, ask the same question one level
   out: who calls it, who consumes its output. Label every item direct or
   indirect and give the chain (A calls B calls C). Stop when a layer adds
   nothing new, and say where you stopped and why.
4. **Check what a search misses** - Tests and fixtures, docs and examples, CI
   and build scripts, config and env files, database schemas and migrations, API
   contracts (OpenAPI, GraphQL, protobuf), stored or serialized data (persisted
   formats, caches, queues), other packages in a monorepo, and outside consumers
   such as a published package, clients, or webhooks. For each, say
   searched-and-found, searched-and-clear, or cannot-search-from-here.
5. **Classify every item** - **Breaks**: will not compile, run, or pass as it
   is. **Changes behavior**: still runs, results differ. **Needs a look**: you
   cannot prove either way, so say what would settle it. **Unaffected**: list
   only the ones a reader would expect to be affected.
6. **Take a baseline** - Where it is cheap and read-only, run the repo's type
   check, linter, and the tests that cover this area, and report what passes
   today. Do not apply the change unless I ask.
7. **Report** - A table of item, `path:line`, direct or indirect,
   classification, and evidence. Then the order to do the work in, the riskiest
   item, and everything you could not verify.

## Verification

- [ ] Every item has a `path:line` that exists, with the line quoted.
- [ ] Direct and indirect items are labeled, and indirect ones show the chain.
- [ ] Each of tests, docs, CI, config, schemas, contracts, stored data, and
      outside consumers is marked found, clear, or unsearchable.
- [ ] Each "Breaks" item is backed by a compiler error, a failing check, or the
      exact line that cannot work.
- [ ] A baseline of the existing type check and tests is reported.
- [ ] No file was changed.

## Rules

- Never list an item from memory or by guess. If there is no `path:line`, it
  goes under "Needs a look" with what would settle it.
- Never write "nothing else is affected" without listing where you searched.
- Never treat a clean search as proof for a place you did not search.
- Do not stop at the first layer of callers.
- Do not edit, rename, or generate anything while analyzing.
