# Summary: 2026-07-22_04-47-30Z_MachineCanAutomaticallyDiscoverParametricFunctions.md
Saved: 2026-07-24 01:26
Source: 2026-07-22_04-47-30Z_MachineCanAutomaticallyDiscoverParametricFunctions.md
Model: None

---

## Summary  
The paper proposes an automated approach to discover parametric functions that model binned data typical of high‑energy physics (HEP) analyses. By replacing the manual trial‑and‑error process with a machine‑driven symbolic regression algorithm, the authors aim to generate candidate functional forms directly from raw data without any prior knowledge of the expected shape. The SymbolFit package integrates this search with uncertainty modeling, enabling reliable selection among many possible fits. Their experiments on CMS and ATLAS Run 2 dijet spectra show that the system can rediscover well‑known dijet functions used in published searches with high confidence.

## Key Contributions  
- [Finding 1] A fully automated symbolic regression pipeline (SymbolFit) that explores a large function space to locate parametric models matching HEP binned data.  
- [Finding 2] Uncertainty quantification for each candidate fit, allowing the selection of the most statistically robust model with χ²/NDF ≈ 1.  
- [Finding 3] Successful rediscovery of previously published dijet functions (the “dijet” and “UA2” functions) across multiple independent runs.

## Methodology  
The authors built a symbolic regression engine that treats each binned spectrum as a data set to be approximated by a parametric function. The search is seeded with 560 random configurations, generating up to 1 000 candidate functions per run. Each candidate’s goodness‑of‑fit is evaluated using χ²/NDF, and the best‑performing models are retained while others are discarded. Uncertainty around each fit is modeled via bootstrapping of the seed runs, providing a confidence interval for the discovered function.

## Results  
Across 560 seeded runs across seven simple fit configurations, the SymbolFit algorithm achieved χ²/NDF ≈ 1 for all models, indicating excellent agreement with the data. Of the 111 runs that successfully identified the dijet and UA2 functions, these were rediscovered with high confidence intervals, confirming their validity as published functional forms.

## Significance  
This work eliminates the subjective, iterative fitting process that has long been a bottleneck in HEP analyses, offering a reproducible, data‑driven method to propose candidate models. By providing uncertainty estimates, SymbolFit supports informed decision‑making and reduces the risk of selecting suboptimal fits, thereby accelerating discovery and improving the reliability of experimental results.

## Related Concepts  
- Symbolic regression  
- Binned data modeling in HEP  
- χ²/NDF goodness‑of‑fit metric  
- Uncertainty quantification via bootstrapping  
- Automated function discovery
