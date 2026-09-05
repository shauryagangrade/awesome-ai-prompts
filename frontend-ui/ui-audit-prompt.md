# Reusable prompt: UI audit [spec]

Copy-paste the block below into any AI coding agent to audit a UI at spec
level - with defined scope, hard constraints, and evidence-backed findings
that cite exact file:line and proposed fixes. Every finding must be
verifiable against the codebase.

---

Audit the UI of `[page / component / feature]` in this repository against the
project's own design system and conventions. Produce a prioritized list of
findings, each with a concrete fix that can be checked against the repo's
styles, tokens, and components.

## Define the scope first

Before auditing, state clearly:

1. **What is in scope** - the specific pages, components, or routes to cover.
2. **What is out of scope** - anything explicitly excluded.
3. **The design system in use** - Confirm which tokens, theme config, component
   library, or style guide the codebase follows. If none exists, say so and
   recommend one - do not invent one.
4. **The rendering context** - Browser targets, supported themes (light/dark),
   and any device-specific requirements the project cares about.

Do not begin the audit until the scope and design system are defined and
confirmed.

## Audit dimensions

For every in-scope element, check these dimensions in order. Stop on a broken
layout before moving to spacing nuance.

1. **Design system adherence** - Compare each component's styles (colors,
   font sizes, spacing, border radii, shadows) against the project's token
   system or established conventions. Flag every hardcoded value that bypasses
   the shared constants. Identify places where the codebase has invented its
   own values.

2. **Visual consistency** - Compare similar components and states side by side:
   primary/secondary buttons, form inputs, cards, badges, alerts, nav items.
   Check that hover, focus, active, disabled, loading, and error states are
   defined and look uniform across the UI. Find orphaned style variations that
   appear in only one component.

3. **Spacing and vertical rhythm** - Audit padding, margin, and gap values.
   Flag inconsistent spacing scales with no reason (e.g. 8px in one place,
   12px in another). Check vertical rhythm in text-heavy layouts. Verify
   alignment across grid, flex, and stacked layouts.

4. **Typography** - Verify heading hierarchy is logical with no skipped levels.
   Check that line-height, letter-spacing, and font-weight usage match the
   project's type scale. Flag text that overflows its container or truncates
   without an ellipsis or tooltip.

5. **Responsive behavior** - Trace layout behavior at 320px, 768px, 1024px,
   and 1440px by reading media queries and responsive styles (or screenshot if
   the agent can render). Flag overflowing containers, unreadable text, touch
   targets smaller than 44x44px, and breakpoints that appear to have been
   chosen without a strategy.

6. **Interaction states and feedback** - Confirm loading, empty, error, and
   success states exist and are styled consistently. Check that interactive
   elements give visible feedback on hover, focus, and press. Flag silent
   failures where the user gets no indication something happened.

7. **Icons, images, and media** - Confirm icons come from a single library or
   use a consistent stroke/fill style. Verify image sizes, aspect ratios, and
   placeholder/skeleton states are handled. Flag mixed icon sets or
   inconsistent image treatment.

8. **Theming** - If the project supports multiple themes, render or trace each
   component through every supported theme. Flag hardcoded colors that break in
   dark mode or components that ignore the theme variables.

## Method

1. **Read the style architecture first** - Find design token definitions, theme
   config, global styles, and any component library before auditing. Understand
   the system you are auditing against.

2. **Walk the component tree** - Read each in-scope component's styles (CSS
   modules, styled-components, Tailwind classes, or inline). Compare every
   value against the token system. Note each deviation with the specific
   file:line and value.

3. **Capture or trace at breakpoints** - If the agent can render or preview,
   capture the UI at 320px, 768px, 1024px, and 1440px. Otherwise, read the
   responsive styles and media queries to trace layout behavior at each
   breakpoint.

4. **Group findings by dimension** - Organize every finding under its audit
   dimension (spacing, typography, color, responsiveness, etc.), not as a
   flat list.

5. **Show the fix, not just the problem** - For each finding, cite file:line,
   state the current value, the correct value, and the exact code change
   needed. If a token should be used, name the token.

## Verification

Before reporting the audit complete, confirm each of these:

- [ ] Every finding cites a specific file:line, not a vague location.
- [ ] No finding invents a design token or convention that does not exist in
      the codebase.
- [ ] If a design system is in use, each finding is checked against it.
- [ ] Findings are prioritized: broken layouts and unreadable text first,
      minor spacing inconsistencies last.
- [ ] Intentional design choices (e.g. a hero heading that deliberately breaks
      the type scale) are not flagged unless they conflict with documented
      guidelines.
- [ ] If the UI is already consistent within scope, that is stated explicitly
      with what was verified, not padded with invented issues.

## Rules

- State the scope and design system before auditing. Do not audit a moving
  target.
- Never report "could be more consistent" without specifying what is
  inconsistent, where it is, and what the correct value should be.
- Never invent design tokens or conventions the codebase does not have. If
  there is no token system, say so and recommend one.
- Do not flag intentional, documented design choices as errors.
- Prioritize by user impact. A broken layout at mobile width is a higher
  priority than a 2px spacing inconsistency.
- If the UI is already consistent within scope, say so and list what was
  verified - do not invent issues to fill the report.
