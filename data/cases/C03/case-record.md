# C03 - Backend Developer

## Intake status

- Case status: Admitted and scored
- Resume source: Image supplied by the user as `example3.jpeg`
- Source platform: Reddit, as confirmed by the student
- Original Reddit post: https://www.reddit.com/r/developersIndia/s/QubPFbAyCa
- Source permission: User confirmed all supplied information is permitted for this test
- Provenance limit: Original author, license, and author consent were not independently verified
- Resume file: `resume.jpeg`
- Direct identifiers: Visually redacted in the supplied image
- Job-post source: https://wellfound.com/jobs/4632678-backend-developer
- Source accessed: 2026-08-31
- Private excluded examples used: No

## Evaluator-only record

- Expected correct action: Research
- Label timing: Revealed after the agent prediction was fixed
- Reason for expected action: Mandatory experience duration and accepted-equivalent experience require verification.
- True posting status: Awaiting evaluator
- Highest-cost possible error: Awaiting evaluator

## Agent-visible résumé evidence

- Backend summary identifies Python, Flask, REST API design, PostgreSQL, and Redis.
- ParkSpace v2 describes 15+ REST endpoints, Celery and Redis asynchronous processing, PostgreSQL caching, a normalized relational schema, and capacity for 300–500 concurrent users.
- The automation project describes AWS EC2 deployment and scaling from one to 150 concurrent accounts.
- Skills show Python, Java, SQL, data structures, algorithms, object-oriented design, distributed systems, MongoDB, PostgreSQL, Redis, Git, and Linux.
- The résumé shows projects but does not clearly show professional employment or establish two to four years of total professional experience.
- It does not clearly establish two or more years designing and implementing large-scale distributed systems.

## Agent-visible job-post evidence

- Role: Backend Developer
- Location: Bengaluru; in-office with work-from-home flexibility
- Required experience: two to four years total experience
- Mandatory foundation: object-oriented programming, data structures, algorithms, software design, and database systems
- Additional stated requirement: two or more years designing and implementing large-scale distributed systems
- Backend and technology evidence: backend services, multiple programming languages, and data stores such as MySQL, MongoDB, and Redis
- Desired rather than mandatory examples include Elasticsearch, MongoDB, MySQL, Redis, Spring Boot, crawling/web scraping, C, C++, Java, and Groovy.
- Visible age at access time: posted four days earlier
- Active signals: Apply Now, Actively Hiring, and recruiter recently active

## Three checks

- Mandatory requirements: Unclear. The résumé demonstrates the technical foundations and backend projects, but it does not prove the stated two-to-four-year total-experience requirement or two years of large-scale distributed-systems experience.
- Project/work evidence: Pass. Multiple dated projects contain specific backend architecture, API, database, caching, asynchronous-processing, concurrency, and deployment evidence.
- Posting recency and reliability: Pass. It is within the hypothetical seven-day window and has several active-status signals on the source page.

## Fixed Version 1 prediction

- Action: Research
- Research question: Does the candidate have at least two years of qualifying professional or accepted equivalent backend/distributed-systems experience that is truthful but not shown clearly in this résumé?
- Action-changing answer: If the employer accepts the documented projects as equivalent experience, or the candidate can document omitted qualifying experience, reconsider Apply. If the employer requires two years of professional large-scale distributed-systems employment and the candidate has none, reconsider Skip.

## Required output

- Action: Research
- Matched evidence: Python, Java, object-oriented design, data structures, algorithms, REST APIs, Flask, MongoDB, PostgreSQL, Redis, distributed-systems concepts, Git, Linux, asynchronous processing, caching, and backend scalability projects.
- Partial evidence: Backend and distributed-system work is demonstrated through projects, but its scale and duration may not satisfy the employer's experience definition.
- Mandatory evidence not shown: Two to four years of total qualifying experience and two or more years designing and implementing large-scale distributed systems.
- Uncertainty: Whether project experience counts toward the employer's mandatory experience requirement and whether any truthful qualifying experience was omitted.
- Research question, if applicable: Ask the employer or recruiter whether substantial project experience is accepted for the stated experience requirement, and ask the candidate whether qualifying experience was truthfully omitted.
- Condition under which the candidate should reconsider the decision: Apply if qualifying or accepted-equivalent experience is verified; Skip if the requirement is strict and the candidate cannot meet it.

## Evaluation

- Prediction fixed before evaluator label reveal: Yes
- Expected action: Research
- Correct: Yes
- False positive: No
- False negative: No
- Human review: No
- Decision cost: 3 hypothetical opportunity-impact units (research action cost)
- Failure category: None; correct decision
