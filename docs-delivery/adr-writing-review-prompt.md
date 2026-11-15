# Reusable prompt: ADR writing and review

Copy-paste the block below into any AI coding agent to write a new Architecture
Decision Record (ADR) or review an existing one against a complete checklist.

Keywords: adr, architecture decision record, decision log, tradeoffs, review, documentation

---

Write a new ADR for `[decision being made]` or review an existing ADR at
`[file path]`. The goal is a thorough, verifiable decision record or a complete
review that catches gaps.

## Steps

1. **Clarity** - Ensure the problem statement and decision are clear, specific,
   and unambiguous.
2. **Alternatives** - Verify that alternative approaches were thoroughly
   considered and documented.
3. **Trade-offs** - Check that pros and cons are explicitly discussed for each
   option considered.
4. **Consequences** - Ensure both positive and negative consequences are
   documented, including long-term impacts.
5. **Context** - Verify links to relevant code, PRs, issues, or external
   references are included and accurate.
6. **Actionability** - Confirm there are clear next steps and implementation
   guidance.
7. **Consistency** - Check that the ADR follows the team's ADR format and
   conventions.

## Verification

- [ ] Problem statement is clear and specific.
- [ ] At least two real alternatives are documented with pros and cons.
- [ ] Trade-offs are explicitly discussed for each option.
- [ ] Consequences (positive and negative) are documented with specifics.
- [ ] Context links to code, PRs, issues, or references are accurate and valid.
- [ ] Next steps and implementation guidance are clear and actionable.
- [ ] ADR follows the team's format and conventions.

## Rules

- Never accept an ADR with only one alternative; at least two must be considered.
- Never document a decision as made when it's still being debated; note it as proposed.
- Do not rewrite history: if a decision looks wrong today, note it as a candidate for a superseding ADR.
- Every claim about the codebase must be verified against the actual code.
- The review must be actionable: either the ADR is complete or specific gaps are identified.
