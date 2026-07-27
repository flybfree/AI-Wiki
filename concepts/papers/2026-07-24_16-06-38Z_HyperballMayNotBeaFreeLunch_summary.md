# Summary: 2026-07-24_16-06-38Z_HyperballMayNotBeaFreeLunch.md
Saved: 2026-07-26 21:54
Source: 2026-07-24_16-06-38Z_HyperballMayNotBeaFreeLunch.md
Model: None

---

## Summary  
The paper investigates the performance of Hyperball‑style optimizers for scale‑invariant deep networks and asks whether their advantage is a genuine learning mechanism or an artifact known as the “free lunch.” By deriving an angular effective learning rate that incorporates the angle between consecutive parameter states, the norm of the parameters, and the norm of the update, the authors decompose optimizer updates into radial and tangential components to understand how each influences one‑step angular displacement. Numerical experiments comparing MuonH (Hyperball with momentum) against MuonWD show that the main difference lies in the evolution of the effective step size rather than a superior update direction induced by Hyperball. The study also demonstrates that enforcing constant angular velocity does not resolve learning‑rate scheduling problems, so careful schedule design remains essential.

## Key Contributions  
- [Finding 1] Derivation of an angular effective learning rate that accounts for parameter‑update angle, parameter norm, and update norm.  
- [Finding 2] Decomposition of optimizer updates into radial and tangential components and analysis of their impact on one‑step angular displacement.  
- [Finding 3] Heuristic experiment showing the primary difference between MuonH and MuonWD stems from effective step‑size evolution, not an intrinsically superior update direction; constant angular velocity does not eliminate learning‑rate scheduling issues.

## Methodology  
The authors start with hyperball optimizers that fix the norms of matrix‑valued parameters and normalize updates. They define the angular displacement between consecutive parameter states and derive a formula for the effective learning rate that combines these three factors. The update is split into radial (changing magnitude) and tangential (rotational) parts, and they analyze how each part contributes to angular displacement. Theoretical analysis is complemented by numerical experiments that train MuonH and MuonWD under identical configurations, followed by a heuristic experiment where only the learning‑rate schedule is altered to reproduce the other optimizer’s dynamics. Finally, pretraining experiments with aggressive decay are performed.

## Results  
Numerical results indicate that the radial component has only a limited direct effect on the angular effective learning rate, so it cannot explain why MuonH converges more slowly than MuonWD early in training but later overtakes it. The heuristic experiment confirms that the main distinction between the two optimizers is the evolution of their effective step size rather than an inherent advantage in update direction. Enforcing constant angular velocity does not solve the learning‑rate scheduling problem; instead, a more aggressive decay can accelerate early pretraining but may impair later performance.

## Significance  
Understanding that Hyperball optimizers’ benefit arises from dynamic step‑size behavior, not from a “free lunch,” clarifies why careful learning‑rate scheduling is crucial for scale‑invariant networks. This insight helps practitioners avoid over‑reliance on optimizer design alone and underscores the importance of adaptive schedules to fully exploit hyperball‑style methods.

## Related Concepts  
Hyperball optimizer, angular effective learning rate, radial/tangential decomposition, MuonH vs. MuonWD, learning‑rate schedule, scale‑invariant deep networks, optimizer dynamics.
