---
title: Overcoming the Weakest-Link Effect in LLM-Driven Program Optimization via Heterogeneous Edit Recombination
published: 2026-07-31T02:05:45Z
authors: Jingwen Fu, Zhen Liu, Yuhan Liu, He Zhang, Nanning Zheng
url: http://arxiv.org/abs/2607.28947v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Overcoming the Weakest-Link Effect in LLM-Driven Program Optimization via Heterogeneous Edit Recombination

## Abstract
Large language models (LLMs) are increasingly used to solve complex problems by searching over program space, offering a general paradigm for scientific problems that can be naturally represented and solved as programs. Despite recent progress, identifying effective optimization directions for a candidate program remains challenging. By analogy with automatic differentiation, existing methods typically guide the search using a textual ``gradient'': a first-order update direction expressed as textual edits. Such gradients are inferred either from previously evaluated programs or from LLM-generated feedback on the implicit program-score mapping. However, these estimates become increasingly unreliable as the program--score mapping grows more complex, limiting their practical utility. We argue that explicit gradients are not essential for effective program optimization. Leveraging their prior knowledge, LLMs can propose plausible atomic edits directly from the current program, thereby enabling a zeroth-order optimization strategy. However, zeroth-order search suffers from a \textit{weakest-link effect}: when a bundle of edits is accepted or rejected as a whole, a single harmful edit can negate the benefits of all remaining edits. To address this issue, we introduce HERO, a program optimizer that prompts an LLM to generate diverse, non-overlapping atomic edits and then systematically selects and composes them into coherent program improvements using evaluator scores. We evaluate HERO across algorithmic problems, strategy games, the design of LLM-based agentic systems, and robotic path planning. Across these domains, HERO consistently discovers higher-scoring programs and converges substantially faster than prior LLM-based optimizers, while consuming fewer tokens.

## Metadata
- **Published**: 2026-07-31T02:05:45Z
- **Authors**: Jingwen Fu, Zhen Liu, Yuhan Liu, He Zhang, Nanning Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28947v1)