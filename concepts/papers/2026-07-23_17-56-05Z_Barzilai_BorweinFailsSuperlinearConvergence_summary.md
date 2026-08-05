# Summary: 2026-07-23_17-56-05Z_Barzilai_BorweinFailsSuperlinearConvergenceonanOpe.md
Saved: 2026-07-24 03:07
Source: 2026-07-23_17-56-05Z_Barzilai_BorweinFailsSuperlinearConvergenceonanOpe.md
Model: None

---

## Summary  
The Barzilai‑Borwein (BB) method is renowned for its strong practical performance in continuous optimization, yet its theoretical guarantee of superlinear convergence remains unresolved. This paper provides a negative answer to that question by constructing counterexamples where BB converges only linearly on a nonempty open set of strictly convex quadratic problems in every dimension \(n\ge 4\). The authors show that the gradient norm and energy norm decay geometrically with matching rates while the objective gap decays quadratically, thereby ruling out superlinear convergence.  

## Semantic links
- [[concepts/papers/2026-07-21_16-03-05Z_SelectionShapestheBoundary_APreregisteredRe_summary.md|Summary: 2026-07-21_16-03-05Z_SelectionShapestheBoundary_APreregisteredReplicati.md]] — 3 title terms overlap; 1 backlink; 7 summary/topic terms overlap
- [[concepts/papers/2026-07-22_15-25-05Z_Self_supervisiondrivesrepresentationalconve_summary.md|Summary: 2026-07-22_15-25-05Z_Self_supervisiondrivesrepresentationalconvergencei.md]] — 3 title terms overlap; 10 summary/topic terms overlap; semantic match 0.08
- [[concepts/papers/2026-08-03_10-47-05Z_TextNCA_NeuralCellularAutomataforLanguageMo_20260804_0045_summary.md|Summary: 2026-08-03_10-47-05Z_TextNCA_NeuralCellularAutomataforLanguageModelingv.md]] — 3 title terms overlap; 10 summary/topic terms overlap; semantic match 0.08

## Key Contributions  
- [Finding 1] Construction of a nonempty open family of strictly convex quadratic problems and initial points for which BB converges but cannot converge root‑superlinearly in dimensions \(n\ge 4\).  
- [Finding 2] Explicit geometric bounds on the gradient norm, energy norm, and objective gap with the same rates, showing all three quantities are bounded below by geometric sequences.  
- [Finding 3] Identification of a nonresonant attracting seven‑cycle in the projectivized BB dynamics as the source of linear convergence.  

## Methodology  
The authors employed a computer‑assisted analysis to locate invariant manifolds of the BB iteration map. By projecting the four‑dimensional dynamics onto a projective space, they computed its Jacobian and identified eigenvalues that generate a stable cycle. This allowed them to characterize parameter regimes where the method exhibits only linear (geometric) convergence rather than superlinear behavior.  

## Results  
For every \(n\ge 4\), the constructed problems satisfy \(\rho_{\min}=10^{-6}\) and \(\rho_{\max}=0.61\), ensuring each spectral component of the gradient is trapped between geometric sequences. Consequently, \(\|\nabla f(x_k)\| \le C\rho^k\) and the energy norm satisfies similar bounds; the objective gap obeys a squared‑rate bound. These theoretical results are supported by simulations confirming linear convergence.  

## Significance  
This work resolves a longstanding open question in optimization theory, demonstrating that superlinear guarantees cannot be assumed for BB even on convex quadratics. It highlights the importance of spectral analysis and dynamical systems in understanding algorithmic behavior, influencing future research on convergence rates and preconditioning.  

## Related Concepts  
- Barzilai‑Borwein method (BB1)  
- Strictly convex quadratic functions  
- Geometric convergence vs superlinear convergence  
- Projectivized dynamics and invariant manifolds  
- Nonresonant cycles in optimization maps
