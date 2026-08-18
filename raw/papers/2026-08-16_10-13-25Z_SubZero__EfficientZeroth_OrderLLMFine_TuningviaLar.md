---
title: SubZero+: Efficient Zeroth-Order LLM Fine-Tuning via Large Learning Rates
published: 2026-08-16T10:13:25Z
authors: Ziming Yu, Shuyao Xiao, Xingyu Zhao, Sike Wang, Pan Zhou, Peiyu Zang, Xiangda Yan, Yongjie Yang, Jia Li
url: http://arxiv.org/abs/2608.15665v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SubZero+: Efficient Zeroth-Order LLM Fine-Tuning via Large Learning Rates

## Abstract
Zeroth-order (ZO) optimization enables backpropagation-free fine-tuning of large language models, but existing ZO methods suffer from high-variance gradient estimators, making convergence unstable and highly sensitive to learning rates. We propose SubZero+, an improved SubZero framework that improves stability in three complementary ways: (i) multi-query gradient estimation within layer-specific low-rank subspaces to reduce variance without exhibiting the multi-query paradox; (ii) a subspace Adam optimizer that performs adaptive updates using in-subspace multi-query gradient statistics; and (iii) a sign correction for QR-based subspace construction to ensure Haar-distributed projection matrices, eliminating implementation-dependent orientation ambiguity. Experiments on models from 1.3B to 32B across SuperGLUE, under both full-parameter tuning and LoRA, show that SubZero+ consistently outperforms prior ZO baselines, enlarges the stable learning-rate range, and narrows the gap to first-order methods with minimal extra memory overhead.

## Metadata
- **Published**: 2026-08-16T10:13:25Z
- **Authors**: Ziming Yu, Shuyao Xiao, Xingyu Zhao, Sike Wang, Pan Zhou, Peiyu Zang, Xiangda Yan, Yongjie Yang, Jia Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15665v1)