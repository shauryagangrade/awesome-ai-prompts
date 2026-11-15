# Reusable prompt: documentation audit

Copy-paste the block below into any AI coding agent to audit documentation
and produce a prioritized, verifiable fix list. The goal is to turn audit
results into actionable, systematic fixes.

Keywords: documentation audit, prioritize, fix list, verification, broken links

---

Audit the documentation for `[file or directory]`. The goal is not just to
produce a list of issues, but to prioritize them with concrete actions and
verifiable acceptance criteria.

## Steps

1. **Identify issues** - Scan the documentation for broken links, outdated info,
   missing docs, clarity issues, and other problems. Record each issue with its
   exact location (file path and line number).
2. **Categorize issues** - Group issues by type: broken links, outdated info,
   missing docs, clarity issues, etc.
3. **Prioritize issues** - Rank each issue by impact (critical/high/medium/low)
   with justification. Critical issues block deployment; low are nice-to-have.
4. **Suggest concrete edits** - For each issue, provide an exact text change or
   clear instructions for the fix. Make it possible to work through fixes
   systematically without guessing.
5. **Include acceptance checks** - For each fix, provide a verifiable criterion
   (e.g., "link resolves", "command runs successfully", "heading style matches").
6. **Verify fixes** - Re-check that each fix resolves the issue and the
   acceptance criterion passes.

## Verification

- [ ] Every identified issue has a specific file path and line number.
- [ ] Issues are categorized by type with consistent definitions.
- [ ] Each issue has a priority ranking with justification.
- [ ] Concrete edit suggestions are provided for each fix.
- [ ] Acceptance criteria are verifiable (commands, URLs, output checks).
- [ ] At least one fix has been verified to pass its acceptance criterion.

## Rules

- Never produce a list of issues without actionable fixes for each one.
- Never assign priority without justification grounded in impact analysis.
- Do not suggest vague edits like "update this"; provide exact text changes.
- Acceptance criteria must be testable without modifying the doc in unexpected ways.
- Focus on making it possible to systematically work through the fix list.
