# Reusable prompt: error handling strategy

Copy-paste the block below into any AI coding agent to design and apply one
coherent error handling strategy across a component or service: every failure
mode mapped to a typed error, a log line that can be searched, and a documented
policy for what is retried versus what reaches the user.

---

Design and apply a consistent error handling strategy for `[component or
service]` in this repository. The goal: no bare try/catch, no swallowed
errors, no unhandled crash on a path a user can hit. Inspection here means
reading code, not trusting it.

## Steps

1. **Read the existing conventions** - Find how this repo currently handles
   errors: exception types or error classes already in use, a logging library,
   response envelopes for APIs, retry utilities, and where errors are caught
   today. Mirror the existing style unless it is the problem. Note every catch
   that swallows the error or logs without context.
2. **Map the failure modes** - Enumerate every way this code can fail:
   transport and timeouts, persistence, validation and authorization, bad
   inputs, and resource limits. For each, name where it surfaces in code and
   what happens to the caller today.
3. **Define the policy** - Write one small policy before touching code:
   which failures are recoverable (retry with backoff and an idempotency
   guard), which are fail-fast (crash loudly so nothing silently drops), and
   which map to a user-visible error message. Distinguish programming errors
   from expected failures; the first are bugs, the second are control flow.
4. **Type the errors** - Introduce a small set of typed errors (framework
   exception or error subclasses) so callers branch on intent, not on message
   text. Carry structured context with each error: operation, resource,
   retryable flag, and a stable code for logs and monitors.
5. **Implement the smallest change** - Route each catch site through the
   policy. Add retries only where the operation is idempotent and the failure
   is transient. Never wrap a generic catch in silence: log the full context,
   then rethrow or map to a clean failure for the caller.
6. **Surface the right thing** - The user-facing layer shows a controlled
   message and a meaningful status; the internal layer records the stack and
   context. Never leak internals (SQL, stack traces, secrets) into what the
   user sees.
7. **Verify by injection** - Prove the policy, do not assert it. Force each
   failure mode (point a config at a dead endpoint, close a pool, pass bad
   data) and confirm the log line contains enough to debug, the retry behaves
   with backoff, and the user path returns the intended result. Show the
   before and after output.

## Rules

- Never add a catch block that swallows the error or logs without context.
- Never guess which failures can happen: find the failure sites in the code
  and list them before deciding the policy.
- Keep the policy close to the code it governs, not a page of theory elsewhere.
- No unrelated edits: this PR leaves the surrounding behavior unchanged unless
  a path was actually erroring silently.

## Verification

Run the repo's test suite and paste the output. Then list, with evidence, the
failure modes you injected and what each produced (log line, retry behaviour,
user-visible result). Confirm no error path exists that catches and ignores.
