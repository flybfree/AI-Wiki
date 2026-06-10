---
title: 'InA-Probe: Instruction-Aware Active Probing for Time Series Forecasting with LLMs'
published: 2026-06-07T12:27:13Z
authors: Peiliang Gong, Emadeldeen Eldele, Chenyu Liu, Ziyu Jia, Yi Ding, Xinliang Zhou, Lianchao Gu, Qi Zhu, Yang Liu, Daoqiang Zhang, Xiaoli Li
url: http://arxiv.org/abs/2606.08601v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# InA-Probe: Instruction-Aware Active Probing for Time Series Forecasting with LLMs

## Abstract
Large Language Models (LLMs) have recently demonstrated impressive potential for time series forecasting. However, existing methods predominantly rely on passive modality alignment or static task reprogramming, which often fail to capture fine-grained, non-stationary temporal patterns or to adapt to nuanced task intents. In this paper, we propose Instruction-aware Active Probing (InA-Probe), which shifts the paradigm from passive alignment toward an active, instruction-driven probing mechanism. Specifically, we design a Multi-Level Instruction Injection mechanism that enriches the model with both global task objectives and fine-grained, patch-level semantic priors. Building on this, an Adaptive Query Generation module produces sample-specific probes that are dynamically modulated by the temporal context. These probes are then refined through a dual-stage attention process: they first internalize task-specific intents via Instruction-Aware Self-Attention, and subsequently interrogate the projected temporal representations through Temporal Cross-Attention to extract salient patterns. Comprehensive experiments on seven real-world benchmarks show that InA-Probe consistently outperforms state-of-the-art deep learning and LLM-based baselines, excelling in both one-for-all generalization and zero-shot transfer while reducing forecasting error by up to 37\% in challenging cross-domain scenarios. Ablation studies further confirm that the synergy between adaptive querying and fine-grained instructions is key to unlocking the reasoning power of LLMs for complex time series.

## Metadata
- **Published**: 2026-06-07T12:27:13Z
- **Authors**: Peiliang Gong, Emadeldeen Eldele, Chenyu Liu, Ziyu Jia, Yi Ding, Xinliang Zhou, Lianchao Gu, Qi Zhu, Yang Liu, Daoqiang Zhang, Xiaoli Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.08601v1)