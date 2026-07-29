---
title: Physics-Informed Broad Learning System: An Efficient Backpropagation-Free Framework for Solving Partial Differential Equations
url: http://arxiv.org/abs/2607.25608v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_11-36-34Z_Physics_InformedBroadLearningSystem_AnEfficientBac.md
generated_at: 2026-07-28 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PI‑BLS, a physics‑informed broad learning system that solves partial differential equations without using backpropagation by reformulating the training as a single linear optimization problem solved via pseudoinverse. It replaces gradient‑based PINNs with deterministic least‑squares solving of an output layer while preserving physical constraints. Experiments show PI‑BLS matches or exceeds PINN performance on forward PDE benchmarks, achieving faster training and fewer parameters.

## Key Takeaways
- The framework eliminates iterative backpropagation by converting the learning problem into a single linear optimization stage solved via pseudoinverse, which is deterministic and scalable.
- It embeds PDE operators and boundary conditions directly into the output layer as linear constraints, preserving physical laws without additional neural network layers.
- Experimental results demonstrate that PI‑BLS achieves competitive accuracy on forward PDE benchmarks while reducing training time and model complexity compared to conventional PINNs.

## Context
Physics‑informed neural networks have become a focal point for AI‑driven scientific computing, yet their reliance on gradient descent limits practical deployment. This work addresses the scalability bottleneck by introducing a linear optimization approach that aligns with the deterministic nature of PDE solutions. The shift toward broad learning systems reflects broader trends in interpretable and efficient deep learning.

## Implications
Practitioners can adopt PI‑BLS to solve complex engineering problems without costly GPU training, opening doors for real‑time simulation applications. The framework’s simplicity may inspire further research into physics‑informed optimization methods that balance accuracy with computational efficiency across various domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25608v1)
