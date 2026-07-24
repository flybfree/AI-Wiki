# Summary: 2026-07-23_15-06-57Z_Cycle_ConsistentandUncertainty_AwareNeuralSurrogat.md
Saved: 2026-07-24 03:00
Source: 2026-07-23_15-06-57Z_Cycle_ConsistentandUncertainty_AwareNeuralSurrogat.md
Model: None

---

## Summary  
The paper proposes a cycle‑consistent and uncertainty‑aware neural surrogate for predicting edge plasma fields in tokamaks. It combines a conditional U‑Net forward model with an optimization‑based inverse method that recovers control parameters without ground‑truth labels. The approach enables rapid real‑time predictions, parameter recovery, and quantified uncertainty quantification. The surrogate attains high accuracy while delivering full 2D outputs in milliseconds.

## Key Contributions  
- [Finding 1] Cycle‑consistent neural surrogate with forward model and inverse method recovers all five control parameters with Pearson r ≥ 0.97.  
- [Finding 2] Ensemble MLP predicts electron temperature/density profiles at the outboard midplane and divertor targets with uncertainty estimates that flag needed simulations.  
- [Finding 3] The model achieves normalized RMSE < 2.6%, Pearson correlation > 0.95, and cycle‑consistency R² up to 0.99 while delivering predictions in milliseconds.

## Methodology  
The authors built a conditional U‑Net forward network that maps five control parameters to two‑dimensional plasma fields on the SOLPS‑ITER mesh. An optimization‑based inverse method enforces consistency between forward and inverse outputs using only the frozen forward network, providing an inference routine with no external labels. Additionally, an ensemble of multilayer perceptrons supplies predictions for electron temperature and density at key locations, each accompanied by uncertainty estimates; a k‑d tree warm start is used to accelerate database completion.

## Results  
The forward model achieves normalized root‑mean‑square errors below 2.6% and Pearson correlations above 0.95 across all fields. Cycle‑consistency regularization lifts the average cyclical R² from 0.59 to 0.99 without degrading accuracy, enabling recovery of core fueling rate with r ≥ 0.97. A k‑d tree warm start yields a database completion rate above 95% versus ~30% cold‑start failures. The model predicts full 2D fields in milliseconds—five to six orders faster than SOLPS‑ITER.

## Significance  
This work bridges the gap between high‑fidelity edge simulations and real‑time control, allowing rapid parameter scans, uncertainty analysis, and digital twins for tokamak operation. By providing a reliable inverse surrogate, it reduces reliance on costly offline simulations, supports optimization, and enhances safety through early detection of simulation gaps.

## Related Concepts  
- Conditional U‑Net forward model  
- Optimization‑based inverse method (cycle consistency)  
- Ensemble MLP with uncertainty quantification  
- k‑d tree warm start for database completion  
- SOLPS‑ITER mesh representation
