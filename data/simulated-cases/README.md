# Simulated Case Set

C17–C50 are fictional cases authored for this project. They are not scraped candidates, real vacancies, or claims about actual employers. C01–C16 remain the separate real-world development records sourced from Reddit.

## Files

- `case-inputs.md` contains only agent-visible résumé and job-post evidence.
- `hidden-labels.md` contains evaluator-only expected actions and must be hidden during a run.

## Test procedure

1. Give the agent one case from `case-inputs.md` without opening `hidden-labels.md` in its context.
2. Save the action and explanation before revealing the label.
3. Reveal the corresponding evaluator label.
4. Record the prediction, correctness, decision cost, and failure condition.
5. Do not alter a case or label after seeing a result; create a new version instead.

## Common assumptions

- Evaluation date: 2026-09-01.
- “Recent” means posted within the previous seven days under the provisional policy.
- All fictional candidates confirm that their résumé statements are truthful.
- No fact omitted from a case may be assumed.
- Fictional company names are used to avoid presenting simulated vacancies as real.
