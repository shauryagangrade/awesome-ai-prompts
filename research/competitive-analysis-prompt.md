# Reusable prompt: competitive analysis

Copy-paste the block below into any AI coding agent to research competing
tools or libraries and produce an evidence-backed comparison you can decide from.

Keywords: competitors, alternatives, comparison, evaluation, decision matrix, tools

---

Compare [the options] for [the use case]. Use current, version-pinned evidence
and deliver a decision matrix, not a feature list copied from marketing pages.

## Steps

1. **Frame** - State the use case, the criteria that matter, and the versions
   or dates the comparison is valid for.
2. **Source** - For each option, use primary sources: official docs, source
   code, changelogs, and reproducible benchmarks. Record a link and version.
3. **Test** - Where a claim affects the decision, verify it yourself with a
   small, repeatable check. Capture the command and output.
4. **Score** - Fill a matrix: rows are options, columns are criteria, each cell
   has evidence and a short note. Mark unknowns instead of guessing.
5. **Decide** - Pick one option for the stated use case, name the tradeoffs,
   and say which finding would change the pick.

## Verification

- [ ] Criteria and version/date bounds are stated before comparing.
- [ ] Every cell cites a primary source or a check you ran.
- [ ] Claims that affect the decision were reproduced, not just quoted.
- [ ] Unknowns are labeled, and no cell is filled with a guess.
- [ ] A single recommendation is given with its tradeoffs.

## Rules

- Never compare from marketing copy or feature lists alone.
- Never mix versions: pin what each claim was measured against.
- If two options are genuinely tied on the stated criteria, say so and name
  the tie-breaker you used.
