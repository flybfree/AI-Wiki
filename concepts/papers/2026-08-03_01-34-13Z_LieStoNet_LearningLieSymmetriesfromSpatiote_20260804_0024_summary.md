# Summary: 2026-08-03_01-34-13Z_LieStoNet_LearningLieSymmetriesfromSpatiotemporalD.md
Saved: 2026-08-04 00:24
Source: 2026-08-03_01-34-13Z_LieStoNet_LearningLieSymmetriesfromSpatiotemporalD.md
Model: None

---

## Summary  
The paper introduces LieStoNet, a template‑free neural framework that discovers continuous Lie‑point symmetries of stochastic differential equations directly from spatiotemporal trajectories. By learning drift and diffusion surrogates from increments and enforcing the SDE determining equations, LieStoNet recovers projectable generators that satisfy the full Lie algebra, enabling efficient and interpretable symmetry discovery for noisy dynamics.

## Key Contributions  
- [Finding 1] LieStoNet learns neural surrogates for drift and diffusion directly from increments without prespecified symmetry groups or canonical coordinates.  
- [Finding 2] The learned generator is constrained by Lie‑algebra axioms (bilinearity, antisymmetry, Jacobi) to ensure closure under Lie brackets and a non‑redundant independent basis.  
- [Finding 3] It simultaneously defines an associated Fokker‑Planck equation whose symmetries can be discovered in parallel.

## Methodology  
The authors build on the SDE Lie‑symmetry theory of Gaeta and Quintero, which formalizes how Lie‑point symmetries correspond to symmetries of the Fokker‑Planck equation. Using spatiotemporal trajectories as input, they train two neural networks: one approximates the drift function and another the diffusion coefficient from discrete increments; a third network generates a projectable generator that is regularized to obey the SDE determining equations. The regularization enforces Lie‑algebra properties (bilinearity, antisymmetry, Jacobi) and selects an independent basis. As a byproduct, the surrogate defines a Fokker‑Planck equation whose symmetries are optionally recovered.

## Results  
Across canonical stochastic systems with known analytic symmetries—such as Ornstein‑Uhlenbeck and geometric Brownian motion—the method recovers generator vectors that align closely with ground‑truth algebra. Experiments on noisy trajectories show high agreement with analytical results, demonstrating robustness to measurement error. Moreover, LieStoNet also uncovers additional symmetries in the associated Fokker‑Planck counterpart, providing a dual view of symmetry discovery.

## Significance  
LieStoNet bridges machine learning and theoretical physics by offering an automated, data‑driven route to uncover continuous symmetries that are otherwise intractable. This improves sample efficiency, robustness, and out‑of‑distribution generalization for stochastic dynamical systems, opening new avenues for scientific modeling and algorithm design.

## Related Concepts  
Lie‑point symmetries, Lie algebra, SDE determining equations, Fokker‑Planck equation, neural surrogates, spatiotemporal data, symmetry discovery, machine learning in physics.
