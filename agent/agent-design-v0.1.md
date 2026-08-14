# Agent design v0.1

> Status: research-stage design. The agent recommends a next action; it does not predict an interview, offer, or a candidate's worth.

## Problem

A job seeker must decide whether to apply for a particular job while important facts are incomplete. The posting may omit pay, work conditions, eligibility details, or whether the role remains active. The candidate may have incomplete evidence about their fit. The agent therefore chooses the most useful next action: **apply**, **research**, **request human help**, or **skip**.

## Input

```mermaid
flowchart LR
  A[Candidate: goals, skills, constraints, effort budget] --> E[Evidence record]
  B[Opportunity: posting, source, date, employer facts] --> E
  C[Candidate or adviser notes] --> E
  E --> D[Observed facts, inferences, missing information, conflicts]
```

Each material claim records its source, date, whether it was observed or inferred, relevance, reliability note, and consent scope.

## Hidden state

Some decision-relevant facts cannot be observed at the time of the recommendation.

```mermaid
flowchart TD
  P[Posted job and candidate profile] --> O[Observable evidence]
  O -. supports but does not prove .-> H1[Employer interest]
  O -. supports but does not prove .-> H2[Opportunity value for this candidate]
  O -. supports but does not prove .-> H3[Actual role conditions and status]
  O -. supports but does not prove .-> H4[Eligibility or feasibility]
```

The agent must label these as uncertain rather than converting them into facts.

## Belief

Beliefs are source-aware summaries of the available evidence, not opaque predictions.

| Belief area | Possible state | Decision use |
| --- | --- | --- |
| Alignment | supported, mixed, unknown | Determines whether the role appears to serve stated goals. |
| Feasibility | confirmed, unconfirmed, conflicting | Identifies candidate-defined hard constraints. |
| Opportunity value | supported, uncertain, conflicting | Shows whether material role qualities remain unknown. |
| Employer response | unknown, weakly supported | Never presented as a guaranteed outcome. |
| Evidence quality | direct, current, attributable, weak | Determines how much confidence is appropriate. |

```mermaid
flowchart LR
  E[Evidence records] --> Q[Quality and provenance check]
  Q --> B[Belief summary]
  M[Missing or conflicting claims] --> B
  B --> U[Uncertainty statement]
  B --> P[Decision policy]
```

## Action

```mermaid
flowchart TD
  D{Decision policy} --> A[Apply]
  D --> R[Research a specific question]
  D --> H[Request human help]
  D --> S[Skip and log the reason]
  A --> L[Decision log]
  R --> E[New evidence]
  H --> E
  S --> L
```

- **Apply:** feasibility and value look sufficient relative to effort; uncertainty is tolerable to the candidate.
- **Research:** a focused answer could materially change the action.
- **Request human help:** the case is high-stakes, conflicting, or needs context the agent cannot interpret safely.
- **Skip:** a verified candidate-defined constraint conflicts with the role, or value is too low for the cost.

## Cost

```mermaid
flowchart TD
  A[Applying: candidate time and effort] --> D[Compare decision costs]
  S[Skipping a valuable role: missed opportunity] --> D
  R[Research or human help: delay and attention] --> D
  D --> P[Apply when feasible and effort is acceptable]
  D --> E[Escalate only for a close hard requirement, conflicting facts, or a novel case]
```

The cost model does not treat every wrong decision equally. A low-effort application can be less costly than skipping a role the candidate would have valued, but applying is not free: tailoring, assessments, deadline pressure, privacy exposure, and emotional load still matter. The candidate defines what an acceptable application cost is.

## Policy

```mermaid
flowchart TD
  S[Start] --> C{Verified hard constraint conflicts?}
  C -->|Yes| K[Skip and log why]
  C -->|No| M{Close hard requirement or contradictory posting?}
  M -->|Yes| H[Request human help]
  M -->|No| G[Run three reasoning passes with different framing]
  G --> X{Do the verdicts split?}
  X -->|Yes| H
  X -->|No| N{Is the material uncertainty novel?}
  N -->|Yes| R[Research the specific unknown]
  N -->|No| V{Value and feasibility justify the effort?}
  V -->|Yes| A[Apply]
  V -->|No| K
```

The policy uses disagreement between independent reasoning passes as an escalation signal instead of a single confidence score. It also escalates close or contradictory job requirements and genuinely novel cases. A familiar uncertainty that has repeatedly been resolved successfully is not escalated solely because confidence dips.

## Feedback

```mermaid
flowchart LR
  R[Research result] --> E[Evidence record]
  A[Application submitted] --> F[Recruiter response or no response]
  F --> I[Interview]
  I --> O[Offer]
  O --> C[Candidate choice and later assessment]
  C --> E
```

Non-response is ambiguous, not an automatic rejection. Each event answers a different question and must not be collapsed into one success label.

## Human reasoning function

```mermaid
flowchart LR
  A[Agent identifies a specific uncertainty] --> H[Candidate, adviser, or mentor]
  H --> Q[Claim, source or comparable case, scope, remaining uncertainty]
  Q --> E[Evidence record]
  E --> P[Policy re-evaluates next action]
```

Human input is evidence with scope and limitations, not ground truth. The human reviewer should state the claim assessed, relevant context, source or comparable case, remaining uncertainty, and recommended next action.

## Core agent loop

```mermaid
flowchart LR
  O[Observe evidence] --> B[Form and revise beliefs]
  B --> D[Choose next action]
  D --> F[Receive feedback or new evidence]
  F --> O
```

## Agent architecture

```mermaid
flowchart TB
  I[1. Collect job and candidate information] --> E[2. Organize what is known]
  E --> C[3. Check for missing or conflicting information]
  C --> U[4. Show what is likely and what is uncertain]
  U --> D[5. Choose the next best action]
  D --> X[6. Explain the choice and let the candidate decide]
  X --> L[7. Save the decision and what happened next]
  L --> E
```

In simple terms, the agent first gathers information about the candidate and the job. It then separates known facts from missing or conflicting details. Based on that, it recommends whether to apply, do more research, ask a person for help, or skip. The candidate can always disagree with the recommendation. New information is saved and used to improve the next decision.

## Relationship between core components

```mermaid
flowchart LR
  I[Inputs] --> E[Evidence]
  E --> B[Beliefs]
  B --> P[Policy]
  C[Costs and candidate preferences] --> P
  H[Human reasoning] --> E
  P --> A[Action]
  A --> F[Feedback]
  F --> E
```

## Current design summary

| Component | Current design |
| --- | --- |
| Decision unit | One candidate considering one opportunity at one point in time. |
| Inputs | Candidate goals and constraints, opportunity details, attributed evidence, and effort budget. |
| Uncertainty | Explicit qualitative states rather than uncalibrated probabilities. |
| Actions | Apply, research, request human help, or skip. |
| Explanation | Supporting evidence, unknowns, conflicts, action cost, and candidate override. |
| Feedback | Separate research, application, recruiter, interview, offer, and candidate-assessment events. |
| Safeguards | Candidate control, privacy scope, no protected-attribute inference, and no automatic submission. |

## Design status

The decision model and diagrams are complete as a conceptual baseline. Thresholds, value trade-offs, research costs, data sources, evaluation metrics, and any probability estimates remain hypotheses that require research, testing, and appropriate legal, privacy, and fairness review.
