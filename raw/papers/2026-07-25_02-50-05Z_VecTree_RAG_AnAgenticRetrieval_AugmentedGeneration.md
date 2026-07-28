---
title: VecTree-RAG: An Agentic Retrieval-Augmented Generation Framework Combining Vector and Tree Retrieval for Efficiency and Accuracy
published: 2026-07-25T02:50:05Z
authors: Xinyan Zhong, Yuwei Shi, Yuqi Wei, Chen Shen, Tianhang Zhou, Zhenghao Wu
url: http://arxiv.org/abs/2607.23006v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VecTree-RAG: An Agentic Retrieval-Augmented Generation Framework Combining Vector and Tree Retrieval for Efficiency and Accuracy

## Abstract
Scientific question answering requires a retrieval system to solve two distinct problems: identifying which papers are relevant and locating the supporting evidence within those papers. Conventional retrieval-augmented generation typically addresses both through similarity search over fixed-length passages, flattening document structure and separating scientific claims from their methodological and argumentative context. We present VecTree-RAG, an agentic framework that assigns these tasks to complementary retrieval mechanisms. Vector search ranks compact document and section representations across the corpus, whereas reasoning-guided traversal of source-verified section trees localizes evidence within shortlisted papers. Full text is retained in a page store and exposed progressively only after structural localization. We evaluate VecTree-RAG on 300 QASPER questions, an open-access subset of 54 LitQA2 questions, and 49 multi-document MOSAIC questions. Compared with Dense RAG, reranked Dense RAG, RAPTOR, and Search-o1, VecTree-RAG obtained the highest observed answer score on all three benchmarks, reaching 0.800 LLM-judge correctness on QASPER, 0.925 accuracy on LitQA2, and a 0.547 composite score on MOSAIC. On QASPER, its evidence-page precision was 0.274, compared with 0.046--0.071 for the baselines. LitQA2 ablations further showed that the complete vector--tree architecture required fewer inference tokens than variants without tree navigation or corpus-level vector routing. These results indicate that vector retrieval narrows the corpus-level search space and tree navigation concentrates reading on structurally relevant evidence. Although multi-turn inference remains more expensive than single-call retrieval, VecTree-RAG provides a structure-aware and traceable architecture for scientific literature question answering.

## Metadata
- **Published**: 2026-07-25T02:50:05Z
- **Authors**: Xinyan Zhong, Yuwei Shi, Yuqi Wei, Chen Shen, Tianhang Zhou, Zhenghao Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23006v1)