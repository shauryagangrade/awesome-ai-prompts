# Reusable prompt: systematic debugging

Copy-paste the block below into any AI coding agent to debug a problem the
way a disciplined engineer does: reproduce first, find the root cause, fix
the smallest thing, and prove it.

---

Debug the reported problem in this repository. Work systematically - do not
guess-and-patch. Follow these steps in order.

## Steps

1. **Reproduce** - Reproduce the bug yourself. If you can't, get the exact
   reproduction steps, inputs, and environment from the report, then try
   harder (check versions, config, seed data). A bug you can't reproduce is a
   bug you can't fix - say so rather than guessing.
2. **Isolate** - Narrow the failure to the smallest input and code path.
   Use `git bisect` if a recent change introduced it. Read the relevant code
   and trace the data flow to find where behavior diverges from intent.
3. **Root cause** - State the root cause precisely, with evidence (file:line).
   Distinguish root cause from symptom. If there are multiple suspects, rank
   them and test them rather than listing everything as "maybe".
4. **Fix** - Make the smallest fix that addresses the root cause without
   breaking existing behavior. Follow repo conventions. Do not band-aid the
   symptom or add speculative handling.
5. **Regression test** - Add or update a test that fails on the old code and
   passes on the fix. If the bug can't be tested, say why and verify manually.
6. **Verify** - Run the full test suite and the repo's checks. Confirm the
   original reproduction no longer reproduces.

## Rules

- Never claim a fix works without running it.
- If you can't find the root cause after genuine effort, report what you've
  ruled out and what you'd try next - do not ship an unverified patch.
- Flag any pre-existing bugs you notice while debugging as notes, don't fix
  them silently.
