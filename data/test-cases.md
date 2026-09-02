# Test Case Inventory

The project contains two intentionally separate sources of cases.

## Real-world development cases

- IDs: C01–C16
- Résumé source: Reddit posts supplied in the ordered source list
- Job-post source: live public listings captured during development
- Status: agent actions already recorded
- Label boundary: development or post-prediction evaluator-confirmed; not fully blinded
- Location: `data/cases/C01` through `data/cases/C16`

## Project-authored simulated cases

- IDs: C17–C50
- Résumé source: fictional evidence authored for this project
- Job-post source: fictional postings authored for this project
- Status: inputs and evaluator labels prepared; agent predictions not yet run
- Label boundary: labels were stored separately before any run
- Inputs: `data/simulated-cases/case-inputs.md`
- Hidden labels: `data/simulated-cases/hidden-labels.md`

## Evaluation boundary

Do not merge the existing development-replay results with the simulated cases until every frozen policy has been run on C17–C50 and its outputs have been saved. Until then, the current result files describe only C01–C16.

The simulated set deliberately includes Apply, Research, Request human help, and Skip labels. Its distribution is a test design choice, not an estimate of real-world prevalence.
