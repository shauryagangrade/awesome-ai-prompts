# Reusable prompt: bug finder with docs [spec]

Copy-paste the block below into any AI coding agent to sweep a codebase
across multiple correctness factors, produce a clear, priority-ordered list
of bugs - and leave behind durable documentation of everything found so the
team can act on it later.

---

Find the real bugs in this repository and document them. Sweep the codebase
across the factors below, read the actual code, and produce a clear,
priority-ordered list of confirmed bugs. Then record every finding in the
repo's documentation so the list survives as a durable artifact. Accuracy
beats volume: only report what you can verify with evidence. Do not change
any code - fix nothing, but do leave the documentation behind.

## Define the scope first

Before reading, state:

1. **Target** - Whole repo, or a specific module/directory/SHA range? If the
   repo is large, propose the highest-value slice (core logic, recently
   changed code) and say so.
2. **Factors to prioritize** - Which bug families matter most for this
   codebase (the stack and its riskiest areas, e.g. a React frontend vs a
   payment CLI vs a data pipeline)? Weight your search accordingly.
3. **Documentation destination** - Where the findings should be recorded: a
   dedicated bug ledger (`BUGS.md` at the repo root), a section in the README,
   a `docs/` page, or somewhere the repo already keeps known issues. Propose
   what fits this repo and say so.

## Factors to examine

1. **Logic & control flow** - Off-by-one errors, inverted or missing
   conditions, dead/unreachable branches, incorrect operators, wrong
   early-returns, missing edge cases (empty input, zero, null, max values).
2. **Data handling** - Off-by-one and boundary issues, type/encoding
   mismatches, integer overflow, truncation, units and timezone mistakes,
   NaN/Infinity, silent data loss.
3. **State & concurrency** - Shared mutable state, race conditions, stale
   closures/caches, resource leaks not closed on error paths, reentrancy,
   unintentional shared references (alias bugs).
4. **Error handling** - Swallowed exceptions, unhandled error paths, wrong
   error recovery, partial-failure inconsistency (some steps done, others
   not), missing rollback/cleanup.
5. **API & integration** - Wrong argument order, mismatched types, broken
   contracts between callers and callees, incorrect external calls,
   off-by-one pagination/offsets, encoding/locale differences.
6. **Configuration & environment** - Wrong defaults, env vars required but
   unchecked, mismatched toggles, incorrect config values for the
   environment.
7. **Null & reference safety** - Null/undefined dereferences, nullable
   values treated as non-null, missing existence checks, stale object
   references.

## Method

1. **Read before concluding** - No claim without reading the code path that
   proves it. Trace inputs from entry point through the buggy line.
2. **Verify each candidate** - For every suspected bug, confirm it is real:
   check the surrounding code, types, callers, and expected behavior. Reject
   anything you cannot prove. A bug you cannot demonstrate is not reported.
3. **Trace the impact** - Show how the bug manifests for a user or system:
   what input triggers it and what wrong thing happens.
4. **Check whether tests cover it** - Note if an existing test should have
   caught it but doesn't, or if one is missing. This shows confidence.
5. **Confirm, don't assume** - Where possible run the repo's tooling (tests,
   linters, type checker) to support a finding, but only report the bug when
   reasoning and/or an executable check confirms it.

## Output

### Part 1 - The bug report

A prioritized bug report. For each confirmed bug:

- **Severity** - Critical (data loss/corruption, crash on a common path,
  wrong money/security result) / High / Medium / Low.
- **The bug** - One clear sentence describing the incorrect behavior.
- **Evidence** - `file:line`, the triggering input/path, and why it is wrong.
- **Impact** - What breaks in practice and who hits it.
- **Fix** - A one-to-three line concrete fix (do not apply it).
- **Docs updated** - What you documented for it and where.

Then end the report with:

- A **summary table**: ID | severity | file:line | one-line bug.
- A **things checked and clean** note listing factors you swept that surfaced
  no confirmed bugs.
- **Needs confirmation** - anything suspicious you could not fully prove,
  clearly separated from confirmed findings.

### Part 2 - The documentation

1. **Create the bug ledger** - If none exists, create a `BUGS.md` (or the
   agreed destination) at the repo root containing: a one-line purpose, the
   date and scope of this sweep, and a table/list of every confirmed bug with
   ID, severity, `file:line`, status `open`, one-line description, and where
   it was reproduced. Mark each entry so it can be closed later, e.g. a
   status column to flip when fixed.
2. **Link the ledger from the README** - Add a short "Known issues / bug
   ledger" pointer in the README (or the closest existing docs) so the ledger
   is discoverable. Follow the repo's existing doc conventions - heading
   style, table format, tone.
3. **Record unconfirmed suspicions** - Put "needs confirmation" items in the
   ledger under a clearly separated section, each with what would resolve it.
4. **Leave the code alone** - Update docs only. Do not fix, refactor, or
   annotate source files unless fixing a doc comment that is wrong
   specifically because it documents the bug's behavior as correct.

## Rules

- Update documentation, never code. Report-and-document first; fixing is a
  separate follow-up.
- Never pad the list. If you found 3 real bugs, report 3 - not 20 that you
  could not verify.
- Distinguish confirmed bugs from "needs confirmation" and from style
  preferences.
- If a suspected bug is guarded by an unclear invariant, mark it "needs
  confirmation" and say what would resolve it.
- Documentation must match the repo's existing style, and every claim in it
  must trace to a verified finding - no filler like "this code could be
  improved".
- If the repo already has a bug ledger or known-issues doc, update it, do not
  create a second one.