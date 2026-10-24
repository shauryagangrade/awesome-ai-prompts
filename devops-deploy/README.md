# DevOps & deploy

Prompts for shipping and running software in production: containers, deploys, infrastructure, migrations, and incidents.

Back to the [main index](../README.md#devops--deploy) or browse
[every prompt on one page](../website/index.html).

## Prompts

- [docker-containerization-prompt.md](docker-containerization-prompt.md) - small, secure, non-root container images.
- [deployment-runbook-prompt.md](deployment-runbook-prompt.md) - safe deploys with preflight checks and a rollback plan.
- [infrastructure-as-code-prompt.md](infrastructure-as-code-prompt.md) - Terraform/CDK with least-privilege IAM and state safety.
- [database-schema-migrations-prompt.md](database-schema-migrations-prompt.md) - backward-compatible schema changes: expand, migrate, contract.
- [monitoring-observability-prompt.md](monitoring-observability-prompt.md) - set up logging, metrics, and alerting with actionable dashboards.
- [incident-response-prompt.md](incident-response-prompt.md) - debug a live incident or write a post-mortem with structured triage.
- [kubernetes-deployment-prompt.md](kubernetes-deployment-prompt.md) - deploy to Kubernetes securely: real probes, zero-downtime rollouts, non-root pods.
- [feature-flag-rollout-prompt.md](feature-flag-rollout-prompt.md) - ship behind flags with progressive rollout, kill switch, and cleanup plan.
- [backup-disaster-recovery-prompt.md](backup-disaster-recovery-prompt.md) - backups proven by restore drills plus a scenario-based DR runbook with RTO/RPO.
- [ci-gate-diagnosis-prompt.md](ci-gate-diagnosis-prompt.md) - diagnose a failing CI gate: read the real log, compare with base branch, recommend one action with evidence.
- [incident-postmortem-prompt.md](incident-postmortem-prompt.md) - evidence-based postmortem: timeline, contributing factors, action items with owners, lessons.
- [infra-drift-detection-prompt.md](infra-drift-detection-prompt.md) - find live infrastructure drift vs IaC: refresh-only, classify differences, approve before any apply.

- [background-jobs-scheduled-tasks-prompt.md](background-jobs-scheduled-tasks-prompt.md) - async work that survives duplicates and deploys: idempotent handlers, bounded retries, dead-letter path, queue metrics, graceful drain.

- [cloud-cost-optimization-prompt.md](cloud-cost-optimization-prompt.md) - cut the bill from measurement: ranked offenders, rightsizing off real utilization, lifecycle policies, before/after savings table.

- [capacity-planning-prompt.md](capacity-planning-prompt.md) - name the wall and the date: headroom per bottleneck, forecast off a product metric, dated scaling options, early alerts.

## Adding a prompt here

Read [CONTRIBUTING.md](../CONTRIBUTING.md) for the file format and the gates,
model the new file on a neighbor in this folder, and add a one-line entry
above plus a [CHANGELOG.md](../CHANGELOG.md) entry under `[Unreleased]`.
