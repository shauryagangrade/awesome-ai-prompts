# Reusable prompt: issue triage for maintainers

Copy-paste the block below into any AI coding agent to turn a backlog of
untriaged issues into labeled, prioritized, answerable queues.

---

Triage the open issues in this repository. The goal is a backlog a
maintainer can act on in priority order, not a pile of "looked at it" noise.

## Steps

1. **Check reproducibility first** - For bug reports, confirm the report
   includes clear repro steps, expected vs actual behavior, and environment
   details. If any are missing, reply asking for the specific missing piece
   (name it, don't say "please provide more info") and label
   `needs-repro`/`needs-info` rather than guessing at the cause.
2. **Detect and link duplicates** - Search open and closed issues for the
   same root cause before triaging as new. Link duplicates to the canonical
   issue, summarize why they match, and close the duplicate with a pointer
   rather than leaving both open in parallel.
3. **Apply a severity/priority rubric consistently** - Use the repo's actual
   label set. If none exists, propose one (e.g. `severity: blocker/high/
   medium/low`) rather than inventing ad hoc labels per issue. Justify the
   assigned severity in one line so the next person doesn't have to re-derive
   it.
4. **Flag good-first-issue candidates with mentoring notes** - When an issue
   is small, well-scoped, and doesn't require deep repo context, label it
   `good first issue` and add a short comment pointing to the relevant
   file(s) or pattern to start from - this is what makes the label honest
   instead of aspirational.
5. **Apply stale-issue policy, don't just silently close** - If the repo has
   a stale-bot policy, follow it. If not, propose one (e.g. ping after 60
   days of no repro/no response, close after 14 more days) and apply it
   consistently, always with a comment explaining why and how to reopen.
6. **Summarize the triage pass** - Report counts by label/severity, the
   duplicates merged, and any issues that need a maintainer decision you
   can't make (design questions, breaking changes, roadmap calls).

## Rules

- Never close an issue as invalid or duplicate without linking the reasoning
  or the canonical issue - a silent close reads as dismissive and loses
  context for whoever revisits it.
- Don't invent a label taxonomy that ignores one the repo already has;
  extend it, don't fragment it.
- Ask, don't assume, when severity or priority genuinely depends on product
  judgment rather than technical facts.
