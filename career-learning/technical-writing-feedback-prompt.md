# Reusable prompt: technical writing feedback

Copy-paste the block below into any AI coding agent to critique technical
documentation for clarity, verifiability, and completeness, with actionable
improvements.

Keywords: technical writing, documentation review, clarity, verifiability, docs feedback

---

Review technical documentation for `[file or directory]`. The goal is to
improve docs quality: is it clear to the audience? Can every step be followed
successfully? Are examples concrete and accurate? Provide specific, actionable
suggestions with before/after examples.

## Steps

1. **Clarity** - Assess whether the documentation is clear to the target
   audience. Are concepts explained well? Is the structure logical?
2. **Verifiability** - Check whether commands are runnable and steps are
   testable. Can someone follow them successfully? Identify any broken or
   unverifiable commands.
3. **Completeness** - Verify prerequisites, expected outputs, and edge cases
   are covered. Check for missing steps or assumptions.
4. **Links** - Validate all links are correct and point to the right places.
   Check for broken references.
5. **Structure** - Assess whether information is organized logically.
   Does the documentation follow a consistent structure?
6. **Accuracy** - Ensure content is up-to-date and correct. Check for outdated
   information or stale references.
7. **Examples** - Verify examples are concrete and helpful. Check that they
   match the actual code behavior.

## Verification

- [ ] Each area above is addressed with specific, actionable feedback.
- [ ] Verifiability findings include concrete examples of commands that fail
      or steps that cannot be followed.
- [ ] Every suggestion includes a before/after example showing the improvement.
- [ ] Links are checked against actual URLs or file paths.
- [ ] Findings distinguish between blocking issues, suggestions, and nitpicks.

## Rules

- Never accept "reads fine" as a substitute for verifying each step works.
- Never claim docs are good without citing specific strengths and weaknesses.
- Do not machine-edit docs based on this review alone; review first, then fix.
- No unrelated edits: keep feedback focused on documentation quality only.
