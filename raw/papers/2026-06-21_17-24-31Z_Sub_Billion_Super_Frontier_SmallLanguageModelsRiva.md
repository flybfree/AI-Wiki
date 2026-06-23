---
title: Sub-Billion, Super-Frontier: Small Language Models Rival Zero-Shot Frontier LLMs on General and Literary Relation Extraction
published: 2026-06-21T17:24:31Z
authors: Despina Christou, Grigorios Tsoumakas
url: http://arxiv.org/abs/2606.22606v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sub-Billion, Super-Frontier: Small Language Models Rival Zero-Shot Frontier LLMs on General and Literary Relation Extraction

## Abstract
Large language models (LLMs) achieve strong relation extraction (RE), but their computational demands and reliance on proprietary APIs limit deployment in resource-constrained or privacy-sensitive settings. We investigate how far small language models (SLMs) can close this gap across general-domain and literary text. We evaluate five models from 360M to 3B parameters under three domain-composition regimes and two prompt-conditioned tuning styles (30 configurations), comparing them with zero-shot frontier LLMs and a discriminative RoBERTa baseline. Across nine benchmarks, the best sub-billion model, Qwen2.5-0.5B fine-tuned on pooled general-domain data, achieves a general-domain positive-class micro-F1 of 0.83, versus 0.69 for GPT-5.4 and 0.66 for Claude Sonnet 4.6 evaluated zero-shot. This does not imply that SLMs are intrinsically stronger; rather, targeted task adaptation enables 4-bit models deployable on a single consumer GPU to outperform general-purpose frontier systems under this protocol. An in-domain RoBERTa baseline also exceeds both frontier models, indicating that the gain stems from task adaptation rather than generative decoding. On literary RE, tuned SLMs reach 0.92 on the human-annotated Biographical benchmark versus 0.83 for GPT-5.4, and 0.833 versus 0.578 on the two-benchmark literary average. A targeted domain-adaptive pretraining case study yields no practically meaningful gain over supervised fine-tuning, while the cleanest within-family scale comparison shows only marginal improvement. These results show that, when task-specific data are available, compact task-adapted models can provide accurate, private, and hardware-efficient RE.

## Metadata
- **Published**: 2026-06-21T17:24:31Z
- **Authors**: Despina Christou, Grigorios Tsoumakas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.22606v1)