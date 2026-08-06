# Summary: 2026-08-05_14-22-23Z_WhenSharedRolloutsFailinDefensiveDrivingEvaluation.md
Saved: 2026-08-05 20:36
Source: 2026-08-05_14-22-23Z_WhenSharedRolloutsFailinDefensiveDrivingEvaluation.md
Model: None

---

## Summary  
The paper investigates why shared rollouts can degrade defensive driving evaluation scores by propagating reference‑conditioned forgiveness errors. It audits NAVSIM v2.2 scoring under a documented‑stack condition, revealing that numerical instability causes blind probes to outperform human replay and PDM‑Closed. The authors propose an audit protocol requiring score basis disclosure, stack transparency, blind probe testing, overwrite reporting, and rollout stability checks before using scores for claims.

## Key Contributions  
- Finding 1: Shared reference failures from unstable rollouts cause compliance credit inflation.  
- Finding 2: Blind probes (Ignore‑All, route‑aware actor‑blind) outperform human replay and PDM‑Closed on the NAVSIM test set.  
- Finding 3: Rolling back to a fixed solver resolves divergence, indicating numerical instability is the trigger.

## Methodology  
The authors implemented NAVSIM v2.2 original scene single‑stage scoring, introduced a documented‑stack condition that fixes rollout transformation, re‑ran blind probes and compared against human replay and PDM‑Closed on a 12,146‑token navtest split; they also performed stack control experiments with same‑source dependencies to isolate numeric behavior.

## Results  
On the full test set, Ignore‑All (blind) and route‑aware actor‑blind probes achieved higher NAVSIM scores than human replay and PDM‑Closed. A 32‑token diagnostic set reproduced rollout divergence; replacing only the solver restored blind‑last ordering while keeping forgiveness enabled.

## Significance  
The findings reveal that numerical instability in score computation can masquerade as policy superiority, undermining trust in defensive driving metrics; the audit protocol offers a safeguard for reliable evaluation.

## Related Concepts  
NAVSIM scoring, rollout transformation, reference‑conditioned forgiveness, blind probes, stack control, numerical stability, compliance credit.
