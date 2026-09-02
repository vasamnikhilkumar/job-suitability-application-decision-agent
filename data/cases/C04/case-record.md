# C04 - Backend Developer (Node.js)

## Intake status

- Source platform: Reddit, as confirmed by the student
- Original Reddit post: https://www.reddit.com/r/SoftwareEngineerJobs/s/xxOXDdelfN
- Source permission: Student confirmed the résumé is permitted for this test
- Provenance limit: Original author, license, and author consent were not independently verified

- Case status: Admitted and scored
- Resume source: Image supplied by the user as `exampl4.webp`
- Source permission: User confirmed all supplied information is permitted for this test
- Resume file: `resume.webp`
- Direct identifiers: Visually obscured in the supplied image
- Job-post source: https://wellfound.com/jobs/3299387-backend-developer-node-js
- Source accessed: 2026-08-31
- Private excluded examples used: No

## Evaluator-only record

- Expected correct action: Skip
- Label timing: Revealed after the agent prediction was fixed
- Reason for expected action: Mandatory Node.js expertise and corresponding project/work evidence are not shown, and the stale posting does not change that mismatch.
- True posting status: Awaiting evaluator
- Highest-cost possible error: Awaiting evaluator

## Agent-visible résumé evidence

- Summary and skills identify Python, Django, Django REST Framework, REST APIs, SQL, object-oriented programming, data structures, algorithms, AWS fundamentals, Git, debugging, documentation, authentication, and authorization.
- A March–June 2025 internship documents Python/Django backend features, REST APIs, MySQL, debugging, documentation, and code reviews.
- Two projects document Python/Django APIs, SQLite, access control, authentication, and testing.
- Node.js, JavaScript, a Node server framework, NoSQL experience, microservices, message queues, and Node-specific project or work evidence are not shown.

## Agent-visible job-post evidence

- Role: Backend Developer - Node.js
- Location: Noida; the page also displays India remote text, while its policy field states in office
- Experience: one year
- Core qualification: Proven backend-development experience with expertise in Node.js
- Other qualifications: server-side frameworks, SQL and NoSQL databases, REST APIs, Git, debugging, communication, and teamwork
- Preferred: SQL/MySQL, microservices, message queues, testing frameworks, cloud services, and Agile
- Visible age at access time: posted one year earlier
- Apply button visible, but no recent-posting or recruiter-activity signal was shown

## Three checks

- Mandatory requirements: Fail. The role explicitly requires Node.js expertise, while the résumé documents Python and Django and does not show Node.js.
- Project/work evidence: Fail for this specific role. Backend evidence exists, but every shown internship and project uses Python/Django rather than the mandatory Node.js stack.
- Posting recency and reliability: Fail. The listing is approximately one year old, far outside the project's hypothetical seven-day limit; an Apply button alone does not establish that hiring is current.

## Fixed Version 1 prediction

- Action: Skip
- Policy basis: Mandatory requirements and role-specific project/work evidence both fail, so the skip rule applies regardless of posting reliability.
- Research avoided: Confirming whether the old listing is open cannot change the current résumé-to-role mismatch.

## Required output

- Action: Skip
- Matched evidence: General backend development, REST APIs, MySQL/SQL, Git, debugging, authentication, authorization, documentation, and code review.
- Partial evidence: One short Python/Django internship and two Python/Django backend projects demonstrate transferable backend ability, but not the required Node.js expertise.
- Mandatory evidence not shown: Node.js expertise, Node server-side framework experience, and Node.js work or project evidence; SQL-and-NoSQL breadth is also not clearly demonstrated.
- Uncertainty: The listing may no longer be active. This uncertainty is not decision-relevant because resolving it would not repair the mandatory Node.js evidence gap.
- Research question, if applicable: Not applicable under the current policy.
- Condition under which the candidate should reconsider the decision: Reconsider only for a different Python/Django role, or if the candidate already has truthful Node.js experience omitted from this résumé and can provide real supporting evidence.

## Evaluation

- Prediction fixed before evaluator label reveal: Yes
- Expected action: Skip
- Correct: Yes
- False positive: No
- False negative: No
- Human review: No
- Decision cost: 0 hypothetical opportunity-impact units because the correct terminal action was selected
- Failure category: None; correct decision
