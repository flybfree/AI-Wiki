---
title: TopoGR: Revealing and Preserving Latent Structure of Semantic ID in Generative Recommendation
published: 2026-07-28T02:45:33Z
authors: Ziyu Zheng, Zhengshun Du, Yaming Yang, Bin Tong, Guan Wang, Meng Yan, Ziyu Guan, Wei Zhao
url: http://arxiv.org/abs/2607.25216v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TopoGR: Revealing and Preserving Latent Structure of Semantic ID in Generative Recommendation

## Abstract
Semantic ID-based generative recommendation tokenizes each item into a sequence of discrete semantic IDs and predicts the next item by generating semantic IDs. However, existing methods typically regard SIDs as independent discrete symbols, while often overlooking the topology of the learned semantic ID space. We identify a structural mismatch between tokenization and generation: the tokenizer learns a structured code space with semantic neighborhood relations, whereas the generator consumes semantic ID tokens as independent categorical symbols. Consequently, item relatedness is reduced to exact semantic ID overlap, making it difficult to identify semantically similar items whose semantic IDs do not overlap. To address this issue, we propose TopoGR, a topology-preserving generative recommendation framework based on Bit-decomposable Semantic ID(Binary SID). Each Binary SID is learned in a bit-decomposable form and can be deterministically converted to a standard integer SID, while exposing an explicit Hamming geometry. TopoGR exploits this topology at three stages: binary SID features preserve Hamming proximity at the input layer; Hamming soft targets inject topology-aware supervision; and Hamming-consistent reranking aligns candidate items with the predicted binary prototype during inference. We further verify that the Hamming topology can capture item relatedness beyond exact SID matching. Experiments on four benchmark datasets show that TopoGR consistently outperforms existing state-of-the-art baselines in recommendation performance.

## Metadata
- **Published**: 2026-07-28T02:45:33Z
- **Authors**: Ziyu Zheng, Zhengshun Du, Yaming Yang, Bin Tong, Guan Wang, Meng Yan, Ziyu Guan, Wei Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25216v1)