# Summary: 2026-07-23_17-56-05Z_Barzilai_BorweinFailsSuperlinearConvergenceonanOpe.md
Saved: 2026-07-24 03:13
Source: 2026-07-23_17-56-05Z_Barzilai_BorweinFailsSuperlinearConvergenceonanOpe.md
Model: None

---

## Summary  
The Barzilai‑Borwein (BB) method is widely used for continuous quadratic optimization and is known to converge superlinearly under certain assumptions. This paper disproves the claim that BB converges superlinearly for almost every strictly convex quadratic problem in dimensions \(n\ge 4\) by constructing a nonempty open set of problems and initial points where convergence occurs but not at root‑superlinear speed. The authors show that all three key quantities—gradient norm, energy norm, and objective gap—are bounded below by geometric sequences with the same rates, ruling out superlinearity.

## Key Contributions  
- **Finding 1**: A nonempty open set of strictly convex quadratic problems and initial points for which BB converges but cannot converge root‑superlinearly in every dimension \(n\ge 4\).  
- **Finding 2**: Explicit constants \(\rho_{\min}=10^{-6}\) and \(\rho_{\max}=0.61\) that bound each spectral component of the gradient, yielding two‑sided geometric estimates for the gradient/energy norm (rate \(\rho_{\max}\)) and a squared rate (\(\rho_{\max}^2\)) for the objective gap.  
- **Finding 3**: Identification of a nonresonant attracting seven‑cycle in the projectivized BB dynamics in dimension four, which is proven via computer‑assisted analysis to prevent superlinear convergence.

## Methodology  
The authors combined theoretical spectral analysis with numerical computation. They derived geometric bounds on the Jacobian of the BB iteration, analyzed how these bounds translate into convergence rates for the error norms and objective gap, and employed a high‑dimensional dynamical system approach to locate a stable cycle that obstructs superlinearity. The construction is nontrivial because it relies on precise control of spectral components across many dimensions.

## Results  
For every finite dimension \(n\ge 4\), there exists an open set with positive Lebesgue measure such that the BB1 method converges, but the error norm decays only at rate \(\rho_{\max}=0.61\) and the objective gap at squared rate \(\rho_{\max}^2\). All three quantities are bounded below by geometric sequences (with lower bound \(\rho_{\min}=10^{-6}\)), confirming that superlinear convergence is impossible on this set.

## Significance  
This work resolves a longstanding open question about theoretical guarantees for BB in quadratic optimization, demonstrating that even in high dimensions the method’s convergence cannot be guaranteed to be superlinear. It underscores the necessity of spectral analysis and dynamical properties beyond simple convexity when assessing algorithmic performance.

## Related Concepts  
- Barzilai‑Borwein (BB) method  
- Quadratic optimization problems  
- Superlinear convergence  
- Geometric convergence rates  
- Projectivized dynamics  
- Nonresonant cycles
