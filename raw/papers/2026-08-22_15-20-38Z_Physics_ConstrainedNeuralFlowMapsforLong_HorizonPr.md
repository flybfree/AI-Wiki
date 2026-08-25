---
title: Physics-Constrained Neural Flow Maps for Long-Horizon Prediction of Spin Dynamics
published: 2026-08-22T15:20:38Z
authors: Haoen Feng, Shenglan Yuan, Shirong Lin
url: http://arxiv.org/abs/2608.22006v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Physics-Constrained Neural Flow Maps for Long-Horizon Prediction of Spin Dynamics

## Abstract
Conventional simulation of current-driven magnetization relies on fine-step integration of the spin-transfer-torque Landau--Lifshitz--Gilbert equation, creating a computational bottleneck in parameter sweeps and control searches. In this work, we propose a physics-constrained neural flow map that learns finite-time dynamics directly on the unit sphere. The model maps the current magnetization, spin-torque strength, and requested time span to a future state in a single forward pass. Tangent-space projection and spherical retraction preserve unit magnetization during recursive, composition-consistent rollout. We validate the framework on single-spin trajectories under in-domain torques and previously unseen but stronger drive. Beyond the training horizon, it achieves an in-domain root mean square error of $0.00425$ with norm drift at the $10^{-7}$ level. The flow outperforms an adapted Long Short-Term Memory (LSTM) in in-domain accuracy and geometric stability, although the LSTM retains slightly lower out-of-distribution state error. The resulting geometry-preserving propagator reduces reliance on fine-step integration and enables physically admissible long-horizon prediction.

## Metadata
- **Published**: 2026-08-22T15:20:38Z
- **Authors**: Haoen Feng, Shenglan Yuan, Shirong Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22006v1)