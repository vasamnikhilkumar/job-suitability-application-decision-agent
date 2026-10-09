# X Thread Draft (Not Yet Posted)

1/ I built a belief-based job-decision agent and tested it on 500 seeded simulated cases. All probabilities and costs are labeled hypothetical.

2/ Hidden states separate actionable fit, factual uncertainty, judgment, mismatch, unavailable opportunities, and residual “other.” Actions: Apply, Research, Human help, Skip.

3/ The surprising failure: my active information policy escalated every case and checked nothing. Human help was too cheap in the loss table, so it dominated.

4/ A redesign charged reviewer capacity and used information gain per cost. Blanket escalation disappeared, but accuracy (40.4%) remained below the full-information policy (45.8%).

5/ Negative results matter. The code, frozen policies, synthetic data, and verification checks are in the project repository. Question: how should reviewer capacity enter a decision-theoretic loss?
