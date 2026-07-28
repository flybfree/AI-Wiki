---
title: SpecFormer: Mitigating Embedding and Attention Collapse via Spectral-Aware Transformer for Recommendation
published: 2026-07-27T05:53:00Z
authors: Yu Cui, Yi Xu, Jiahao Wang, Hao Zhang, Yu Zhang, Xiaoyi Zeng, Can Wang, Jinxin Hu, Jiawei Chen
url: http://arxiv.org/abs/2607.24025v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SpecFormer: Mitigating Embedding and Attention Collapse via Spectral-Aware Transformer for Recommendation

## Abstract
Transformer architectures have achieved remarkable success across diverse domains; however, directly applying their standard self-attention mechanism to recommendation often yields suboptimal performance, sometimes even trailing behind well-designed simple recommendation models. In this paper, we reveal that this performance bottleneck stems from severe embedding and attention collapse unique to recommendation scenarios. The heterogeneity and long-tail nature of recommendation data lead to a severe spectral collapse dominated by a few principal singular values. We further theoretically demonstrate that this triggers a vicious cycle in recommendation model's forward and backward propagation, which accelerates embedding and attention collapse and limits the model's scaling capability with increased depth. To address these issues, we propose SpecFormer, a novel Spectral-Aware Transformer designed for mitigating embedding and attention collapse in recommendation. Specifically, SpecFormer introduces 1) a Learnable Spectral Softening module to dynamically smooth the singular values distribution of the input token embeddings; 2) a Spectrum-softened Attention mechanism to model feature interaction under a more uniform spectral distribution space; 3) a Spectral Residual Position Encoding via Taylor expansion of singular values, explicitly providing a spectral inductive bias for feature interactions. Extensive experiments on one industrial and two public datasets demonstrate that SpecFormer significantly outperforms state-of-the-art baselines. Notably, SpecFormer has been successfully deployed in a real-world commercial recommender system and exhibits exceptional scaling capabilities: stacking SpecFormer layers actively improves the attention effective rank and recommendation performance.

## Metadata
- **Published**: 2026-07-27T05:53:00Z
- **Authors**: Yu Cui, Yi Xu, Jiahao Wang, Hao Zhang, Yu Zhang, Xiaoyi Zeng, Can Wang, Jinxin Hu, Jiawei Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24025v1)