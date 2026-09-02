# Frozen Policy Comparison

Status: rules frozen before comparative scoring

These rules are provisional and intended for pilot evaluation. They do not predict interviews, offers, or opportunity value.

## Shared inputs

Each method receives the same candidate résumé and exact job-post evidence. Missing evidence is not treated as confirmed evidence, and résumé fabrication is prohibited.

## Baseline — Binary Match Rule

Purpose: provide a simple comparison system without explicit uncertainty management.

1. Check only mandatory résumé-to-job evidence.
2. If every clearly mandatory requirement is shown, output **Apply**.
3. Otherwise output **Skip**.
4. Do not evaluate posting age or reliability.
5. Do not output Research or Request human help.

This baseline is intentionally limited. It shows what is gained or lost by adding uncertainty-aware actions and posting checks.

## Policy 1 — Current Four-Action Rule

Evaluate three checks:

1. mandatory requirements;
2. truthful project/work evidence relevant to the role;
3. posting recency and reliability, with a posting considered recent only when posted within seven days.

Mark each check Pass, Fail, or Unclear and apply the existing rule order:

1. Hard stop: Skip when a clearly mandatory requirement is unmet and no truthful omitted evidence, accepted equivalent, or research result could change the conclusion.
2. If any decision-relevant check is Unclear, Research.
3. Apply only when all three checks Pass.
4. Skip when mandatory requirements and project/work evidence both Fail.
5. Request human help when posting reliability Fails and exactly one of the other two checks Passes.
6. Research when exactly one check Fails and an answer could change the action.
7. If research cannot resolve a judgment call, Request human help.
8. Otherwise, Request human help.

## Policy 2 — Separated Recency and Active-Status Rule

Purpose: test whether separating age from current hiring evidence reduces unnecessary Research decisions.

Evaluate four checks:

1. mandatory requirements;
2. truthful project/work evidence;
3. posting recency: within seven days, older than seven days, or unknown;
4. active-status reliability: strong, weak, contradictory, or unavailable.

Strong active-status evidence requires at least two current signals from the exact listing, such as:

- Apply control currently available;
- employer marked actively hiring;
- recruiter recently active;
- recent repost or update;
- explicit application deadline still open;
- employer confirmation that applications are progressing.

Rules:

1. Apply the same hard-stop rule as Policy 1.
2. Apply when mandatory requirements and project/work evidence Pass and either:
   - the posting is within seven days with no reliability contradiction; or
   - it is older than seven days but has at least two strong, non-contradictory active-status signals.
3. Research when a missing factual answer could change the action, including unknown eligibility, work authorization, location feasibility, experience equivalence, or vacancy status.
4. Request human help when the unresolved issue is a transferability or equivalence judgment that factual research cannot settle.
5. Skip when mandatory requirements and project/work evidence both Fail, or a hard-stop requirement is conclusively unmet.
6. If active-status signals conflict, Research rather than Apply.

Policy 2 does not assume that an Apply button alone proves a vacancy is active.

## Frozen comparison rules

- Use the same case evidence for all methods.
- Save every method's action for every case.
- Do not change a rule after seeing comparative results; create a new numbered policy instead.
- Report action distribution, agreement, human-review rate, decision cost, and error types—not accuracy alone.
- The current 16 cases are a development pilot and lack independently stored pre-run labels; results must be described as provisional.

