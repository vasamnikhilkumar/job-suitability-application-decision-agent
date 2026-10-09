# Reddit Follow-up Draft (Not Yet Posted)

I tested the job-suitability agent discussed earlier on 500 reproducible simulated cases. The original active policy sent every case to human review because review was effectively free in its loss model. A revised policy charges review capacity and selects evidence by expected information gain per generalized cost. It stopped blanket escalation, but did not outperform the full-information policy on every metric.

For practitioners: is a fixed deferral cost defensible, or should review cost rise with queue length? What held-out test would convince you that the revised stopping rule is not tuned to this simulation?
