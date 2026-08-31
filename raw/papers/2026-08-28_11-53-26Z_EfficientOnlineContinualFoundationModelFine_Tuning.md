---
title: Efficient Online Continual Foundation Model Fine-Tuning for Predictive Process Monitoring
published: 2026-08-28T11:53:26Z
authors: Sjoerd van Straten, Marwan Hassani
url: http://arxiv.org/abs/2608.28237v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient Online Continual Foundation Model Fine-Tuning for Predictive Process Monitoring

## Abstract
Predictive Process Monitoring (PPM) models are increasingly deployed in dynamic environments where concept drift causes the underlying process distribution to shift over time. While recent work has moved toward online continual learning, existing methods train compact, task-specific networks entirely from scratch, leaving a persistent cold-start problem. Foundation Models (FMs) offer a compelling solution to this problem, but their continual fine-tuning in the process mining domain remains unexplored. We propose COMPASS (Continual Online foundation Model-based PPM with Adaptive SubSpaces), the first framework for online continual fine-tuning of FMs for PPM. COMPASS adapts loss-plateau drift detection to autonomously identify task boundaries in event streams and maintains a unified knowledge subspace including both pre-trained and task-specific directions. We evaluate our approach on nine event streams covering synthetic and real-world concept drift scenarios, across task-free and task-aware settings with multiple backbones and with consistent hyperparameter tuning across all methods. Our approach outperforms three SOTA non-FM competitors and two update strategy baselines, with particularly strong gains on streams exhibiting recurrent drift and complex, long-running cases, while incurring acceptable computational overhead compared to the non-FM competitors.

## Metadata
- **Published**: 2026-08-28T11:53:26Z
- **Authors**: Sjoerd van Straten, Marwan Hassani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28237v1)