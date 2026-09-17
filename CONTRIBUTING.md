# Contributing to Awesome AI Prompts

---

## How to Contribute

### Reporting Bugs

Open an issue using the [bug report template](.github/ISSUE_TEMPLATE/bug_report.yml). Include steps to reproduce, expected vs actual behavior, and which prompt/agent you were using.

### Requesting Features

Open an issue using the [feature request template](.github/ISSUE_TEMPLATE/feature_request.yml).

### Adding a Prompt

1. Fork the repo and create a branch: `git checkout -b docs/add-my-prompt`
2. Model your file on an existing prompt (or [.github/PROMPT_TEMPLATE.md](.github/PROMPT_TEMPLATE.md) if present): an H1 title, a one-line "copy-paste this block" usage note, then the prompt block separated by a `---` divider.
3. Name it `kebab-case-prompt.md` and place it in the matching category folder (`a-a-p-contributing/`, `core-coding/`, `git-github/`, `code-review/`, `testing-quality/`, `docs-delivery/`, `security-performance/`, `devops-deploy/`, `career-learning/`, `frontend-ui/`, `system-design/`, `data-ai/`, `mobile-dev/`).
4. Verify locally: `bash scripts/check-links.sh` - must pass clean. This checks that every README link resolves and each prompt file follows the repo's structure.
5. Open a PR against `main` with a one-line entry added to the matching category in the README. If the prompt takes on a big, risky task, mark its entry with the light-blue [spec] badge (`<img src="docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px">`) and bump the spec-count badge on the category's Contents line.

---

## Automated Gates

The `Commit checklist` workflow runs on every PR and enforces:

- **Listed** - every `*-prompt.md` in a category folder must be linked from the README
- **Changelogged** - newly added prompts need an entry under `[Unreleased]` in CHANGELOG.md
- **In sync** - category folders and README sections must match in both directions, and the Contents counts must match the files on disk
- **Conventional title** - PR titles follow Conventional Commits (`feat | fix | docs | style | refactor | perf | test | ci | chore`)

Run the consistency checks locally before pushing:

```bash
bash scripts/check-consistency.sh
bash scripts/check-prettier.sh
```

The `URL rot check` workflow runs weekly (and on manual dispatch) and fails if an
external link in the README or any prompt file is dead, so badges and referenced
tools cannot rot silently. Run it locally with
`python3 scripts/check-external-links.py`.

---

## Good First Issues

Look for issues labeled [`good first issue`](https://github.com/shauryagangrade/awesome-ai-prompts/labels/good%20first%20issue).

---

## Code Style

- Prompts are tool-agnostic: they work with any AI coding agent (Claude, ChatGPT, Copilot, Cursor, opencode, ...)
- Ground every prompt in verification - "verify, don't guess"; no claims without a way to check them
- Keep prompts self-contained: everything a user needs to paste is inside the block after the `---`

---

## PR Guidelines

- One prompt (or one logical change) per PR - keep scope tight
- PR description must explain _why_, not just _what_
- Run `bash scripts/check-links.sh` before opening the PR
- AI-assisted contributions are welcome - provided you have reviewed and tested the output

---

## Review Policy

External pull requests get a first response from a maintainer within 48 hours,
weekends excepted. The response is a real review note, never an auto-reply.

For small, correct pull requests - one prompt, a broken link, a stale count -
we merge first and fix nits ourselves. A nit is something that does not affect
correctness: a missing period, minor wording, an awkward line wrap. Substantive
feedback - wrong category, a broken gate, prompt instructions that are wrong -
goes back to the author before merge. If a review says "looks good, I will fix
the nits after merge", expect the PR merged without another round trip. If it
requests changes, treat that as a real change, not a style preference.

Why: a first-time contributor whose PR merges inside a week comes back. A
first-time contributor whose PR sits for two weeks does not.

---

## Commit Style

[Conventional Commits](https://www.conventionalcommits.org/):

```text
docs: add code-interview-practice prompt
docs: fix broken link in README
chore: add docs lint CI
```

Types: `feat | fix | docs | style | refactor | perf | test | ci | chore`

---

## Community

Questions and discussion happen in [GitHub Discussions](https://github.com/shauryagangrade/awesome-ai-prompts/discussions).
