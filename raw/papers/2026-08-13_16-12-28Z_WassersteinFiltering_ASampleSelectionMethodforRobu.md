---
title: Wasserstein Filtering: A Sample Selection Method for Robust Distribution Learning
published: 2026-08-13T16:12:28Z
authors: Yikai Xu, Zhao Chen, Jian Huang
url: http://arxiv.org/abs/2608.13418v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Wasserstein Filtering: A Sample Selection Method for Robust Distribution Learning

## Abstract
Given a dataset where a portion of the samples are contaminated, our goal is to recover the underlying clean population distribution. To this end, we propose Wasserstein Filtering (WF), a novel sample selection framework that discards a fraction of suspicious samples and estimates the target distribution using the empirical measure of the remaining data. The core insight is to select a subset of samples whose empirical distribution maximizes its Wasserstein distance to the fully contaminated empirical distribution, thereby preferentially isolating and removing geometrically influential outliers. To render this optimization computationally tractable, we introduce three algorithms: a marginal screening scheme, SinkMarg, and two joint optimization algorithms, SinkWF and SlicedWF, leveraging entropic optimal transport and sliced Wasserstein approximations, respectively. On the theoretical front, we introduce the Far Exclusion and Local Projection (FELP) contamination model, which characterizes corruptions consisting of well-separated outliers and locally indistinguishable perturbations. Under this model, we prove that the WF estimator achieves minimax optimality over distribution families with bounded covariance. Extensive numerical experiments on synthetic datasets, benchmark anomaly detection suites, and robust generative learning with diffusion models demonstrate that WF serves as a highly practical, model-agnostic preprocessing tool. It delivers competitive outlier detection performance and provides substantial downstream benefits for generative modeling under heavy contamination.

## Metadata
- **Published**: 2026-08-13T16:12:28Z
- **Authors**: Yikai Xu, Zhao Chen, Jian Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13418v1)