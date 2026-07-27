---
title: Trajectory-Regularized Stochastic Optimal Control via KL Divergence
url: http://arxiv.org/abs/2607.22201v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_11-15-27Z_Trajectory_RegularizedStochasticOptimalControlviaK.md
generated_at: 2026-07-26 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes trajectory-regularized stochastic optimal control (TRSOC), a framework that adds a Kullback-Leibler divergence penalty between the actual and reference trajectories to standard stochastic optimal control. By applying Girsanov's theorem, the KL term simplifies to a quadratic drift mismatch cost, preserving the dynamic programming structure. The authors derive the associated Hamilton-Jacobi-Bellman equation and obtain closed-form solutions for linear-quadratic problems.

## Key Takeaways
- The TRSOC formulation introduces a KL divergence regularization that measures how closely the controlled trajectory follows an offline reference distribution.
- This regularization converts into a quadratic drift penalty, allowing the problem to remain solvable via dynamic programming without sacrificing tractability.
- Experiments demonstrate that adjusting the regularization parameter balances performance against trace fidelity, especially when the reference dynamics are learned from data.

## Context
In AI and control theory, aligning system behavior with desired trajectories is crucial for safe and reliable operation. Standard stochastic optimal control often neglects such alignment, leading to suboptimal or unsafe policies. This work bridges that gap by integrating a principled regularization that directly penalizes deviation from reference dynamics.

## Implications
For practitioners in robotics and autonomous systems, TRSOC offers a method to enforce adherence to learned specifications while maintaining computational efficiency. The approach can be applied across industries where precise trajectory control is essential, such as aerospace, automotive, and industrial automation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22201v1)
