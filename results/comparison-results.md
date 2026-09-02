# Provisional Policy Comparison — 16-Case Replay

Status: completed replay on the current development batch

These results compare frozen rules against evaluator-confirmed labels. They are not a blinded test: labels for C02–C16 were confirmed after the Policy 1 predictions were visible, and C01 is explicitly a development case. The dataset also contains no expected Apply cases.

## Saved actions

| Case | Evaluator-confirmed action | Baseline | Policy 1 | Policy 2 |
|---|---|---|---|---|
| C01 | Research | Skip | Research | Research |
| C02 | Research | Apply | Research | Apply |
| C03 | Research | Skip | Research | Research |
| C04 | Skip | Skip | Skip | Skip |
| C05 | Research | Skip | Research | Research |
| C06 | Research | Skip | Research | Research |
| C07 | Request human help | Skip | Request human help | Request human help |
| C08 | Skip | Skip | Skip | Skip |
| C09 | Research | Skip | Research | Research |
| C10 | Skip | Skip | Skip | Skip |
| C11 | Skip | Skip | Skip | Skip |
| C12 | Research | Skip | Research | Research |
| C13 | Research | Skip | Research | Research |
| C14 | Research | Skip | Research | Research |
| C15 | Research | Skip | Research | Research |
| C16 | Research | Skip | Research | Research |

Policy 2 changes only C02: it treats multiple current active-hiring signals as sufficient despite the listing being older than seven days.

## Action distribution

| Method | Apply | Research | Request human help | Skip |
|---|---:|---:|---:|---:|
| Evaluator labels | 0 | 11 | 1 | 4 |
| Baseline | 1 | 0 | 0 | 15 |
| Policy 1 | 0 | 11 | 1 | 4 |
| Policy 2 | 1 | 10 | 1 | 4 |

## Agreement and review behavior

| Method | Agreement quantity | Agreement rate | Research rate | Human-help rate |
|---|---:|---:|---:|---:|
| Baseline | 4/16 | 25.00% | 0.00% | 0.00% |
| Policy 1 | 16/16 | 100.00% | 68.75% | 6.25% |
| Policy 2 | 15/16 | 93.75% | 62.50% | 6.25% |

Agreement is reported for completeness, not as a predictive accuracy claim. Policy 1's labels were confirmed after its outputs were visible, so its 100% agreement is likely optimistic and must not be presented as independent validation.

## Multiclass confusion matrices

Rows are evaluator labels; columns are predicted actions in the order Apply, Research, Human help, Skip.

### Baseline

| Actual \\ Predicted | Apply | Research | Human help | Skip |
|---|---:|---:|---:|---:|
| Apply | 0 | 0 | 0 | 0 |
| Research | 1 | 0 | 0 | 10 |
| Human help | 0 | 0 | 0 | 1 |
| Skip | 0 | 0 | 0 | 4 |

### Policy 1

| Actual \\ Predicted | Apply | Research | Human help | Skip |
|---|---:|---:|---:|---:|
| Apply | 0 | 0 | 0 | 0 |
| Research | 0 | 11 | 0 | 0 |
| Human help | 0 | 0 | 1 | 0 |
| Skip | 0 | 0 | 0 | 4 |

### Policy 2

| Actual \\ Predicted | Apply | Research | Human help | Skip |
|---|---:|---:|---:|---:|
| Apply | 0 | 0 | 0 | 0 |
| Research | 1 | 10 | 0 | 0 |
| Human help | 0 | 0 | 1 | 0 |
| Skip | 0 | 0 | 0 | 4 |

## Per-action precision and recall

“N/A” means the dataset contains no evaluator-labeled example for that action or the method never predicted it.

| Method/action | Precision | Recall |
|---|---:|---:|
| Baseline — Apply | 0.00% | N/A |
| Baseline — Research | N/A | 0.00% |
| Baseline — Human help | N/A | 0.00% |
| Baseline — Skip | 26.67% | 100.00% |
| Policy 1 — Apply | N/A | N/A |
| Policy 1 — Research | 100.00% | 100.00% |
| Policy 1 — Human help | 100.00% | 100.00% |
| Policy 1 — Skip | 100.00% | 100.00% |
| Policy 2 — Apply | 0.00% | N/A |
| Policy 2 — Research | 100.00% | 90.91% |
| Policy 2 — Human help | 100.00% | 100.00% |
| Policy 2 — Skip | 100.00% | 100.00% |

## Error quantities

| Method | Incorrect Apply actions | Incorrect Skip actions | Other incorrect actions |
|---|---:|---:|---:|
| Baseline | 1 | 11 | 0 |
| Policy 1 | 0 | 0 | 0 |
| Policy 2 | 1 | 0 | 0 |

There are no evaluator-labeled Apply cases, so false-negative quantity for Apply cannot be meaningfully evaluated in this batch.

## Provisional decision cost

The previously chosen hypothetical opportunity-impact costs are used only for comparison:

- correct Apply or Skip: 0;
- Research action: 3;
- Request human help action: 2;
- incorrect Apply: 5;
- incorrect Skip: 100.

| Method | Cost calculation | Total | Mean per case |
|---|---|---:|---:|
| Baseline | 11 incorrect Skips × 100 + 1 incorrect Apply × 5 | 1105 | 69.06 |
| Policy 1 | 11 Research × 3 + 1 Human help × 2 | 35 | 2.19 |
| Policy 2 | 10 Research × 3 + 1 Human help × 2 + 1 incorrect Apply × 5 | 37 | 2.31 |

These costs are hypothetical and unvalidated. Changing the cost assumptions can change the preferred policy.

## Current finding

Policy 1 has the lowest provisional cost in this replay. Policy 2 reduces one Research action but converts C02 into an incorrect Apply relative to the evaluator-confirmed label. The result suggests that active-hiring signals should not automatically override unresolved posting-age concerns. This is a design hypothesis, not a validated conclusion.

## Required next evaluation work

1. Analyze at least five incorrect decisions, using the Baseline errors and Policy 2's C02 error.
2. Add independently pre-labeled cases later, especially expected Apply cases.
3. Re-run all frozen methods without changing rules.
4. Evaluate calibration only after the agent records numerical beliefs before labels are revealed.

