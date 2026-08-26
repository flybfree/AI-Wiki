---
title: Enhancing Bayesian Optimization and Active Learning Through Kernel Diversity
published: 2026-08-25T15:35:47Z
authors: Heng Zhang, Haotian Xiang, Qin Lu, Konstantinos D. Polyzos, Tara Javidi
url: http://arxiv.org/abs/2608.24721v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enhancing Bayesian Optimization and Active Learning Through Kernel Diversity

## Abstract
Hyperparameter selection remains a key challenge in Bayesian optimization (BO) and Bayesian active learning (AL), as model misspecification can lead to suboptimal performance, while more accurate fully Bayesian treatments typically rely on computationally expensive MCMC sampling. This paper proposes a unified framework, KENDO (Kernel ENsemble Disagreement-aware Operator), that integrates Ensemble Gaussian Processes (EGP) with disagreement-aware acquisition strategies. The central idea is to replace hyperparameter sampling with a kernel ensemble and adaptive Bayesian weighting, combined with disagreement-aware acquisition strategies. Within this unified framework, we instantiate KENDO-BO for BO and KENDO-AL for Bayesian AL, demonstrating that both arise from a common self-correcting mechanism with task-specific acquisition objectives. We further extend the approach to multi-objective optimization via random scalarization that preserves the single-optimizer conditioning structure. Thorough numerical tests on synthetic and real-world benchmarks across single-objective optimization, multi-objective optimization, and active learning demonstrate that (i) KENDO-BO achieves competitive or superior optimization performance compared to state-of-the-art methods while reducing computational overhead by up to $5\times$ and (ii) KENDO-AL achieves superior predictive calibration over MCMC-based active learning baselines with up to $27\times$ speedup.

## Metadata
- **Published**: 2026-08-25T15:35:47Z
- **Authors**: Heng Zhang, Haotian Xiang, Qin Lu, Konstantinos D. Polyzos, Tara Javidi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24721v1)