---
title: SeqLLM: Augmenting LLMs with Behavioral-Sequence Modeling for High-Stakes Decisions at WeChat Pay
published: 2026-08-04T03:23:12Z
authors: Guilin Li, Jiaxing Zhang, Matthias Hwai Yong Tan, Bo Wang, Weiran Huang
url: http://arxiv.org/abs/2608.03063v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SeqLLM: Augmenting LLMs with Behavioral-Sequence Modeling for High-Stakes Decisions at WeChat Pay

## Abstract
Merchant risk control at large payment platforms screens tens of millions of merchants daily, where false positives harm legitimate merchants and false negatives leave harmful activity undetected. The hardest cases require jointly understanding a merchant's textual profile and long behavioral sequence. Large language models (LLMs) excel at text but cannot natively model such sequences, while adapting them often causes catastrophic forgetting. We present SeqLLM, a framework that adds behavioral-sequence modeling to a pretrained LLM while preserving its language ability. SeqLLM combines three components: a compact discrete vocabulary that represents behavioral events as native tokens; a lightweight projector, trained with a two-stage alignment curriculum, that grounds these tokens in the LLM's semantic space; and prefix-guided capability injection, which acquires sequence-modeling ability through task-prefixed supervised fine-tuning rather than continual pre-training. SeqLLM is deployed at WeChat Pay, screening millions of merchants daily. Against the production DeepSeek-based LLM baseline, it raises screening precision from 92.0% to 97.5%. Its pretrained behavior-token embeddings also improve Precision@Top-0.01% by 26.8 percentage points in a production fraud detector serving billion-scale transaction traffic. Beyond payments, SeqLLM achieves state-of-the-art results on public recommendation benchmarks. On MovieLens and Amazon, it surpasses the strong User-LLM baseline by up to 32% relative Recall@5 while retaining markedly stronger language ability. On RecIF, it improves Pass@32 by 14.2% over the full OneRec-8B pipeline using only one-fifth of its GPU-days.

## Metadata
- **Published**: 2026-08-04T03:23:12Z
- **Authors**: Guilin Li, Jiaxing Zhang, Matthias Hwai Yong Tan, Bo Wang, Weiran Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03063v1)