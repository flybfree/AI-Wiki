---
title: Derivative Computation in PINNs: Automatic Differentiation, Finite Differences and Beyond
published: 2026-08-11T15:01:29Z
authors: Maciej J. Mikulski, Tadeusz Uhl
url: http://arxiv.org/abs/2608.11020v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Derivative Computation in PINNs: Automatic Differentiation, Finite Differences and Beyond

## Abstract
We systematically investigate finite-difference (FD) derivative computation in Physics-Informed Neural Networks (PINNs) as an alternative to automatic differentiation (AD). On three benchmark PDEs we show that, with a properly calibrated step size, FD matches AD in accuracy on every problem while running faster across the full tested batch-size range and using substantially less GPU memory, and that a stochastic variant we propose outperforms AD on a stationary problem. We further show that for neural architectures with inter-sample dependencies (e.g. BatchNorm, self-attention) the standard PyTorch autograd idiom is silently incorrect; the correct per-sample alternative is computationally infeasible at PINN-relevant batch sizes, while FD provides a forward-only approximation that is empirically an order of magnitude closer to the true per-sample derivative.

## Metadata
- **Published**: 2026-08-11T15:01:29Z
- **Authors**: Maciej J. Mikulski, Tadeusz Uhl
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11020v1)