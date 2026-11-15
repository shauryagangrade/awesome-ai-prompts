# Reusable prompt: runbook writing

Copy-paste the block below into any AI coding agent to write an incident
runbook. The goal is to create verifiable, executable documentation that guides
responders through diagnosis, mitigation, and recovery.

Keywords: runbook, incident response, troubleshooting, recovery, verification, steps

---

Write a runbook for `[incident type or scenario]` in `[service or system]`. The
runbook must be precise, verifiable, and actionable. Every command should be
copy-pasteable and verifiable in the actual environment.

## Steps

1. **Symptoms** - Define the observable symptoms that indicate this incident.
2. **Diagnosis** - Provide specific commands with expected outputs for each check
   (e.g., curl, grep, netstat). Include how to interpret the output.
3. **Mitigation** - List step-by-step actions to contain or resolve the issue.
   Include verification steps for each action.
4. **Rollback** - Provide clear rollback procedures with verification steps.
   State the trigger conditions for rolling back.
5. **Verification** - Define how to confirm the issue is resolved.
6. **Escalation** - Specify when and how to escalate, with contact information.

## Verification

- [ ] All commands are copy-pasteable and have expected results.
- [ ] Each verification step has a concrete expected outcome.
- [ ] Rollback procedures are clear and verifiable.
- [ ] Escalation criteria and contacts are included.
- [ ] The runbook is written for the actual environment, not hypothetical.

## Rules

- Never put secrets in the runbook; reference how they're supplied.
- If a step is uncertain, mark it as needing confirmation rather than stating
  it as fact.
- Match the environment's conventions (naming, logging, alerting).
- Do not fabricate commands you haven't validated.
- Every step must be verifiable, not just subjective.
