# Using these prompts with opencode

[opencode](https://opencode.ai) is an AI coding agent that runs in the
terminal. These prompts are tool-agnostic, and opencode is the agent the demo in
the [main README](../README.md) runs on, so it is a good place to start. This
page covers the three ways to use a prompt, and how to keep the verification
rules in every session.

## 1. Paste it into a session

Run `opencode` in the repository you want to work on:

```bash
opencode
```

Open a prompt, copy everything below the `---` divider, and paste it into the
session with your task appended. The agent reads files itself, so do not paste
the code as well.

```text
<the prompt body>

Task: add rate limiting to the upload endpoint in src/api/upload.ts
```

## 2. Run it once, without the interface

`opencode run` submits a prompt and prints the result, which suits scripts and
CI. The `awk` expression copies the body and skips the intro above the divider:

```bash
opencode run "$(awk 'f{print} /^---$/{f=1}' \
  core-coding/feature-implementation-prompt.md) \
  Add rate limiting to the upload endpoint"
```

## 3. Save it as a slash command

A Markdown file in `.opencode/commands/` becomes a command named after the file.
This turns any prompt in this repo into `/codebase-audit`:

```bash
mkdir -p .opencode/commands
awk 'f{print} /^---$/{f=1}' code-review/codebase-audit-prompt.md \
  > .opencode/commands/codebase-audit.md
```

Then pass the target, which opencode substitutes for `$ARGUMENTS`:

```text
/codebase-audit the payments module
```

Add `$ARGUMENTS` to the command file where the target should go if the prompt
does not already ask for it. Commit `.opencode/commands/` so the rest of the
team gets the same commands.

## Make the verification rules permanent

Every prompt here ends by demanding evidence: read the code, run the project's
own tooling, and show the result before claiming the work is done. opencode
reads `AGENTS.md` for guidance that applies to every session, so the repeated
part belongs there instead of in each paste:

```markdown
# Project instructions

- Run `bun test` and `bun typecheck` before claiming a change works.
- Never modify unrelated code.
- Cite every finding as `path:line` and paste the command output that proves it.
```

opencode combines `AGENTS.md` files from the workspace directory up to the
project root, and V2 reads `AGENTS.md` only (not `CLAUDE.md`). Keep
repository-wide rules at the root and narrower rules next to the code they
cover.

## Good first prompts for a terminal agent

These lean on reading a repository and running its tooling, which is where
opencode is strongest:

- [codebase-audit-prompt.md](../code-review/codebase-audit-prompt.md) - a
  read-only pass over an unfamiliar repository.
- [feature-implementation-prompt.md](../core-coding/feature-implementation-prompt.md) -
  plan, implement, and verify one feature.
- [pr-review-prompt.md](../git-github/pr-review-prompt.md) - review a diff
  against the real gates before you push.
