# Summary: 2026-07-22_16-03-43Z_DecentralizedOnlineRiemannianOptimizationforStrong.md
Saved: 2026-07-24 02:05
Source: 2026-07-22_16-03-43Z_DecentralizedOnlineRiemannianOptimizationforStrong.md
Model: None

---

## Summary  
The paper tackles decentralized online optimization of strongly geodesically convex (strongly g‑convex) losses on Riemannian manifolds that have bounded sectional curvature, including positively curved spaces. While centralized strong g‑convexity yields an \(O(\log T)\) regret bound, the decentralized setting has been largely ignored for this regime. The authors overcome two obstacles: they first develop a general network‑error analysis that accommodates time‑varying step sizes, and then use this framework to obtain the first \(O(\log T)\) static regret guarantee for decentralized Riemannian gradient descent, matching the minimax‑optimal rate for Euclidean online optimization. They also extend these ideas to two‑point bandit feedback via strong subconvexity arguments for smoothed losses.

## Key Contributions  
- [Finding 1] A general network‑error analysis for time‑varying schedules that can be applied to Riemannian manifolds with bounded curvature.  
- [Finding 2] The first \(O(\log T)\) static regret bound for decentralized online Riemannian gradient descent on strongly g‑convex losses, attaining the minimax‑optimal rate.  
- [Finding 3] An \(O(\log T)\) regret guarantee for two‑point bandit feedback using strong subconvexity arguments applied to smoothed loss functions.

## Methodology  
The authors start by formulating a network‑error analysis that quantifies how deviations from the optimal schedule affect convergence, allowing step sizes to decay over time. This analysis is then leveraged to construct a decentralized algorithm where each participant uses a fixed step size derived from the worst‑case error bound, ensuring convergence without requiring online communication of exact schedules. By exploiting the strong g‑convexity property—where the Hessian satisfies \( \langle \nabla^2 f(x), v\rangle \ge g\|v\|^2\) for all tangent vectors \(v\)—they derive a regret bound that mirrors Euclidean results, and they further apply strong subconvexity of smoothed versions to obtain analogous guarantees in bandit settings.

## Results  
The main theoretical result is an \(O(\log T)\) static regret bound for decentralized Riemannian gradient descent on strongly g‑convex losses, which matches the minimax‑optimal rate known from Euclidean online optimization. The same bound holds for two‑point bandit feedback when the loss functions are smoothed and their strong subconvexity is exploited. Prior work had only achieved \(O(\sqrt{T})\) regret for g‑convex problems, so these results fill a significant gap in distributed learning theory.

## Significance  
This work provides optimal rates for strongly geodesically convex losses in decentralized settings, enabling efficient and theoretically sound distributed optimization on curved manifolds. It bridges the gap between centralized strong g‑convexity guarantees and practical networked scenarios where communication overhead must be minimized, opening new avenues for applications such as federated learning on Riemannian data.

## Related Concepts  
Strongly geodesically convex (strongly g‑convex) loss functions, Riemannian manifolds with bounded sectional curvature, online optimization, decentralized algorithms, network error analysis, minimax optimal rate \(O(\log T)\), two‑point bandit feedback, strong subconvexity.
