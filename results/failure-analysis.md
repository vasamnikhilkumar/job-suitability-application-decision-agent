# Failure Analysis — Current 16-Case Replay

Status: six incorrect decisions examined

This analysis uses errors from the intentionally simple Baseline and Policy 2. Policy 1 has no recorded disagreement in this development batch, but its labels were confirmed after its predictions were visible, so that result is not independent validation.

## Failure 1 — Missing-Evidence Collapse

- Case: C01
- Method and incorrect action: Baseline → Skip
- Evaluator-confirmed action: Research
- What happened: React and React Query duration was not clearly evidenced. The Baseline converted “not shown” directly into failure instead of asking whether truthful omitted experience existed.
- Why incorrect: The missing fact could change the action. A Skip prematurely closes a potentially suitable opportunity.
- Corrective rule: When a mandatory qualification is absent from the document but could truthfully exist outside it, mark it Unclear and ask a targeted question.

## Failure 2 — Equivalent-Experience Blindness

- Case: C03
- Method and incorrect action: Baseline → Skip
- Evaluator-confirmed action: Research
- What happened: Strong backend and distributed-systems projects were present, but the listing's experience-duration language was not clearly satisfied. The Baseline could not ask whether the employer accepts substantial projects as equivalent experience.
- Why incorrect: The case involves an employer interpretation that may be resolved through factual research.
- Corrective rule: Separate demonstrated capability from the employer's definition of qualifying experience.

## Failure 3 — Eligibility-Uncertainty Collapse

- Case: C06
- Method and incorrect action: Baseline → Skip
- Evaluator-confirmed action: Research
- What happened: Technical qualifications were strong, but mandatory U.S. citizenship/permanent-residency and location evidence was hidden or redacted. The Baseline treated missing eligibility evidence as ineligibility.
- Why incorrect: Work authorization is a factual question and cannot be inferred from a résumé omission.
- Corrective rule: Ask directly about legal and location feasibility when it is mandatory and not visible.

## Failure 4 — Transferability Suppression

- Case: C07
- Method and incorrect action: Baseline → Skip
- Evaluator-confirmed action: Request human help
- What happened: The candidate had substantial adjacent DevOps experience but lacked several product-specific technologies. The Baseline treated the stack gap as definitive.
- Why incorrect: Whether deep Azure/Kubernetes experience transfers to MongoDB, Kafka, and ClickHouse responsibilities is a judgment call rather than a simple keyword failure.
- Corrective rule: Escalate close transferability and accepted-equivalence judgments to a trusted human instead of forcing a binary decision.

## Failure 5 — Location-Feasibility Assumption

- Case: C09
- Method and incorrect action: Baseline → Skip
- Evaluator-confirmed action: Research
- What happened: Flutter experience matched, but the résumé location differed from the in-person job location. The Baseline assumed infeasibility without asking whether the candidate could already work there independently.
- Why incorrect: A current address does not prove inability or unwillingness to satisfy an on-site requirement.
- Corrective rule: Treat location compatibility as a factual feasibility check unless a direct contradiction is documented.

## Failure 6 — Active-Signal Overreach

- Case: C02
- Method and incorrect action: Policy 2 → Apply
- Evaluator-confirmed action: Research
- What happened: Policy 2 allowed multiple active-hiring signals to override the listing being older than seven days.
- Why incorrect: Apply controls and recruiter activity indicate platform activity, but do not prove that this exact vacancy is currently progressing candidates.
- Corrective rule: Use active signals to raise posting reliability, but do not automatically convert an older listing into a recent one. Require direct vacancy confirmation when the seven-day policy is binding.

## Highest-cost error

The highest-cost failure condition is **Missing-Evidence Collapse leading to an incorrect Skip**. Equivalent-experience blindness, eligibility-uncertainty collapse, and location-feasibility assumptions can produce the same high-cost action.

Under the provisional cost model:

- incorrect Skip: 100 opportunity-impact units;
- incorrect Apply: 5 units;
- Research: 3 units;
- Request human help: 2 units.

An incorrect Skip has the highest assigned cost because it can permanently remove a potentially life-changing opportunity before the candidate or employer answers a decision-relevant question. Research and human help preserve the option to apply. This ranking is a project assumption and must be validated with candidates and advisers before being treated as an empirical fact.

## Failure families for later testing

1. Missing-Evidence Collapse
2. Equivalent-Experience Blindness
3. Eligibility-Uncertainty Collapse
4. Transferability Suppression
5. Location-Feasibility Assumption
6. Active-Signal Overreach

Future independently labeled cases should include at least two examples of each family so the agent is not tuned to a single anecdote.

