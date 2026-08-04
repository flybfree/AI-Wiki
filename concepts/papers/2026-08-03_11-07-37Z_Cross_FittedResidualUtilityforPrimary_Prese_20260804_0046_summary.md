# Summary: 2026-08-03_11-07-37Z_Cross_FittedResidualUtilityforPrimary_PreservingCo.md
Saved: 2026-08-04 00:46
Source: 2026-08-03_11-07-37Z_Cross_FittedResidualUtilityforPrimary_PreservingCo.md
Model: None

---

## Summary  
The paper tackles the post‑inference decision problem in automatic modulation classification, where a cognitive receiver must decide when heterogeneous evidence justifies overriding a trusted default prediction. It proposes cross‑fitted residual utility together with a primary‑preserving cognitive decision policy that balances representation accuracy against cognitive utility. The approach integrates structured KAN‑Fourier classifiers with neural and non‑neural candidate models while learning candidate‑specific residuals from out‑of‑fold predictions. A disjoint validation split freezes action thresholds, approved transitions, conditional routes, and a unified risk mask for evaluation.

## Key Contributions  
- [Finding 1] Cross‑fitted residual utility provides a data‑driven measure of the benefit of overriding default predictions, learned from train‑split out‑of‑fold predictions.  
- [Finding 2] Primary‑preserving cognitive decision policy ensures that only when evidence justifies it does the receiver deviate from the trusted model, preserving primary prediction integrity.  
- [Finding 3] The complete system (classifier + utility + frozen policy) yields statistically significant accuracy gains across RMLA, RMLB, and HISAR with all paired confidence intervals above zero.

## Methodology  
The authors employ a structured KAN‑Fourier classifier to generate default probability predictions. Neural and non‑neural candidate models produce observable evidence. Residual utilities are computed via cross‑fitting using out‑of‑fold predictions from train splits. A disjoint validation split freezes action thresholds, approved transitions, conditional routes, and a unified risk mask for held‑out evaluation. The policy selects overrides based on residual utility while respecting primary‑preserving constraints.

## Results  
On RMLA overall accuracy rises from 63.632 % to 66.332 %; on RMLB it improves from 65.161 % to 66.168 %; on HISAR it increases from 77.769 % to 79.867 %. Paired bootstrap and Holm‑corrected McNemar analyses confirm the gains are significant across all conditions. Frozen‑policy stress tests under carrier‑frequency offset, I/Q imbalance, and synthetic Rayleigh/Rician fading show positive gains in every one of the eleven scenarios.

## Significance  
This work bridges representation learning with cognitive utility, offering a principled framework for when to trust or override automated decisions. By integrating residual utility with a primary‑preserving policy, the system improves real‑world performance and reliability of automatic modulation classification, reducing unnecessary overrides while preserving core prediction accuracy.

## Related Concepts  
Automatic Modulation Classification (AMC), KAN‑Fourier classifiers, out‑of‑fold predictions, residual utility, primary‑preserving policies, cross‑fitting, risk masking, cognitive decision correction, Monte Carlo dropout, bootstrap analysis, McNemar test.
