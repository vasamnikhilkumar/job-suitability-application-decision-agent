# Review Record

## Review scope

This review checks internal consistency, evidence boundaries, reproducibility, safety, and assignment coverage. It is not an external peer review or legal opinion.

Review date: 2026-09-01  


## Artifact review

| Artifact | Review result | Finding |
|---|---|---|
| README | Pass with limitation | Repetition steps, measurements, costs, append procedure, and limitations are documented. Final evaluation still requires independently pre-labeled additions. |
| Research file | Pass | Uses authoritative sources and clearly separates supported findings from unvalidated assumptions. |
| Discussion record | Pass | External anecdotes are attributable, their influence is traceable, and rejected/deferred suggestions are recorded. |
| Agent prompt | Pass for prototype | Returns one action, cites evidence, forbids fabrication, and distinguishes Research from human judgment. |
| Implementation notes | Pass for minimum version | Defines input, hidden state, belief, actions, costs, policy, feedback boundary, human function, and stop condition. |
| Probability decision record | Pass as decision analysis | Priors and posteriors sum to 100%; likelihood assumptions, costs, thresholds, audit data, and calibration limits are explicit. |
| Case records | Pass for development use | Evidence and predictions are retained with permission, but original labels were not independently committed before Policy 1 outputs. |
| Frozen policy comparison | Pass | Baseline and two policies are distinct and versioned. |
| Comparison results | Arithmetic pass; validity limitation | Confusion matrices and rates are internally consistent. Results are replay/development evidence, not blinded validation. |
| Failure analysis | Pass | More than five incorrect decisions are named and the highest-cost error is justified. |
| Paper | Pending | LaTeX and PDF are explicit placeholders; no finished paper claim is made. |
| Social posts | Pending | Files are placeholders until claims are approved. |

## Mathematical checks

- Posterior unsafe event: 70.44%.
- Posterior favorable-or-judgment event: 29.56%.
- Apply expected loss: 3.522 hypothetical units.
- Skip expected loss: 29.56 hypothetical units.
- Research action cost: 3 hypothetical units.
- Resulting action: Research.

## Policy-consistency checks

- Hard-stop rule precedes ordinary uncertainty handling.
- Missing evidence is not automatically confirmed evidence.
- Research is limited to questions whose answers can change the action.
- Human help is reserved for unresolved equivalence, transferability, or preference judgments.
- Apply requires evidence and feasibility rather than résumé keywords alone.
- Skip is allowed for conclusive hard failure or combined mandatory/evidence failure.
- The agent remains advisory and cannot submit an application.

## Safety and integrity checks

- Résumé fabrication is prohibited.
- No ATS score is produced.
- No private excluded example is included in repository artifacts.
- Direct identifiers in supplied résumé images are redacted or obscured where provided.
- Permissions are recorded for the current case material.
- Probability values and costs are labeled hypothetical.
- Legal sources are treated as scope warnings, not legal advice.
- Age-based scoring is rejected.

## Material limitations

1. Evaluator labels were confirmed after Policy 1 predictions rather than independently stored beforehand.
2. The current action distribution does not include expected Apply cases.
3. Research recommendations dominate the current development records.
4. Live job pages can change after access.
5. The posting-age rule lacks empirical validation.
6. Outcome labels such as assessment, interview, offer, and candidate-rated value are unavailable.
7. Calibration cannot be claimed from elicited probabilities.
8. Fairness cannot be established without appropriately consented and sufficiently sampled subgroup evaluation.

## Corrections already made

- Separated posting recency from reliability.
- Added hard-stop precedence so pointless Research does not override conclusive failure.
- Preserved post-prediction label timing instead of calling the replay fully blinded.
- Added a Baseline and a second policy.
- Added confusion matrices, per-action precision/recall, error quantities, review rates, and decision costs.
- Replaced an unsupported generic probability example with a transparent case-specific update and sensitivity analysis.
- Reorganized artifacts to the required repository structure.


## Requirements for the next review

- Add cases with evaluator labels committed before any policy output.
- Include every action, especially Apply.
- Re-run all frozen methods without changing their rules.
- Recalculate results and repeat failure analysis.
- Add outcome follow-up only with consent, privacy controls, and clear outcome definitions.
- Approve paper claims only after the expanded evaluation is complete.

