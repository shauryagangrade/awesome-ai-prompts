# Reusable prompt: UI audit

Copy-paste the block below into any AI coding agent to perform a thorough UI
audit - visual consistency, design system adherence, spacing, typography, and
actionable fixes with file:line references.

---

Audit the UI of `[page / component / feature]` in this repository. The goal:
find every visual inconsistency, broken pattern, and UX rough edge, then
provide concrete fixes. Read the actual code and styles - never guess from
assumptions.

## Scope to cover

1. **Design system adherence** - Check every component against the project's
   design tokens, theme, or style guide. Flag hardcoded colors, font sizes,
   spacing values, or border radii that bypass the token system. Identify where
   the codebase invents its own values instead of using shared constants.
2. **Visual consistency** - Compare similar components and states side by side.
   Are buttons, inputs, cards, and badges styled consistently? Are hover,
   focus, active, and disabled states defined and uniform across components?
   Check for orphaned style variations that only appear in one place.
3. **Spacing and alignment** - Audit padding, margin, and gap values for
   consistency. Flag inconsistent spacing scales (e.g. 8px in one place, 12px
   in another with no reason). Check vertical rhythm in text-heavy layouts.
   Verify alignment across grids, flex rows, and stacked elements.
4. **Typography** - Verify heading hierarchy is logical and consistent (no
   skipped levels). Check line-height, letter-spacing, and font-weight usage
   match the type scale. Flag text that overflows containers or truncates
   without an ellipsis or tooltip.
5. **Responsive behavior** - Inspect layouts at common breakpoints (320px,
   768px, 1024px, 1440px). Flag elements that overflow their containers, text
   that becomes unreadable, touch targets smaller than 44x44px, or layouts
   that break without a clear responsive strategy.
6. **Interaction states and feedback** - Verify loading, empty, error, and
   success states exist and are styled consistently. Check that interactive
   elements give visual feedback on hover, focus, and press. Flag silent
   failures where the user gets no indication something happened.
7. **Icon and image consistency** - Check that icons use a single library or
   consistent stroke/fill style. Verify image sizes, aspect ratios, and
   placeholder/skeleton states are handled. Flag mixed icon sets or
   inconsistent image treatment.
8. **Dark mode / theming** - If the project supports multiple themes, verify
   all components render correctly in each. Flag hardcoded colors that break
   in dark mode or missing theme variable usage.

## Method

1. **Read the style architecture** - Find the design token definitions, theme
   config, global styles, and any component library in use. Understand the
   system before auditing against it.
2. **Walk the component tree** - Read each component's styles (CSS modules,
   styled-components, Tailwind classes, or inline). Compare values against the
   token system. Note every deviation.
3. **Screenshot at breakpoints** - If the agent can render or preview, capture
   the UI at 320px, 768px, 1024px, and 1440px. If not, read the responsive
   styles and CSS media queries to trace layout behavior at each breakpoint.
4. **Cite specific instances** - For each finding, reference the exact
   file:line and the specific value that is wrong. Group findings by category
   (spacing, typography, color, etc.).
5. **Propose concrete fixes** - Show the exact code change needed: the token
   to use, the spacing value to adopt, the component to align with. Do not
   just say "make it consistent" - show how.

## Rules

- Never report "could be more consistent" without specifying what is
  inconsistent, where it is, and what the correct value should be.
- Never invent design tokens or style conventions that do not exist in the
  codebase. If there is no token system, say so and recommend one.
- If the UI is already consistent, say so and list what was verified rather
  than inventing issues.
- Do not flag intentional design choices (e.g. a larger hero heading that
  deliberately breaks the type scale) unless they conflict with documented
  guidelines.
- Prioritize findings by user impact: broken layouts and unreadable text
  first, minor spacing inconsistencies last.
