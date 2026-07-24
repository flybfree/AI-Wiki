# Summary: 2026-07-22_16-03-43Z_DecentralizedOnlineRiemannianOptimizationforStrong.md
Saved: 2026-07-24 02:08
Source: 2026-07-22_16-03-43Z_DecentralizedOnlineRiemannianOptimizationforStrong.md
Model: None

---

## Summary  
The paper addresses decentralized online optimization for strongly geodesically convex (strongly g‑convex) losses on Riemannian manifolds, showing O(log T) static regret bound matching Euclidean minimax rate. It introduces a general network‑error analysis for time‑varying step‑size schedules and uses it to achieve the optimal rate in both standard and two‑point bandit settings. The work extends existing decentralized methods that only handle g‑convex losses, bridging a gap between centralized and distributed regimes. The algorithm’s performance is independent of the specific manifold as long as curvature bounds are satisfied.  

## Key Contributions  
- [Finding 1] Provides a general network‑error analysis for time‑varying step‑size schedules on Riemannian manifolds with bounded sectional curvature.  
- [Finding 2] Establishes the first O(log T) static regret bound for decentralized online Riemannian gradient descent, matching the minimax optimal rate for strongly‑convex Euclidean online optimization.  
- [Finding 3] Extends these results to the two‑point bandit feedback setting via strong subconvexity arguments on smoothed loss functions.  

## Methodology  
The authors first analyze how network errors affect convergence when step sizes decay over time, deriving bounds that hold under bounded curvature. They then apply this analysis to construct a decentralized algorithm for strongly g‑convex losses, proving optimality up to constants. For the bandit case, they employ smoothed loss functions and strong subconvexity lemmas to obtain the same regret bound. The analysis leverages convexity properties that are preserved under isometric embeddings.  

## Results  
The main theoretical result is that the algorithm achieves O(log T) static regret in both settings, which is optimal for strongly convex Euclidean online optimization. The analysis holds on any Riemannian manifold with bounded sectional curvature, including positively curved manifolds.  

## Significance  
This work resolves a longstanding gap between centralized and decentralized Riemannian optimization, showing that strong convexity can be leveraged to obtain logarithmic regret even in distributed settings where step‑size decay is needed. It also provides a unified framework for network errors across different online paradigms. This insight simplifies practical deployment across diverse geometric spaces such as spheres and hyperbolic spaces.  

## Related Concepts  
Strongly geodesically convex (strongly g‑convex) functions, Riemannian manifolds with bounded sectional curvature, decentralized online optimization, network error analysis, static regret bounds, two‑point bandit feedback, strong subconvexity, smoothed loss functions.
