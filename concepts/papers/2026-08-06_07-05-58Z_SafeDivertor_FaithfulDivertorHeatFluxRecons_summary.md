# Summary: 2026-08-06_07-05-58Z_SafeDivertor_FaithfulDivertorHeatFluxReconstructio.md
Saved: 2026-08-06 20:33
Source: 2026-08-06_07-05-58Z_SafeDivertor_FaithfulDivertorHeatFluxReconstructio.md
Model: None

---

## Summary  
The paper tackles the challenge of reconstructing time‑resolved radial heat‑flux profiles from macroscopic plasma‑state signals during a discharge, bypassing the traditional post‑discharge infrared inversion that requires detailed material and geometry models. By leveraging physical priors embedded in the signal’s time‑frequency content, SafeDivertor provides an online, model‑free reconstruction of divertor heat flux, thereby improving safety monitoring and diagnostics for magnetic‑confinement fusion devices.

## Key Contributions  
- [Finding 1] The authors introduce **DivMPS2HF**, a multi‑source discharge dataset that serves as the benchmark for signal‑based heat‑flux reconstruction.  
- [Finding 2] They propose **SafeDivertor**, a task‑driven framework that integrates physical prior‑aware initialization, input perturbation to mitigate signal heterogeneity, spectral‑aware optimization exploiting time‑frequency priors, and progressive training to stabilize the learning process.  
- [Finding 3] Experimental results show that SafeDivertor outperforms all evaluated time‑series baselines across five performance metrics, establishing a new benchmark for this reconstruction task.

## Methodology  
SafeDivertor tackles signal‑based heat‑flux reconstruction by first grounding the model in physical constraints: radial distribution guidance is supplied via prior‑aware initialization that respects known plasma physics; input perturbation randomly samples multiple source channels to avoid over‑reliance on any single heterogeneous signal; a spectral‑aware loss function incorporates time‑frequency priors, encouraging preservation of transient dynamics while minimizing reconstruction error; finally, progressive training sequentially optimizes these complementary objectives, gradually increasing the complexity of the model and stabilizing convergence.

## Results  
On the DivMPS2HF benchmark, SafeDivertor achieves the lowest mean absolute error and highest correlation with ground‑truth heat flux across all five metrics (RMSE, MAE, Pearson r, RMSE‑MAE ratio, and reconstruction speed). It consistently outperforms conventional Fourier‑based baselines, deep‑learning baselines, and hybrid approaches, confirming its superiority in both accuracy and computational efficiency.

## Significance  
By enabling real‑time, model‑free heat‑flux estimation directly from plasma signals, SafeDivertor reduces the need for post‑discharge infrared inversion and eliminates reliance on device‑specific material models. This accelerates safety monitoring, facilitates rapid diagnostics during operation, and supports adaptive control strategies that can mitigate divertor overheating before damage occurs.

## Related Concepts  
- Divertor heat flux  
- Plasma state signals (e.g., electron density, temperature)  
- Time‑frequency analysis  
- Prior‑aware initialization  
- Input perturbation / channel diversity  
- Spectral‑aware reconstruction optimization  
- Progressive training  
- Multi‑source dataset (DivMPS2HF)
