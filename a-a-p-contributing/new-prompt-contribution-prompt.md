# Reusable prompt: new prompt contribution

Copy-paste the block below into any AI coding agent to add a new prompt to
this repository, in a form a maintainer can merge on the first pass.

---

Help me add a new prompt to this `awesome-ai-prompts` repository. Every prompt
here follows strict conventions and CI enforces them, so read the rules before
writing anything. Do not write the file until we have agreed on the idea.

## Steps

1. **Read the conventions first** - Read `CONTRIBUTING.md`,
   `.github/PROMPT_TEMPLATE.md`, and two or three existing prompts in the
   category you intend to use. Note the exact structure: an H1 title, a short
   copy-paste usage note, a `---` divider, then the prompt body.
2. **Confirm the idea is new** - List the closest existing prompts and say how
   this one is different. If it duplicates an existing prompt, stop and propose
   a distinct idea instead. Never add a near-copy.
3. **Draft after the divider** - Write the body below the `---` divider. Keep
   it direct and prescriptive: numbered `## Steps` with bold lead-ins, a
   `## Rules` list, and a `## Verification` section that names actual commands.
   Ground it in "verify, don't guess": no claim without a way to check it.
4. **Follow the repo's rules** - Tool-agnostic (works with Claude, ChatGPT,
   Copilot, Cursor, opencode, and others). Self-contained: everything the user
   pastes lives inside the block. No em dashes anywhere, use an ASCII hyphen.
   Flag the file with `[spec]` in README and CHANGELOG only for multi-section
   prompts for big, risky work.
5. **Name and place it** - `kebab-case-action-prompt.md` in the matching
   category folder. Never put prompt files at the repo root.
6. **Update the index** - Add a one-line entry in the matching README section
   followed by a short description ending in a period, and bump that category's
   count in the Contents list.
7. **Add a changelog entry** - Under `## [Unreleased]` in `CHANGELOG.md`, add a
   line that names the file in backticks, then a hyphen, then a short
   description.
8. **Verify before claiming done** - Run `bash scripts/check-links.sh` and
   `bash scripts/check-consistency.sh`, and run markdownlint on the changed
   files with `npx --yes markdownlint-cli2@0.17.2 <file>`. All must pass. Show
   me the script output; never just your word that they passed.
9. **Commit and PR** - One conventional commit (`docs: add <name> prompt`),
   reference any related issue, and write a PR description that explains why
   this prompt belongs here.

## Rules

- Never write a prompt that demands verification without naming the actual
  command or check that runs it.
- Never say a check passed unless you ran it and saw the output.
- Keep the change tight: one prompt per PR, no unrelated wording or format
  edits to existing prompts.
- If a rule is ambiguous, ask before writing.

## Verification

Run every command in step 8 and paste the outputs. Confirm the README section
lists exactly one new entry, the Contents count matches the folder, and the
CHANGELOG entry names the new file.
