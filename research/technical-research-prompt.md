# Reusable prompt: technical research [spec]

Paste this entire prompt into your agent when a decision needs deep technical
research: it forces scope, reproducible checks, and a cited recommendation.

Keywords: technical research, investigate, compare options, evidence, reproduce, recommendation

---

## Define the scope first

Before researching, state and confirm:

1. **Question** - The exact decision or question to answer, and what a useful
   answer must let the reader do.
2. **Constraints** - Environment, versions, budget, deadlines, and any
   must-have or must-not-have properties.
3. **Criteria** - How options will be compared, with the criteria named and
   weighted before any option is examined.
4. **Depth** - How far to go: a quick survey, a reproducible benchmark, or a
   full prototype. State the time box.
5. **Out of scope** - What will not be investigated, so "done" is bounded.

Do not begin until the scope is confirmed.

## What to produce

1. **Option list** - The candidates considered, with the source that surfaced
   each one.
2. **Evidence matrix** - Each option scored against every criterion, with a
   file:line, benchmark output, or source link for each cell.
3. **Reproduction notes** - For every benchmark or key claim, the exact
   commands, versions, and raw output needed to reproduce it.
4. **Recommendation** - One choice, with the tradeoffs stated and the
   conditions under which a different option would win.
5. **Open risks** - Unknowns and assumptions that could change the answer.

## Method

1. Lock the criteria and weights before looking at options, so the comparison
   is not reverse-engineered to a preferred answer.
2. Gather candidates from primary sources: docs, source code, papers, and
   official release notes. Record where each came from.
3. Reproduce the claims that matter. Run the benchmark or minimal prototype;
   capture commands, versions, and output verbatim.
4. Score each option against each criterion using only evidence you reproduced
   or verified from a primary source. Mark gaps as unknown, never inferred.
5. Write the recommendation from the matrix, and name the conditions that
   would flip it.

## Verification

- [ ] Scope, constraints, criteria, and out-of-scope were confirmed before work
      started.
- [ ] Criteria were fixed before options were examined.
- [ ] Every matrix cell has evidence (output, file:line, or primary source).
- [ ] Each key claim was reproduced, with commands and versions recorded.
- [ ] Unknowns are marked unknown, not filled with guesses.
- [ ] The recommendation follows from the matrix and states its flip conditions.

## Rules

- Never score an option on a criterion you did not actually check.
- Never cite a vendor's marketing page as evidence for a technical claim.
- Never change the criteria after seeing the results to favor a winner.
- If a claim cannot be reproduced, report that and lower its confidence rather
  than dropping it silently.
