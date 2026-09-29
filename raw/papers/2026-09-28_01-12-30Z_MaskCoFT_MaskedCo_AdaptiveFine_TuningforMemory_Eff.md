---
title: MaskCoFT: Masked Co-Adaptive Fine-Tuning for Memory-Efficient MoE Inference
published: 2026-09-28T01:12:30Z
authors: Junfeng Wu, Zehao Fan, Hadjer Benmeziane, Kaoutar El Maghraoui, Liu Liu, Yinan Wang
url: http://arxiv.org/abs/2609.34077v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MaskCoFT: Masked Co-Adaptive Fine-Tuning for Memory-Efficient MoE Inference

## Abstract
Mixture-of-experts (MoE) language models often exceed the memory of a single GPU. Expert offloading keeps most experts in host memory and loads them on demand, so decoding speed depends on how many experts each token must fetch. Caching and prefetching reduce this cost only as far as the routing allows. Router-only fine-tuning can reshape the routing to reuse experts, but it keeps the experts frozen, so they cannot adapt to the tokens the new routing sends them. We propose MaskCoFT, a masked co-adaptive fine-tuning method that trains routers and experts together with the cross-entropy loss alone. During fine-tuning, a learnable binary mask restricts the Top-K routing of each layer to a subset of experts, and the experts adapt to the tokens redirected to them. At inference, the learned mask becomes a soft prior that re-ranks experts, so every expert remains selectable. We simulate a GPU cache of 4 experts per layer for Mixtral-8x7B and 12 for DeepSeek-V2-Lite. MaskCoFT cuts expert fetches per token by 23.7% and 10.1% relative to the base model. In real offloading system serving, it lowers the time per output token by up to 16.4% and 5.5%, respectively. Its average accuracy over nine benchmarks stays above the base model by 0.92 and 0.53 points.

## Metadata
- **Published**: 2026-09-28T01:12:30Z
- **Authors**: Junfeng Wu, Zehao Fan, Hadjer Benmeziane, Kaoutar El Maghraoui, Liu Liu, Yinan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34077v1)