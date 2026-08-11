---
title: VDGR-RAG: Vectors, Directories, Graphs, and Reflection Are All You Need for Unified Reasoning over Hierarchical Enterprise Knowledge
published: 2026-08-08T08:03:34Z
authors: Wenqi Chen, Haofei Yang, Rui Yang, Fangming Li
url: http://arxiv.org/abs/2608.07994v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VDGR-RAG: Vectors, Directories, Graphs, and Reflection Are All You Need for Unified Reasoning over Hierarchical Enterprise Knowledge

## Abstract
Retrieval-Augmented Generation (RAG) is essential for enterprise knowledge question answering (QA), particularly in domains with complex product documentation like telecommunications. However, existing RAG approaches largely overlook the holistic integration of diverse retrieval strengths, leading to inaccurate domain routing, poor utilization of hierarchical document structures, and consequently limited reasoning capabilities over enterprise knowledge. To address these limitations, we present VDGR-RAG, which integrates vector retrieval, directory-driven reasoning, graph traversal, and iterative reflection in a unified framework for accurate enterprise knowledge QA. Specifically, VDGR-RAG is an agentic GraphRAG system that first constructs a Hierarchical Heterogeneous Knowledge Graph ($\text{H}^2$KG) from document chunks to preserve both hierarchical directory structures and semantic relationships, and then employs a set of atomic tools for knowledge retrieval that can be freely composed to navigate the $\text{H}^2$KG: (1) a directory-enhanced routing tool that uses table-of-contents (TOC) structures to route user queries to appropriate domain-specific $\text{H}^2$KGs; (2) a multi-route retrieval tool that combines vector search, TOC-based agentic search, and graph search for comprehensive knowledge retrieval; (3) a directory backtracking tool that corrects knowledge localization biases; and (4) a dynamic reflection tool that iteratively plans the next retrieval phase. We conduct extensive experiments on our enterprise product documents across four wireless domains (e.g., energy saving and fault management). Experimental results demonstrate that our method significantly outperforms a variety of RAG baselines in terms of both knowledge retrieval recall and QA accuracy.

## Metadata
- **Published**: 2026-08-08T08:03:34Z
- **Authors**: Wenqi Chen, Haofei Yang, Rui Yang, Fangming Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07994v1)