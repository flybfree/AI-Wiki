# Summary: 2026-08-08_04-41-36Z_WhenIsBenchmarkContaminationDetectable_Information.md
Saved: 2026-08-10 22:49
Source: 2026-08-08_04-41-36Z_WhenIsBenchmarkContaminationDetectable_Information.md
Model: None

---

## Summary  
The paper tackles the problem of distinguishing between a clean benchmark and one that has been contaminated by an unknown fraction α of test items seen during training, while also accounting for limited audit power. It formalizes detectability as α·ρ·√m where ρ measures behavioral separability and derives a distribution‑free lower bound on α using matched clean/seen controls. The authors introduce a power‑calibrated audit framework that estimates scalar detector efficacy ef and variance, bounds ef by ρ, and provides a two‑stage planner that abstains when probe transport is absent. Empirical work shows that calibration efficacy predicts held‑out performance with high R² but that a naïve Gaussian budget miscalibrates at small sample sizes.

## Key Contributions  
- Formalization of detectability as α·ρ·√m and derivation of a distribution‑free lower bound on the contamination fraction α using chi‑squared divergence between P₀ and P₁.  
- Development of a power‑calibrated audit protocol that uses matched controls to estimate efficacy ef, variance Var₀(f), and constructs a scalar detector bounded by ρ, together with a two‑stage planner that abstains when probe transport is absent.  
- Empirical evidence that fidelity‑only Gaussian budgets misclassify 9 out of 9 gate‑passing channels at small sample sizes, while a calibrated budget with simulation yields uniform conservatism.

## Methodology  
The authors model the behavioral channel as Qα = (1−α)P₀ + αP₁ and compute second‑moment statistics to obtain efficacy ef = |E₁f − E₀f|/√Var₀(f) ≤ ρ, where ρ² = χ²(P₁||P₀). They propose using matched clean and seen controls before the audit to estimate ef and Var₀(f), yielding a scalar detector that is interpretable as an efficacy‑budget. A distribution‑free certificate for α is derived from a sample‑split analysis, independent of any orientation assumption. Experiments employ exact‑permutation channels, frozen calibration efficacy, and paired injection studies to validate the theoretical bounds.

## Results  
Theoretically, detectability scales with √m and is proportional to α·ρ, while scalar detectors cannot exceed ρ in magnitude. Empirically, across six exact‑permutation channels, frozen calibration efficacy explains held‑out power curves with R² = 0.83–0.98. However, a Gaussian budget that only uses fidelity miscalibrates at small sample sizes (9/9 failures). A predeclared two‑stage planner that simulates the deployed test repairs budgets uniformly conservatively and abstains when probe transport is absent; its certificate is valid but vacuous at audit scale. Paired injection studies recover the mechanism ordering verbatim, explaining apparent answer‑only signals as baseline drift.

## Significance  
This work provides a principled way to detect benchmark contamination that separates clean benchmarks from limited audit power, enabling interpretable non‑rejection via efficacy and validity gates. It improves calibration of Gaussian budgets for small samples and offers a scalable audit contract that is valid only when accompanied by the full set of gates.

## Related Concepts  
contamination fraction α, separability ρ, chi‑squared divergence, efficacy ef, variance Var₀(f), Gaussian budget, two‑stage planner, matched controls, scalar detectors, audit contract, baseline drift.
