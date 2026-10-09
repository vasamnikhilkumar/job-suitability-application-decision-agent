# Full Belief Model

Version: `W2-BM-v1`, frozen before the Week 2 simulation. All probabilities are hypothetical modelling assumptions informed by the deliberately balanced C17–C50 case design; they are not empirical hiring frequencies.

## Mutually exclusive hidden states

| State | Meaning | Correct next action | Prior | Prior source |
|---|---|---|---:|---|
| H1 actionable match | Mandatory fit is supported and the vacancy is actionable | Apply | 0.25 | Hypothetical assumption, informed by 10/34 Apply cases in the designed C17–C50 set but deliberately rounded down |
| H2 resolvable factual uncertainty | A missing fact such as duration, authorization, location, or status can change the decision | Research | 0.25 | Hypothetical assumption, informed by 10/34 designed Research cases |
| H3 judgment-dependent fit | Transferability, equivalence, or preference needs human judgment | Request human help | 0.15 | Hypothetical assumption, informed by 6/34 designed human-help cases |
| H4 conclusive mismatch | A mandatory requirement and role-specific evidence conclusively fail | Skip | 0.20 | Hypothetical assumption, informed by the dominant failure type among 8/34 designed Skip cases |
| H5 unavailable or infeasible opportunity | The vacancy is closed/unreliable or a hard feasibility constraint fails | Skip | 0.10 | Hypothetical assumption separating opportunity status from candidate mismatch |
| H6 other | Residual unmodelled condition not represented above | Request human help | 0.05 | Explicit residual hypothetical assumption |

The states are mutually exclusive by construction and the priors sum to 1.00. The residual state prevents false completeness.

## Evidence source E1: candidate-fit audit

Outcomes are `strong`, `ambiguous`, and `contradictory`.

| State | strong | ambiguous | contradictory |
|---|---:|---:|---:|
| H1 | 0.80 | 0.15 | 0.05 |
| H2 | 0.25 | 0.65 | 0.10 |
| H3 | 0.35 | 0.55 | 0.10 |
| H4 | 0.05 | 0.15 | 0.80 |
| H5 | 0.45 | 0.35 | 0.20 |
| H6 | 0.25 | 0.50 | 0.25 |

Source: hypothetical expert judgement based on the Week 1 failure families. Each row sums to 1.00.

## Evidence source E2: exact-vacancy status audit

Outcomes are `active`, `unclear`, and `inactive`.

| State | active | unclear | inactive |
|---|---:|---:|---:|
| H1 | 0.85 | 0.12 | 0.03 |
| H2 | 0.65 | 0.30 | 0.05 |
| H3 | 0.70 | 0.25 | 0.05 |
| H4 | 0.65 | 0.25 | 0.10 |
| H5 | 0.05 | 0.20 | 0.75 |
| H6 | 0.30 | 0.45 | 0.25 |

Source: hypothetical expert judgement informed by Active-Signal Overreach in C02. Each row sums to 1.00.

## Evidence source E3: targeted clarification

Outcomes are `confirms`, `judgment`, `refutes`, and `unavailable`.

| State | confirms | judgment | refutes | unavailable |
|---|---:|---:|---:|---:|
| H1 | 0.75 | 0.10 | 0.05 | 0.10 |
| H2 | 0.30 | 0.15 | 0.35 | 0.20 |
| H3 | 0.10 | 0.65 | 0.10 | 0.15 |
| H4 | 0.05 | 0.05 | 0.80 | 0.10 |
| H5 | 0.05 | 0.05 | 0.65 | 0.25 |
| H6 | 0.15 | 0.30 | 0.20 | 0.35 |

Source: hypothetical expert judgement based on equivalent-experience, eligibility, and transferability failures. Each row sums to 1.00.

## Reproducible Bayesian update

For evidence `E1=ambiguous`, Bayes' rule is

`P(Hi | e) = P(e | Hi)P(Hi) / sum_j P(e | Hj)P(Hj)`.

The unnormalized weights are:

| State | Prior | Likelihood | Weight | Posterior |
|---|---:|---:|---:|---:|
| H1 | 0.25 | 0.15 | 0.0375 | 0.10067 |
| H2 | 0.25 | 0.65 | 0.1625 | 0.43624 |
| H3 | 0.15 | 0.55 | 0.0825 | 0.22148 |
| H4 | 0.20 | 0.15 | 0.0300 | 0.08054 |
| H5 | 0.10 | 0.35 | 0.0350 | 0.09396 |
| H6 | 0.05 | 0.50 | 0.0250 | 0.06711 |

The weights sum to 0.3725 and the rounded posteriors sum to 1.00000. The executable audit retains full precision.

## Entropy

Entropy is `H(p) = -sum_i p_i log2(p_i)` bits. Before evidence it is 2.42322 bits; after `E1=ambiguous` it is 2.21203 bits, a reduction of 0.21119 bits. The exact values and normalization checks are generated and verified in `results/belief-audit.json`. A particular surprising outcome can still increase entropy even when expected information gain is positive.
