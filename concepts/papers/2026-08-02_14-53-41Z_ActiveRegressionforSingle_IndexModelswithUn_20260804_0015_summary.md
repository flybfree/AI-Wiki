# Summary: 2026-08-02_14-53-41Z_ActiveRegressionforSingle_IndexModelswithUnknownLi.md
Saved: 2026-08-04 00:15
Source: 2026-08-02_14-53-41Z_ActiveRegressionforSingle_IndexModelswithUnknownLi.md
Model: None

---

## Summary  
The paper tackles active regression for single-index models where the link function is unknown but satisfies a 1‑Lipschitz constraint, and the loss is an arbitrary ℓ_p norm with p ≥ 1. It seeks to approximate the optimal solution within (1+ε) using a non‑adaptive sampling algorithm that queries only the response vector b while observing A fully. The work fills the gap left by prior results, which only handled known link functions or limited loss norms.

## Key Contributions  
- [Finding 1] A non‑adaptive sampling algorithm achieving (1+ε) approximation for any p ≥ 1 with query complexity O(d^{p/2∨1}/ε^{p∨2} poly log(n/ε)).  
- [Finding 2] Nearly tight lower bounds for the problem, showing that no algorithm can achieve better than Ω(d^{p/2∨1}/ε^{p∨2}) queries when p > 2.  
- [Finding 3] Extension of known results to unknown link functions, providing upper and lower bounds that match across all p ≥ 1.

## Methodology  
The authors formulate the active regression problem as min_{f,x} ||f(Ax)−b||_p^p with f a 1‑Lipschitz function. They employ a randomized sampling strategy that selects a subset of rows from A to construct an approximate linear model, leveraging concentration inequalities for ℓ_p norms and the Lipschitz constraint on f to bound error. The algorithm is non‑adaptive: it samples once and then outputs predictions without further queries.

## Results  
The proposed method attains query complexity O(d^{p/2∨1}/ε^{p∨2} poly log(n/ε)) and guarantees a (1+ε) approximation of the optimal value. The lower bound matches this order, establishing near‑tightness for p > 2. For p = 2, the algorithm recovers the classic active regression bound with O(d / ε^2) queries.

## Significance  
This work closes much of the remaining theoretical gap in active ℓ_p regression for single-index models, where prior results were limited to known link functions or specific loss norms. By handling unknown Lipschitz links and general p ≥ 1, it provides a unified framework that can be applied across diverse applications such as compressed sensing and robust statistics.

## Related Concepts  
- Single‑index model  
- Active regression  
- ℓ_p norm with arbitrary p ≥ 1  
- Unknown 1‑Lipschitz link function  
- Non‑adaptive sampling  
- Approximation algorithms
