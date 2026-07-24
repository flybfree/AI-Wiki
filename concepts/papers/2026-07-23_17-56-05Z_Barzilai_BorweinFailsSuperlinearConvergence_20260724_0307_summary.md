# Summary: 2026-07-23_17-56-05Z_Barzilai_BorweinFailsSuperlinearConvergenceonanOpe.md
Saved: 2026-07-24 03:07
Source: 2026-07-23_17-56-05Z_Barzilai_BorweinFailsSuperlinearConvergenceonanOpe.md
Model: None

---

## Summary  
The paper investigates a long‑standing conjecture about the Barzilai–Borwein (BB) method: whether it converges superlinearly for almost every strictly convex quadratic problem and initialization in any dimension \(n\ge 4\). The authors disprove this claim by constructing, for each such dimension, an open set of quadratic problems and starting points where BB converges but cannot achieve root‑superlinear convergence. Their analysis shows that the gradient norm, energy norm, and objective gap are all bounded below by geometric sequences with identical rates, which mathematically precludes superlinear behavior.

## Key Contributions  
- [Finding 1] The authors construct a nonempty open, positive‑measure family of strictly convex quadratic problems and initial points in every dimension \(n\ge 4\) for which the long Barzilai–Borwein method converges but fails to converge root‑superlinearly.  
- [Finding 2] They provide explicit constants \(\rho_{\min}=10^{-6}\) and \(\rho_{\max}=0.61\) that bound every spectral component of the gradient between corresponding geometric sequences, establishing two‑sided geometric estimates for both the error norm and the objective gap.  
- [Finding 3] The analysis demonstrates that all three quantities—gradient norm, energy norm, and objective gap—are bounded below by geometric sequences with the same rates, thereby ruling out superlinear convergence.

## Methodology  
The proof relies on a computer‑assisted investigation of the projectivized BB dynamics in dimension four. By analyzing the system’s nonresonant, attracting seven‑cycle, the authors obtain precise bounds on the spectral components of the gradient. These bounds are then lifted to higher dimensions through analytical extension, yielding the geometric estimates that characterize convergence.

## Results  
For every \(n\ge 4\), there exists an open set of quadratic problems and initializations such that BB converges linearly with rates \(\rho_{\min}\) and \(\rho_{\max}\). The gradient norm satisfies \(\|\nabla f(x_k)\| \in [c_1\rho^{\,k}, c_2\rho^{\,k}]\) for some constants \(c_i>0\), the energy norm obeys a similar bound, and the objective gap follows the squared rate: \(|f(x_k)-\min f| \le C\rho^{2k}\). The lack of superlinear convergence is formalized by showing that no sequence \(\{x_k\}\) can satisfy \(\lim_{k\to\infty} |f(x_k)-\min f| / \|x_k-x^*\|^p = 0\) for any \(p>1\).

## Significance  
This work challenges the assumption that BB enjoys universal superlinear convergence in quadratic optimization, revealing that its practical performance may be limited by geometric constraints. The findings have implications for algorithm design, as they highlight the need to consider initialization and problem structure when evaluating convergence guarantees.

## Related Concepts  
- Quadratic optimization  
- Barzilai–Borwein method (BB1)  
- Convergence rates (linear vs. superlinear)  
- Spectral components of gradients  
- Geometric sequences in analysis  
- Nonresonant cycles and projectivized dynamics  
- Computer‑assisted proof techniques
