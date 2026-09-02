# Minimum Testable Implementation

## Form

The minimum implementation is an LLM prompt plus ordered deterministic rules. It accepts a résumé and an exact job-post link and produces one recommendation. No spreadsheet is used.

## Input

- candidate résumé;
- exact job-post URL;
- visible posting content and access date.

## Hidden state

- the candidate truly matches and the résumé shows evidence;
- the candidate truly matches but project/work evidence is unclear;
- the candidate truly lacks a mandatory qualification;
- the opportunity is unreliable, stale, paused, or closed;
- an unmodelled eligibility, feasibility, or opportunity condition affects the decision.

## Belief

A source-aware, revisable assessment of each hidden state. Version 1 records Pass, Fail, or Unclear evidence rather than claiming calibrated probabilities. Earlier numerical priors remain hypothetical and are not used for predictive claims.

## Action

- Apply
- Research a specific factual question
- Request human help for a judgment call
- Skip

The action is advice to the candidate. The implementation never autonomously applies.

## Cost

The provisional comparison uses hypothetical opportunity-impact values:

- correct terminal decision: 0;
- Research: 3;
- Request human help: 2;
- incorrect Apply: 5;
- incorrect Skip: 100.

These values are unvalidated assumptions.

## Policy

The ordered rules are frozen in `agent-prompt.md` and `../experiments/policy-comparison.md`. Rule order matters: the hard stop precedes uncertainty handling, and decision-relevant uncertainty precedes the remaining pass/fail table.

## Feedback

Version 1 does not update from outcomes. A later feedback version may record whether an application was submitted and whether an assessment invitation arrived within 30 days. That later version must not treat the absence of an invitation as proof of candidate mismatch.

## Human reasoning function

The selected human reasoning function is **identify uncertainty and ask for more information**. The agent names the missing fact, explains why it matters, and states how each possible answer would change the action. If the issue is a transferability or equivalence judgment, the agent advises the candidate to consult a trusted person.

## Stop condition

Stop researching when no remaining evidence could change the recommended action or when the expected value of the evidence is lower than its cost. This threshold is conceptual until costs are validated.
