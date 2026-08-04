---
title: TRACE-TS: Attribution-Grounded and Traceable Sensor-Language Reasoning for Human Activity Understanding
published: 2026-07-31T18:26:17Z
authors: Sparsh Rastogi, Tanmay Kumar, Baiyu Chen, Jatin Bedi, Zechen Li, Flora D. Salim
url: http://arxiv.org/abs/2608.00200v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACE-TS: Attribution-Grounded and Traceable Sensor-Language Reasoning for Human Activity Understanding

## Abstract
Wearable sensors capture fine-grained motion patterns that support rich behavioral understanding, yet most existing methods reduce these signals to activity labels. Recent LM-based approaches generate natural-language explanations for sensor data, but their reasoning is weakly grounded in the underlying signal, leading to fluent yet unverifiable explanations. We introduce TRACE-TS (Traceable Reasoning with Attribution-Grounded Evidence), a framework for structured and signal-grounded reasoning over wearable time series. TRACE-TS uses attribution from an expert classifier to identify salient spatio-temporal sensor regions, uses them to construct DAG reasoning traces with explicit evidence provenance, and trains a compact language model to generate these traces through gated cross-attention over sensor memory tokens. At inference, the adapted model jointly outputs the activity prediction and its reasoning trace, without requiring attribution computation or teacher guidance. We introduce Semantic Node Match(SNM), an LLM-as-judge metric that diagnoses reasoning fidelity at the observation, inference, and synthesis levels, localizing hallucinated observations and broken evidence chains missed by standard NLG metrics. Across seven wearable benchmarks, TRACE-TS achieves the best average accuracy and F1 among all evaluated methods (84.43%/81.24%), and outperforms the best LLM-based baseline by 17.96% in F1. Our code is available at https://github.com/SparshRastogi/TRACE-TS.

## Metadata
- **Published**: 2026-07-31T18:26:17Z
- **Authors**: Sparsh Rastogi, Tanmay Kumar, Baiyu Chen, Jatin Bedi, Zechen Li, Flora D. Salim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00200v1)