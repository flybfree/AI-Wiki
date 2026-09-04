---
title: Lngram v2: Latent N-Gram Memory with Interpretable Discrete Representations
published: 2026-09-03T06:33:23Z
authors: Yunao Zheng, Bin Wen, Xiaojie Wang
url: http://arxiv.org/abs/2609.03426v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lngram v2: Latent N-Gram Memory with Interpretable Discrete Representations

## Abstract
Transformers lack a native lookup mechanism, requiring repeated dense computation to recognize and reuse local static patterns. Lngram v1 introduces tokenizer-independent conditional memory through discrete latent n-gram addressing, but its memory capacity is coupled with the backbone width, limiting scalability due to high parameter and activation costs. We propose Lngram v2, which decouples the number of routes, memory dimension, and backbone width, and introduces a context-aware grouped-query attention readout to scale memory capacity independently. A zero-value Sink and counterfactual surrogate gradients further improve readout selectivity and routing trainability while preserving hard discrete addressing. Experiments across vision--language models (VLMs) of different scales show consistent improvements, including successful scaling to a 30B-parameter model. Compared with Lngram v1, Lngram v2 substantially reduces both total and activated memory parameters while maintaining or improving language modeling performance. Further analysis shows that its discrete IDs preserve substantial semantic structure of continuous hidden states, enabling semantic recovery from IDs alone and stable ID--semantic associations across datasets. These results establish Lngram v2 as an efficient and scalable latent conditional memory mechanism whose discrete addresses also provide a structured interface for analyzing internal model representations.

## Metadata
- **Published**: 2026-09-03T06:33:23Z
- **Authors**: Yunao Zheng, Bin Wen, Xiaojie Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03426v1)