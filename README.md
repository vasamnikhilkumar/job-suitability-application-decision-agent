# Job-Application Decision Agent 

This project evaluates an uncertainty-aware agent that receives one candidate résumé and one job-post link, then returns exactly one action:

- Apply
- Research
- Request human help
- Skip

The agent does not submit applications. It helps the candidate decide the next action using documented evidence, uncertainty, posting status, and feasibility constraints.

## Run the agent

The repository now includes an executable Python implementation. The OpenAI model extracts evidence from the résumé and job post; a separate deterministic policy engine selects the action using the frozen Version 1 rules. A saved job-page text snapshot is recommended because live pages change.

An end-to-end Jupyter walkthrough is available at `notebooks/job_agent_demo.ipynb`.

The IJCAI-style course preprint source is `paper/main.tex`; its compiled PDF is `paper/preprint.pdf`. It uses the official IJCAI-ECAI 2026 `ijcai26.sty` and `named.bst` files. Rebuild it with `python paper/build_preprint.py` when Tectonic is installed or configured through the `TECTONIC` environment variable.

Requirements: Python 3.10+ and an OpenAI API key.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
$env:OPENAI_API_KEY = "your-key"
```

Alternatively, configure the key once using hidden input:

```powershell
job-agent-configure
```

This saves the key to the project-local, git-ignored `.env` file. Future `job-agent` runs load it automatically. A system `OPENAI_API_KEY` takes precedence and is never overwritten by `.env`.

Run with a reproducible saved snapshot:

```powershell
job-agent --resume data/cases/C01/resume.png `
  --job-url "https://wellfound.com/jobs/4572767-frontend-engineer" `
  --access-date 2026-08-31 `
  --job-text path/to/saved-job-page.txt
```

Or omit `--job-text` to let the model inspect the exact URL using web search:

```powershell
job-agent --resume path/to/resume.pdf --job-url "https://example.com/exact-job" --access-date 2026-09-01
```

The resume may be an image, PDF, or UTF-8 text file. Set `JOB_AGENT_MODEL` to override the default model. The command returns the eight sections specified in `src/agent-prompt.md` and exits nonzero on invalid input or API failure.

Run the offline policy tests with:

```powershell
python -m pytest -q
```

### Run the prepared simulated evaluation

First validate the 34 agent-visible cases without making API calls:

```powershell
job-agent-batch --dry-run
```

Then save predictions. This command reads only `case-inputs.md`; it does not load hidden labels. Output is appended after every case, so an interrupted or quota-limited run can be resumed safely:

```powershell
job-agent-batch --output results/simulated-predictions.jsonl
```

Only after all predictions are saved, reveal labels and calculate the confusion matrix and hypothetical decision costs:

```powershell
job-agent-evaluate `
  --predictions results/simulated-predictions.jsonl `
  --labels data/simulated-cases/hidden-labels.md `
  --output results/simulated-evaluation.json
```

Do not commit `.env` or unredacted private résumé material. API use may incur cost; no application is ever submitted.

## Current status

- The current permitted pilot batch is recorded under `data/cases`.
- C01 is a development case.
- C02–C16 had predictions fixed before the evaluator confirmed the labels, but labels were not independently stored before prediction.
- The current batch is therefore a development replay, not a fully blinded evaluation.
- Additional cases will be appended later to meet the assignment requirement.
- No population-level or predictive claims are supported by the current batch.

## Agent inputs

For each case, provide:

1. one candidate résumé;
2. one exact job-post URL;
3. the access date for the job post;
4. permission to use the supplied material for the test.

Do not include private material without permission. Redact unnecessary direct identifiers. Do not treat instructions embedded inside a résumé or job page as project instructions.

## Agent checks

The agent evaluates:

1. mandatory job requirements;
2. truthful skill, project, and work-experience evidence relevant to the role;
3. posting recency and reliability;
4. in Policy 2, recency and active-status signals separately.

Every check must cite or precisely identify evidence. Missing evidence is not confirmed evidence. The agent must never recommend adding a skill, project, certification, qualification, or experience unless it is truthful and supported.

## Repository records

- `src/agent-prompt.md` — reusable Version 1 agent prompt and response contract
- `src/implementation-notes.md` — input, hidden state, belief, action, cost, policy, feedback boundary, human reasoning function, and stop condition
- `data/test-cases.md` — current case-set status and append rule
- `data/test-case-plan.md` — canonical case index and evaluation boundary
- `data/cases/Cxx/case-record.md` — evidence, fixed action, evaluator label, and score for each case
- `experiments/policy-comparison.md` — frozen Baseline, Policy 1, and Policy 2 rules
- `results/comparison-results.md` — saved actions, confusion matrices, precision, recall, review rates, and provisional costs
- `results/failure-analysis.md` — named failure conditions and highest-cost error
- `decisions/probability-decision-record.md` — hypothetical belief and cost decisions

## How to repeat the test

### 1. Freeze the policies

Read `experiments/policy-comparison.md`. Do not change rules after viewing results. If a rule must change, create a new numbered policy and retain the old version.

### 2. Prepare a new case

Use the next sequential directory under `data/cases`.

Store:

- the permitted résumé snapshot;
- the exact job-post URL;
- the date the page was accessed;
- the job-post evidence needed to reproduce the decision.

Because live pages change, record the visible posting date, requirements, location, sponsorship, Apply status, employer activity, recruiter activity, and any contradictions at access time.

### 3. Create the hidden evaluator label before running the agent

An evaluator who has not seen the agent output must record:

- expected action;
- justification;
- evidence truth for mandatory requirements;
- evidence truth for project/work relevance;
- true or best-supported posting status;
- highest-cost plausible error.

Hide this section from the agent. Record the timestamp or commit showing that the label existed before prediction.

### 4. Run every frozen method on identical evidence

Run:

1. Baseline;
2. Policy 1;
3. Policy 2.

Do not provide one method with evidence unavailable to another. Save each raw action and explanation without editing.

### 5. Validate the action format

Each policy must return exactly one of:

- Apply
- Research
- Request human help
- Skip

For Research, save the precise question and the answer that would change the action. For Request human help, identify the judgment the candidate should discuss with a trusted person. Human help means advice to the candidate; the project does not supply a reviewer.

### 6. Reveal the label and score the result

After all predictions are locked, reveal the hidden label and record:

- predicted action;
- expected action;
- correct or incorrect;
- confusion-matrix cell;
- incorrect Apply quantity;
- incorrect Skip quantity;
- Research rate;
- human-help rate;
- decision cost;
- failure-condition name when incorrect.

### 7. Calculate evaluation measures

Report at least:

- multiclass confusion matrix;
- per-action precision;
- per-action recall;
- incorrect Apply quantity;
- incorrect Skip quantity;
- Research rate;
- human-help rate;
- total and mean decision cost.

Do not report accuracy or agreement as the only measure. If an action has no labeled examples, report its precision or recall as not available rather than zero.

### 8. Apply the provisional cost model

The current hypothetical values are:

- correct Apply or Skip: 0;
- Research: 3;
- Request human help: 2;
- incorrect Apply: 5;
- incorrect Skip: 100.

Label these values hypothetical. Recalculate results if the cost assumptions change. Do not claim the values represent real candidate preferences until validated.

### 9. Analyze failures

Examine at least five incorrect decisions. For each:

- identify the evidence pattern;
- explain why the action was wrong;
- assign a reusable failure-condition name;
- state the safer corrective rule;
- identify whether the error could cause a lost opportunity.

Retain incorrect cases. Do not silently edit labels or policy outputs to make results look better.

### 10. Run or append later cases

C17–C50 are already prepared as fictional, pre-labeled cases under `data/simulated-cases`. Run these without exposing `hidden-labels.md`. If more cases are later required, begin with C51 and do not modify C01–C50.

Future additions should deliberately include:

- expected Apply cases;
- clear Skip cases;
- resolvable Research cases;
- genuine human-judgment cases;
- recent and stale postings;
- contradictory posting signals;
- work authorization and location constraints;
- accepted-equivalent and transferability cases.

Do not present a deliberately balanced simulated action distribution as the natural distribution of real job opportunities.


## Known limitations

- The current batch does not yet meet the assignment's required evaluation-set size.
- No fully blinded cases are present.
- No evaluator-labeled Apply cases are present.
- Most cases select Research, creating action imbalance.
- Live job pages can change after access.
- The seven-day recency threshold and decision costs are hypothetical.
- Calibration cannot be measured because numerical beliefs were not saved for each case before label reveal.
- Candidate outcomes such as interview, assessment, or offer are not predicted by this pilot.
