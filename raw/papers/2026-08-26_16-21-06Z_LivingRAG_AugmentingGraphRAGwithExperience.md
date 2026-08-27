---
title: LivingRAG: Augmenting Graph RAG with Experience
published: 2026-08-26T16:21:06Z
authors: Yuzhuo Cui, Zongye Zhang, Qingjie Liu
url: http://arxiv.org/abs/2608.25960v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LivingRAG: Augmenting Graph RAG with Experience

## Abstract
Graph-based RAG improves multi-hop question answering by organizing evidence as a knowledge graph. However, most existing RAG systems process each query in isolation and discard useful reasoning from the LLM's response after inference. As a result, later related queries need to retrieve evidence and reason from scratch. We propose LivingRAG, a Graph RAG framework with writable and reusable reasoning experience. LivingRAG adds a writable experience store to a graph-based retrieval backbone, enabling verified experiences to be reused during inference in two ways. Stored graph signals help retrieval find entities and passages that were useful in earlier related queries. Stored summaries provide a reference reasoning pattern for answer generation. We analyze online QA streams and find reusable signals from shared entities, graph neighborhoods, and question templates. Experiments on multi-hop QA benchmarks show that LivingRAG improves accuracy over strong RAG baselines and reduces completion-token use when relevant prior experience is reused.

## Metadata
- **Published**: 2026-08-26T16:21:06Z
- **Authors**: Yuzhuo Cui, Zongye Zhang, Qingjie Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25960v1)