# Summary: 2026-07-22_14-56-15Z_DynamicalandOptimizationTrade_offsofLevi__CivitaCo.md
Saved: 2026-07-24 02:04
Source: 2026-07-22_14-56-15Z_DynamicalandOptimizationTrade_offsofLevi__CivitaCo.md
Model: None

---

**## Summary**  
The paper investigates how the Levi‑Civita coordinate system, a classical regularization of the Kepler problem, behaves when used for learning Hamiltonian dynamics with a smooth quadrupole perturbation. By comparing Cartesian and planar Levi‑Civita formulations under identical physical constraints, the authors demonstrate that the regularized coordinates achieve far smaller relative energy errors near high eccentricity while remaining stable, whereas the Cartesian version fails catastrophically. The study quantifies these trade‑offs in terms of rollout success rates, raw‑basis optimisation difficulty and residual learning performance. This work is presented as a controlled falsification plus trade‑off analysis rather than a definitive solution for learned close‑encounter dynamics.

**## Key Contributions**  
- Finding 1: The Levi‑Civita Hamiltonian splitting yields a relative energy error of about \(2.1\times10^{-5}\) through eccentricity \(e=0.99\), roughly four to eight orders of magnitude better than the Cartesian baseline (\(3\times10^{-5}\)).  
- Finding 2: In matched physical horizon and force‑evaluation budgets, regularized models produce finite rollouts in all 40/40 test runs, while Cartesian models fail entirely (0/40).  
- Finding 3: The exact‑feature residual is a degree‑6 four‑monomial polynomial that can be fitted to the baseline with L‑BFGS after two iterations of orthogonalisation, yet small MLP residuals remain at \(\mathcal{O}(1)\) rollout error.

**## Methodology**  
The authors construct both Cartesian and planar Levi‑Civita formulations of a Kepler orbit perturbed by a smooth quadrupole potential. A fixed‑shell construction is employed to preserve the exact initial orbital energy, allowing a comparison of residual learning across identical sampling budgets. Neural models are trained with four residual objectives, and the optimisation landscape is examined for raw‑basis conditioning using orthogonalisation and L‑BFGS. The study runs 40/40 held‑out tests at high eccentricity to assess rollout finiteness.

**## Results**  
The regularized Levi‑Civita approach achieves a maximum relative energy error of \(2.1\times10^{-5}\) while the Cartesian splitting becomes unstable, leading to zero successful rollouts. Optimisation experiments show that orthogonalising the raw basis reduces L‑BFGS iterations to two, yet small MLP models still exhibit \(\mathcal{O}(1)\) residual errors even after gauge symmetrisation. The exact‑feature polynomial fitting demonstrates a clear linear relationship with the baseline error.

**## Significance**  
These findings clarify an important trade‑off: Levi‑Civita coordinates improve dynamical conditioning and reduce numerical energy errors, but they introduce severe raw‑basis optimisation challenges that hinder residual learning. Understanding this dichotomy is crucial for designing robust neural Hamiltonians in celestial mechanics where both accuracy and computational efficiency matter.

**## Related Concepts**  
- Kepler problem regularization  
- Cartesian vs. Levi‑Civita coordinate systems  
- Hamiltonian dynamics with smooth perturbations  
- Residual learning objectives  
- Raw‑basis optimisation and orthogonalisation  
- Gauge symmetrisation in neural networks
