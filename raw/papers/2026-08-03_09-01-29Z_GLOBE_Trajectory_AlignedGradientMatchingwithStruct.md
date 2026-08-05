---
title: GLOBE: Trajectory-Aligned Gradient Matching with Structured SparseOptimization for Coreset Selection
published: 2026-08-03T09:01:29Z
authors: Hetian Liu, Jin Cui, Mengcheng Shi, Yanbin Hu, Xinyue Long, Boran Zhao, Pengju Pen
url: http://arxiv.org/abs/2608.02690v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GLOBE: Trajectory-Aligned Gradient Matching with Structured SparseOptimization for Coreset Selection

## Abstract
On-device training of deep neural networks is fundamentally constrained by the computational and memory costs of large-scale datasets. Coreset selection offers a practical solution by retaining only a compact subset of real training samples. However, existing gradient-based methods commonly rely on gradients computed at a single model snapshot and employ greedy or pursuit-based selection procedures, limiting their ability to capture evolving optimization dynamics and handle strongly correlated samples. We propose GLOBE (Gradient Local-Balanced Extraction), a trajectory-aligned coreset selection framework that formulates sample selection as a globally optimized sparse weighting problem. GLOBE represents each sample by a gradient trajectory constructed across multiple training checkpoints, thereby capturing its influence throughout different stages of optimization. To preserve the training behavior of the full dataset, we introduce a multi-order matching objective that jointly aligns the first-order mean and projected uncentered second-order moments of gradient trajectories. GLOBE further combines Group LASSO, Elastic Net regularization, and nonnegative budget constraints to induce group- and sample-level sparsity while stabilizing the weights of correlated trajectories. Finally, class-balanced Top-K selection maintains adequate category coverage under limited sampling budgets. Experiments across six benchmarks and five evaluation architectures demonstrate that GLOBE consistently outperforms existing coreset selection methods in downstream test accuracy, particularly at low retention ratios. These results highlight the effectiveness of combining dynamic gradient information, multi-order distribution matching, and structured sparsity for data-efficient learning.

## Metadata
- **Published**: 2026-08-03T09:01:29Z
- **Authors**: Hetian Liu, Jin Cui, Mengcheng Shi, Yanbin Hu, Xinyue Long, Boran Zhao, Pengju Pen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02690v1)