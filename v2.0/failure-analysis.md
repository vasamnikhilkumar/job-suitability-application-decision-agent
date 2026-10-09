# Failure Analysis and Redesign

## Original policy failure

P3 chose `request human help` for all 500 cases and acquired zero evidence. Its frozen loss matrix made human help cost at most 2, so no paid observation could reduce Bayes risk enough to be worthwhile. Classification: objective misspecification/deferral trap, not a coding error. The test led to P3b: human help receives a capacity cost, correct escalation is not free, and an entropy budget permits efficient evidence acquisition. P3b was introduced only after the original results were recorded.

## Five P3b failures

| Case | True → predicted | Evidence pattern | Classification | Design implication |
|---|---|---|---|---|
| W2C001 | Skip → Apply | strong, unclear, refutes | Misleading/noisy evidence | A high-stakes Skip guard should inspect clarification before Apply when status is unclear |
| W2C002 | Skip → Research | contradictory, unclear, judgment | State overlap | H4 and H3 likelihoods need better separating evidence |
| W2C004 | Research → Apply | strong, unclear, confirms | Premature stop | Treat unresolved vacancy status as a blocking factual condition |
| W2C006 | Skip → Research | contradictory, inactive, refutes | Loss-driven conservative error | Add a deterministic conjunction for mutually reinforcing negative signals, then validate separately |
| W2C007 | Human → Apply | strong, active, judgment | Deferral underuse | Restore human review when targeted clarification explicitly returns `judgment` |

The first redesign was rerun and is reported as P3b. The five later cases are diagnostic proposals, not silently incorporated improvements; implementing them now would reuse the test set as training data.

## Concepts learned from failure

1. **Deferral trap:** an apparently safe reject/escalate option can dominate every decision when reviewer cost or capacity is omitted.
2. **Evidence-budget brittleness:** entropy reduction can force useful checks, but an arbitrary entropy threshold can optimize uncertainty rather than downstream loss.

These concepts motivate a future held-out evaluation with reviewer-capacity constraints and a decision-relevant information objective.
