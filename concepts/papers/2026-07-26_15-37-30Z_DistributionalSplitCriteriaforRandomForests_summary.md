# Summary: 2026-07-26_15-37-30Z_DistributionalSplitCriteriaforRandomForests_Extens.md
Saved: 2026-07-27 21:29
Source: 2026-07-26_15-37-30Z_DistributionalSplitCriteriaforRandomForests_Extens.md
Model: None

---

## Summary  
The paper proposes distributional split criteria for random forests that compare the full conditional response distribution in candidate children rather than relying on mean‑based CART splits, aiming to improve robustness and capture non‑location structure. It implements a suite of such criteria within an honest‑forest framework based on maximum mean discrepancy (MMD), frequency selection, sliced Wasserstein, etc., and studies them empirically across synthetic and real data. The main contribution is a systematic extension of distributional splitting with empirical findings on when they help versus hurt performance. The work also provides the open‑source drforest library for efficient implementation.

## Key Contributions  
- [Finding 1] Among distributional criteria isotropic MMD already performs close to best, while anisotropic, adaptive‑frequency, sliced‑Wasserstein extensions and post‑hoc shrinkage do not systematically improve it.  
- [Finding 2] Mean‑based CART splitting remains the robust default and wins many cells across scalar tabular regression experiments.  
- [Finding 3] Multivariate responses are the regime where distributional splitting clearly benefits, especially on pure‑dependence copulas where energy scores separate criteria despite marginal CRPS not doing so.

## Methodology  
The authors replace mean‑based CART with criteria that compare full conditional response distributions using an honest‑forest implementation. They consider isotropic random‑Fourier‑feature MMD, anisotropic diagonal‑bandwidth MMD, adaptive per‑split frequency selection, and a non‑kernel sliced‑Wasserstein criterion, plus post‑hoc kernel‑mean shrinkage of forest weights. Experiments are conducted via paired‑seed comparisons across synthetic quantile mechanisms, real univariate benchmarks (California housing), multivariate synthetic/real responses, and multivariate pure‑dependence copulas.

## Results  
Isotropic MMD is already near optimal among distributional criteria; extensions rarely outperform it. Mean‑based CART retains superiority in scalar regression cells. Distributional splitting excels only on multivariate data with non‑location structure, particularly pure‑dependence copulas where energy scores separate criteria. The honest forest and paired‑comparison harness enable exhaustive sweep of criterion space efficiently.

## Significance  
This work clarifies that distributional splitting is not universally superior; it adds value only when non‑location structure exists and can be estimated. It also demonstrates practical trade‑offs between theoretical improvements and computational cost, guiding practitioners to choose the right split strategy for their data regime.

## Related Concepts  
- Distributional random forests  
- Mean‑based CART splitting  
- Honest forest implementation  
- Maximum mean discrepancy (MMD) as a distribution similarity measure  
- Wasserstein distance and sliced Wasserstein criterion  
- CRPS (continuous relative rank probability score)
