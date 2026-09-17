# Reusable prompt: memory leak hunting

Copy-paste the block below into any AI coding agent to hunt down a memory leak
in a running service: measure the growth, isolate what retains memory, apply a
minimal fix, and verify the allocation curve goes flat under the same load.

---

Find and fix the memory leak in `[service or component]`. Work from
measurements, never from suspicion: a process that "seems to grow" is not
evidence. Establish the baseline curve, reproduce steady growth, isolate the
retainer, fix it minimally, and prove the curve flattens.

## Steps

1. **Take the baseline** - Determine the repo's own memory tooling and how the
   service is run (entry command, config, test harness). Measure RSS and, where
   available, the heap across a fixed window of the service's normal work. Record
   the numbers so the hunting has a before to compare against.
2. **Reproduce the growth** - Drive a repeatable scenario (same request, same
   operation, looped) and show the allocation curve rising with the loop count.
   A leak reproduces deterministically: the scenario you cannot grow is a
   symptom you have not isolated yet, not a non-issue.
3. **Get an allocation snapshot** - Use the stack's profiler or heap snapshot
   tooling (heap snapshot / sampling profiler / native tooling, whichever the
   repo already uses). Diff two snapshots taken one interval apart to see which
   objects and which root hold them.
4. **Name the retainer** - Identify the shortest ownership chain that keeps
   memory alive. Common suspects to check with evidence: an unbounded cache or
   public static collection, event listeners or subscriptions never removed,
   timers or intervals not cleared, closures holding large objects, pooled or
   reused objects accumulating fields, streams or connections not closed.
5. **Fix the smallest thing** - Change the retainer, not the surroundings: bound
   or evict the cache, remove the listener on unmount, clear the interval, close
   the stream. Prefer the boring fix that removes the reference over a clever
   rewrite.
6. **Verify by re-running the same scenario** - Run the exact loop from step 2
   for at least as long as before and show the curve is flat (or bounded) where
   it used to climb. Report the before and after numbers; a claim that it is
   fixed without the curve is not a fix.

## Rules

- Never patch based on an anecdote. Every change must be tied to a measured
  retainer from a snapshot, not a guess.
- One fix per investigation until the curve is flat; do not stack unrelated
  memory changes in the same change.
- Never disable a feature to hide the leak, and never add a periodic GC or pool
  flush as the "fix" without proving the root cause.
- No unrelated edits: this change only touches the leak path and its test.

## Verification

Paste the before and after memory curves (same scenario, same duration) with the
command that produced each. Show the retainer and ownership chain from the
diffed snapshots, and quote the line that holds the reference, with the fix on
top of it. Run the repo's test suite and show it passes.
