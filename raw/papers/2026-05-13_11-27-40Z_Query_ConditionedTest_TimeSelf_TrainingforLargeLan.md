---
title: Query-Conditioned Test-Time Self-Training for Large Language Models
published: 2026-05-13T11:27:40Z
authors: Chaehee Song, Minseok Seo, Yeeun Seong, Doyi Kim, Changick Kim
url: http://arxiv.org/abs/2605.13369v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Query-Conditioned Test-Time Self-Training for Large Language Models

## Abstract
Large language models (LLMs) are typically deployed with fixed parameters, and their performance is often improved by allocating more computation at inference time. While such test-time scaling can be effective, it cannot correct model misconceptions or adapt the model to the specific structure of an individual query. Test-time optimization addresses this limitation by enabling parameter updates during inference, but existing approaches either rely on external data or optimize generic self-supervised objectives that lack query-specific alignment. In this work, we propose Query-Conditioned Test-Time Self-Training (QueST), a framework that adapts model parameters during inference using supervision derived directly from the input query. Our key insight is that the input query itself encodes latent signals sufficient for constructing structurally related problem--solution pairs. Based on this, QueST generates such query-conditioned pairs and uses them as supervision for parameter-efficient fine-tuning at test time. The adapted model is then used to produce the final answer, enabling query-specific adaptation without any external data. Across seven mathematical reasoning benchmarks and the GPQA-Diamond scientific reasoning benchmark, QueST consistently outperforms strong test-time optimization baselines. These results demonstrate that query-conditioned self-training is an effective and practical paradigm for test-time adaptation in LLMs.

## Metadata
- **Published**: 2026-05-13T11:27:40Z
- **Authors**: Chaehee Song, Minseok Seo, Yeeun Seong, Doyi Kim, Changick Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.13369v1)