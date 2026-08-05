# Summary: 2026-07-26_14-02-46Z_NoFreeLunchinFlowSurrogatesunderTime_VaryingBounda.md
Saved: 2026-07-27 21:29
Source: 2026-07-26_14-02-46Z_NoFreeLunchinFlowSurrogatesunderTime_VaryingBounda.md
Model: None

---

## Summary  
The paper investigates whether flow surrogates that are validated on a simple regime can be transferred to more complex, time‑varying flows in semiconductor manufacturing and fluid dynamics. It compares eight surrogate models across two transient flows—three‑dimensional slurry film from chemical‑mechanical planarisation (CMP) and the two‑dimensional Karman vortex street behind a cylinder—under evolving boundary conditions that emulate process startup. The study shows that no single architecture dominates both regimes, highlighting the need to match surrogate design to the specific dynamical character of each flow. Evaluation reveals faster query response but limited transfer value without appropriate validation.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- [Finding 1] No single surrogate model wins both the CMP slurry film and KVS wake studies; performance depends on regime‑specific dynamics.  
- [Finding 2] Autoregressive latent models (DeepONet) preserve shedding power in time‑varying wake flows, while direct one‑shot full‑field models excel for boundary‑driven shear stress capture.  
- [Finding 3] Pointwise RMSE misidentifies the best model because it ignores field structure and timing; better metrics must resolve failure modes.

## Methodology  
The authors built eight surrogates that vary between learning the full velocity field or a latent representation, and between predicting trajectories in one shot or step by step. All models were trained on high‑fidelity simulations of both flows using a shared evaluation pipeline that queries each surrogate against a finite‑element solver thousands to ten‑thousands times, measuring response speed and accuracy.

## Results  
In the CMP film, a one‑shot full‑field model reconstructs cumulative wall shear stress with 3.2 % relative error. In the KVS wake, DeepONet retains about 96 % of the shedding power compared to near‑zero for direct or one‑shot models. Training cost is high (queries needed before benefit), but surrogate queries are orders of magnitude faster once trained.

## Significance  
The work demonstrates that flow surrogates must be tailored to the underlying dynamical regime and validated with failure‑mode‑resolved metrics; otherwise they offer no transfer advantage despite speed gains. This insight guides the selection and evaluation of surrogate models in engineering applications where time is critical but training resources are limited.

## Related Concepts  
Flow surrogates, time‑varying boundary conditions, latent representation learning, autoregressive deep networks (DeepONet), field reconstruction, surrogate model validation, transient flows, CMP process, Karman vortex street, pointwise RMSE.
