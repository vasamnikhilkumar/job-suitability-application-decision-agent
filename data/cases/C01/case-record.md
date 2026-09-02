# C01 - Frontend Engineer

## Intake status

- Case status: Development case; excluded from blinded headline test metrics
- Resume type: Reddit-sourced image; student confirmed permission for this test
- Original Reddit post: https://www.reddit.com/r/cscareeradvice/s/G8hwetgKky
- Provenance limit: Original author, license, and author consent were not independently verified
- Resume file: `resume.png`
- Direct personal identifiers: Placeholder values only
- Job-post source: https://wellfound.com/jobs/4572767-frontend-engineer
- Source accessed: 2026-08-31
- Private excluded examples used: No

## Evaluator-only record

Complete this section before scoring the agent. Do not derive the expected action from the agent's prediction.

- True hidden state: TBD by evaluator
- True React experience: TBD by evaluator
- True React Query experience: TBD by evaluator
- True posting status: TBD by evaluator
- Expected correct action: Research
- Label timing: Confirmed by evaluator after seeing the Version 1 prediction
- Reason for expected action: A decision-relevant React/React Query experience gap requires verification before apply or skip
- Highest-cost possible error: TBD by evaluator

## Agent-visible resume evidence

The permitted synthetic resume presents a senior front-end engineer with approximately ten years of experience. It provides extensive Angular, enterprise web, component architecture, accessibility, REST API, leadership, and scalable-application evidence. React and TypeScript appear in the skills list. The visible work bullets do not clearly establish two years of React or React Query experience.

## Agent-visible job-post evidence

- Role: Frontend Engineer
- Location: Bangalore Urban; in-office
- Employment: Full-time
- Experience signals: listing header states one year; detailed requirements request two or more years of React.js and React Query experience and at least one year building scalable, responsive web applications
- Core evidence requested: React.js, React Query, component architecture, reusable code, data structures and algorithms, design patterns, HTML, CSS, REST APIs, Git, and Linux
- Additional signals: TypeScript, Canvas APIs, Electron.js, Agile/GitHub, Tailwind CSS, and Ant Design
- Visible status at access time: Apply action present, company marked actively hiring, recruiter recently active
- Visible age at access time: approximately two weeks
- Recency under the project's hypothetical seven-day rule: Fail
- Reliability signals: Provisionally positive, but live visibility does not prove internal hiring status

## Saved Version 1 prediction

- Action: Research
- Mandatory-requirement check: Unclear
- Project/work-evidence check: Pass for broad senior front-end work; unclear for the requested React-specific duration
- Posting recency: Fail
- Posting reliability: Pass provisionally
- Research question: Does the candidate genuinely have at least two years of hands-on React and React Query experience that the resume does not currently evidence?
- Decision-change condition: If truthful supporting experience exists, reconsider after documenting it. If it does not, treat the mandatory React requirement as failed.

## Evaluation

- Expected action assigned before scoring: No
- Prediction scored: Yes, for development feedback only
- Correct: Yes
- False positive: TBD
- False negative: TBD
- Human review: No
- Decision cost: TBD
- Failure category: None for this development run
- Included in blinded headline metrics: No - the label was assigned after the prediction was visible

## Design finding

Posting recency and posting reliability should be recorded separately. A posting can fail the seven-day rule while still showing active-hiring signals.
