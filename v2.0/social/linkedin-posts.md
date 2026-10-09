# LinkedIn Drafts (Not Yet Posted)

## Post 1 — the belief model

I am building a job-suitability decision agent that does not pretend uncertainty is one number. It tracks six mutually exclusive hidden states: actionable match, resolvable factual uncertainty, judgment-dependent fit, conclusive mismatch, unavailable opportunity, and residual other. I assumed the priors and likelihoods rather than presenting them as hiring statistics. What hidden state is missing, and which distinction would you merge?

## Post 2 — information has a cost

My three checks have different value: a vacancy-status audit gives less raw information than targeted clarification, but much more information per unit of time, money, and attention. The active policy buys a check only when expected decision-loss reduction exceeds its cost. Where would you put the cost of attention in a real workflow?

## Post 3 — assumed, tested, discovered

I assumed that human review was a cheap safe action. I tested that assumption on 500 seeded simulated cases. I discovered a deferral trap: the active policy escalated 100% of cases and bought no evidence because the loss table made review dominate. I changed the design to charge scarce reviewer capacity and use an entropy budget. The fix removed blanket escalation but did not beat every baseline. What capacity constraint would make this test more realistic?

## Post 4 — honest negative result

The full-information policy reached 45.8% action accuracy. The redesigned active policy reached 40.4% while using two rather than three checks on average. That is not a universal win: it fixes over-deferral and saves evidence, but increases modeled decision cost. I am sharing the trade-off rather than hiding it. Which metric should be primary for a candidate-facing tool?

## Post 5 — human control

This agent recommends Apply, Research, Request human help, or Skip; it never submits or rejects automatically. A false Skip is modeled as much more costly than an unnecessary Apply, and high-cost Skip decisions should be reviewed. What evidence would you require before allowing even a recommendation-only system to influence a real job search?
