---
title: Hybrid Latent Attention for Looped Language Models
published: 2026-10-06T08:14:07Z
authors: Yuhan Chen, Siyuan Zhang, Nan Wang, Feiyang Kang, Ruoxi Jia
url: http://arxiv.org/abs/2610.07940v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hybrid Latent Attention for Looped Language Models

## Abstract
Looped language models apply the same stack of layers T times to each token, which deepens the model without adding parameters but multiplies its key-value (KV) cache by T. The larger cache limits how many sequences a GPU can decode at once and slows each decoding step, which reads the whole cache. We propose Hybrid Latent Attention (HLA), which keeps exact keys and values within a sliding window of W recent tokens and stores each older token as a compact latent that the query of each loop reads directly, without reconstructing keys and values. We uptrain HLA on Ouro looped models (T=4) with 1.4B and 2.6B parameters, keeping the pretrained weights frozen and training only the added parameters to reproduce the original attention. The cache shrinks by 10.7x per token, fitting 4.0-8.8x as many concurrent sequences per GPU, and decoding throughput improves by 2.5x at 1K-token contexts and by up to 7.4x at 16K. HLA retains over 97% of the original accuracy on math, knowledge and reasoning benchmarks, and 96-100% on long-context retrieval up to 16K tokens. After supervised fine-tuning, it performs on par with the fine-tuned original model on competition-level math.

## Metadata
- **Published**: 2026-10-06T08:14:07Z
- **Authors**: Yuhan Chen, Siyuan Zhang, Nan Wang, Feiyang Kang, Ruoxi Jia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07940v1)