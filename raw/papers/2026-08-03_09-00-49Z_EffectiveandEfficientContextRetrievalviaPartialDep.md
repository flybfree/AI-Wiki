---
title: Effective and Efficient Context Retrieval via Partial Dependency Graph for Repository-Level Code Generation
published: 2026-08-03T09:00:49Z
authors: Zhongxin Liu, Zhonghao Jiang, Zhifan Ye, Haoye Wang, Jiakun Liu, Xiaoxue Ren
url: http://arxiv.org/abs/2608.01927v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Effective and Efficient Context Retrieval via Partial Dependency Graph for Repository-Level Code Generation

## Abstract
LLM-based repository-level code generation aims to generate code using the context available in a software repository, requiring LLMs to reason over complex code dependencies. Due to limited context windows and insufficient repository-specific understanding, LLMs typically rely on retrieval-augmented generation (RAG) to incorporate relevant code. Early RAG approaches primarily employ similarity-based retrieval, which often fails to retrieve code snippets that the target function depends on. Recent work introduces graph-based retrieval to model such dependencies, but typically relies on manually designed rules and static global graphs, leading to limited flexibility and high construction and maintenance costs. In contrast, human developers collect helpful context by implicitly constructing a partial dependency graph and iteratively inspecting along it. Inspired by this behavior, we propose DyRetriever, an efficient context retrieval method via partial dependency graphs. DyRetriever uses an LLM to first select a set of entry-point functions and then perform multi-hop reasoning along the code dependency graph. During multi-hop reasoning, it uses the LLM's semantic understanding to validate whether a function can help generate the target function, eliminating manually designed rules and enabling flexibility across scenarios. Instead of statically constructing a global dependency graph, DyRetriever builds a partial graph on demand and discards it after use, reducing construction and maintenance costs. We integrate DyRetriever with a similarity-based code retriever to build DyCoder and evaluate it on CoderEval and DevEval. Experimental results show that DyCoder achieves relative Pass@1 improvements of 25.63% and 59.73% on CoderEval and DevEval, respectively, compared with existing RAG-based methods, while being 7.4x faster than baselines based on static dependency graph construction.

## Metadata
- **Published**: 2026-08-03T09:00:49Z
- **Authors**: Zhongxin Liu, Zhonghao Jiang, Zhifan Ye, Haoye Wang, Jiakun Liu, Xiaoxue Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01927v1)