# Reusable prompt: infrastructure drift detection

Copy-paste the block below into any AI coding agent to find where live
infrastructure no longer matches its Terraform, CloudFormation, or Pulumi code,
rank the differences by risk, and choose a safe fix for each one.

Keywords: infrastructure drift, terraform plan, config drift, out of sync, manual change, iac, cloudformation drift

---

Detect drift between this repository's infrastructure code and the live
environment. The goal: a verified list of every difference, ranked by risk,
with a recommended fix for each, and nothing changed until it is approved.

## Steps

1. **Establish the scope** - Identify the IaC tool and the stacks, workspaces,
   accounts, and environments it manages, and how state is stored. Confirm which
   environment you are looking at before you run anything. Use read-only
   credentials. If you only have write access, stop and say so.
2. **Detect drift read-only** - Run the tool's own comparison without applying
   anything: `terraform plan -refresh-only` (or `terraform plan -detailed-exitcode`),
   `aws cloudformation detect-stack-drift`, `pulumi refresh --diff`, or the
   equivalent. Save the full output. Note any resources the code does not manage
   at all, since a plain plan will not show them.
3. **List every difference** - For each drifted resource, record its address or
   ID, the attribute that differs, the value in code, the value that is live,
   and when it last changed if the audit log (CloudTrail, activity log) shows
   it. Quote the tool output, not a summary.
4. **Classify the severity** - Rank each one **critical** (open network access,
   public storage, widened IAM, disabled encryption or logging), **high**
   (affects availability, data, or cost materially), **medium** (behavior or
   capacity differs from code), or **low** (tags, descriptions, cosmetic). Give
   the reason for each rating.
5. **Find the origin** - Decide whether each difference is an **intentional
   manual change** (a hotfix, an incident response, a console experiment), an
   **unintended drift** (an external system, an autoscaler, a forgotten edit),
   or **expected** (an attribute the tool is meant to ignore). Use the audit
   log and the change history as evidence, and mark it unknown if there is
   none.
6. **Recommend a fix per item** - Choose between **updating the code to match
   reality** (when the live change is right and should be kept) and **applying
   the code to restore the intended state** (when the live change is wrong).
   Flag any restore that could cause downtime or data loss, and say how to
   avoid it.
7. **Define the verification** - For each fix, state how to prove it worked: a
   clean refresh or plan with no diff, a re-run of the drift check, and the
   service check that shows nothing broke. Do not apply anything until the
   plan is reviewed and approved.

## Verification

- [ ] The environment and credentials were confirmed read-only before any
      command ran.
- [ ] The drift output is saved and each finding quotes it.
- [ ] Each difference lists the code value, the live value, and the severity
      with a reason.
- [ ] Each difference is labeled intentional, unintended, or expected, with the
      evidence or "unknown".
- [ ] Each recommended fix names its direction (change code or restore state)
      and a verification step.
- [ ] Nothing was applied, destroyed, or imported without approval.

## Rules

- Never run `apply`, `destroy`, or an import while detecting drift.
- Never assume the code is right; a manual change made during an incident may
  be the correct one.
- Never print secret values from state files or live resources in the report.
- Never treat an empty plan as "no drift" without checking for resources the
  code does not manage.
- If you cannot tell which environment you are connected to, stop and ask.
