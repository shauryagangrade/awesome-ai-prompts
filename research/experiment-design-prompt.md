# Reusable prompt: experiment design

Copy-paste the block below into any AI coding agent to turn a question into a
reproducible experiment with an honest measurement and reporting plan.

Keywords: experiment, hypothesis, benchmark, measure, controlled, reproducible

---

Design an experiment to answer [question]. Produce a plan someone else can run
and that will report the result honestly, whatever it turns out to be.

## Steps

1. **Question** - Write the question as a testable hypothesis, with the
   predicted outcome and what a result would mean.
2. **Variables** - Name the independent variable you change, the dependent
   variable you measure, and everything you hold constant.
3. **Method** - Specify the setup, the number of trials, the control, and the
   exact steps or commands. Choose a sample size that could actually detect
   the effect you care about.
4. **Analysis** - State in advance how you will compare results, including
   how you will handle noise, outliers, and failed runs.
5. **Reporting** - Define what you will publish: raw data, the summary table,
   and a conclusion limited to what the data supports.

## Verification

- [ ] The hypothesis is testable and falsifiable.
- [ ] Variables and controls are named, with constants listed.
- [ ] The method is reproducible from the commands and settings given.
- [ ] The analysis plan is written before the result is known.
- [ ] The reporting plan includes raw data and a bounded conclusion.

## Rules

- Never design an experiment that can only confirm the desired answer.
- Never change the success threshold after seeing the results.
- If the effect is too small to measure with the available setup, say so
  instead of designing a test that cannot answer the question.
