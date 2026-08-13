---
title: Learning with Bilevel-Minimax Optimization for Efficient and Reliable Transfer Attacks
published: 2026-08-12T08:58:22Z
authors: Yaohua Liu, Yifan Guo, Jiaxin Gao
url: http://arxiv.org/abs/2608.11815v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning with Bilevel-Minimax Optimization for Efficient and Reliable Transfer Attacks

## Abstract
Transfer-based adversarial attacks craft adversarial examples using surrogate models to mislead black-box victim models. Beyond perturbation generation, transferability is fundamentally governed by the coupling of initialization, surrogate adaptation, and gradient dynamics. We revisit this challenge from a bilevel-minimax perspective and propose BMAT (Bilevel-Minimax Adversarial Transfer). The bilevel formulation captures the dependency between initialization and perturbation, while the inner minimax problem promotes surrogate robustness for cross-architecture generalization. Algorithmically, we develop an integrated bottom-up solver that combines a Soft Weight Modulator and an Implicit Gradient Approximator to enable ternary coupling among initialization, surrogate adaptation, and perturbation optimization. We further provide theoretical insights into the optimization dynamics of the proposed bilevel-minimax framework. Extensive experiments on classification and segmentation benchmarks show that BMAT outperforms more than 10 strong baselines across more than 30 victim models, improving both intra- and cross-architecture transfer and yielding up to a 2x reduction in mIoU. Code is available at https://github.com/callous-youth/BMAT.

## Metadata
- **Published**: 2026-08-12T08:58:22Z
- **Authors**: Yaohua Liu, Yifan Guo, Jiaxin Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11815v1)