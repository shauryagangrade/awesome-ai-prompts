# Reusable prompt: migration guide

Copy-paste the block below into any AI coding agent to write a migration guide
for a breaking change, upgrade, or API move - every step tested, with a way to
roll back and a way to check it worked.

Keywords: migration guide, breaking changes, upgrade, deprecation, rollback, verification

---

Write a migration guide for `[the change: version X to Y, an API move, a config
format, or a schema change]`, for the people who have to upgrade. The goal: a
reader on the old version can reach the new one, can check that it worked, and
can go back. Every command and code sample in the guide must be one you ran.

## Steps

1. **Establish the facts** - Read the diff, the changelog, and the linked issues
   between the two versions (`git diff <old>..<new>`, `git log`). List every
   breaking change as: what it was before, what it is now, and who is affected.
   Look for removed or renamed options, changed defaults and output formats,
   behavior changes, new minimum versions, and data or schema changes. Mark
   anything you cannot confirm from the code as unverified.
2. **Name the audience** - Say who is upgrading (app developers, operators,
   plugin authors) and which starting versions the guide covers. If the path
   differs by starting version, split it.
3. **Order the steps** - Preparation first (back up, pin versions, read the list
   of breaking changes), then the changes in the order they must happen, then
   cleanup. For each step give what to do, the before and after code or config,
   and what the reader should see when it worked.
4. **Run every example** - Check out the old version, follow your own steps, and
   run each command and sample against the new one. Show the output. When an
   example fails, fix the guide, not the example. Anything you could not run is
   marked untested.
5. **Write the rollback** - How to return to the old version, which data or state
   cannot be rolled back (migrated databases, written files), and the point
   after which going back is no longer simple.
6. **Add checks and deprecations** - A short list of commands the reader can run
   to confirm success, with the expected output. If the old behavior still works
   for now, give the deprecation timeline: what warns, from which version, and
   when it stops. Add the failures you hit while testing, with their fixes.
7. **Link it from where readers look** - The release notes, the README, and any
   deprecation warning the code prints.

## Verification

- [ ] Every breaking change in the diff appears in the guide, or the guide says
      why it needs no action.
- [ ] Each command and sample was run starting from the old version, with the
      output shown.
- [ ] The rollback section names what cannot be undone.
- [ ] The success check uses commands with expected output.
- [ ] Unverified claims and untested examples are marked as such.
- [ ] The guide is linked from the release notes and the README.

## Rules

- Never include an example you did not run.
- Never leave out a breaking change because it looks minor to you.
- Never promise a rollback you did not try. Say what is irreversible.
- Give every deprecation a date or a version it ends in.
- Keep the reasons for the change short. The reader needs the steps.
