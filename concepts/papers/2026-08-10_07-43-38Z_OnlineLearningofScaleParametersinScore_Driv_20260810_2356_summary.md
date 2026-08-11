# Summary: 2026-08-10_07-43-38Z_OnlineLearningofScaleParametersinScore_DrivenFilte.md
Saved: 2026-08-10 23:56
Source: 2026-08-10_07-43-38Z_OnlineLearningofScaleParametersinScore_DrivenFilte.md
Model: None

---

## Summary  
The paper investigates how to learn the gain that scales a log‑likelihood score in online, score‑driven filters, treating the gain as a decision variable rather than a fixed constant. It formulates gain selection as a conditional predictive problem whose loss is a Kullback‑Leibler divergence between reachable next states and the true distribution. The authors derive that scalar unscaled gains correspond to the negative product of consecutive scores, while positive aGAS scaling merely rescales the effective step size. By analyzing monotone differentiable gain links they show that bounded domains induce mirror‑descent dynamics and that persistence creates a Bregman pull toward a reference gain.

## Key Contributions  
- [Finding 1] The authors establish dynamic‑regret bounds for projected and discounted mirror updates of the gain selector, comparing them to time‑varying comparators that use only current information.  
- [Finding 2] They prove that monotone differentiable gain links produce a mirror‑descent geometry on bounded domains, while persistence yields Bregman‑pull behavior toward a reference gain.  
- [Finding 3] Empirical out‑of‑sample experiments on equity‑index volatilities demonstrate that the bounded mirror gain generally matches or exceeds constant‑gain strategies and avoids extreme spikes, with the greatest gains observed in multi‑crisis market regimes.

## Methodology  
The study treats the filter’s gain as a stochastic process whose update is governed by a conditional predictive decision problem. For each admissible gain the reachable next state lies on either a line (scalar) or coordinatewise transmission (diagonal), and the one‑step‑ahead predictive density is used to compute a Kullback‑Leibler objective. The scalar unscaled gain’s stochastic gradient is identified as the negative raw product of consecutive scores, while positive aGAS scaling only rescales the effective step. By imposing convexity, compactness, and regularity on the gain domain, the authors derive dynamic‑regret bounds for both projected mirror updates and discounted versions relative to comparators that rely solely on current information.

## Results  
Theoretical analysis yields asymptotic regret bounds that hold under the stated assumptions, showing that mirrored updates converge faster than naive comparator strategies. Simulations across various scaling rules, link geometries (linear vs. diagonal), persistence settings, and transmission rates illustrate how each factor influences convergence speed and stability. An out‑of‑sample panel of equity‑index volatilities confirms that the bounded mirror gain strategy generally matches or outperforms constant gains while avoiding the extreme spikes characteristic of nominally unbounded exponential links; multi‑crisis markets exhibit the strongest improvements.

## Significance  
This work advances online learning for score‑driven filters by providing a principled, regret‑bound approach to gain selection that is robust to market turbulence. By leveraging mirror‑descent geometry and Bregman pull, the method mitigates the risk of large, destabilizing updates while maintaining performance comparable to or better than simpler constant‑gain policies.

## Related Concepts  
score‑driven filters, gain scaling (aGAS), mirror descent, Bregman divergence, dynamic regret, Kullback‑Leibler objective, projection onto bounded domains, coordinatewise transmission, persistence, multi‑crisis markets.
