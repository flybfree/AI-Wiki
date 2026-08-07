# Summary: 2026-08-06_15-42-40Z_OnSame_SampleandIndependent_SampleStochasticExtrag.md
Saved: 2026-08-06 22:19
Source: 2026-08-06_15-42-40Z_OnSame_SampleandIndependent_SampleStochasticExtrag.md
Model: None

---

## Summary  
The paper investigates stochastic extragradient (SEG) methods for solving monotone variational inequality problems (VIPs), focusing on the same‑sample variant (S‑SEG) whose convergence behavior has been poorly understood compared with independent‑sample SEG (I‑SEG). It demonstrates that mean Lipschitzness and bounded variance alone are insufficient to guarantee convergence, even when the feasible set is compact. Moreover, it establishes high‑probability restricted‑gap convergence for both S‑SEG and I‑SEG under a relaxed set of assumptions while showing that certain theoretical improvements cannot be achieved in general. Finally, it reveals that an asymmetric double step‑size selection that ensures almost sure last‑iterate convergence for I‑SEG can fail catastrophically for S‑SEG.

## Key Contributions  
- [Finding 1] Same‑sample SEG is sensitive to samplewise Lipschitz parameters; mean Lipschitzness and bounded variance do not ensure convergence, even on a compact domain.  
- [Finding 2] High‑probability restricted‑gap convergence can be achieved for both S‑SEG and I‑SEG under relaxed assumptions, but some fundamental improvements are impossible in general.  
- [Finding 3] The asymmetric double step‑size selection that guarantees almost sure last‑iterate convergence for I‑SEG can fail for S‑SEG, leading to almost sure divergence.

## Methodology  
The authors analyze the stochastic operators governing both SEG variants using martingale convergence theory and restricted‑gap analysis. They derive necessary conditions on samplewise Lipschitzness and variance, construct counterexamples that illustrate divergence of S‑SEG despite modified step‑sizes, and compare the assumptions required for I‑SEG versus S‑SEG to identify where additional restrictions are needed.

## Results  
Theoretical results include high‑probability convergence rates under relaxed Lipschitz and bounded variance bounds, a proof that certain improvements cannot be universally applied, and an explicit stochastic monotone VIP where S‑SEG diverges almost surely even when the asymmetric double step‑size strategy is employed. These findings close a gap in the literature regarding the stability of same‑sample SEG.

## Significance  
Clarifying these conditions helps practitioners design robust algorithms for monotone VIPs, prevents reliance on insufficient assumptions that could lead to algorithmic failure, and informs future work on stochastic optimization methods that require samplewise information.

## Related Concepts  
Monotone variational inequality (VIP), stochastic extragradient (SEG), samplewise Lipschitzness, bounded variance, restricted‑gap convergence, high‑probability convergence, asymmetric double step‑size selection.
