# Reusable prompt: deployment readiness assessment [spec]

Copy-paste the block below into any AI coding agent before a release ships.
It gates the deploy with evidence, not vibes, and ends in an explicit
go/no-go verdict.

Keywords: deployment readiness, go no-go, preflight, rollback, migrations, smoke test, feature flags

---

Assess whether `[service or version]` is ready to deploy to `[environment]`.
The goal is a go/no-go verdict where every line of the checklist is backed by
a command, a config, or a link, not by confidence.

## Define the scope first

- The exact artifact and environment being deployed.
- What is in scope: migrations, rollback, smoke tests, flags, observability,
  dependencies, security, configuration.
- Out of scope: post-deploy tuning, unrelated services, future features.

## What to produce

1. Readiness matrix - one row per check, with the evidence, the command run,
   and the pass/fail result.
2. Migration plan - the exact migration commands, their rollback, and proof
   they were rehearsed.
3. Rollback plan - ordered revert steps, the trigger conditions, and the point
   after which rollback is no longer safe.
4. Smoke test results - the critical-path checks with their expected output
   and the actual output captured.
5. Flag and config state - the flag values and config keys that the deploy
   depends on, with where each is set.
6. Verdict - go or no-go, with the failing checks named if no-go.

## Method

1. **Migrations** - List every migration in the release. Verify each is
   reversible and was run against a copy of production data. Quote the
   command and its output.
2. **Rollback** - Find the repo's rollback procedure. Run its dry-run or
   rehearsal if one exists. Name the trigger that would fire it.
3. **Smoke tests** - Run the critical-path checks against a staging copy.
   Capture actual output for each.
4. **Feature flags** - Read the current flag state. Verify the rollout
   percentage and kill switch behave as the plan says.
5. **Observability** - Confirm logs, metrics, alerts, and dashboards exist for
   this service. Open one alert rule and one dashboard and name them.
6. **Dependencies** - Check each external dependency is up and version-pinned.
   Name the check command and its result.
7. **Security** - Verify secrets are from env config, permissions are
   least-privilege, and the security scan passes.
8. **Configuration** - Diff environment config against the release manifest.
   Flag anything unexpected.

## Verification

- [ ] Every check in the matrix has a command, config, or link as evidence.
- [ ] Migrations were rehearsed and their rollback is stated.
- [ ] Rollback trigger conditions are explicit, not "if something looks wrong".
- [ ] Smoke tests produced actual output, not planned output.
- [ ] Flag state matches the rollout plan.
- [ ] Observability was confirmed by opening a real alert rule and dashboard.
- [ ] Dependencies were checked with their status recorded.
- [ ] Secrets, permissions, and scans all pass.
- [ ] The final verdict is go or no-go, with failing checks named.

## Rules

- Never mark a check passed without the evidence line that proves it.
- Never deploy with an untested migration or a missing rollback trigger.
- Never put a secret value in the report; only how each secret is supplied.
- Never paper over an uncertain check; mark it unverified and block the deploy.
- Never skip the verdict: the report ends with go or no-go, never "probably".
