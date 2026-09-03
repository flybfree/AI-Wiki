---
title: RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations in Large Vision-Language Models
published: 2026-09-02T15:40:40Z
authors: Canjie Liu, Jiawen Kang, Jinbo Wen, Zishao Zhong
url: http://arxiv.org/abs/2609.02731v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations in Large Vision-Language Models

## Abstract
Large vision-language models have achieved remarkable success in vision-language tasks. However, they remain prone to Visual Hallucinations (VHs), undermining their reliability in real-world applications. Existing solutions typically require curated datasets, additional training, or multi-round decoding, resulting in considerable computational overhead. In this paper, we propose \textbf{RVSD} (\underline{R}etrieval \underline{V}ision \underline{S}parse \underline{D}ecoding), a training-free and plug-and-play decoding framework that, for the first time, unifies token sparsification and \textbf{Semantic-Space Visual Retrieval} (SSVR) within a single decoding pass. Within RVSD, we introduce a \textbf{semantics-directed token selection} strategy that selectively sparsifies redundant tokens while preserving critical visual information. We further propose the SSVR mechanism, which reformulates visual compensation as an on-demand cross-modal retrieval process within a shared semantic space. Extensive experiments demonstrate that RVSD achieves state-of-the-art performance in mitigating VHs while maintaining robust suppression capabilities under long-context generation settings. Our code is available here.\footnote{https://github.com/canjie-liu/RVSD}

## Metadata
- **Published**: 2026-09-02T15:40:40Z
- **Authors**: Canjie Liu, Jiawen Kang, Jinbo Wen, Zishao Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02731v1)