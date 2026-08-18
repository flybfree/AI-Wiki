---
title: Conditional Evaluation of Language Models with Cheap Auxiliary Signals
published: 2026-08-17T07:44:22Z
authors: Zhi Zhang, Lingfeng Lyu, Yue Kang, Doudou Zhou
url: http://arxiv.org/abs/2608.16210v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conditional Evaluation of Language Models with Cheap Auxiliary Signals

## Abstract
Aggregate accuracy hides where models succeed and fail. Estimating conditional performance profiles from gold labels alone is expensive, while cheap auxiliary signals such as LLM-judge scores, pairwise comparisons, confidence scores, and judge-disagreement features can be collected for every benchmark item but are often biased or miscalibrated. We propose LACE (Local Augmented Control-Variate Evaluation), a semi-supervised estimator for conditional LLM evaluation. The key step is local centering: after subtracting the conditional mean of a cheap signal within the target profile region, any linear augmentation has zero conditional mean and therefore cannot change the estimand. The augmentation coefficient is used only for efficiency, and a local ridge control variate combines a gold-label residual mean from the labeled subset with a cheap-signal mean from the full item pool. We prove calibration-free identification, unbiasedness for grouped profiles, local oracle optimality within centered linear augmentations, and first-order adaptivity to the estimated coefficient. The resulting gain formula is governed by a population local $R^2$, which characterizes how the efficiency attainable from the cheap signals varies across profile values. We also derive corresponding estimators for direct paired model gaps and deployment-weighted scores. We empirically evaluate the primary performance-profile estimator on MATH-500, ScienceQA, MMLU, WinoGrande, HellaSwag, TruthfulQA, GSM8K, and ARC.

## Metadata
- **Published**: 2026-08-17T07:44:22Z
- **Authors**: Zhi Zhang, Lingfeng Lyu, Yue Kang, Doudou Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16210v1)