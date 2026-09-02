# Probability Decision Record — C03

## Method status

This is a defensible decision-analysis record, not a calibrated prediction. No permissioned, outcome-labeled historical applications were available for this exact candidate/role question. Inventing such outcomes would make the record look precise but invalid.

To make the estimate useful without fabricating data, the record uses:

1. observed résumé and job-post facts;
2. a deliberately small, recent, role-comparable posting sample;
3. transparent smoothing and one explicitly stated reliability assumption;
4. a sequential evidence update;
5. expected-cost thresholds and sensitivity analysis.

## Selected unknown case

Case C03 asks whether a backend candidate with strong projects, but no clearly documented professional distributed-systems tenure, should pursue a role requiring backend experience and two or more years designing large-scale distributed systems.

The correct state is unknown because the employer has not clarified whether the documented projects count as accepted equivalent experience.

## Evidence available at time T0

### Candidate evidence

- Python, Flask, REST APIs, PostgreSQL, Redis, MongoDB, Java, algorithms, and object-oriented design.
- A backend project reports 15+ REST endpoints, asynchronous processing with Celery and Redis, PostgreSQL caching, a relational schema, and capacity for 300–500 concurrent users.
- Another project reports AWS EC2 deployment and scaling an automation system to 150 concurrent accounts.
- No clearly documented professional employment period establishes two years of production distributed-systems ownership.

### Opportunity evidence initially exposed

- Backend Developer role in Bengaluru.
- Listing header indicates two years of experience.
- Listing was four days old at access time.
- Apply, actively-hiring, and recruiter-recently-active signals were visible.

The detailed distributed-systems experience clause is intentionally introduced later as the new evidence item.

## Small recent comparable reference class

Search date: 2026-09-01. The search deliberately used a small role-focused set rather than a large convenient dataset. Included postings concern backend, scalable-service, distributed-system, or closely adjacent backend/ML-systems work and were recently crawled or published. Seniority is not identical across every posting, so this is weak prior evidence rather than a matched outcome cohort.

### Evidence supporting the safer, project-sensitive state

| Comparable posting | Coding | Evidence relevant to C03 |
|---|---|---|
| [TestMu AI Backend Developer](https://wellfound.com/jobs/4118911-backend-developer) | Flexible/project-sensitive | Requests two to three years of hands-on backend experience, but explicitly screens project depth and states that advancement is based on complexity solved rather than years alone. This supports asking whether substantial projects can affect interpretation; it does not prove acceptance. |
| [Ashoka University AI Evaluation Engineer](https://careers.ashoka.edu.in/wp-content/uploads/2026/05/JD-for-AI-Evaluation-Engineer_V2DD.pdf) | Flexible/project-sensitive | Treats one to four years across backend engineering, ML systems, or research engineering as desirable and accepts several forms of systems-building evidence. It is adjacent rather than identical to C03, so its weight is limited. |

### Evidence supporting the unsafe, strict-tenure state

| Comparable posting | Coding | Evidence relevant to C03 |
|---|---|---|
| [Bureau Backend Engineer I](https://wellfound.com/jobs/3403565-backend-engineer-i) | Strict tenure | Explicitly requests two or more years of professional backend development experience. |
| [The Product Highway Backend Engineer](https://wellfound.com/jobs/4144491-backend-engineer) | Strict tenure | Requires four or more years building backend systems in production and says side projects alone are not sufficient. |
| [Skyclad Ventures Senior Backend Engineer](https://wellfound.com/jobs/3535783-senior-backend-engineer-mern-ai) | Strict tenure | Requires three or more years of professional Node.js/Express backend experience. |
| [Atomic Backend Engineer](https://www.ycombinator.com/companies/atomic/jobs/XWj8902-backend-engineer) | Strict tenure | Requires two or more years designing and developing highly scalable distributed systems and APIs, plus successful production delivery. |

### Evidence supporting an unresolved interpretation

| Comparable posting | Coding | Evidence relevant to C03 |
|---|---|---|
| [Chattermill Senior Backend Engineer](https://wellfound.com/jobs/4250780-senior-backend-engineer) | Ambiguous | Uses strong professional and production-ownership language without a numerical year threshold. It shows that evidence can be qualitative while still demanding production depth. |

Observed coding: two flexible/project-sensitive, four strict-tenure, and one ambiguous. This coding records wording patterns, not application outcomes. None of these postings establishes what C03's employer will decide.

Laplace smoothing adds one pseudo-count to each category:

- flexible: (2 + 1) / (7 + 3) = 30%;
- strict: (4 + 1) / (7 + 3) = 50%;
- ambiguous: (1 + 1) / (7 + 3) = 20%.

This coding measures wording patterns in comparable postings. It does not measure hiring outcomes.

## Initial probability decision record

| Item | Required information |
|---|---|
| Evidence | Candidate backend/project evidence, absence of documented professional tenure, recent target listing, and the small comparable-posting coding above. |
| Hidden states | H1: vacancy active and employer accepts projects as equivalent evidence. H2: vacancy active and employer strictly requires professional production tenure that is not shown. H3: vacancy active but equivalence remains a genuine employer judgment or unmodelled interpretation. H4: vacancy is stale, paused, closed, or otherwise unreliable. |
| Beliefs | H1 28.50%; H2 47.50%; H3 19.00%; H4 5.00%. The four probabilities are normalized and sum to one. |
| Event | User-important favorable event F = H1. Option-preserving uncertain event J = H3. Unsafe/non-actionable event U = H2 or H4. Prior P(F) = 28.50%; P(J) = 19.00%; P(U) = 52.50%. |
| Actions | Apply; Research a specific factual question; Request human help; Skip. The agent never submits an application. |
| Costs | Hypothetical opportunity-impact units: correct terminal action 0; Research 3; Request human help 2; incorrect Apply 5; incorrect Skip 100. |
| Policy | Compute immediate expected error cost. Apply is eligible only when its expected error cost is no greater than Research and no unresolved hard requirement remains. Skip is eligible only when its expected lost-opportunity cost is no greater than Research or a hard failure is conclusive. Otherwise Research if a factual answer can resolve the case; Request human help only when factual research cannot settle the judgment. |
| Decision | Research. At T0, Apply expected loss = 5 × P(U) = 5 × 0.525 = 2.625, but H3 represents unresolved mandatory interpretation, so the hard-uncertainty gate prevents Apply. Skip expected loss = 100 × P(F or J) = 100 × 0.475 = 47.50. A targeted employer-policy check is available for cost 3. |
| Audit data | Decision record updated: 2026-09-01, Asia/Calcutta. Original case access: 2026-08-31. Data version: C03-T0-v3. Comparable-posting search snapshot: 2026-09-01. Model: OpenAI Codex; exact deployed model identifier was not exposed in the artifact. Policy version: probability-cost-policy-v2. Reference-class coding version: backend-equivalence-RC2. |

### Construction of the initial joint beliefs

The posting displayed several current activity signals. In the absence of outcome data, the record assigns a stated assumption of 95% to “active” and 5% to H4 “unreliable.” The active probability is then distributed using the smoothed comparable-posting proportions. The fresh reference-class search retained the same observed category counts as the earlier record, so the numerical prior is unchanged even though the supporting sources are stronger and more recent:

- H1 = 0.95 × 0.30 = 28.50%;
- H2 = 0.95 × 0.50 = 47.50%;
- H3 = 0.95 × 0.20 = 19.00%;
- H4 = 5.00%.

The above value is an elicited assumption, not a measured platform reliability statistic.

## Sequential update

### 1. Prior probability

| Hidden state | Prior |
|---|---:|
| H1 — projects accepted | 28.50% |
| H2 — strict tenure not shown | 47.50% |
| H3 — employer judgment/unknown interpretation | 19.00% |
| H4 — vacancy unreliable | 5.00% |

The four prior probabilities are normalized and sum to one.

### 2. New evidence

E: Deeper inspection of the target listing reveals both “Experience: 2–4 years” and “2+ years of experience designing and implementing large-scale distributed systems.” This is stronger and more specific than the initially exposed two-year header.

### 3. Likelihood estimate

These likelihoods encode how compatible the newly revealed strict wording is with each state. They are elicited assumptions and are shown so another evaluator can challenge or replace them.

| Hidden state | P(E given H) | Rationale |
|---|---:|---|
| H1 | 0.25 | Strict duration language is possible even when equivalents are accepted, but it is not strongly expected. |
| H2 | 0.85 | The detailed clause is highly compatible with a strict professional-tenure interpretation. |
| H3 | 0.55 | The wording can still leave interpretation to employer judgment. |
| H4 | 0.30 | A stale or unreliable listing may still contain strict wording, but wording is weak evidence of current status. |

### 4. Posterior calculation

`weight = prior × likelihood`

`posterior = weight / sum of all state weights`

| State | Prior | Likelihood | Weight | Posterior |
|---|---:|---:|---:|---:|
| H1 | 0.2850 | 0.25 | 0.07125 | 11.985% |
| H2 | 0.4750 | 0.85 | 0.40375 | 67.914% |
| H3 | 0.1900 | 0.55 | 0.10450 | 17.578% |
| H4 | 0.0500 | 0.30 | 0.01500 | 2.523% |

The four posterior probabilities are normalized and sum to one.

Posterior events:

- P(F | E) = P(H1 | E) = 11.985% (11.98% at two decimals).
- P(J | E) = P(H3 | E) = 17.578% (17.58% at two decimals).
- P(U | E) = P(H2 or H4 | E) = 67.914% + 2.523% = 70.437% (70.44% at two decimals).

### 5. Decision-threshold comparison

The cost model gives two useful thresholds when Research is assumed to resolve the factual uncertainty:

- Apply versus Research: `5 × P(U) <= 3`, so Apply is cost-preferred only when P(U) is at most 60% and the hard-uncertainty gate is clear.
- Skip versus Research: `100 × P(F or J) <= 3`, so Skip is cost-preferred only when P(F or J) is at most 3%, unless a hard failure is conclusive.

Posterior comparison:

- P(U | E) = 70.44%, above the 60% Apply ceiling.
- P(F or J | E) = 11.98% + 17.58% = 29.56%, above the 3% Skip ceiling.
- Immediate expected loss of Apply = 5 × 0.7044 = 3.522 units.
- Immediate expected loss of Skip = 100 × 0.2956 = 29.56 units.
- Research action cost = 3 units.

### 6. New action

**Research remains the selected action.**

After the strict clause is revealed, Apply becomes more expensive than Research, while Skip remains far more expensive because a meaningful chance of a favorable or judgment-dependent state remains.

Specific research question:

> Does the employer count the candidate's documented backend and distributed-systems projects as qualifying equivalent experience for the stated two-to-four-year and two-year distributed-systems requirements?

- Employer confirms equivalent evidence: shift probability toward H1 and reconsider Apply.
- Employer requires professional production tenure: shift probability toward H2 and reconsider Skip.
- Employer will not clarify and the issue remains interpretive: Request human help.

## Sensitivity analysis

The action should not depend on one fragile likelihood choice. Holding the policy costs fixed:

- Research is preferred to Apply whenever posterior P(U) exceeds 60%.
- Research is preferred to Skip whenever posterior P(F or J) exceeds 3%.

The current posterior is 70.44% unsafe and 29.56% favorable-or-judgment-dependent. The Research decision therefore has margins of 10.44 percentage points over the Apply boundary and 26.56 points over the Skip boundary.

The decision is locally robust, but not calibrated. A reviewer should vary the four likelihoods and the 95% activity assumption. If reasonable changes push P(U) below 60%, the result is sensitive and must be reported as such.

## What would make the probabilities genuinely calibrated

Collect a small, permissioned reference set restricted to comparable early-career backend applications and record, before model use:

- employer wording on experience and equivalents;
- candidate professional tenure and project evidence;
- whether the vacancy was confirmed active;
- recruiter screening decision;
- whether projects were accepted as equivalent;
- timestamps and source provenance.

Use time-separated cases: estimate priors and likelihoods on earlier cases, then test calibration on later untouched cases. Until such data exists, this record supports transparent decision reasoning, not probability accuracy.
