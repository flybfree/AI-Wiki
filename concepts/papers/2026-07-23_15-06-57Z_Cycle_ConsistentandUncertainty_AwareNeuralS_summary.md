# Summary: 2026-07-23_15-06-57Z_Cycle_ConsistentandUncertainty_AwareNeuralSurrogat.md
Saved: 2026-07-24 02:48
Source: 2026-07-23_15-06-57Z_Cycle_ConsistentandUncertainty_AwareNeuralSurrogat.md
Model: None

---

## Summary  
The paper proposes a cycle‑consistent and uncertainty‑aware neural surrogate for predicting tokamak edge plasma fields, replacing the slow SOLPS‑ITER simulations that are required for parameter scans and real‑time control. By integrating a conditional U‑Net forward model with an optimization‑based inverse method that enforces consistency without ground‑truth labels, the approach enables fast recovery of input parameters and quantifies prediction uncertainty. The surrogate achieves sub‑percent accuracy across five key control variables while operating in milliseconds.

## Semantic links
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 2 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-20_16-27-56Z_IsaacSim_to_Real_ReinforcementLearningbased_summary.md|Summary: 2026-07-20_16-27-56Z_IsaacSim_to_Real_ReinforcementLearningbasedLocomot.md]] — 3 title terms overlap; 1 backlink; 11 summary/topic terms overlap
- [[concepts/papers/2026-08-01_11-12-39Z_Uncertainty_guidedactivelearningforsurrogat_summary.md|Summary: 2026-08-01_11-12-39Z_Uncertainty_guidedactivelearningforsurrogatepredic.md]] — 3 title terms overlap; 12 summary/topic terms overlap; semantic match 0.11

## Key Contributions  
- Introduces a cycle‑consistent neural surrogate that recovers all five control parameters from edge plasma fields without external supervision.  
- Provides calibrated Monte‑Carlo uncertainty estimates for electron temperature and density profiles, guiding where additional simulations are needed.  
- Demonstrates sub‑percent prediction errors (RMSE < 2.6%) and near‑perfect parameter recovery (Pearson r ≥ 0.97) while improving cyclical R² to 0.99.

## Methodology  
The authors train a conditional U‑Net on SOLPS‑ITER simulations that maps five control parameters—fueling rate, divertor power, and others—to two‑dimensional plasma fields defined on the mesh. An inverse method solves for these parameters using fixed forward predictions and enforces cycle consistency through an optimization loop. A separate multilayer perceptron ensemble predicts electron temperature and density profiles at the outboard midplane and divertor targets, generating uncertainty estimates via Monte‑Carlo sampling. Cycle‑consistency regularization is applied during training to reinforce the relationship between forward and inverse outputs.

## Results  
The surrogate attains normalized root‑mean‑square errors below 2.6 % and Pearson correlations above 0.95 for all fields. Cyclical R² rises from 0.59 to 0.99, enabling reliable recovery of the core fueling rate (r ≥ 0.97). Using a k‑d tree warm start, database completion exceeds 95 %, compared with roughly 30 % failure when cold‑started. Full 2D predictions are generated in milliseconds using ~4 × 10⁶ parameters, which is five to six orders of magnitude faster than SOLPS‑ITER.

## Significance  
This work enables real‑time control, high‑fidelity parameter sweeps, and uncertainty analysis for edge plasmas, accelerating tokamak operation and design. The surrogate serves as a digital twin that can be updated online, supporting optimization loops and rapid response to operational changes without prohibitive simulation time.

## Related Concepts  
- Neural surrogates  
- Cycle consistency  
- Inverse modeling  
- Uncertainty quantification  
- U‑Net architecture  
- SOLPS‑ITER simulations  
- k‑d tree warm start  
- Digital twin
