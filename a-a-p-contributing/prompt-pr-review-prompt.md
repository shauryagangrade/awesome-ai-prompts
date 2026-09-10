# Reusable prompt: prompt PR review

Copy-paste the block below into any AI coding agent to review a pull request
that adds or changes prompts in this repository, against its real gates.

---

Review pull request `#N`, which changes prompts in this `awesome-ai-prompts`
repository. Return an explicit verdict: APPROVE, READY AFTER FIXES, or REQUEST
CHANGES, with every finding tied to a file and line. Do not skim - read the
whole diff and the full text of every changed prompt.

## Steps

1. **Read the PR in full** - Read the description and every changed file,
   especially the complete body of each new or edited `*-prompt.md`, above and
   below the `---` divider.
2. **Run the repo's own gates** - Run `bash scripts/check-links.sh` and
   `bash scripts/check-consistency.sh`. They must pass clean; if they fail,
   name each failing check with its output.
3. **Check structure** - Every prompt starts with an H1 title (`# Reusable
   prompt: ...`), has a short usage note, a `---` divider, then the body. Files
   sit in a category folder, are kebab-case, and end in `-prompt.md`. No em
   dashes anywhere; use an ASCII hyphen.
4. **Check the index is in sync** - The README section links the file, the
   one-line description is accurate, the Contents count for that category
   matches the folder, and a `## [Unreleased]` CHANGELOG entry names the file.
5. **Review quality, not just format** - The prompt must be tool-agnostic,
   self-contained (everything to paste sits after the `---`), and
   verification-first: every command or check it names must be real and
   runnable in this repo. Flag any step that asks an agent to "verify" without
   naming how.
6. **Verify claims about the repo** - If the prompt references scripts,
   workflows, or conventions, confirm they exist and behave as described by
   reading `scripts/`, `.github/workflows/`, and `CONTRIBUTING.md`.
7. **Give a verdict** - Summarize what is right, list each fix with the exact
   file, and approve only when the gates pass, the index is in sync, and the
   prompt would actually keep an agent honest.

## Rules

- Never approve on the author's description alone; the checks must run.
- Separate taste from mistakes: note a style preference separately from a rule
  violation.
- Keep the review in the repo's terms: mergeable first time, verified, tight
  scope.

## Verification

Show the outputs of the two scripts and the markdownlint run, and state that
the em-dash scan was clean, with the commands you used.
