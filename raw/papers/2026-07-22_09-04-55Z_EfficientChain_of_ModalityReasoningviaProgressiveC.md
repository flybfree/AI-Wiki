---
title: Efficient Chain-of-Modality Reasoning via Progressive Compression for Spoken Language Models
published: 2026-07-22T09:04:55Z
authors: Pengchao Feng, Chao-Hong Tan, Qian Chen, Wen Wang, Xiangang Li, Xie Chen
url: http://arxiv.org/abs/2607.19932v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient Chain-of-Modality Reasoning via Progressive Compression for Spoken Language Models

## Abstract
Spoken language models (SLMs) enable natural human-computer interaction, but their reasoning ability still lags behind that of text-based large language models, especially on spoken mathematical question answering tasks. One important reason is that SLMs reason over purely verbalized mathematical expressions, which are harder to interpret than symbolic text. However, directly transferring text-based reasoning to SLMs is nontrivial due to architectural constraints and the additional computational requirements. To address this challenge, we propose Efficient Chain-of-Modality Reasoning (ECoM Reasoning), the first framework to introduce compressed reasoning into SLMs. By compressing the textual component so that it jointly serves as speech guidance and reasoning representation, ECoM Reasoning improves reasoning accuracy while using a smaller token budget than the standard Chain-of-Modality (CoM) architecture, which generates intermediate text before speech. To train this capability, we further propose Progressive Compression, a curriculum-based strategy that gradually trains the model from full-form reasoning to compressed reasoning. Experiments on spoken mathematical question answering benchmarks show that ECoM Reasoning improves accuracy by 21% over standard CoM without explicit reasoning, and by 3% over CoM with full reasoning traces while using only 40% of the text tokens, demonstrating that it enhances SLM reasoning while remaining inference-efficient.

## Metadata
- **Published**: 2026-07-22T09:04:55Z
- **Authors**: Pengchao Feng, Chao-Hong Tan, Qian Chen, Wen Wang, Xiangang Li, Xie Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19932v1)