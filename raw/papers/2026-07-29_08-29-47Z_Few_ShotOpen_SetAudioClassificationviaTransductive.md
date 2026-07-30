---
title: Few-Shot Open-Set Audio Classification via Transductive Prototype Refinement and Class Logit Enhancement
published: 2026-07-29T08:29:47Z
authors: Tianyan Deng, Yanxiong Li, Rui Gao, Jiahao Du
url: http://arxiv.org/abs/2607.26607v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Few-Shot Open-Set Audio Classification via Transductive Prototype Refinement and Class Logit Enhancement

## Abstract
Few-shot Open-set audio classification requires classifying query samples from known classes with a few labeled support samples while rejecting query samples from unknown classes. Transductive inference jointly observes the full unlabeled query set to improve prototype estimation, yet standard transductive updates do not distinguish known from unknown query samples, leaving prototypes vulnerable to open-set contamination. Drawing on latent-inlierness weighting and decoupled scoring for unknown-class samples, we propose a two-phase transductive method operating over a frozen audio encoder. First, each query sample is assigned a latent inlierness score that down-weights likely unknown-class samples, so that prototype refinement is driven primarily by known-class evidence. The refined prototypes are then directly optimized on a transductive loss combining support cross-entropy, inlierness-weighted conditional entropy minimization, and inlierness-weighted marginal entropy maximization, while open-set rejection uses a prior-adaptive free-energy score that adjusts its threshold with the prior proportion of unknown-class samples, decoupling detection from classification. Experiments on three audio datasets show our method achieves state-of-the-art results for few-shot open-set audio classification under multiple experimental conditions.

## Metadata
- **Published**: 2026-07-29T08:29:47Z
- **Authors**: Tianyan Deng, Yanxiong Li, Rui Gao, Jiahao Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26607v1)