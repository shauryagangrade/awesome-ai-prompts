# Reusable prompt: regular expressions that don't bite

Copy-paste the block below into any AI coding agent to write or repair a
regular expression the way a senior engineer would: a defined purpose, a corpus
of cases that proves the behavior, and a check that the pattern cannot blow up
on adversarial input.

---

Help me write `[what the regex must match]` in `[language or stack]`. Treat a
regex as risky code, not a magic one-liner: it needs a stated purpose, tests
against real inputs, and evidence that it cannot hang on bad input. Write it
only after we agree on the behavior it must have.

## Steps

1. **State the purpose in plain words** - One sentence: what strings must
   match, what must not, and where the pattern runs (validation, extraction,
   a hot path, user-supplied input or not). If the plain statement is hard to
   write, the regex is the wrong tool; say so and propose ordinary string
   handling instead.
2. **Choose the simplest expression** - Prefer the smallest pattern that meets
   the purpose. A string method, an index operation, or a tiny state machine
   often beats a regex entirely. If the language offers a parser for the
   format being matched (JSON, URL, email, numbers), use it instead of a regex.
3. **Write it with anchors and boundaries** - Anchor start and end or use word
   boundaries where the behavior demands it. Match what the caller needs, not
   a fuzzy subproblem, and avoid dot-all or unconstrained groups unless the
   purpose requires them.
4. **Build a corpus and test** - List the inputs that must match, must not
   match, edge cases (empty, whitespace, unicode, mixed case, very long
   strings, lookalike characters, embedded newlines), and run the pattern over
   all of them in a throwaway test. Paste the results; do not assert them.
5. **Hunt for catastrophic backtracking** - Inspect for nested quantifiers and
   alternatives that re-scan the same text (`(a+)+`, `(a|a)*`), especially on
   untrusted input. Check that the pattern either cannot backtrack
   quadratically or that input length is bounded first. If in doubt, time the
   worst-case input you found in step 4 and show it returns quickly.
6. **Make it maintainable** - Add a short comment in a place the team will see
   it: the purpose in plain words, the matching corpus, and why this
   construction. Keep flags and escaping explicit so the next reader can
   predict the behavior.
7. **Land it as a test, not a script** - The adopted pattern ships with its
   corpus as a repeatable test (unit test or checked-in script) that fails if
   the regex behavior changes. A regex without its test cases is a bug waiting
   for an anecdote.

## Rules

- Never write a regex without running it against the agreed corpus and showing
  the output.
- Never accept a pattern with nested loops over the same input on
  user-controlled data without bounding it first.
- Prefer parser, string, or index operations over a regex when the format is
  structured. Regexes are for matching text with a shape; parsers are for
  formats with grammar.
- No pattern change in production code without the corpus test landing in the
  same change.

## Verification

Paste the test run over the corpus (passes and intended non-matches), the
worst-case timing for any adversarial input you constructed, and the final
pattern. Confirm the behavior is pinned by a repeatable test in the repo.
