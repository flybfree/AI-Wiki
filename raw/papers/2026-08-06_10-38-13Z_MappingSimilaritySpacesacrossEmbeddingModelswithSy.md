---
title: Mapping Similarity Spaces across Embedding Models with Synthetic Query Probing
published: 2026-08-06T10:38:13Z
authors: Marcin Rozmus, Peter van der Putten
url: http://arxiv.org/abs/2608.05857v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mapping Similarity Spaces across Embedding Models with Synthetic Query Probing

## Abstract
Retrieval-Augmented Generation systems rely on similarity scores to retrieve relevant content, yet scores are not directly comparable across embedding models due to differing geometric properties, complicating model migration and limiting threshold reuse. We study how similarity scores can be related by learning mappings between score distributions rather than embeddings. We introduce Synthetic Query Probing, generating queries from documents to create controlled query-chunk pairs, enabling large-scale, reference-free analysis of cross-model similarity behavior. We evaluate the approach on multiple embedding configurations and learn score conversion functions using linear, isotonic, and quantile mappings. Experiments on SciFact and a proprietary corpus show that while models largely agree on rankings, their absolute scores exhibit systematic distortions. Learned mappings partially align these spaces and improve threshold portability, with isotonic regression performing best. Our results highlight the need for cross-model calibration and position Synthetic Query Probing as a scalable framework for analyzing embedding comparability.

## Metadata
- **Published**: 2026-08-06T10:38:13Z
- **Authors**: Marcin Rozmus, Peter van der Putten
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05857v1)