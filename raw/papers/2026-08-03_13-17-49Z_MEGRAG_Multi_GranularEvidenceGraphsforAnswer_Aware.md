---
title: MEGRAG: Multi-Granular Evidence Graphs for Answer-Aware Multi-Hop RAG
published: 2026-08-03T13:17:49Z
authors: Weidong Bao, Yingying Sun, Jun Yang, Yilin Wang, Zili Wei, Yubin Bao, Fangling Leng, Minghe Yu, Tiancheng Zhang, Ge Yu
url: http://arxiv.org/abs/2608.02195v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MEGRAG: Multi-Granular Evidence Graphs for Answer-Aware Multi-Hop RAG

## Abstract
Multi-hop question answering is a fundamental challenge in retrieval-augmented generation (RAG), because deriving an answer requires integrating dispersed evidence. Iterative RAG (iRAG) is widely used for this challenge, but existing methods have two limitations. First, most methods still support each reasoning step with single-granularity evidence, making it difficult to balance information density and contextual noise. Second, existing methods often answer the original question only after aggregating evidence retrieved across intermediate steps, so redundant evidence and intermediate retrieval errors may accumulate and degrade the final answer. To address these limitations, we propose MEGRAG, an answer-aware framework that represents multi-hop reasoning as a path-structured multi-granular evidence graph. Offline, MEGRAG links passages to their sentences and extracted triples through a cross-granularity index. Online, it retrieves passages for the current query and selects aligned evidence, starting with compact triples and adding sentence or passage context as needed. MEGRAG uses the resulting intermediate answer and prior reasoning to decide whether the Initial Query has been resolved. If not, it identifies the missing information and formulates a focused next query; otherwise, it stops retrieval and returns the answer. Extensive experiments demonstrate consistent gains over a diverse set of RAG baselines.

## Metadata
- **Published**: 2026-08-03T13:17:49Z
- **Authors**: Weidong Bao, Yingying Sun, Jun Yang, Yilin Wang, Zili Wei, Yubin Bao, Fangling Leng, Minghe Yu, Tiancheng Zhang, Ge Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02195v1)