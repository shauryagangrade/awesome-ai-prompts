# Security & performance

Prompts for hardening and speeding up software: vulnerabilities, secrets, dependencies, auth, load, and memory leaks.

Prompts carrying the light-blue badge are the heavyweight
[spec](../README.md#security--performance) prompts: multi-section, with
hard constraints and required verification.

Back to the [main index](../README.md#security--performance) or browse
[every prompt on one page](../website/index.html).

## Prompts

- [security-audit-prompt.md](security-audit-prompt.md) <img src="../docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - full-repo audit: injection, auth, secrets, dependencies, with verified findings.
- [performance-optimization-prompt.md](performance-optimization-prompt.md) - measure-first optimization with before/after proof.
- [secrets-management-prompt.md](secrets-management-prompt.md) - audit and remediate hardcoded secrets, set up env-based secret management.
- [load-testing-prompt.md](load-testing-prompt.md) - design and run load/stress tests with measurable thresholds.
- [dependency-audit-prompt.md](dependency-audit-prompt.md) - audit dependencies for vulnerabilities, license issues, and staleness.
- [threat-modeling-prompt.md](threat-modeling-prompt.md) - STRIDE-style threat model ranked by real risk, with verified mitigations.
- [auth-implementation-prompt.md](auth-implementation-prompt.md) - implement sessions/OAuth/JWT safely with server-side authorization everywhere.
- [dependency-vuln-triage-prompt.md](dependency-vuln-triage-prompt.md) - triage dependency vulnerability reports: reachability proof, exploitability rating, cheapest verified fix.
- [secrets-scanning-response-prompt.md](secrets-scanning-response-prompt.md) - respond to a leaked secret: rotate first, find copies, assess misuse, plan cleanup, prevent recurrence.
- [memory-leak-hunting-prompt.md](memory-leak-hunting-prompt.md) - find and remove a leak from measurements: baseline, reproduced growth, diffed snapshots, and a flat after-curve.

- [prompt-injection-defense-prompt.md](prompt-injection-defense-prompt.md) <img src="../docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - threat-model one attack class: where untrusted text reaches the context, out-of-band tool gating, a red-team suite, honest residual risk.

- [privacy-gdpr-compliance-review-prompt.md](privacy-gdpr-compliance-review-prompt.md) <img src="../docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - systematic privacy pass: data inventory with retention, lawful basis, consent withdrawal, user rights flows, processors, ranked minimization.

- [rate-limiting-abuse-prevention-prompt.md](rate-limiting-abuse-prevention-prompt.md) <img src="../docs/media/spec-badge.svg" alt="spec" style="vertical-align:-3px"> - protect public endpoints: limits tiered by cost, algorithm chosen for the traffic shape, shared counters, load-test proof.

## Adding a prompt here

Read [CONTRIBUTING.md](../CONTRIBUTING.md) for the file format and the gates,
model the new file on a neighbor in this folder, and add a one-line entry
above plus a [CHANGELOG.md](../CHANGELOG.md) entry under `[Unreleased]`.
