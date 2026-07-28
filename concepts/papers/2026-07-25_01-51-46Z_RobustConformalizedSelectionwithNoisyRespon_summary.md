# Summary: 2026-07-25_01-51-46Z_RobustConformalizedSelectionwithNoisyResponses.md
Saved: 2026-07-27 23:30
Source: 2026-07-25_01-51-46Z_RobustConformalizedSelectionwithNoisyResponses.md
Model: None

---

## Summary  
The paper tackles the problem of selecting high‑quality candidates from large datasets when calibration data contain noisy responses, a scenario that invalidates existing conformal selection methods. It introduces Robust Conformalized Selection (RCS), a unified framework that guarantees valid false discovery rate (FDR) control even under general label contamination. RCS leverages class‑specific conditioning to transform intractable label noise into localized covariate shift and provides an empirical‑Bayes estimate of the number of false selections. The method is shown to be asymptotically FDR‑controlling, power‑optimal, and robust across diverse applications.

## Key Contributions  
- [Finding 1] RCS achieves valid FDR control under general label contamination by conditioning on each class separately.  
- [Finding 2] It provides an empirical‑Bayes‑type estimate of the number of false selections that is optimal in terms of power.  
- [Finding 3] The method works both for selecting candidates with true labels and those exceeding response thresholds, including a randomized response model instantiation.

## Methodology  
The authors first reframe typical conformal selection tasks—such as reliable labeling or drug‑discovery candidate selection—as problems of choosing items whose predicted label exceeds a threshold or whose response value surpasses a cut‑off. They treat label noise as covariate shift that is confined to each class, allowing the problem to be decomposed into independent sub‑problems. By conditioning on each class separately, RCS derives a conditional empirical‑Bayes estimator for the number of false selections. This estimator yields an FDR bound that holds asymptotically and is calibrated to maximize power while respecting the desired false discovery rate.

## Results  
Theoretical analysis establishes asymptotic FDR control with confidence level 1 – δ, demonstrating that RCS’s false selection rate does not exceed the prescribed threshold as sample size grows. Empirically, on simulated datasets with controlled contamination rates (up to 30 % label noise) and real‑world benchmarks such as medical imaging classification and NLP intent detection, RCS outperforms standard conformal methods in both power (fewer false rejections) and FDR control (lower actual false discoveries). The randomized response model instantiation further confirms robustness when responses are generated via a Bernoulli mechanism with unknown probability.

## Significance  
RCS is significant because it provides the first framework that maintains reliable selection performance when calibration data are contaminated, which is common in practice. By decoupling label noise across classes and using covariate‑adjusted estimation, RCS enables trustworthy candidate selection in drug discovery, scientific literature mining, and large language model alignment—domains where false discoveries can have costly consequences.

## Related Concepts  
- Conformal selection  
- False discovery rate (FDR) control  
- Covariate shift  
- Empirical‑Bayes estimation  
- Randomized response model  
- Label contamination
