---
title: Scale-invariant Optimal Sampling for Rare-events Data with Sparse Models
published: 2026-08-23T21:03:34Z
authors: Jing Wang, HaiYing Wang, Qiang Zhang, Hao Helen Zhang
url: http://arxiv.org/abs/2608.22597v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scale-invariant Optimal Sampling for Rare-events Data with Sparse Models

## Abstract
Subsampling is effective in tackling computational challenges for massive data with rare events. Overly aggressive subsampling may adversely affect estimation efficiency, and optimal subsampling is essential to mitigate the information loss. However, existing optimal subsampling probabilities depend on data scales, and some scaling transformations may result in inefficient subsamples. This problem is more significant when there are inactive features, because their influence on the subsampling probabilities can be arbitrarily magnified by inappropriate scaling transformations. We tackle this challenge and introduce a scale-invariant optimal subsampling function in the context of sparse models, where inactive features are commonly assumed. Instead of focusing on estimating model parameters, we define an optimal subsampling function to minimize the prediction error, using adaptive lasso to outline the estimation procedure and study its theoretical guarantee. We first introduce the adaptive lasso estimator for rare-events data and establish its oracle properties, thereby validating the use of subsampling. Then we derive a scale-invariant optimal subsampling function that minimizes the prediction error of the inverse probability weighted (IPW) adaptive lasso. Finally, we present an estimator based on the maximum sampled conditional likelihood (MSCL) to further improve the estimation efficiency. We conduct numerical experiments using both simulated and real-world data sets to demonstrate the performance of the proposed methods.

## Metadata
- **Published**: 2026-08-23T21:03:34Z
- **Authors**: Jing Wang, HaiYing Wang, Qiang Zhang, Hao Helen Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22597v1)