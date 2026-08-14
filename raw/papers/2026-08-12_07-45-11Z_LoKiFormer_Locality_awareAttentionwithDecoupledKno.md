---
title: LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining
published: 2026-08-12T07:45:11Z
authors: Qiuwu Chen, Zimo Liu, Yuchen Li, Ying Sun, Yifan Zhang, Zhijie Qiu, Zeng You, Ryan Dong, Simeng Ma, Yaofo Chen, Mingkui Tan
url: http://arxiv.org/abs/2608.12419v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining

## Abstract
Large language models (LLMs) have achieved remarkable breakthroughs across various applications. However, their architectures remain inefficient in pretraining due to two main limitations: (i) self-attention lacks an explicit inductive bias for locality, leading to redundant modeling of sequence-internal local information; (ii) mixture-of-experts (MoE) implicitly couples knowledge storage with computational pathways, hindering flexible access to sequence-external global knowledge. To overcome these limitations, we propose LoKiFormer, a novel LLM architecture that augments the standard decoder with two dedicated modules: 1) Local Fusion Attention (LFA), which incorporates a convolutional fusion to attention, explicitly capturing local patterns and allowing the attention to operate on more informative representations; 2) Knowledge Memory Module (KMM), which introduces a parametric key-value memory that explicitly stores global knowledge in addressable slots, decoupling storage from computation and enabling direct knowledge retrieval. Together, these modules enable LoKiFormer to achieve more efficient and effective integration of information at both levels. Experimental results show that LoKiFormer converges 1.33x faster in pre-training than baseline models, underscoring its superiority over existing LLM architectures.

## Metadata
- **Published**: 2026-08-12T07:45:11Z
- **Authors**: Qiuwu Chen, Zimo Liu, Yuchen Li, Ying Sun, Yifan Zhang, Zhijie Qiu, Zeng You, Ryan Dong, Simeng Ma, Yaofo Chen, Mingkui Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12419v1)