# Test Case Plan

## Case groups

| IDs | Source type | Label timing | Prediction status | Permitted use |
|---|---|---|---|---|
| C01 | Real-world development case | Label assigned after output | Completed | Policy debugging only |
| C02–C16 | Real-world Reddit résumé and live job post | Evaluator confirmed after Policy 1 output | Completed | Development replay only |
| C17–C50 | Project-authored fictional résumé and job post | Hidden label stored before any output | Not yet run | Controlled simulated evaluation |

## Simulated-case coverage

| IDs | Expected action | Main condition |
|---|---|---|
| C17–C26 | Apply | Mandatory evidence, relevant work evidence, recency, and reliability pass |
| C27–C36 | Research | A factual, decision-changing uncertainty remains |
| C37–C42 | Request human help | Available evidence leaves an equivalence or transferability judgment |
| C43–C50 | Skip | Mandatory requirements and relevant evidence conclusively fail |

## Frozen execution sequence

1. Keep `hidden-labels.md` outside the model context.
2. Run the Baseline, Policy 1, and Policy 2 on identical C17–C50 inputs.
3. Save every raw action before revealing labels.
4. Reveal labels and compute the required measurements.
5. Analyze at least five incorrect decisions without editing the inputs, policies, or labels.
6. Report real-world replay and simulated evaluation results separately.

## Claim boundary

The simulated evaluation can test rule consistency and known failure conditions. It cannot establish real-world hiring accuracy, probability calibration, fairness, interview likelihood, offer likelihood, or candidate-specific opportunity value.
