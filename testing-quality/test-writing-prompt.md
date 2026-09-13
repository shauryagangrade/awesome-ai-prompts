# Reusable prompt: comprehensive test writing

Copy-paste the block below into any AI coding agent to write tests that
actually protect the code - meaningful assertions, real edge cases, and the
repo's own testing conventions.

---

Write tests for `[function/module/feature]` in this repository. The goal is
tests that catch regressions and document behavior - not tests that pad the
coverage number.

## What good looks like

1. **Read the code first** - Understand the inputs, outputs, side effects,
   error paths, and the contract callers rely on before writing anything.
2. **Test behavior, not implementation** - Assert what the code does
   (return values, state changes, errors raised, side effects), not how it
   does it. Don't restate the code path in test assertions.
3. **Cover the meaningful cases** - The happy path, key edge cases (empty
   input, boundary values, missing data, invalid input), and error handling.
   Prioritize the cases most likely to break in the future.
4. **Match the repo's style** - Use the existing test framework, naming
   conventions, fixture/double patterns, and directory layout. Look at
   neighboring tests and imitate them.
5. **Isolate tests** - Each test should be independent and fast. Clean up any
   state it creates. Don't depend on test order or shared mutable state.
6. **Verify** - Run the suite. Every new test should pass, and (where
   practical) confirm each one actually fails if the behavior is removed -
   a test that always passes is noise.

## Rules

- Never write tests that only cover code added "for coverage". Test the
  contract, not the lines.
- Never weaken assertions (broaden matchers, catch-and-ignore) to make a test
  pass.
- If the code is untestable as written, say so and suggest a small refactor -
  don't contort the test to work around it.
- Run the repo's full suite and checks to confirm nothing else broke.
