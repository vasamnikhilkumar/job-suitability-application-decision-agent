# Evaluation Deliverable Status

## Completed for the current pilot batch

- Permitted résumé and job-post records are saved case by case.
- Correct labels are hidden while each new decision is produced, and label timing is documented.
- Baseline, Policy 1, and Policy 2 rules are frozen.
- Every method's replay action is saved.
- The comparison includes multiclass confusion matrices.
- Per-action precision and recall are reported where defined.
- Incorrect Apply and incorrect Skip quantities are reported.
- Research and human-help rates are reported.
- Provisional total and mean decision costs are reported.
- Six incorrect decisions are examined.
- Every examined failure has a reusable name.
- The highest-cost error is identified and justified.
- A README gives complete instructions for repeating and extending the test.
- Limitations and prohibited predictive claims are stated explicitly.
- The required full case inventory is prepared: C01–C16 are real-world development cases and C17–C50 are project-authored simulated cases.
- C17–C50 have evaluator labels stored separately before agent execution.
- The simulated labels exercise all four actions and multiple failure families.

## Pending before final submission

- Run every frozen method on C17–C50 while hiding the evaluator labels.
- Save all new predictions and explanations without editing them.
- Recalculate every measurement using the full case inventory while reporting real-world replay and simulated results separately.
- Repeat the failure analysis using errors from the pre-labeled simulated evaluation.
- Evaluate calibration only if numerical beliefs are recorded before labels are revealed.

## Current gate

Case preparation is complete. The final evaluation gate remains open until the pre-labeled simulated cases are run and scored.
