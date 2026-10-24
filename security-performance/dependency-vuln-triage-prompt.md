# Reusable prompt: dependency vulnerability triage

Copy-paste the block below into any AI coding agent to turn a raw vulnerability
report (npm audit, Dependabot, Snyk, osv-scanner) into a ranked fix list based
on whether each issue is actually exploitable in this codebase.

Keywords: cve triage, npm audit, dependabot alerts, osv-scanner, exploitability, false positive, vulnerable dependency

---

Triage the vulnerability findings for this repository's dependencies. The goal:
decide which findings are truly exploitable here, rank them, and give a
verified remediation for each, with the reasoning written down.

## Steps

1. **Collect the report** - Use the scanner output the user provides, or run the
   repo's own tooling (`npm audit`, `pip-audit`, `cargo audit`, `osv-scanner`,
   or read the Dependabot or Snyk alerts). List every finding with its
   advisory ID, package, installed version, fixed version, and the scanner's
   severity. Paste the raw output rather than a paraphrase.
2. **Trace how each package is used** - For each finding, find whether the
   package is a direct or transitive dependency (`npm ls`, `pipdeptree`,
   `cargo tree`), whether it ships to production or only runs in dev and test,
   and which files import the vulnerable function. Name the call sites with
   `file:line` references.
3. **Judge exploitability** - Read the advisory and decide whether the
   vulnerable code path is reachable with input an attacker controls. Rate it:
   **exploitable** (reachable, attacker input), **conditional** (needs a
   specific configuration or feature), **not reachable** (the vulnerable
   function is never called), or **dev-only**. Record the evidence for the
   rating, not just the verdict.
4. **Evaluate the fix options** - For each finding, list the options in order
   of effort: a patch or minor upgrade, a major upgrade (with the breaking
   changes from the changelog), an override or resolution of the transitive
   version, a replacement package, or a workaround such as disabling the
   feature. Note which options the lockfile and the version constraints allow.
5. **Prioritize** - Rank by exploitability first, then by business impact (what
   the affected code protects), then by how easy the fix is. Group findings
   that one upgrade resolves together.
6. **Apply and verify** - Make the chosen fix for the highest-priority items,
   then re-run the scanner and the test suite and show the output. For any
   finding left open, write the reason and a date to re-check.
7. **Record the decisions** - Write a short triage record: each finding, its
   rating, the evidence, the decision (fix, defer, accept), and the owner.

## Verification

- [ ] The raw scanner output was captured, and every finding appears in the
      triage record.
- [ ] Every rating of "not reachable" or "dev-only" cites the code or config
      that proves it.
- [ ] Each fix was checked against the package changelog before being applied.
- [ ] The scanner and the test suite were re-run after the fixes, with output
      shown.
- [ ] Any finding left open has a written reason and a re-check date.
- [ ] No finding was dismissed on the scanner's severity label alone.

## Rules

- Never mark a finding "not exploitable" without evidence from the code, the
  config, or the advisory itself.
- Never upgrade a major version without reading the changelog and running the
  tests.
- Never silence or ignore an alert without writing down why.
- Never add a new dependency just to clear a finding before checking whether
  the existing package has a fixed version.
- If you cannot tell whether a path is reachable, say so and rate it
  conditional rather than guessing.
