# Summary: 2026-07-24_05-56-00Z_FromPerturbationCorrectiontoGeometry_AwareSampling.md
Saved: 2026-07-26 21:38
Source: 2026-07-24_05-56-00Z_FromPerturbationCorrectiontoGeometry_AwareSampling.md
Model: None

---

## Summary  
Long‑tailed learning suffers from a dual problem: head classes dominate the training data while under‑represented tail classes converge to sharp loss regions, limiting generalization.  The authors propose **Sharpness‑Guided Equilibrium Sampling (SGS)**, which treats the sampling distribution as an active control variable that dynamically balances class exposure and optimisation geometry without extra perturbations or backward passes.  

## Key Contributions  
- [Finding 1] SGS introduces a sampling‑side mechanism that adjusts mini‑batch probabilities using only cumulative class counts and EMA sharpness estimates, avoiding per‑class perturbations.  
- [Finding 2] The authors provide a continuous‑time stochastic differential equation and a PAC‑Bayes analysis showing how frequency‑sharpness feedback can steer training toward balanced flat loss landscapes.  
- [Finding 3] Empirically, SGS‑SAM improves tail accuracy by **10.85** points on CIFAR‑100 LT (vs Focal‑SAM) and overall by **3.56** points, with only a **1.02×** training‑time overhead compared to vanilla SAM.  

## Methodology  
The authors model the sampling process as an active control variable in a continuous‑time stochastic differential equation.  The drift of this SDE is guided by two streams of information: (i) cumulative class counts that increase the probability of rare classes, and (ii) EMA sharpness estimates derived from standard SAM updates that penalise large loss changes for those classes.  New sampling probabilities are computed to up‑weight under‑sampled classes while suppressing classes whose perturbations would cause excessive loss spikes, all without additional forward passes or class‑specific perturbations.  

## Results  
On CIFAR‑100 LT with an imbalance ratio of 100, SGS‑SAM outperforms Focal‑SAM by **10.85** points in tail accuracy and **3.56** points overall; training time is only **1.02×** that of vanilla SAM.  On ImageNet‑LT, it improves ImbSAM by **6.59** points on tail classes and **1.20** points overall.  

## Significance  
This work establishes a sampling‑driven route to loss‑landscape control, enabling future long‑tailed methods to jointly regulate data exposure and optimisation geometry rather than treating them as separate fixed components.  By coupling frequency feedback with sharpness awareness, SGS demonstrates that geometry can be actively shaped through the very way data are sampled.  

## Related Concepts  
- Long‑tailed learning (head vs. tail classes)  
- Sharpness‑aware minimization (SAM)  
- Focal loss  
- Exponential moving average (EMA) sharpness estimates  
- Stochastic differential equations (continuous‑time SDE)  
- PAC‑Bayes analysis for sampling control
