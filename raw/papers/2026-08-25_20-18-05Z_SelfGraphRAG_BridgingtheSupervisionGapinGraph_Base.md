---
title: SelfGraphRAG: Bridging the Supervision Gap in Graph-Based RAG with Synthetic QA Generation
published: 2026-08-25T20:18:05Z
authors: Ben Lagnese, Manas Gaur
url: http://arxiv.org/abs/2608.25123v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SelfGraphRAG: Bridging the Supervision Gap in Graph-Based RAG with Synthetic QA Generation

## Abstract
Retrieval-augmented generation (RAG) improves large language models by incorporating external knowledge without retraining, but existing methods often underuse the relational structure encoded in knowledge graphs. Graph-based RAG can capture entity relationships, yet supervised graph retrieval typically requires labeled question-answer data that may not be available for newly constructed graphs. We address this limitation with SelfGraphRAG, a framework that generates question-answer pairs directly from knowledge graph structure and uses them to train a query-conditioned graph retriever. The generated questions capture multi-hop paths and local neighborhoods, providing relational supervision without manual annotation. Experiments on multi-hop question answering and classification benchmarks show that SelfGraphRAG improves retrieval precision and downstream reasoning performance over embedding-based baselines. These results suggest that knowledge graph structure can provide useful supervision for training graph retrievers when labeled data are unavailable.

## Metadata
- **Published**: 2026-08-25T20:18:05Z
- **Authors**: Ben Lagnese, Manas Gaur
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25123v1)