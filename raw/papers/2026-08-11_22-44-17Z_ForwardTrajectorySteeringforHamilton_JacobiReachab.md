---
title: Forward Trajectory Steering for Hamilton-Jacobi Reachability Analysis
published: 2026-08-11T22:44:17Z
authors: Sungje Park, Stephen Tu
url: http://arxiv.org/abs/2608.11480v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Forward Trajectory Steering for Hamilton-Jacobi Reachability Analysis

## Abstract
Hamilton-Jacobi (HJ) reachability provides a mathematically rigorous framework for safe control of dynamical systems, but its practical application is bottlenecked by the computational complexity of solving Hamilton-Jacobi-Isaacs variational inequality PDEs in high dimensions. Physics-informed neural networks (PINNs) have recently emerged as a promising alternative to classical mesh-based solvers, yet their performance is highly sensitive to the choice of collocation sampling. In order to learn accurate safety value functions, existing PINNs-based HJ reachability solvers must rely on complex training pipelines and auxiliary supervision. In this work, we propose STEER2REACH (S2R), a PINNs-based HJ reachability solver that requires minimal modification on top of standard PINNs training. S2R's key contribution is a lightweight, low-overhead adaptive collocation sampling distribution constructed by steering forward trajectories using a combination of the optimal control and disturbance signals induced by the current value function, with injected stochastic exploration noise. We demonstrate that despite its simplicity, S2R achieves competitive--and in some cases improved--performance on safety metrics while reducing relative L2 error across a range of reachability benchmarks compared with SoTA MPC-guided HJ reachability solvers, all without requiring multi-stage training or MPC-based supervision.

## Metadata
- **Published**: 2026-08-11T22:44:17Z
- **Authors**: Sungje Park, Stephen Tu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11480v1)