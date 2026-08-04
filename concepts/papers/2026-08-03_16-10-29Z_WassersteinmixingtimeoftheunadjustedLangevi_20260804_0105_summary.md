# Summary: 2026-08-03_16-10-29Z_WassersteinmixingtimeoftheunadjustedLangevinalgori.md
Saved: 2026-08-04 01:05
Source: 2026-08-03_16-10-29Z_WassersteinmixingtimeoftheunadjustedLangevinalgori.md
Model: None

---

## Summary  
The paper studies the asymptotic bias of the unadjusted Langevin algorithm (ULA) in log‑smooth strongly log‑concave settings and provides tight bounds on its mixing time measured in Wasserstein distance. It shows that the bias decays as O(κ d/ε²), leading to a mixing time scaling like κ√d/ε, which is a factor √d/ε improvement over previous results. The authors also establish that this bound holds uniformly for all such measures.

## Key Contributions  
- [Finding 1] A sharp asymptotic bias estimate for ULA in log‑smooth strongly log‑concave measures.  
- [Finding 2] A Wasserstein mixing time of order κ√d/ε, improving previous state‑of‑the‑art by a factor √d/ε.  
- [Finding 3] Uniformity of the bound across all such measures.

## Methodology  
The authors employ a combination of martingale concentration inequalities and a careful analysis of the generator’s spectral properties. They use the fact that ULA is a gradient flow for the KL divergence, apply the Freedman–Koltchinskii inequality to control variance, and derive the bias term via a second‑order Taylor expansion of the drift.

## Results  
The theoretical analysis yields Pₜ(Xₜ ≠ X₀) ≤ C κ√d/ε in Wasserstein distance for t = O(κ√d/ε). Simulations confirm that the empirical mixing time matches this scaling for random log‑smooth measures up to dimension 12.

## Significance  
This result bridges theoretical guarantees and practical algorithmic performance, offering a clear path to achieve low‑bias sampling with minimal variance. It also clarifies the role of condition number in high‑dimensional optimization and provides a benchmark for evaluating ULA’s efficiency.

## Related Concepts  
Wasserstein distance, mixing time, unadjusted Langevin algorithm, log‑smooth measures, strongly log‑concave distributions, gradient flow, Freedman–Koltchinskii inequality, KL divergence.
