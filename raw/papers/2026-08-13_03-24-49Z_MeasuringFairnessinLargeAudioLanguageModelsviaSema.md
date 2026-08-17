---
title: Measuring Fairness in Large Audio Language Models via Semantic-Aware Bias Estimation
published: 2026-08-13T03:24:49Z
authors: Zhe Liu
url: http://arxiv.org/abs/2608.13624v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring Fairness in Large Audio Language Models via Semantic-Aware Bias Estimation

## Abstract
Large Audio Language Models (LALMs) have seen increasing use for audio understanding tasks such as speech recognition and audio question answering, raising concerns about fairness across demographic subgroups. Fairness evaluation in spoken-input settings is challenging due to confounding factors, including semantic variation in spoken content and speaker-specific characteristics. Ignoring these factors can result in misleading conclusions about model bias. We propose a semantic-aware mixed-effects regression framework for fairness evaluation in LALMs that explicitly accounts for these confounders. Our approach incorporates sentence-level semantic embeddings of reference text as covariates and models speaker identity as a random effect. Notably, semantic representations are extracted from the same LALM under evaluation, enabling semantic control over variation as perceived by the model itself. Experiments on simulated data and real-world benchmarks demonstrate that the proposed approach substantially reduces spurious fairness findings and yields more robust and interpretable estimates of subgroup performance differences.

## Metadata
- **Published**: 2026-08-13T03:24:49Z
- **Authors**: Zhe Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13624v1)