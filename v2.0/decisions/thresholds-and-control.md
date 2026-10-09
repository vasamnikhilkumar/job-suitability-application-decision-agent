# Thresholds, Costs, and Human Control

## Error costs

The loss matrices are in `src/model.py`. A false Skip costs 100 units because a suitable opportunity may be lost; an incorrect Apply costs 5. Research costs 3–5, and human review costs 0–2 in the frozen Week 1 matrix. The redesign charges 6 for unnecessary deferral and 2 even when deferral is correct, representing scarce reviewer capacity. These values are assumed and are varied in sensitivity tests.

## Three operational actions plus escalation

- Apply when Apply has minimum posterior expected loss.
- Research when a resolvable fact has minimum expected loss.
- Skip when Skip has minimum expected loss.
- Request human help is an explicit escalation action for judgment-dependent or residual cases, never a claim that the agent resolved them.

P3 acquires a check only above the strict net-value threshold `VOI > 0`; it stops at or below zero. P3b acquires evidence while uncertainty is above 1.80 bits and EIG/cost is at least 0.50. Ties are deterministic in the order Apply, Research, Human, Skip.

## Mandatory umbrella problem

Assume carrying an umbrella unnecessarily costs 1 inconvenience unit and being caught in rain costs 20. Carry when `P(rain) * 20 > (1-P(rain)) * 1`, equivalently `P(rain) > 1/21 = 0.0476`. At exactly 0.0476 the actions tie; the stated conservative policy carries. If inconvenience rises to 5, the threshold becomes `5/25 = 0.20`. This illustrates that thresholds belong to a context and cost model, not to probability alone.

## Human override

Every recommendation records posterior beliefs, checks used, and the selected action. A human may override any action, must decide cases marked for help, and should inspect high-cost Skip decisions. The agent does not submit applications, contact employers, or reject opportunities automatically.
