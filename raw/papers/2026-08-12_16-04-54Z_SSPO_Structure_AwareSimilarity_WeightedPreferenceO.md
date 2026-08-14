---
title: SSPO: Structure-Aware Similarity-Weighted Preference Optimization for Neural Combinatorial Optimization
published: 2026-08-12T16:04:54Z
authors: Yuanyu Li, Jintao Xu, Zijiang Liu, Yongzhi Qi, Ningxuan Kang, Jianshen Zhang, Wei Qi, Chen Xie, Zuo-Jun Max Shen
url: http://arxiv.org/abs/2608.12443v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SSPO: Structure-Aware Similarity-Weighted Preference Optimization for Neural Combinatorial Optimization

## Abstract
Neural combinatorial optimization (NCO) relies on parallel solution sampling for training, yet existing methods fail to fully exploit the rich information latent in a co-sampled solution group. Preference-optimization methods anchor on the single best solution and discard fine-grained quality and structural signal from all other peers-a failure we term gradient signal polarization. Mean-based baselines instead weight peers uniformly, so structurally near-identical peers flood the baseline with redundant information and keep gradient variance high-a failure we term baseline redundancy. We propose SSPO (Structure-Aware Similarity-Weighted Preference Optimization), which scores all $B$ sampled solutions jointly through a dissimilarity-weighted leave-one-out baseline: structurally distinct peers receive higher weight, resolving both failures in a single mechanism. The baseline uses zero-parameter, problem-adaptive solution embeddings built from the encoder's existing node representations. Experiments on TSP, EFL, and JSP benchmarks show consistent gains over prior best-anchor and uniform-weight baselines. A direct comparison against uniform RLOO on TSP and EFL confirms that structure-aware weighting is the primary driver of improvement. The SSPO-trained EFL policy has been deployed in a production facility-location system at JD$\mathord{.}$com, confirming practical viability at scale.

## Metadata
- **Published**: 2026-08-12T16:04:54Z
- **Authors**: Yuanyu Li, Jintao Xu, Zijiang Liu, Yongzhi Qi, Ningxuan Kang, Jianshen Zhang, Wei Qi, Chen Xie, Zuo-Jun Max Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12443v1)