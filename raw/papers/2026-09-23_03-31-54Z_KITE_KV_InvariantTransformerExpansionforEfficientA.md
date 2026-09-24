---
title: KITE: KV-Invariant Transformer Expansion for Efficient Agentic LLM Scaling
published: 2026-09-23T03:31:54Z
authors: Zhiheng Hu, Yixun Wei, Jian Zhou, Yizhuang Zhou, Ji Li, Xing Chen, Yang Li, Bojun Wang, Yibo Zhu, Xiangyu Zhang, Daxin Jiang
url: http://arxiv.org/abs/2609.27294v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KITE: KV-Invariant Transformer Expansion for Efficient Agentic LLM Scaling

## Abstract
Scaling a language model is not only a question of final quality: the architectural choice determines how much computation is spent during training, prompt processing, and autoregressive decoding to achieve certain model quality. An ideal model architecture should lower all above computation costs to facilitate scaling to a larger model, while ensure the larger model indeed outperforms smaller baselines. We introduce KV-Invariant Transformer Expansion (KITE), a scaling paradigm that achieves this goal. It trains the model from a smaller size to a larger size (i.e., saving training costs via upcycling), while places newly added parameters in regions that do not affect attention KV. Consequently, during inference, prefilling KV only relies on the smaller part of the model, so the inference costs are saved. As a concrete instantiation, we present Step Scale Transformer (SST), a two-tower decoder in which one tower produces KV and the other reads them. At comparable cumulative training compute, SST, a 67B MoE model with 2.15B active body parameters per decode token, achieves lower training loss than 47B and 63B MoE Transformers with 1.48B and 2.02B active body parameters, respectively, while reducing estimated inference cost by 6.7% and 31.6%.

## Metadata
- **Published**: 2026-09-23T03:31:54Z
- **Authors**: Zhiheng Hu, Yixun Wei, Jian Zhou, Yizhuang Zhou, Ji Li, Xing Chen, Yang Li, Bojun Wang, Yibo Zhu, Xiangyu Zhang, Daxin Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27294v1)