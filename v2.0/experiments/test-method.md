# Reproducible Test Method

1. Freeze `belief-model.md`, `experiments/frozen-policies.md`, and `src/model.py` before reading results.
2. Use Python's local pseudorandom generator with seed `20260910`.
3. For each of 500 cases, sample one state from the priors and one outcome per evidence source from that state's likelihood row.
4. Run P0, P2, P3, and the explicitly post-failure P3b on the same saved cases.
5. Score decision accuracy, per-action precision and recall, decision loss, evidence cost, checks, and human-review rate.
6. Run `python v2.0/src/verify_results.py`; it checks row sums, priors, case identity, prediction counts, and recomputed metrics.

Commands from the project root:

```text
python v2.0/src/run_simulation.py
python v2.0/src/analyze_results.py
python v2.0/src/verify_results.py
```
