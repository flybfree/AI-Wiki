---
title: Token-Level Diagnosis of Sycophancy in LLMs with Attribution-Guided Steering
published: 2026-07-31T00:05:36Z
authors: Hieu Nguyen, Mahammed Kamruzzaman, Anshuman Chhabra, Gene Louis Kim
url: http://arxiv.org/abs/2607.28906v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Token-Level Diagnosis of Sycophancy in LLMs with Attribution-Guided Steering

## Abstract
Sycophancy refers to the tendency for large language models (LLMs) to match user beliefs at the cost of factual correctness, thereby undermining model reliability. Prior work on evaluating sycophancy in LLMs aims to assess whether a model's output matches an authority's claim, but cannot reveal which part of the prompt drives this sycophantic behavior. To bridge this gap, we investigate the relationship of sycophantic responses with an authority's credentials, their assertive claim, and the problem statement. We introduce the Authority Share Index (ASI), an Integrated Gradients-based token attribution method, which measures the degree to which a model's decision is driven by authority-related text. Through extensive experiments across five models and 30 test configurations, we find that sycophantic responses consistently direct more attention toward authority tokens than resistant ones. Moreover, our token attribution method reveals that for the sycophantic cases, the claim asserted by the authority receives more attention than the authority's credentials. Building on these findings, we propose attribution-guided contrastive activation steering to mitigate LLM sycophancy. Our method constructs a steering vector from high-attribution tokens of sycophantic and resistant responses, selectively pushing models toward resistance. This enables inference-time steering without retraining, lowering sycophancy from 96% to 25% in the strongest case. Together, our results show that token-level attribution can both explain what drives sycophancy and directly inform a practical intervention.

## Metadata
- **Published**: 2026-07-31T00:05:36Z
- **Authors**: Hieu Nguyen, Mahammed Kamruzzaman, Anshuman Chhabra, Gene Louis Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28906v1)