# Summary: 2026-08-03_01-34-13Z_LieStoNet_LearningLieSymmetriesfromSpatiotemporalD.md
Saved: 2026-08-04 00:24
Source: 2026-08-03_01-34-13Z_LieStoNet_LearningLieSymmetriesfromSpatiotemporalD.md
Model: None

---

## Summary  
The paper proposes LieStoNet, a template‑free neural network that discovers Lie‑point symmetries of stochastic differential equations directly from spatiotemporal data. It leverages the theoretical framework linking SDE symmetries to Fokker‑Planck symmetries and learns projectable generators while enforcing algebraic consistency.

## Key Contributions  
- LieStoNet automatically recovers Lie point symmetry generators for a wide range of canonical SDEs without prior knowledge of symmetry groups or templates.  
- The method enforces the full Lie algebra axioms (bilinearity, antisymmetry, Jacobi) and ensures non‑redundancy via an independent basis.  
- It simultaneously learns drift/diffusion surrogates from increments, enabling optional discovery of associated Fokker‑Planck symmetries.

## Methodology  
The authors construct neural surrogates for SDE drift and diffusion using incremental trajectory data, then train a generator network to satisfy the SDE determining equations. Regularization includes closure under Lie brackets, adherence to the Lie algebra axioms (bilinearity, antisymmetry, Jacobi), and selection of an independent basis. The surrogate also defines a Fokker‑Planck equation whose symmetries can be explored in parallel.

## Results  
Across multiple canonical SDEs with known analytic symmetries (e.g., Ornstein‑Uhlenbeck, geometric Brownian motion), LieStoNet recovers generators that match ground‑truth symmetry algebras, demonstrating high accuracy and interpretability. The method also successfully discovers symmetries of the associated Fokker‑Planck equations when requested.

## Significance  
By providing an end‑to‑end framework for automatic symmetry discovery in stochastic systems, LieStoNet bridges theoretical physics and machine learning, improving sample efficiency and generalization. It enables researchers to uncover hidden invariances that guide modeling without manual intervention or prior assumptions.

## Related Concepts  
- Lie‑point symmetries of SDEs; Fokker‑Planck equations; neural surrogates; Lie algebra axioms (bilinearity, antisymmetry, Jacobi); spatiotemporal trajectory data; template‑free learning.
