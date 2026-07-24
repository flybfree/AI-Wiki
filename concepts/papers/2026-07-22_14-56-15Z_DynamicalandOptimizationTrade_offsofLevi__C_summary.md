# Summary: 2026-07-22_14-56-15Z_DynamicalandOptimizationTrade_offsofLevi__CivitaCo.md
Saved: 2026-07-24 02:01
Source: 2026-07-22_14-56-15Z_DynamicalandOptimizationTrade_offsofLevi__CivitaCo.md
Model: None

---

## Summary  
The paper investigates how Levi‑Civita coordinate regularization influences both dynamical stability and optimization performance in learned close‑encounter dynamics for a perturbed Kepler problem, comparing planar versus Cartesian formulations. It demonstrates that the Levi‑Civita Hamiltonian splitting maintains relative energy error ≤ 2.1×10⁻⁵ up to eccentricity e=0.99, whereas the Cartesian version becomes unstable and accumulates errors of many orders of magnitude. The study also reveals a trade‑off: better numerical conditioning but poorer raw‑basis optimization due to ill‑conditioning of neural residual learning. This work is presented as a controlled falsification‑plus‑trade‑off analysis rather than a solution.

## Key Contributions  
- Finding 1: Levi‑Civita Hamiltonian splitting yields relative energy error ≤ 2.1×10⁻⁵ up to eccentricity e=0.99, outperforming Cartesian splitting which becomes unstable.  
- Finding 2: Within matched physical horizon and force‑evaluation budgets the regularized baseline error is 3×10⁻⁵ versus 4.7–8.3 orders of magnitude larger for Cartesian, especially at high eccentricity.  
- Finding 3: Neural residual models with exact features fit a four‑monomial degree‑6 polynomial; however raw‑basis ill‑conditioning limits L‑BFGS convergence to two iterations and leaves small MLPs at O(1) rollout error.

## Methodology  
The authors construct both planar Levi‑Civita and Cartesian coordinate systems for the Kepler problem perturbed by an analytic quadrupole potential. They evaluate dynamical stability via energy error across a range of eccentricities, compare performance under fixed physical horizon and force‑evaluation budgets, and train neural residual models using exact feature controls to assess optimization conditioning.

## Results  
The regularized Levi‑Civita model achieves finite rollouts in 40/40 test runs with negligible error, whereas Cartesian yields zero successful rollouts. Energy errors are on the order of 10⁻⁵ versus a baseline of 3×10⁻⁵, and residual learning fits a four‑monomial degree‑6 polynomial; L‑BFGS converges in two iterations after orthogonalization, while small MLPs retain O(1) error.

## Significance  
This study clarifies that coordinate choice influences both dynamical conditioning and optimization feasibility, highlighting a non‑trivial trade‑off. It provides empirical evidence for the instability of Cartesian regularizations in learned dynamics and underscores challenges in neural residual learning despite exact feature representations.

## Related Concepts  
- Levi‑Civita coordinates  
- Hamiltonian splitting  
- Close‑encounter dynamics  
- Neural residual learning  
- Energy error  
- Raw‑basis ill‑conditioning  
- L‑BFGS optimization
