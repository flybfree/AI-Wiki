---
title: Learning Implicit Constitutive Laws for Dynamic 3D Gaussian Splatting from Monocular Videos
published: 2026-08-22T20:47:17Z
authors: Xiaoyang Liu, Kai Han
url: http://arxiv.org/abs/2608.22102v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Implicit Constitutive Laws for Dynamic 3D Gaussian Splatting from Monocular Videos

## Abstract
We present GCA (Gaussian Constitutive Alignment), a framework for learning implicit constitutive laws from monocular dynamic video of deformable objects represented by 3D Gaussians. Given a static multi-view scan for geometric initialization, our method learns intrinsic physical dynamics solely from a single fixed-viewpoint video of the moving object. Existing implicit methods often suffer from local minima under noisy supervision and lack physical interpretability, while explicit approaches rely on predefined constitutive equations, limiting generalizability and becoming unstable in monocular settings. To address these challenges, our framework unifies LoRA-based adaptation with two key alignment modules. First, we propose Rank-based Depth-Geometric Anchors (RDGA) to establish robust geometric constraints from monocular dynamic observations via scale-invariant rank-based depth alignment, reducing the reliance on unreliable pixel-level color supervision. Second, a Constitutive Prior Regularizer (CPR) integrates classical constitutive models as soft differentiable priors, regularizing the optimization while preserving the flexibility of implicit modeling---even when the actual material is absent from the hypotheses. Extensive experiments on synthetic, real-to-sim, and real-world datasets demonstrate that GCA outperforms existing methods, achieving 48% lower Chamfer Distance than the strongest baseline on synthetic benchmarks while remaining robust under monocular supervision.

## Metadata
- **Published**: 2026-08-22T20:47:17Z
- **Authors**: Xiaoyang Liu, Kai Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22102v1)