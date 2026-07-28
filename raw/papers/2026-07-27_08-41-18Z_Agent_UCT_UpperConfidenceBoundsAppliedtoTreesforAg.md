---
title: Agent-UCT: Upper Confidence Bounds Applied to Trees for Agentic Workflow Optimization with Cost-Awareness
published: 2026-07-27T08:41:18Z
authors: Yang Li, Hai Liu, Dian Shao, Yu Wang, Xiyu Chen, Sergey Volkov, Bozhi Wang, Ziyu Sun, Sihang Liu, Ye Luo, Xiaowei Zhang
url: http://arxiv.org/abs/2607.24162v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent-UCT: Upper Confidence Bounds Applied to Trees for Agentic Workflow Optimization with Cost-Awareness

## Abstract
Optimizing agentic workflows, such as retrieval-augmented generation (RAG) pipelines, requires navigating a combinatorial space of discrete component choices under tight evaluation budgets. Existing approaches - heuristic search, black-box optimization, and standard tree search methods - do not explicitly exploit the compositional structure of these workflows, leading to redundant computation and inefficient budget allocation. We introduce Agent-UCT (Agent-based Cost-Aware Upper Confidence Bounds Applied to Trees), a tree search algorithm that extends UCT with a reuse-aware regularization term derived from a bipartite prefix reuse graph. Agent-UCT biases selection toward branches that leverage previously materialized configuration prefixes, reducing redundant execution while maintaining effective exploration. Our framework, RAGSpace, unifies heterogeneous RAG components from LongRAG, LightRAG, and Self-RAG into a five-dimensional configuration space, enabling systematic cross-framework recombination. WTB (Workflow Test Bench) provides deterministic replay, content-addressable caching, and transactional consistency, ensuring that intermediate states are materialized once and reused across the search. Experiments on HotpotQA and UltraDomain demonstrate that Agent-UCT identifies configurations with the highest out-of-sample performance among the evaluated fixed framework presets. Under full-pool evaluation, bipartite prefix reuse reduces logical search cost by 73.6% relative to the no-prefix-sharing cost upper bound. Compared with full-pool evaluation, sampling-based evaluation further achieves a 4.2x wall-clock speedup. Agent-UCT, RAGSpace, and WTB together provide a unified framework for cost-aware, reproducible, and compositionally efficient agentic workflow optimization.

## Metadata
- **Published**: 2026-07-27T08:41:18Z
- **Authors**: Yang Li, Hai Liu, Dian Shao, Yu Wang, Xiyu Chen, Sergey Volkov, Bozhi Wang, Ziyu Sun, Sihang Liu, Ye Luo, Xiaowei Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24162v1)