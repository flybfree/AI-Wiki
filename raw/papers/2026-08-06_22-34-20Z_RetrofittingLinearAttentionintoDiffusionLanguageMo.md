---
title: Retrofitting Linear Attention into Diffusion Language Models
published: 2026-08-06T22:34:20Z
authors: Jinha Kim, Younghun Roh, Jaeyeon Kim
url: http://arxiv.org/abs/2608.06628v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrofitting Linear Attention into Diffusion Language Models

## Abstract
Diffusion language models (dLLMs) offer a promising alternative to autoregressive models by accelerating inference through parallel decoding. Recent dLLMs commonly use blockwise semi-autoregressive decoding, generating blocks autoregressively while denoising tokens within each active block in parallel. However, despite KV caching, each denoising step still attends to all previous blocks, repeatedly incurring prefix-attention cost. Motivated by this bottleneck, we ask whether dLLM inference can be further accelerated by linearizing attention over previous blocks. We introduce block-hybrid attention, which retains exact softmax attention within the active denoising block while applying linear attention over previous blocks. We show that this hybrid attention can be retrofitted into a pretrained dLLM with minimal post-training: LLaDA-Hybrid replaces 6 of the 20 attention layers in LLaDA~2.1, a 16B open-source dLLM, largely following LoLCAT (Zhang et al, 2024). The conversion takes only approximately 60 hours while preserving benchmark performance: 72.0% vs. 75.6% on HumanEval, 63.0% vs. 57.7% on MBPP+, and 86.7% vs. 88.3% on CMATH. With a Triton implementation, LLaDA-Hybrid achieves up to $1.7\times$ higher decoding throughput and supports more concurrent requests before exhausting memory, showing that pretrained dLLMs can be efficiently linearized for faster inference. Our code is available at: https://github.com/Diuven/LLaDA-Hybrid.

## Metadata
- **Published**: 2026-08-06T22:34:20Z
- **Authors**: Jinha Kim, Younghun Roh, Jaeyeon Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06628v1)