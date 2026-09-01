---
title: MERIT: Mitigating Exposure Bias in Generative XMC for User-Interest Propensity Modeling
published: 2026-08-28T23:03:14Z
authors: Abhinav Mahajan, Arindam Sarkar, Prakash Mandayam Comar
url: http://arxiv.org/abs/2608.28931v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MERIT: Mitigating Exposure Bias in Generative XMC for User-Interest Propensity Modeling

## Abstract
Matching users to interest categories at scale is central to personalized shopping, but the task is challenging in large e-commerce platforms, where label spaces continually evolve and user-interest signals are sparse and long-tailed. Autoregressive language models are appealing because their world knowledge and semantic priors over descriptors generalize across extreme label spaces and accommodate multiple valid label assignments. Yet under teacher-forced fine-tuning, inference-time predictions become part of the conditioning context: early errors steer later outputs toward co-occurring labels, over-generating near-correlates and missing unrelated true interests. We present MERIT, a framework for user-interest propensity modeling that mitigates this exposure bias through a self-correction objective. A permutation-invariant multi-target loss over shuffled mixtures of gold and mined hard-negative labels exposes the generator to erroneous prefixes while preserving the efficiency of teacher-forced training. This training objective concentrates supervision at classification positions, yielding propensity-aligned hidden states powering a lightweight scorer for bidirectional retrieval (interests for users and users for interests). On a proprietary e-commerce dataset with 250k+ interest categories, MERIT improves global recall by at least 11.9% and average Hit@k by 6.1%. In production A/B tests, it achieves +0.26% gain in user conversion.

## Metadata
- **Published**: 2026-08-28T23:03:14Z
- **Authors**: Abhinav Mahajan, Arindam Sarkar, Prakash Mandayam Comar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28931v1)