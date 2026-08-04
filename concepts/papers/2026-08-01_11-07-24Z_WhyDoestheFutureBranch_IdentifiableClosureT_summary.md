# Summary: 2026-08-01_11-07-24Z_WhyDoestheFutureBranch_IdentifiableClosureTestsfor.md
Saved: 2026-08-03 21:27
Source: 2026-08-01_11-07-24Z_WhyDoestheFutureBranch_IdentifiableClosureTestsfor.md
Model: None

---

## Summary  
The paper tackles the ambiguity that arises in stochastic world models when predicting future observations: the same conditional distribution can stem from state aliasing or from random process noise after the full state is fixed, and ordinary transition data cannot resolve this. To address this, the authors introduce **ClosurePairs**, an interventional evaluation protocol that measures “why futures branch,” a source of uncertainty that standard forecast scores ignore. By reducing attribution errors across diverse dynamical conditions, ClosurePairs demonstrates that proper NLL‑based forecasts miss crucial dynamics.

## Key Contributions  
- [Introduces ClosurePairs, an interventional evaluation protocol that crosses compatible microstates with repeated exogenous disturbances.]  
- [Provides a two‑way variance decomposition identifying state aliasing, process noise, and their nonlinear interaction.]  
- [Shows that ClosurePairs reduces attribution MAE from 0.372 to 0.051 and sensing regret from 0.0138 to 0.0003 across 18 nonlinear Langevin conditions without changing NLL.]

## Methodology  
The authors adopt an interventional approach: they apply exogenous disturbances to a set of compatible microstates, enabling a two‑way variance decomposition that separates the contributions of state aliasing and process noise. The protocol is applied both in repeated‑disturbance settings (two‑way) and independent‑repeat scenarios where disturbances cannot be reused. Experiments include likelihood‑equivalent Gaussian systems, 18 nonlinear Langevin conditions, a pixel‑conditioned recurrent model, and a REFINE/BRANCH benchmark.

## Results  
On likelihood‑equivalent Gaussian systems, alias‑fraction error drops 15.96‑fold at identical test NLL. Across the 18 nonlinear Langevin conditions, attribution MAE falls from 0.372 to 0.051 and sensing regret from 0.0138 to 0.0003 while NLL remains unchanged. In a pixel‑conditioned recurrent model, ClosurePairs reduces in‑distribution MAE from 0.584 to 0.130 and out‑of‑distribution MAE from 0.630 to 0.170 over ten seeds. The REFINE/BRANCH test yields a total‑variance router accuracy of 66.48 ± 1.06 % versus ClosurePairs’ 99.99 ± 0.02 %, and NLL improves from –2.087 to –2.717 over five seeds.

## Significance  
The work reveals that conventional forecast scores cannot identify the reasons futures branch—state aliasing or process noise—leading to misattribution of uncertainty. ClosurePairs provides a precise measurement of this hidden information, which is essential for reliable forecasting and model calibration in stochastic physical systems.

## Related Concepts  
- Stochastic world models  
- Conditional future distribution  
- State aliasing  
- Process noise  
- Variance decomposition (two‑way)  
- Interventional evaluation  
- Likelihood‑equivalent testing  
- REFINE/BRANCH test  
- Marginal NLL  
- Sensory regret
