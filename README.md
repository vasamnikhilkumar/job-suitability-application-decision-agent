# job-suitability-application-decision-agent

## Status

Research and design phase complete (v0.1). The project is ready for a small, transparent implementation and user research.

The current design is a baseline: its policy thresholds, research costs, and evaluation measures remain provisional and must be validated before any predictive claims are made.

**Questions for people who help others make job-application decisions:**

- What do you check first before deciding whether a job is worth applying for?
- Which details in job posts are commonly incomplete, misleading, or stale?
- What makes a past application outcome meaningfully comparable to a new opportunity?
- Which research checks are cheap versus expensive in time, effort, or emotional load?
- When would you apply despite uncertainty, research first, ask a trusted person, or skip?

Please open a Discussion or Issue with experience, examples, sources, or objections. Personal anecdotes are valuable for discovering questions, but they are not population-level evidence without further validation.

## Focus

This project designs and evaluates an **uncertainty-aware job suitability and application-decision agent**. Given a candidate profile and one job opportunity, the agent does not know whether the candidate will be shortlisted or whether the role will ultimately be valuable to that candidate. Instead of presenting a final answer as certain, it chooses the next useful action:

- **Apply**
- **Research**
- **Request human help**
- **Skip**

Core question driving the work:

> Can an agent make safer and more useful application decisions when it explicitly represents uncertainty, evidence quality, candidate preferences, and action costs?

The agent is modeled as an iterative loop:

**Observe → Form beliefs → Choose action → Receive feedback → Update beliefs → Choose next action**

* **Input** – candidate goals, constraints, skills, experience, application budget, job-post content, source, employer information, and prior research results.
* **Hidden state** – employer interest, actual opportunity value for this candidate, true role conditions, job-post status, and eligibility or feasibility details not yet verified.
* **Belief** – a source-aware, revisable summary of alignment, feasibility, opportunity value, employer-response uncertainty, and evidence quality.
* **Action** – apply, research a specific question, request human help, or skip; the agent does not autonomously submit applications.
* **Cost** – application time, research time, effort, deadline pressure, privacy exposure, and missed-opportunity risk.
* **Policy** – the decision rule that chooses the next action from available evidence, uncertainty, candidate preferences, and costs.
* **Feedback** – research results, application submission, recruiter response, interview, offer, candidate choice, and later candidate assessment.
* **Human reasoning function** – structured input from the candidate, adviser, or mentor, recorded as attributable evidence rather than treated as infallible truth.

The design is intentionally non-predictive at this stage. Any numerical probabilities, action thresholds, data sources, and evaluation claims require research, calibration, and appropriate privacy, fairness, and legal review.

## Where to look

* [agent/agent-design-v0.1.md](agent/agent-design-v0.1.md) — the current agent design: problem, inputs, hidden states, beliefs, actions, costs, policy, feedback, human reasoning, and architecture diagrams.
* [research/research_file.md](research/research_file.md) — research questions, initial research goal, principles, findings, implications, sources, and supported versus uncertain assumptions.

## Safety and scope

- The agent is decision support for a candidate, not an employer-side ranking or hiring system.
- It must show the evidence, missing information, uncertainty, and rationale for its suggested next action.
- It must not claim that a candidate will receive an interview, offer, or positive job outcome unless that outcome is directly observed.
- The candidate can override a recommendation and record why.
- The system must not infer protected attributes or use sensitive information beyond the candidate's chosen scope.
