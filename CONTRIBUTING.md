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
3. Name it `kebab-case-prompt.md` and place it in the matching category folder (`a-a-p-contributing/`, `core-coding/`, `git-github/`, `code-review/`, `testing-quality/`, `docs-delivery/`, `security-performance/`, `devops-deploy/`, `career-learning/`, `frontend-ui/`, `system-design/`, `data-ai/`).
4. Verify locally: `bash scripts/check-links.sh` - must pass clean. This checks that every README link resolves and each prompt file follows the repo's structure.
5. Open a PR against `main` with a one-line entry added to the matching category in the README.

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
```

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
- PR description must explain *why*, not just *what*
- Run `bash scripts/check-links.sh` before opening the PR
- AI-assisted contributions are welcome - provided you have reviewed and tested the output

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
