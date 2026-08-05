---
title: Noise-Aware Shrinkage for Differentially Private Zeroth-Order Fine-Tuning of Large Language Models
published: 2026-08-04T07:52:23Z
authors: Lele Zheng, Weifeng Kong, Xinyi Zhang, Ke Cheng, Tao Zhang, Yulong Shen
url: http://arxiv.org/abs/2608.03277v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Noise-Aware Shrinkage for Differentially Private Zeroth-Order Fine-Tuning of Large Language Models

## Abstract
Differentially private zeroth-order optimization (DP-ZO) enables memory-efficient private fine-tuning of large language models using only forward evaluations. Existing aggregation-based DP-ZO methods reconstruct model updates at a fixed scale, ignoring that the strength of useful signals varies throughout training. Consequently, noise-dominated updates may receive excessive weight and degrade model utility. To address this issue, we propose SAGE, a noise-aware shrinkage method that adaptively attenuates privatized estimates according to their estimated signal quality. SAGE subtracts the known Gaussian noise variance from the observed second moment to estimate the underlying signal energy, stabilizes this estimate through temporal tracking, and compares its current signal-to-noise level with a warm-up reference to derive a bounded shrinkage factor. As pure post-processing, SAGE requires neither additional privacy budget nor model queries and introduces only constant additional state. Our theoretical analysis shows that shrinkage reduces the quadratic update-risk term faster than the linear descent term, preserving useful descent while limiting the influence of noise-dominated updates. Experiments on RoBERTa-large, OPT-1.3B, and OPT-6.7B demonstrate that SAGE outperforms existing baselines in most settings under the same privacy budgets while preserving the forward-only memory efficiency of DP-ZO.

## Metadata
- **Published**: 2026-08-04T07:52:23Z
- **Authors**: Lele Zheng, Weifeng Kong, Xinyi Zhang, Ke Cheng, Tao Zhang, Yulong Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03277v1)