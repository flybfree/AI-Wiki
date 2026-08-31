---
title: Dynamic Alignment Compensation for Hallucination Mitigation in Large Vision-Language Models
published: 2026-08-28T08:21:31Z
authors: Kairong Yu, Zixin Zhu, Le Yu, Hongwei Wang
url: http://arxiv.org/abs/2608.28058v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic Alignment Compensation for Hallucination Mitigation in Large Vision-Language Models

## Abstract
Large Vision-Language Models (LVLMs) remain prone to hallucinations, producing responses that are irrelevant or inconsistent with the multimodal input. Existing mitigation methods mainly rely on external supervision, output calibration, or attention regulation, leaving the internal representation dynamics of autoregressive generation underexplored. We identify an inference-time failure mode in which cross-modal representations degrade across decoder layers and drift across generation steps, destabilizing token prediction and increasing hallucination risk. We propose \emph{Dynamic Alignment Compensation} (DAC), a training-free inference-time method that detects representation divergence and selectively applies lightweight residual compensation. DAC combines Layer-wise Semantic Compensation to mitigate inter-layer degradation with Sequential Semantic Correction to constrain temporal drift. Experiments on nine hallucination-focused and general-purpose multimodal benchmarks across multiple LVLM backbones show that DAC consistently reduces hallucinations while maintaining strong overall performance.

## Metadata
- **Published**: 2026-08-28T08:21:31Z
- **Authors**: Kairong Yu, Zixin Zhu, Le Yu, Hongwei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28058v1)