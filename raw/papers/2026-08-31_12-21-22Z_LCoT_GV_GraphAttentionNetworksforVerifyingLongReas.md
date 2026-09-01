---
title: LCoT-GV: Graph Attention Networks for Verifying Long Reasoning Chains in Large Language Models
published: 2026-08-31T12:21:22Z
authors: Bérénice Jaulmes, Mehwish Alam
url: http://arxiv.org/abs/2608.30679v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LCoT-GV: Graph Attention Networks for Verifying Long Reasoning Chains in Large Language Models

## Abstract
Large Reasoning Models produce Long Chains-of-Thought (LCoTs) which involve breaking down the problem into smaller reasoning steps before reaching the conclusion. However, these steps often contain contradictions, unsupported inferences, or irrelevant steps, even when the final answer is correct. We propose Long Chain-of-Thought Graph Verifier (LCoT-GV), a graph-based framework that represents LCoTs as reasoning graphs. Each node in the graph represents a reasoning step and the edges encode semantic and logical relations. A Graph Attention Network is then trained to predict chain-of-thought correctness from the reasoning graph. We construct a new graph-oriented verification dataset from multiple reasoning benchmarks for question answering in various domains. The results show that our method is competitive with the most similar approaches.

## Metadata
- **Published**: 2026-08-31T12:21:22Z
- **Authors**: Bérénice Jaulmes, Mehwish Alam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30679v1)