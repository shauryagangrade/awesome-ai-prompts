---
prompt: Reusable PR Review
repo: TourneyRadar API
link: https://github.com/AnayDhawan/tourneyradar-api
commit: d00dc36
---

# TourneyRadar API: IPv6 rate limiting bypass

**Task:** Review a security fix for a rate limiter that could be bypassed via IPv6 address rotation.

**Agent:** Claude (Code)

**Stack:** Express, TypeScript, Upstash Redis

**Before:** The rate limiter keyed on the full IPv6 address. Since IPv6 clients can pick any of 2^64 addresses per request from a /64 delegated prefix, every request hit a separate limit bucket. The limiter was unenforceable.

**What the prompt made the agent do:**
1. Identified the security failure: IPv6 clients can circumvent limits by rotating addresses.
2. Verified the fix: /64 masking identifies the subscriber line, not individual requests.
3. Tested edge cases: IPv4-mapped IPv6, compressed notation, malformed headers.
4. Checked test coverage: grew from 54 to 67 cases with 13 new IPv6-specific scenarios.
5. Caught a second DoS vector: malformed inputs now key on themselves, not a shared fallback.

**After:**
- IPv6 addresses masked to /64 prefix.
- IPv4 untouched.
- All edge cases covered by tests.
- Malformed headers cannot merge unrelated clients into the same limit.

**Would you use it again?** Yes. The prompt's systematic adversarial thinking exposed not just the bypass, but a second vulnerability in error handling that testing alone would have missed.
