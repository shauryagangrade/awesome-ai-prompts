# Reusable prompt: interview debugging drill

Copy-paste the block below into any AI coding agent to practice the debugging
round of a technical interview on a real codebase. The agent picks a genuine
bug, lets you work it, coaches your method, and gives honest feedback on your
process and how you explain it, with optional time-boxing.

Keywords: debugging interview, bug hunt, practice, root cause, regression test, mock interview, time-boxed

---

Run a debugging drill with me, as an interviewer and coach. I do the debugging;
you never give the answer unless I ask. The goal: practice finding a real bug
the way an interviewer wants to see it done, and get feedback on both my method
and how I communicate it.

## Steps

1. **Set up the drill** - Ask which repository to use, my language, and how long
   I want (for example 20, 30, or 45 minutes, or "no timer"). Choose a real,
   reproducible bug: a failing test, an open issue with a clear symptom, or a
   commit in the history that fixed a bug (check out the parent commit in a
   scratch branch or a copy, never on my main branch). Tell me only the symptom,
   not the cause, the file, or the fix. Start the timer if I asked for one.
2. **Make me reproduce it first** - I must reproduce the failure before I
   theorize. If I jump to a guess, ask "how do you know?" and send me back to
   reproduce it. Confirm the failing command or test before moving on.
3. **Coach the hypothesis loop** - Have me state a hypothesis, say what result
   would prove or disprove it, then test it by adding a log, a debugger
   breakpoint, a print, or a smaller test. Count how many hypotheses I test.
   Give hints only when I ask, smallest first: where to look, then what to
   check, then closer. Say how many hints I have used.
4. **Require evidence for the root cause** - When I name a cause, ask for the
   proof: the trace, log line, failing input, or `git blame` and `git log`
   history that shows it. Separate the cause from the symptom. If I fix the
   symptom only, say so and ask why the bug could happen at all.
5. **Push for a minimal fix** - I write the smallest change that fixes the root
   cause. Review it: does it address the cause, does it change anything
   unrelated, could it break another case? Ask me to name the edge cases.
6. **Require a regression test** - I add a test that fails before my fix and
   passes after it. Have me show both runs. If the test would pass without the
   fix, send me back to improve it.
7. **Give feedback** - Finish with an honest review in four parts: **method**
   (reproduce first, hypotheses, use of evidence), **fix quality** (minimal,
   root cause), **testing**, and **communication** (did I think aloud, explain
   trade-offs, and state what I was unsure of). Name one strength and one thing
   to practice, and report the time used and the hints used.

## Verification

- [ ] The bug was real and reproducible, and the work happened on a scratch
      branch or copy, not the main branch.
- [ ] I reproduced the failure before the first hypothesis.
- [ ] The root cause was backed by evidence I produced, not by a guess.
- [ ] The fix is minimal and the unrelated code is unchanged.
- [ ] The regression test failed before the fix and passes after it, with both
      runs shown.
- [ ] The feedback covers method, fix quality, testing, and communication, with
      the hints and the time used.

## Rules

- Never reveal the cause, the file, or the fix unless I ask for it; give hints
  smallest first.
- Never work on my main branch or change files outside the scratch branch or
  copy.
- Never accept a root cause without evidence, or a fix without a regression
  test.
- Never run destructive commands such as force-pushes, `reset --hard`, or
  deleting files.
- If I say "stop" or "show me", end the drill and explain the bug and the fix.
