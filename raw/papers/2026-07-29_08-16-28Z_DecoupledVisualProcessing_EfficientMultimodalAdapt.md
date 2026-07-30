---
title: Decoupled Visual Processing: Efficient Multimodal Adaptation via Modality-Specific Transformer Substitution
published: 2026-07-29T08:16:28Z
authors: Mingkuan Feng, Zhengqi Wen, Jianhua Tao
url: http://arxiv.org/abs/2607.26596v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decoupled Visual Processing: Efficient Multimodal Adaptation via Modality-Specific Transformer Substitution

## Abstract
Multimodal large language models (MLLMs) have demonstrated remarkable capabilities by integrating visual and textual understanding within a unified transformer architecture. However, fine-tuning all parameters of these models for visual instruction tuning is computationally expensive and often unnecessary, as the representation requirements for visual and textual tokens diverge significantly in the deeper layers of the network. In this paper, we propose Decoupled Visual Processing (DVP), an efficient training framework that replaces the upper decoder layers of a pretrained LLM with a lightweight, independently trainable single transformer block dedicated exclusively to visual token processing. Specifically, after shared processing through the first half of the decoder layers, visual and textual tokens are split: visual tokens are routed through a newly initialized single transformer block while textual tokens continue through the original frozen decoder layers. The two streams are then concatenated before the language modeling head. During training, only the single transformer block is updated, dramatically reducing the number of trainable parameters. Experiments on the LLaVA-1.5 framework demonstrate that DVP achieves competitive performance on MME, POPE, and ChartQA benchmarks while training only a fraction of the total parameters, suggesting that visual representations in MLLMs can be effectively learned through a decoupled, parameter-efficient pathway.

## Metadata
- **Published**: 2026-07-29T08:16:28Z
- **Authors**: Mingkuan Feng, Zhengqi Wen, Jianhua Tao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26596v1)