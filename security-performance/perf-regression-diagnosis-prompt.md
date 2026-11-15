# Reusable prompt: performance regression diagnosis [spec]

Copy-paste the block below into any AI coding agent when a change made this
service slower and you need the root cause with proof, not a guess.

Keywords: performance regression, profiling, benchmark, latency, throughput, before after, root cause

---

Diagnose a performance regression in `[service or component]`: the symptom is
`[what got slower, by how much, under what load]`. The goal is a root cause
tied to a specific code change, with before/after measurements that prove the
fix.

## Define the scope first

- Platform and environment where the regression was observed.
- Inputs: the workload, the traffic shape, the data size.
- Outputs: the metric that regressed, its unit, and the threshold that
  counts as fixed.
- Out of scope: unrelated services, known flaky benchmarks, hardware changes.

## What to produce

1. Baseline report - the metric on the base branch, with N runs, mean, and
   spread. Evidence shape: benchmark output pasted verbatim.
2. Regression report - the same metric on the current branch, same N runs.
3. Profile evidence - flame graph or profiler output naming the hot path.
4. Root cause - the commit and file:line that introduced the regression, with
   the diff excerpt.
5. Fix and verification - the minimal change, and the same benchmark re-run
   showing the metric back inside threshold.
6. Regression guard - the benchmark or test to add so this cannot regress
   silently again.

## Method

1. **Reproduce** - Run the repo's own benchmark or load tool (or add one if
   none exists) with a fixed workload. Run it on the base branch and on the
   current branch. Do not proceed until the gap is reproducible.
2. **Control noise** - Same machine, same load, same data, multiple runs.
   Report mean and spread, not a single sample.
3. **Profile** - Attach the repo's profiler or tracing tool. Capture the hot
   path on the regressed branch. Save the flame graph or trace file.
4. **Bisect to the change** - Use git history to find the commit that moved
   the metric. Name the file:line and quote the diff.
5. **Fix the smallest thing** - Change the hot path, not the surroundings.
   One change at a time.
6. **Verify** - Re-run the identical benchmark. Report before/after numbers
   with units and spread.
7. **Guard** - Add the benchmark to CI or the repo's perf suite so a future
   regression fails the gate.

## Verification

- [ ] The baseline and regression reports used the same workload and environment.
- [ ] The gap is reproducible across multiple runs, with mean and spread shown.
- [ ] The profile names a specific hot path, not a guess.
- [ ] The root cause is a commit with file:line evidence, quoted from the diff.
- [ ] The fix is minimal and changes only the hot path.
- [ ] The same benchmark re-run shows the metric back inside threshold.
- [ ] A regression guard (benchmark or test) was added to the repo's suite.

## Rules

- Never claim a regression without reproducible numbers on both branches.
- Never fix by disabling work, caching blindly, or adding a sleep; fix the root
  cause the profile names.
- Never report "faster" without the before/after numbers and units.
- Never ship a fix without the regression guard that would catch it again.
- Never tune what you cannot measure; if the metric is unclear, state it.
