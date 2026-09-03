---
title: hLLM: Single Pass Decoding for Generative Reranking
published: 2026-09-01T19:30:04Z
authors: Emil Laftchiev, Prachi Agrawal, Moe Kayali, Bixing Yan, Qi Xu, Zijie Lei, Chen Qiu, Zhi Hua, Ke Li, Luke Simon
url: http://arxiv.org/abs/2609.01807v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# hLLM: Single Pass Decoding for Generative Reranking

## Abstract
Large language models (LLMs) achieve state-of-the-art generative ranking quality, but the ranking they produce must be decoded, and autoregressive decoding spends one sequential forward pass per emitted token. We observe that the only tokens a ranker must emit are the $N$ ordinal values naming the items in ranked order, and that this narrow, permutation-structured output format admits decoding strategies which are much more efficient than left-to-right generation. We introduce hLLM (Hungarian LLM), a format-specialized decoding strategy that decodes all $N$ ordinals in $O(1)$ forward passes. hLLM reads an $N \times K$ item-position score matrix off the LLM's prefill hidden states with a lightweight self-attention head, then decodes the ordinals as the optimal bipartite assignment of that matrix via the Hungarian algorithm, yielding a valid permutation by construction rather than by repair. Through a systematic study of training signals and backbone adaptation, we show that LoRA-based fine-tuning combined with teacher ranking distillation reaches 28 ms end-to-end inference, a speed-up of $64\times$ while maintaining ranking quality on par with the teacher. We provide a complete ablation decomposing the contributions of architecture, training signal, and backbone adaptation. Our framework connects generative ranking to combinatorial optimization, opening a path toward other $O(1)$-decode mechanisms for real-time ranking.

## Metadata
- **Published**: 2026-09-01T19:30:04Z
- **Authors**: Emil Laftchiev, Prachi Agrawal, Moe Kayali, Bixing Yan, Qi Xu, Zijie Lei, Chen Qiu, Zhi Hua, Ke Li, Luke Simon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01807v1)