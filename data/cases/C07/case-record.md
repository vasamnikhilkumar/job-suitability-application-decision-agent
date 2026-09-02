# C07 - DevOps Engineer

## Intake status

- Source platform: Reddit, as confirmed by the student
- Original Reddit post: https://www.reddit.com/r/devopsGuru/s/aIvTjlvpuI
- Source permission: Student confirmed the résumé is permitted for this test
- Provenance limit: Original author, license, and author consent were not independently verified

- Case status: Admitted and scored
- Resume file: `resume.jpeg`
- Source permission: User confirmed all supplied information is permitted for this test
- Job-post source: https://wellfound.com/jobs/4408966-devops-engineer
- Source accessed: 2026-08-31
- Private excluded examples used: No

## Evaluator-only record

- Expected correct action: Request human help
- Label timing: Revealed after the agent prediction was fixed
- Reason for expected action: Strong adjacent DevOps evidence makes transferability a human judgment, while required product-specific technologies and current vacancy status remain problematic.

## Evidence assessment

- Mandatory requirements: Fail on evidence shown. The résumé exceeds the two-year DevOps requirement and shows Kubernetes, Docker, Linux, Bash, CI/CD, GitHub Actions, and communication/collaboration. However, the listing requires good knowledge of MongoDB, Kafka, and ClickHouse, none of which is shown.
- Project/work evidence: Pass. Five-plus years of professional DevOps work includes AKS/Kubernetes, Docker, Helm, Linux deployments, Bash, GitHub Actions, Jenkins/Azure DevOps pipelines, monitoring, troubleshooting, security, and cross-functional work.
- Posting recency and reliability: Fail under the hypothetical seven-day rule. The listing was posted two months earlier. Apply and employer-response signals remain visible, but those do not make the posting recent.

## Fixed Version 1 prediction

- Action: Request human help
- Policy basis: Posting reliability/recency fails and exactly one of the other two checks—project/work evidence—passes. A human adviser can judge whether the candidate's strong adjacent DevOps record makes the missing product-specific data-stack experience an acceptable transferability case.
- Matched evidence: Five-plus years in DevOps; Kubernetes/AKS, Docker, Linux, Bash, CI/CD, GitHub Actions, Helm, monitoring, troubleshooting, automation, security, and collaboration.
- Partial evidence: Azure-native data and monitoring services demonstrate adjacent infrastructure experience, but they do not prove MongoDB, Kafka, ClickHouse, or Grafana knowledge.
- Mandatory evidence not shown: MongoDB, Apache Kafka, and ClickHouse experience; Grafana is nice-to-have and also not shown.
- Uncertainty: Whether the employer will accept adjacent Azure platform experience and whether the two-month-old vacancy is still progressing applications.
- Research question, if applicable: Not the selected action. A human should assess transferability and advise whether contacting the employer about stack flexibility is worthwhile.
- Condition under which the candidate should reconsider the decision: Reconsider Apply if truthful omitted experience covers the missing technologies or a trusted adviser/employer confirms that adjacent experience is acceptable and the vacancy is active; reconsider Skip if those technologies are strict and the candidate lacks them.

## Evaluation

- Prediction fixed before evaluator label reveal: Yes
- Expected action: Request human help
- Correct: Yes
- Human review: Yes, meaning the candidate is advised to seek help; the agent builder does not supply a reviewer
- Decision cost: 2 hypothetical opportunity-impact units (human-help action cost)
- Failure category: None; correct decision
