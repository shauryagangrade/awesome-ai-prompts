# Reusable prompt: codebase understanding [spec]

Copy-paste the block below into any AI coding agent to build a verified,
detailed understanding of an unfamiliar repository. The agent must confirm
every claim against real code and configuration, not the README alone, and
produce a structured report with file:line citations.

---

Build a detailed understanding of this repository. Produce a report that a
new team member could use to navigate the codebase on day one. Verify
everything against the code, lockfiles, and config - do not paraphrase the
README.

## Define the scope first

Before reading code, state:

1. **What you need to understand** - Clarify the focus: full repo overview, a
   particular subsystem, the data flow for a specific feature, or something
   else. If the request is broad, pick the highest-value slice and say so.
2. **What depth** - Quick orientation (stack + entry points) or deep dive
   (data flow, conventions, extension points)? State the level explicitly.
3. **What is out of scope** - Exclude anything not relevant to the request.

Do not begin reading until the scope and depth are defined.

## What to produce

1. **What it is** - One or two sentences: what the project does and who it is
   for. Confirm with the README and with real code, not just the repo name.

2. **Tech stack, verified** - Languages, frameworks, runtimes, package/build
   tooling, and the versions that matter. Pull these from lockfiles, manifests,
   and config files - not from README claims or guesses. If versions cannot be
   determined, say so.

3. **Architecture, with evidence** - The high-level shape: how the code is
   organized (monolith, services, packages, monorepo), the entry points (main,
   CLI, server, worker, script), and how the major pieces communicate. For each
   structural claim, cite a file, directory, or function that proves it.

4. **Key data flow** - Walk one or two realistic user journeys through the code:
   entry point → core logic → storage or external calls → response. Cite
   file:line for each hop. If multiple paths exist, pick the most representative
   and note the alternatives.

5. **Conventions and gotchas** - Things a newcomer will trip on: unusual patterns,
   required env vars, config files, build and test setup, extension points, and
   known quirks. Distinguish documented conventions from observed behavior.

6. **How to run it** - Exact commands to install dependencies, run, and test.
   Verify against the README, Makefile, scripts/, package.json/pyproject.toml,
   and CI workflows. If a command cannot be verified, say so.

7. **Open questions** - List anything that could not be confirmed from the code,
   and what would resolve it (e.g. a missing env var, an undocumented script,
   a dependency version that could not be read).

## Method

1. **Read the top-level structure** - Start with the root: manifest files,
   package/dependency configs, build scripts, CI workflows, and any
   documentation that describes the architecture. Form initial hypotheses.

2. **Form hypotheses, then verify** - For each structural claim (e.g.
   "this is a React app with a Node backend"), find the file or config that
   proves it. If a hypothesis cannot be confirmed, mark it as an open question.

3. **Trace a real journey** - Pick a concrete flow a user or system would take,
   and read the actual code path end to end. Cite file:line for each step.

4. **Inspect the test suite** - Read how the project tests itself. The test
   layout and patterns often reveal conventions and architecture more clearly
   than the source alone.

5. **Check the CI and scripts** - Read the workflows and helper scripts to
   understand how the project is built, tested, and deployed. These often
   expose requirements and gotchas that source code alone does not.

6. **Summarize with citations** - Produce the report above, with file:line
   references for every structural claim. No claim without evidence.

## Verification

Before reporting the understanding complete, confirm each of these:

- [ ] Every structural claim (stack, architecture, entry points) is backed by a
      file, config, or function citation.
- [ ] Versions and dependencies are read from lockfiles or manifests, not
      inferred from the README.
- [ ] At least one real data flow is traced end to end with file:line citations.
- [ ] Run commands are verified against the project's actual tooling (README,
      Makefile, scripts/, CI, manifest), not invented.
- [ ] Anything that could not be confirmed is listed as an open question, not
      stated as fact.
- [ ] The report distinguishes documented conventions from observed behavior.

## Rules

- Read the code. For every structural claim, point to a file or function that
  proves it.
- If the README is wrong or stale, say so and rely on the code.
- Be concise and concrete. No filler like "this project is built with modern
  best practices".
- State scope and depth before reading. Do not attempt the whole repo plus a
  deep dive in one pass unless the request is small.
- If something cannot be determined from the repository, say what is missing
  and how to find it - do not guess.
