# Research File — Job-Application Decision Agent

## 1. Experience Level

This project is being developed as a learning project about probabilistic and uncertainty-aware AI agents.

No professional expertise in hiring technology, employment law, psychometrics, or probability calibration is claimed.

The research therefore relies on:

- official guidance;
- academic research;
- public job-post evidence;
- practitioner discussions;
- transparent assumptions; and
- reproducible tests.

---

## 2. Selected Problem

**Job-Application Decision Agent**

The agent receives:

- one candidate résumé; and
- one job-post link.

It must choose exactly one next action:

- Apply;
- Research;
- Request human help; or
- Skip.

The employer’s interest, the vacancy’s actual status, accepted-equivalent experience, eligibility feasibility, and the opportunity’s eventual value are not directly known.

---

## 3. Project Objective

Design and evaluate an AI agent that helps a candidate make a job-application decision under uncertainty.

The agent should:

- observe résumé and job-post evidence;
- separate known, missing, and conflicting information;
- assess mandatory requirements;
- examine truthful project and work evidence;
- assess posting recency and reliability;
- select one next action;
- explain the evidence supporting that action; and
- update its decision when new evidence becomes available.

The goal is not to predict an interview, offer, or career outcome.

The central research question is:

> **Can an agent make safer and more useful application decisions when it explicitly represents uncertainty, evidence quality, candidate preferences, and action costs?**

---

## 4. Type of Agent

The project is an **uncertainty-aware job-application decision agent**.

The agent contains:

- Input
- Hidden state
- Belief
- Action
- Cost
- Policy
- Feedback

The intended later version follows:

**Observe → Form Beliefs → Choose Action → Receive Feedback → Update Beliefs → Choose the Next Action**

The current agent is advisory. It does not autonomously submit applications.

---

## 5. Human Reasoning Function

The selected human reasoning function is:

> **Identify a decision-relevant uncertainty and ask for the smallest item of evidence that could change the action.**

Examples include:

- asking whether truthful experience was omitted from the résumé;
- checking whether an employer accepts project experience as equivalent;
- confirming work authorization or location feasibility;
- checking whether the exact vacancy is still active; and
- sending an unresolved transferability judgment to a trusted person.

The project advises the candidate to seek human help when necessary. It does not claim to provide a human reviewer.

---

## 6. Information We Currently Do Not Know

The following questions require research and validation.

### Hidden States

- Does the candidate actually satisfy every mandatory requirement?
- Does the employer accept equivalent project or adjacent work experience?
- Is the vacancy genuinely active and progressing applicants?
- Are location, sponsorship, clearance, or authorization conditions feasible?
- Would the opportunity ultimately be valuable to this candidate?

### Résumé and Job-Post Evidence

- Which requirements are genuinely mandatory rather than preferred?
- When does missing résumé evidence mean absence, omission, or different terminology?
- Which posting signals reliably indicate that a vacancy remains active?
- How should contradictory requirements be represented?
- Which evidence makes two candidate-job cases meaningfully comparable?

### Actions

- When should uncertainty produce Research instead of Skip?
- Which factual questions provide enough information to change the action?
- When does accepted equivalence require human judgment?
- When is a hard requirement conclusive enough to justify Skip?
- When should the agent stop researching?

### Probability and Cost

- How should prior probabilities be estimated?
- Which historical cases are sufficiently recent and comparable?
- How should likelihoods be estimated without fabricating precision?
- How costly is an unnecessary Apply?
- How costly is an incorrect Skip that removes a meaningful opportunity?
- Do different candidates assign different values to these errors?

### Fairness, Privacy, and Accessibility

- Could résumé omissions be related to disability or accessibility?
- Could the policy systematically advise some groups to Skip more often?
- Which candidate data should be excluded or minimized?
- What consent and provenance records are necessary?
- Which legal requirements apply in each jurisdiction and use context?

### Evaluation

- What should count as a correct next action?
- Which cases should be labeled before the agent runs?
- How should Apply, Research, Request human help, and Skip be represented?
- Which measurements should accompany agreement or accuracy?
- How should calibration be evaluated on later untouched cases?

---

## 7. Initial Research Goal

The research should help determine:

1. realistic hidden states for job-application decisions;
2. observable evidence available in a résumé and job post;
3. the actions available to the agent;
4. how factual uncertainty differs from human judgment;
5. how recent and comparable cases should be selected;
6. how beliefs should change after new evidence;
7. which costs should affect the decision;
8. how opportunity-denial errors should be measured;
9. which privacy, fairness, accessibility, and legal safeguards are required; and
10. how the agent can be tested without making predictive claims.

These findings are used to refine the agent prompt, policies, cases, probability-decision record, and evaluation.

---

## 8. Research Principle

AI-generated recommendations must not be treated as verified facts.

Important recommendations should be checked against:

- primary sources;
- official guidance;
- research papers;
- practitioner experience;
- real discussions;
- recent comparable evidence; and
- reproducible evaluation records.

Anecdotes can reveal questions and failure conditions, but they do not establish population-level evidence.

Unsupported thresholds, probabilities, costs, and performance claims must remain labeled as assumptions.

# Research Findings

## Practitioner and Employment Research

### Finding 1 — Missing résumé evidence is not confirmed failure

A qualification absent from a résumé may be:

- genuinely absent;
- truthfully omitted;
- described with different terminology;
- represented by an accepted equivalent; or
- difficult to communicate because of an accessibility issue.

The agent should therefore mark decision-relevant missing evidence as **Unclear** when a factual answer could change the action.

### Finding 2 — Incorrect Skip decisions require explicit attention

Agreement or accuracy alone can hide a consequential error: advising a candidate to Skip a worthwhile opportunity.

The evaluation should separately retain:

- incorrect Skip quantity;
- incorrect Apply quantity;
- per-action precision and recall;
- Research rate;
- human-help rate;
- decision cost; and
- named failure conditions.

The project currently treats an incorrect Skip as more costly than an unnecessary Apply. This is a provisional candidate-centered assumption, not a measured fact.

### Finding 3 — Posting recency and reliability are different

A recent post may still be unreliable, duplicated, paused, or inconsistent.

An older post may still display:

- an active application control;
- recent recruiter activity;
- an explicit open deadline; or
- a recent repost.

These signals can increase confidence but do not prove that the exact vacancy is progressing candidates. The seven-day rule remains a project hypothesis.

### Finding 4 — Factual research and human judgment should be separated

Research is appropriate when a fact can change the action, such as:

- authorization status;
- exact experience duration;
- vacancy status; or
- whether the candidate possesses truthful omitted evidence.

Human help is more appropriate when the available facts leave a qualitative judgment, such as:

- transferability between technology stacks;
- portfolio quality;
- project experience as professional equivalence; or
- domain-experience substitution.

### Finding 5 — Comparable evidence must be narrow and transparent

The probability record uses a deliberately small reference class of recent, role-related postings containing backend, experience, production, and distributed-systems language.

The postings provide evidence about wording patterns. They do not provide:

- recruiter decisions;
- interview outcomes;
- evidence that projects were accepted;
- candidate opportunity value; or
- calibrated probabilities.

Recent comparable postings are therefore useful for forming a transparent prior, but not for claiming a hiring probability.

### Finding 6 — Employment-related AI requires governance

The NIST AI Risk Management Framework treats governance, mapping, measurement, and management as continuing activities.

Employment guidance from the U.S. Equal Employment Opportunity Commission warns that selection procedures can create discrimination risks and that disability-related accommodation and access require attention.

Although this project is candidate-side and advisory, harmful steering remains possible. Human oversight, provenance, audit data, and false-Skip analysis are therefore necessary.

### Finding 7 — Calibration requires untouched later evidence

An elicited probability is not calibrated merely because it is numerical.

Calibration requires:

- beliefs saved before outcomes are known;
- later observable outcomes;
- comparable cases;
- an untouched evaluation group; and
- comparison between predicted probability bands and observed frequencies.

The current probability-decision record is a transparent decision analysis, not a calibrated forecast.

---

## Current Research Implications

The research supports the following current design choices:

- keep the agent advisory and candidate-controlled;
- forbid autonomous application submission;
- prohibit fabricated résumé content;
- classify important missing evidence as Unclear;
- use Research only for a decision-changing factual question;
- use human help for unresolved qualitative judgment;
- separate posting recency from reliability;
- record incorrect Skips explicitly;
- preserve source, time, data, model, policy, and label-timing information;
- keep numerical costs and thresholds provisional; and
- prohibit claims about interview, offer, or opportunity-value prediction.

The research does **not** validate:

- the seven-day posting threshold;
- the current numerical action costs;
- the probability values in the decision record;
- résumé matching as a predictor of hiring outcomes;
- fairness across candidate groups; or
- any claim that the agent is ready for deployment.

---

## Research Status

### Confirmed or Supported

- Missing evidence should not automatically be treated as confirmed evidence or confirmed failure.
- The agent should remain advisory and candidate-controlled.
- Research should name a specific decision-changing question.
- Human help should identify the unresolved judgment.
- Posting recency and posting reliability should be represented separately.
- Incorrect Skip decisions should be measured separately.
- Audit data and provenance are necessary.
- Numerical probabilities are not calibrated without untouched later evidence.
- Fairness and accessibility require evaluation before broader use.

### Still Uncertain

- Whether seven days is an appropriate posting-age threshold.
- Which vacancy-status signals reliably predict an active hiring process.
- How employers treat projects as equivalent professional experience.
- Which hidden-state categories provide the best representation.
- How probability priors and likelihoods should be estimated.
- What decision costs reflect real candidate preferences.
- When repeated model disagreement should trigger escalation.
- How novelty should be measured.
- Whether the policy improves real candidate outcomes.
- How performance varies across job families and candidate groups.

---

## Current Conclusion

The research supports a documented, uncertainty-aware, candidate-controlled prototype.

It does not support predictive claims, calibrated probabilities, an optimized posting-age rule, validated action costs, or claims that the system is fair.

Those remain explicit subjects for later research and testing.
