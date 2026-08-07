---
title: Hierarchical Latent Prediction for Language Models
published: 2026-08-06T09:41:41Z
authors: Chang Shi, Tim Pearce, Manan Tomar, Siddhartha Sen, John Langford
url: http://arxiv.org/abs/2608.05806v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hierarchical Latent Prediction for Language Models

## Abstract
While standard Next-Token Prediction (NTP) lays the foundation of language model pre- training, its teacher-forced training paradigm may not be optimal for long-horizon reasoning and planning. Recent works such as Multi-Token Prediction (MTP) and Next-Latent prediction (NextLat) try to mitigate the problem through predicting multiple future tokens and self-supervised prediction in the latent space. However, those auxiliary objectives either have a limited horizon or suffer from compounding error from multi-step rollout. We introduce Hierarchical Latent Prediction (HiLP), which introduces an auxiliary higher-level abstract latent to help reduce the error accumulation effect in latent-space rollouts. Experiments show that HiLP can lead to longer-horizon coherent belief state representation and demonstrate the effectiveness of our method across coding and multi-step reasoning benchmarks, and offers more speculative decoding efficiency.

## Metadata
- **Published**: 2026-08-06T09:41:41Z
- **Authors**: Chang Shi, Tim Pearce, Manan Tomar, Siddhartha Sen, John Langford
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05806v1)