# Summary: 2026-07-23_15-06-57Z_Cycle_ConsistentandUncertainty_AwareNeuralSurrogat.md
Saved: 2026-07-24 03:05
Source: 2026-07-23_15-06-57Z_Cycle_ConsistentandUncertainty_AwareNeuralSurrogat.md
Model: None

---

## Summary  
The paper proposes a cycle‑consistent and uncertainty‑aware neural surrogate for predicting edge plasma fields in tokamaks, enabling fast parameter scans and real‑time control without requiring ground‑truth labels. It combines a conditional U‑Net forward model with an optimization‑based inverse method that enforces consistency between forward and inverse predictions. An ensemble of MLPs also predicts electron temperature and density profiles at the outboard midplane and divertor targets, providing quantified uncertainties. The approach achieves high accuracy (RMSE < 2.6%, Pearson > 0.95) and can recover all five control parameters.

## Key Contributions  
- [Finding 1] Introduces a cycle‑consistent neural surrogate that recovers input control parameters from predicted plasma fields.  
- [Finding 2] Provides uncertainty estimates for plasma profiles, guiding where additional simulations are needed.  
- [Finding 3] Achieves sub‑second inference speed with >95 % database completion rate using a warm‑start k‑d tree.

## Methodology  
The authors built a conditional U‑Net trained on SOLPS‑ITER simulations that maps five control parameters to two‑dimensional field values. An inverse method uses gradient descent to enforce cycle consistency, while an ensemble of MLPs predicts temperature and density profiles with Monte‑Carlo uncertainty bounds. A k‑d tree stores the model for fast lookup; warm starts improve completion rates dramatically.

## Results  
The forward model yields normalized RMSE 2.6% and Pearson correlations >0.95 across all fields. Cycle‑consistency raises average cyclical R² from 0.59 to 0.99 without degrading accuracy, enabling recovery of the core fueling rate with r ≥ 0.97. Database completion exceeds 95 %, versus ~30 % when cold‑started.

## Significance  
This surrogate replaces slow edge simulations, allowing real‑time control, high‑fidelity parameter sweeps, and uncertainty‑aware decision making in tokamak operation.

## Related Concepts  
conditional U‑Net, inverse modeling, cycle consistency, Monte‑Carlo uncertainty quantification, k‑d tree warm start, SOLPS‑ITER, digital twin, plasma edge physics.
