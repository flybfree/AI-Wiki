---
title: Retrieval Augmented Biomedical Question Answering with Weak Question Recovery and Neural Reranking for BioASQ Task 14b
published: 2026-08-02T20:02:44Z
authors: Xueying Zhao, Lee Mai, Balaji Anandganesh
url: http://arxiv.org/abs/2608.01468v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieval Augmented Biomedical Question Answering with Weak Question Recovery and Neural Reranking for BioASQ Task 14b

## Abstract
This work presents DS@GT ARC BioASQ team's work for a biomedical question answering pipeline, integrating multi-source query expansion, neural reranking, retrieval refinement, and OpenBioLLM-assisted answer generation. The system combines PubMed retrieval with fine-tuned MiniLM-based semantic reranking, Reciprocal Rank Fusion (RRF), and feature-based relevance scoring to improve document ranking quality. To address challenging queries with weak retrieval performance, we introduce a conditional weak-question recovery strategy that applies semantic expansion, relationship-aware augmentation, and selective result merging. A post-retrieval pruning stage further removes redundant or low-relevance snippets while preserving evidence coverage for downstream answer generation. Experimental results on BioASQ evaluation batches demonstrate that the proposed recovery and cleanup strategies substantially improve retrieval robustness and MAP@10 performance on difficult question sets. The final system also incorporates output validation and post-processing steps to ensure formatting consistency and submission reliability across BioASQ phases.

## Metadata
- **Published**: 2026-08-02T20:02:44Z
- **Authors**: Xueying Zhao, Lee Mai, Balaji Anandganesh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01468v1)