# Reusable prompt: monitoring and observability

Copy-paste the block below into any AI coding agent to set up logging,
metrics, and alerting - actionable dashboards and alerts, not noisy
dashboards nobody checks.

---

Set up monitoring and observability for `[service / application / endpoint]`.
The goal: when something goes wrong, you know what, where, and why within
minutes, not hours of log-diving.

## Steps

1. **Understand the system** - Read the code to identify the critical paths,
   external dependencies, error conditions, and performance-sensitive
   operations. Understand what "healthy" looks like before defining what
   "broken" looks like.
2. **Structured logging** - Add structured (JSON) logging at key points:
   request entry/exit, external service calls, database queries, error
   paths, and business-critical operations. Use consistent log levels
   (error, warn, info, debug) and include correlation IDs for request
   tracing. Follow the repo's existing logging conventions.
3. **Define metrics** - Instrument the four golden signals:
   - **Latency** - response time for requests (p50, p95, p99)
   - **Traffic** - requests per second
   - **Errors** - error rate and error types
   - **Saturation** - CPU, memory, connection pool usage
     Use the repo's existing metrics library (Prometheus client, StatsD,
     OpenTelemetry).
4. **Set up dashboards** - Create dashboards that answer the questions you'd
   ask during an incident: Is the service healthy? What's the error rate?
   Which endpoints are slow? Are dependencies responding? Keep dashboards
   focused - one service per dashboard, key signals visible at a glance.
5. **Configure alerts** - Create alerts for actionable conditions only:
   error rate above threshold, latency exceeding SLA, dependency
   unreachable, disk/memory critical. Every alert must have a clear
   severity, a runbook link, and a person/team who owns the response.
   Avoid alert fatigue from noisy or informational alerts.
6. **Verify** - Trigger a real error or simulate one (kill a dependency,
   return an error). Confirm the logs capture it, the metrics reflect it,
   the dashboard shows it, and the alert fires.

## Rules

- Never add logging in hot loops or high-frequency paths without considering
  the performance impact.
- Never create alerts that nobody should act on - if you can't define the
  response action, don't alert on it.
- Never use plain text logging when structured logging is available in the
  stack.
- If the repo already has observability tooling, extend it rather than
  introducing a parallel system.
