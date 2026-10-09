# Evidence Selection Record

All values are computed at the prior. Generalized cost is `money + 0.03 * minutes + 0.50 * attention`. These are explicit hypothetical utility units, not market prices.

| Source | Expected information gain (bits) | Money | Time | Attention | Generalized cost | EIG/cost | Typical failure | Can change action? |
|---|---:|---:|---:|---:|---:|---:|---|---|
| E1 candidate-fit audit | 0.42445 | 0.20 | 4 min | 0.25 | 0.445 | 0.954 | Resume evidence can be incomplete | Yes; strong and contradictory outcomes can separate Apply from Skip/Research |
| E2 vacancy-status audit | 0.25128 | 0.10 | 2 min | 0.10 | 0.210 | 1.197 | Platform status can be stale | Yes; inactive strongly raises H5 |
| E3 targeted clarification | 0.49382 | 0.50 | 20 min | 1.00 | 1.600 | Employer may not reply | Yes; judgment and refutation outcomes separate H3/H4 |

E3 has the largest raw information gain, while E2 has the best information per cost. Information is not automatically valuable: under frozen Week 1 error costs, human review already minimizes prior expected loss, so every source has negative net decision value after acquisition cost. That is why P3 stops immediately. P3b is a documented, post-failure redesign: it uses an entropy budget and picks the highest EIG/cost source while the ratio is at least 0.50.

## Stopping rule

P3 stops when every unused source has `expected reduction in Bayes risk - generalized evidence cost <= 0`. P3b stops when posterior entropy is at most 1.80 bits, no source remains, or the best EIG/cost falls below 0.50. No evidence outcome is inspected before its source is selected.
