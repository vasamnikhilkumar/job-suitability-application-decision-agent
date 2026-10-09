# Week 2 — Active Information Selection

This directory is a self-contained Week 2 extension of the candidate-controlled job-application decision agent. It adds a complete belief model, entropy and value-of-information calculations, frozen P0/P2/P3 policies, a seeded local simulation, failure-driven redesign, generalization exercises, social drafts, and a Week 2 preprint.

The simulation uses no LLM or API calls.

## Reproduce

From the repository root:

```powershell
python v2.0/src/run_simulation.py
python v2.0/src/analyze_results.py
python v2.0/src/verify_results.py
```

Outputs are written to `v2.0/data` and `v2.0/results`. The fixed seed is `20260910`, and the default experiment contains 500 cases. The notebook `agent.ipynb` runs the same local workflow and requires no API key.

## Directory map

- `belief-model.md` — hidden states, priors, likelihoods, Bayes and entropy audit
- `information-selection.md` — expected information gain and evidence-cost comparison
- `decisions/thresholds-and-control.md` — thresholds, actions, escalation, stop rule, and umbrella exercise
- `experiments/frozen-policies.md` — P0/P2/P3 definitions frozen before results
- `src/` — standard-library-only simulation and verification code
- `data/` — generated identical cases and policy predictions
- `results/` — metrics, failures, redesign comparison, and generalization
- `paper/` — IJCAI-style Week 2 LaTeX preprint and compiled PDF
- `social/` — five project-specific LinkedIn drafts plus Reddit/X participation plan

## Claim boundary

The experiment is a model-consistency simulation. It does not validate hiring outcomes, fairness, calibrated real-world probabilities, or the assumed costs. C01–C16 remain a separate Week 1 development replay.
