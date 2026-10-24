# Reusable prompt: incident postmortem

Copy-paste the block below into any AI coding agent to write a blameless,
evidence-based postmortem after an incident is resolved. Every timeline entry
points at a log, alert, or message, and every action item has an owner and a
way to check it is done.

Keywords: postmortem, blameless, incident review, root cause, timeline, action items, outage retrospective

---

Write the postmortem for a resolved incident. The goal: a document the team can
learn from, built only on evidence, that names causes in the system and not
people, and ends in actions that can be verified.

## Steps

1. **Gather the evidence first** - Collect what exists: alert history,
   dashboards, logs, deploy and config change history, the incident channel or
   chat export, and the tickets. List each source with a link or path. If a
   source is missing, say so. Do not write the narrative until the evidence is
   in front of you.
2. **Write the summary** - In a few sentences: what broke, who or what was
   affected, the start and end times, the duration, and the size of the impact
   (error rate, failed requests, users affected, money). Use numbers from the
   evidence, not estimates, and label anything that is an estimate.
3. **Reconstruct the timeline** - List events in time order, in one time zone,
   with a timestamp and a source for each one: when the change or trigger
   happened, when it was detected, when someone responded, each mitigation
   attempt and its result, and when service recovered. Mark each entry as
   **confirmed** (a log or alert shows it) or **reported** (a person said so).
   Show the gaps, for example the time between the trigger and the first alert.
4. **Find the contributing factors** - Ask why repeatedly, down to the system
   and process level: what allowed the change to ship, why detection took as
   long as it did, why the first mitigation did not work. Separate the
   **trigger** from the **underlying conditions**. Describe what the system and
   the process made easy, not what a person should have done.
5. **Record what went well and what did not** - Name the things that worked
   (fast detection, a good runbook, a safe rollback) so they are kept, and the
   gaps in tooling, alerts, documentation, or access.
6. **Write the action items** - Each item is a concrete change with one owner,
   a due date, a priority, and a **verification** (how anyone can check it is
   done, such as "alert fires in a test", not "improve monitoring"). Prefer
   fixes that prevent, detect sooner, or reduce impact, over reminders to be
   careful.
7. **Add the lessons** - A few points the wider team can reuse. Then have the
   people involved review the draft for factual errors before it is shared.

## Verification

- [ ] Every timeline entry has a timestamp, a source, and a confirmed or
      reported label.
- [ ] The summary numbers match the evidence, and estimates are labeled.
- [ ] The trigger and the underlying conditions are written separately.
- [ ] No sentence blames a named person; each describes the system or process.
- [ ] Every action item has one owner, a due date, and a verification step.
- [ ] Missing evidence and open questions are listed, not filled in with
      guesses.

## Rules

- Never name an individual as the cause; write what the system allowed.
- Never add a timeline event you cannot back with a source; mark it as
  unknown.
- Never write "human error" as a root cause; ask why the system made the error
  possible.
- Never write an action item without an owner and a way to verify it.
- If the evidence conflicts, show both versions instead of choosing one
  silently.
