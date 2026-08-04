---
title: LieStoNet: Learning Lie Symmetries from Spatiotemporal Data for Stochastic Dynamical Systems
url: http://arxiv.org/abs/2608.01582v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_01-34-13Z_LieStoNet_LearningLieSymmetriesfromSpatiotemporalD.md
generated_at: 2026-08-03 23:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
LieStoNet is a template‑free neural framework that discovers Lie‑point symmetries of stochastic differential equations directly from spatiotemporal trajectories. By learning drift and diffusion surrogates and enforcing Lie algebra axioms, the method recovers generators consistent with known analytical symmetries while also generating an associated Fokker‑Planck equation.

## Key Takeaways
- The framework learns projectable generators that satisfy closure under Lie brackets, bilinearity, antisymmetry and Jacobi identity without prespecifying symmetry groups.  
- It simultaneously produces a Fokker‑Planck surrogate whose symmetries can be discovered in parallel, providing a complete symmetry picture of the SDE.  
- Experiments on canonical SDEs show that LieStoNet recovers the exact symmetry algebra with high accuracy even under noisy data.

## Context
Understanding invariances improves sample efficiency and robustness in machine learning, yet stochastic models lack systematic symmetry discovery. This work bridges AI and theoretical physics by applying deep learning to uncover continuous symmetries of SDEs, a problem that remains largely unexplored.

## Implications
Practitioners can leverage LieStoNet to design more efficient training pipelines for stochastic systems, reduce overfitting through invariance exploitation, and gain interpretable symmetry insights for scientific modeling.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01582v1)
