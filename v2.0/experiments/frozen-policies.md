# Frozen Week 2 Policies

Frozen version: `W2-POLICY-v1`, before reading simulation outcomes. Redesign `P3b` is defined only after the documented failure analysis and is reported separately.

## Shared model

All policies receive the same 500 cases generated with seed `20260910`. Each case samples one hidden state from the priors and one outcome for each of E1, E2, and E3 from the matching likelihood row. No policy can resample or alter a case.

## P0 — Most-common-action baseline

Use no evidence. Aggregate prior mass by correct action and always output the most common action. Ties use the fixed order Skip, Research, Apply, Request human help. Information cost and checks asked are zero.

## P2 — Belief update plus expected-cost threshold

Observe all three evidence sources, update the six-state posterior by Bayes' rule, aggregate posterior state mass by action, and select the action with minimum posterior expected decision loss. P2 pays every evidence cost. Human escalation occurs when Request human help has minimum expected loss.

## P3 — Active information value and cost

Start from the prior. At each step, calculate every unused check's expected reduction in minimum Bayes risk and subtract its generalized evidence cost. Select the check with the largest positive net value; after observing it, update the posterior and repeat. Stop when no unused check has positive net value. Return the minimum-risk action. Ties use the fixed order Apply, Research, Request human help, Skip.

Generalized evidence cost converts time and human attention to hypothetical units using the frozen rates in `src/model.py`.

## P3b — Post-failure redesign

P3's zero-check, all-human result revealed a deferral trap caused by flat low escalation cost. P3b (defined only after that result) adds a penalty for unnecessary deferral and an entropy budget: while posterior entropy exceeds 1.80 bits, ask the unused check with the greatest expected information gain per generalized-cost unit if that ratio is at least 0.50 bits/unit. Then choose the minimum-risk action. This is a separate redesign result, not part of the frozen P0/P2/P3 comparison.

## One-sentence stop rule

Stop asking questions when no unused check has positive expected reduction in decision loss after monetary, time, and human-attention cost.
