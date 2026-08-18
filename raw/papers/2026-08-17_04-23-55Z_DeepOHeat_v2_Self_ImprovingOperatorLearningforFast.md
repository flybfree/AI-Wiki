---
title: DeepOHeat-v2: Self-Improving Operator Learning for Fast and Trustworthy Thermal Optimization in 3D-IC Design
published: 2026-08-17T04:23:55Z
authors: Xinling Yu, Yixing Li, Ziyue Liu, Xin Ai, Zhiyu Zeng, Hai Li, Zheng Zhang
url: http://arxiv.org/abs/2608.16080v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeepOHeat-v2: Self-Improving Operator Learning for Fast and Trustworthy Thermal Optimization in 3D-IC Design

## Abstract
Thermal-aware optimization of multi-die 3D integrated circuits evaluates many designs, each a costly heat-equation solve. Operator-learning surrogates replace this solve with a fast forward pass, ideally trained from physics alone, without labeled data. DeepOHeat-v1 made such surrogates fast and trustworthy, but only on low-contrast geometries. High-contrast multi-die stacks break it in two ways: discontinuous conductivities make the continuous physics loss ill-defined at material interfaces, and ill-conditioning ($κ_2(A_h) \approx 6 \times 10^4$) puts the discretized strong-form loss beyond first-order optimization. We propose DeepOHeat-v2 to overcome both. First, we train on a discretized physics loss that handles the discontinuities natively; its energy form reduces the prediction-space loss-Hessian conditioning from $κ^2$ to $κ$, and a matrix-preconditioned optimizer cuts the mean peak temperature error from over 30 K to 0.55 K. Second, because optimization leaves the training distribution, we propose a self-improving framework: a hotspot trust gate sends flagged placements to a reference solver, and the surrogate incrementally retrains on the refined solutions, keeping an update only when it improves held-out validation error. On a multi-die benchmark, the surrogate-true peak gap on the returned design falls from 1.12 K to 0.11 K, matching a solve-at-every-step optimizer while running $56\times$ faster.

## Metadata
- **Published**: 2026-08-17T04:23:55Z
- **Authors**: Xinling Yu, Yixing Li, Ziyue Liu, Xin Ai, Zhiyu Zeng, Hai Li, Zheng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16080v1)