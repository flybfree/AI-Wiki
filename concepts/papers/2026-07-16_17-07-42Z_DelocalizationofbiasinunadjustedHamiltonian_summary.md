# Summary: 2026-07-16_17-07-42Z_DelocalizationofbiasinunadjustedHamiltonianMonteCa.md
Saved: 2026-07-16 21:01
Source: 2026-07-16_17-07-42Z_DelocalizationofbiasinunadjustedHamiltonianMonteCa.md
Model: None

---

## Summary  
The paper investigates the bias that persists in unadjusted Hamiltonian Monte Carlo (HMC) and underdamped Langevin integrators, which are known to be biased without Metropolis‑Hastings correction. It extends the previously observed *delocalization of bias* phenomenon—first shown for overdamped Langevin—to these two samplers, showing that a modest number of integration steps can control the \(W_2\) distance of any marginal distribution. The authors develop a matrix‑polynomial framework to handle the discrete‑time propagators inherent in unadjusted schemes and demonstrate that this bias delocalization holds for large friction parameters, implying similar benefits for the Leimkuhler‑Matthews integrator used in overdamped Langevin.

## Key Contributions  
- [Finding 1] The bias delocalization phenomenon is extended to both unadjusted HMC and underdamped Langevin algorithms.  
- [Finding 2] For a \(K\)-dimensional marginal, \(O(\sqrt{K})\) integration steps are sufficient up to \(\log d\) terms to bound the \(W_2\) bias, assuming weak or sparse variable interactions.  
- [Finding 3] The discrete‑time integrators’ technical difficulties are addressed through a broadly applicable matrix‑polynomial framework that characterizes their propagators.

## Methodology  
The authors treat the dynamics as a linear operator and encode its action on basis functions using matrix polynomials, which allows them to compute exact or approximate propagators. By analyzing how these propagators act on test functions, they derive conditions under which the cumulative bias remains localized in a small number of steps. Their framework generalizes the Leimkuhler‑Matthews analysis for overdamped Langevin and provides a unified treatment for unadjusted HMC and underdamped Langevin.

## Results  
Theoretical analysis shows that with \(O(\sqrt{K})\) steps (up to \(\log d\) terms) the \(W_2\) bias of any marginal is controlled, independent of the number of variables. The result holds for large friction parameters in underdamped Langevin, confirming delocalization for the Leimkuhler‑Matthews integrator used in overdamped settings. This theoretical bound translates into practical efficiency gains: no Metropolis correction is needed and sampling complexity grows only with \(\sqrt{K}\) rather than \(K\).

## Significance  
This work offers a route to unbiased, low‑complexity integration for unadjusted samplers that are otherwise considered biased due to the need for costly acceptance rates. By reducing the required number of steps to \(O(\sqrt{K})\) and eliminating Metropolis adjustments, it enables scalable Bayesian inference in high‑dimensional settings where traditional HMC becomes prohibitive.

## Related Concepts  
- Bias delocalization  
- \(W_2\) distance  
- Hamiltonian Monte Carlo (unadjusted)  
- Underdamped Langevin dynamics  
- Overdamped Langevin and Leimkuhler‑Matthews integrator  
- Matrix‑polynomial framework for propagators  
- Marginal distributions in high dimensions  
- Weak or sparse variable interactions
