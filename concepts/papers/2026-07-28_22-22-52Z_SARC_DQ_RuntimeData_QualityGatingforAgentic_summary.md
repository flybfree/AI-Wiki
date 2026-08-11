# Summary: 2026-07-28_22-22-52Z_SARC_DQ_RuntimeData_QualityGatingforAgenticAI_Sile.md
Saved: 2026-07-29 21:33
Source: 2026-07-28_22-22-52Z_SARC_DQ_RuntimeData_QualityGatingforAgenticAI_Sile.md
Model: None

---

## Summary  
The paper introduces SARC‑DQ, a runtime data‑quality gating mechanism that isolates “silent evidence defects” in agentic AI systems where metadata‑borne anomalies—such as stale prices or superseded records—lead to costly actions without triggering any quality flags. By treating evidence integrity as an independent system axis rather than a model capability issue, the authors demonstrate that downstream remediation can fully recover losses only when it is placed after the inference step and covers the relevant predicates. Their work reveals that even highly capable models across a wide price spectrum exhibit a flat defect‑conversion rate of roughly 60 % with no measurable skepticism (AUC ≤ 0.5). The contribution lies in providing a deterministic analysis pipeline that links these observations to an analytical form derived from the task’s decision geometry.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Runtime data‑quality gating can detect silent evidence defects that cause agents to act on stale or superseded metadata, resulting in actions with no quality flags and minimal doubt markers.  
- [Finding 2] Model capability does not translate into reduced defect conversion rates; the 60 % conversion rate persists across four model tiers spanning a 15× price difference, yielding an AUC ≤ 0.5 on detection signals.  
- [Finding 3] Downstream‑only remediation recovers full loss only for predicates that are covered by the gating predicates, leaving uncovered defects untouched.

## Methodology  
The authors built a priced replenishment benchmark in which metadata‑borne defects were injected into the data stream while preserving payload integrity. Agents retrieved evidence without awareness of freshness or provenance issues and performed actions accordingly. To quantify detection performance, they constructed a model‑free oracle based on the task’s decision geometry, mapping measured conversion rates to an analytical form with a mean absolute error (MAE) of 0.015 and covering 15 out of 16 outcome cells. The gating mechanism was implemented as a post‑inference predicate check that flags only when downstream remediation can be applied.

## Results  
Across the benchmark, agents silently converted injected metadata defects into costly actions about 60 % of the time, with zero quality‑flag detections and skepticism markers at chance (AUC ≤ 0.5). The flat conversion rate held constant across model tiers differing by roughly fifteenfold in inference price. The analytical oracle derived from decision geometry achieved MAE = 0.015 and Pearson’s r = 0.876, with interval coverage of 15/16 cells, confirming the analytical form. Downstream‑only remediation fully recovered losses for covered predicates but left uncovered defects unmitigated.

## Significance  
This research underscores that data‑quality is a distinct system axis from model capability; merely improving an agent’s inference does not reduce its susceptibility to metadata‑borne defects. The findings advocate for strategic placement of runtime gating and remediation, emphasizing predicate coverage as the primary lever for mitigating downstream costs. By providing a deterministic analysis pipeline (code at https://github.com/besanson/dqSarc), the work offers a practical framework for enterprises to evaluate and enforce evidence integrity in agentic workflows.

## Related Concepts  
- Runtime data‑quality gating  
- Metadata‑borne defects  
- Silent evidence defects  
- Incompetence shield (agentic AI)  
- Downstream remediation  
- Evidence integrity as a systems axis  
- Decision geometry and analytical modeling
