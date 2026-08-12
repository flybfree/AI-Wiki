---
title: Derivative Computation in PINNs: Automatic Differentiation, Finite Differences and Beyond
url: http://arxiv.org/abs/2608.11020v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_15-01-29Z_DerivativeComputationinPINNs_AutomaticDifferentiat.md
generated_at: 2026-08-11 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates finite-difference derivative computation in Physics-Informed Neural Networks as an alternative to automatic differentiation. On three benchmark PDEs it shows that with a properly calibrated step size, FD matches AD accuracy while running faster and using less GPU memory across various batch sizes. A stochastic variant also outperforms AD on stationary problems.

## Key Takeaways
- FD matches AD accuracy with a proper step size across all tested batch-size ranges and uses substantially less GPU memory.
- The proposed stochastic FD variant achieves higher performance than AD specifically for stationary PDEs.
- Standard PyTorch autograd is silently incorrect for neural architectures that have inter-sample dependencies such as BatchNorm or self‑attention, while the correct per‑sample derivative would be computationally infeasible at PINN-relevant batch sizes.

## Context
In AI research, PINNs depend on accurate gradient estimates to solve inverse problems. Traditional automatic differentiation can be error‑prone and memory‑intensive, especially when dealing with complex network structures that involve shared state across samples.

## Implications
For practitioners the finite-difference approach provides a practical solution that avoids costly autograd errors and memory bottlenecks, enabling larger batch sizes and real‑time applications of PINNs. This opens new possibilities for training neural networks on resource‑constrained hardware without sacrificing derivative fidelity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11020v1)
