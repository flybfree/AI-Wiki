---
title: DocNavRAG: Document-Structured Graph RAG with Stateful Evidence Construction for Complex Document Question Answering
published: 2026-08-03T00:48:05Z
authors: Dongyang Xie, Yao Tian, Hao Zhang, Yifei Yuan, Tieyun Qian, Ming Zhong, Jiawei Jiang, Yuanyuan Zhu
url: http://arxiv.org/abs/2608.01565v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DocNavRAG: Document-Structured Graph RAG with Stateful Evidence Construction for Complex Document Question Answering

## Abstract
Answering complex questions over large document collections requires assembling complementary evidence across sections and documents. GraphRAG offers structured retrieval but typically uses fixed traversal, while agentic RAG operates over weakly structured interfaces. Our key insight is that agents should navigate document structure within and across documents rather than repeatedly search from scratch. We introduce DocNavRAG, which organizes document hierarchies and cross-region relations into a navigable graph, exposes graph operations for locating, navigating, expanding, and fetching, and maintains an evolving evidence state to guide retrieval until sufficient evidence is collected. Across four long- and multi-document QA benchmarks, DocNavRAG improves answer quality and context sufficiency over the strongest baseline by 7.8\% and 17.7\% on average.

## Metadata
- **Published**: 2026-08-03T00:48:05Z
- **Authors**: Dongyang Xie, Yao Tian, Hao Zhang, Yifei Yuan, Tieyun Qian, Ming Zhong, Jiawei Jiang, Yuanyuan Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01565v1)