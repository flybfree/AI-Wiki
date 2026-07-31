---
title: QQWorld: Quantile-Quantile Matching for World Model Regularization
published: 2026-07-30T16:00:39Z
authors: Zhoushun Yu, Xiaoyu Hu, Xiangyu Xu
url: http://arxiv.org/abs/2607.28415v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QQWorld: Quantile-Quantile Matching for World Model Regularization

## Abstract
Latent world models enable efficient planning by predicting future states in a compact representation space, but their performance depends critically on the quality of the learned latent distribution. LeWorldModel (LeWM) regularizes its latents toward an isotropic Gaussian using the Epps-Pulley (EP) objective. We show that the corrective gradients of EP rapidly vanish for isolated tail samples, leaving heavy-tailed deviations insufficiently controlled. To address this limitation, we propose QQWorld, which replaces EP with a quantile-quantile matching objective that directly aligns projected latent samples with rank-matched Gaussian quantiles, thereby maintaining effective corrective gradients in the tails. We further develop cross-batch QQ, which enlarges the effective ranking pool using detached samples from previous batches, and characterize its bias-variance trade-off. Across four control environments, QQWorld effectively improves the average planning success rate of LeWM, while consistently yielding better Gaussian alignment and thinner latent tails.

## Metadata
- **Published**: 2026-07-30T16:00:39Z
- **Authors**: Zhoushun Yu, Xiaoyu Hu, Xiangyu Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28415v1)