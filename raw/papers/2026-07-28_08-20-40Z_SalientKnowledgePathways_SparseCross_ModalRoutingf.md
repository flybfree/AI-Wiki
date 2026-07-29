---
title: Salient Knowledge Pathways: Sparse Cross-Modal Routing for Efficient Knowledge-Intensive Multimodal Question Answering
published: 2026-07-28T08:20:40Z
authors: Noor Islam S. Mohammad, Uluğ Bayazıt
url: http://arxiv.org/abs/2607.25422v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Salient Knowledge Pathways: Sparse Cross-Modal Routing for Efficient Knowledge-Intensive Multimodal Question Answering

## Abstract
Knowledge-intensive multimodal question answering (KI-MMQA) sits at the intersection of three expensive primitives: long visual token sequences, dense retrieval over large external corpora, and full cross-modal fusion. Existing systems pay all three costs uniformly per query, even though only a small fraction of visual content and retrieved knowledge is actually relevant to any given question. We introduce SKIP (Salient Knowledge-Injected Pathways), a unified inference architecture that routes computation along sparse pathways jointly conditioned on the question, the image, and a difficulty estimate. SKIP combines question-guided visual token pruning, region-conditional sparse retrieval, bipartite sparse cross-attention, and speculative knowledge verification with an adaptive budget controller that allocates compute proportional to predicted question difficulty. We derive an information-bottleneck bound showing that the optimal visual sparsity rate scales as $O(1/\sqrt{N})$ under realistic question-image mutual-information assumptions, with retained accuracy guarantees. Across five KI-MMQA benchmarks (OK-VQA, A-OKVQA, InfoSeek, Encyclopedic-VQA, and ViQuAE), SKIP matches or exceeds the accuracy of strong dense baselines while using $3.4$--$6.8\times$ fewer FLOPs and $2.7\times$ less end-to-end latency. Code available at: https://pmlrbd.github.io/skip/

## Metadata
- **Published**: 2026-07-28T08:20:40Z
- **Authors**: Noor Islam S. Mohammad, Uluğ Bayazıt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25422v1)