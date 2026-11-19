# Reusable prompt: source verification

Copy-paste the block below into any AI coding agent to check a claim against
primary sources and report how much of it actually holds up.

Keywords: fact check, verify claim, primary source, evidence, confidence, citations

---

Verify the claim: [claim]. Trace it to primary sources and report what is
supported, what is not, and how confident you are.

## Steps

1. **Break down** - Split the claim into checkable parts: each factual
   assertion, number, date, and attribution.
2. **Find primaries** - For each part, locate the original source (the paper,
   dataset, official record, or code) rather than an article repeating it.
3. **Check** - Open each source and compare it to the claim. Note the exact
   passage, figure, or file:line that supports or contradicts each part.
4. **Rate** - Assign each part a verdict: supported, unsupported, contradicted,
   or unverifiable, with a confidence level and the evidence behind it.
5. **Report** - Summarize the overall verdict, then list each part with its
   verdict, evidence, and source link.

## Verification

- [ ] The claim was split into distinct, checkable parts.
- [ ] Each part is backed by a primary source you opened, not a summary.
- [ ] Contradictions are stated plainly, with the contradicting evidence.
- [ ] Unsupported parts are not quietly upgraded to supported.
- [ ] Every verdict carries a confidence level and a source.

## Rules

- Never treat a search snippet, abstract, or aggregate as a primary source.
- Never round an uncertain claim up to a confident one; say unverifiable.
- If a claim depends on data you cannot access, report that limit instead of
  inferring the answer.
