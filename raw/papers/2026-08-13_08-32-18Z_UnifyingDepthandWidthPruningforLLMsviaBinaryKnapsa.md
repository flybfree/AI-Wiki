---
title: Unifying Depth and Width Pruning for LLMs via Binary Knapsack Optimization
published: 2026-08-13T08:32:18Z
authors: Palaash Goel, Ayan Sengupta, Akshay Nambi, Tanmoy Chakraborty
url: http://arxiv.org/abs/2608.12953v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unifying Depth and Width Pruning for LLMs via Binary Knapsack Optimization

## Abstract
Structured pruning is a promising approach for compressing large language models (LLMs), yet existing methods rely heavily on greedy heuristics that produce myopic decisions, and often fail to precisely meet target compression budgets. We present SNIPER, a two-stage structured pruning framework that solves a knapsack optimization over coarse-granularity components to yield conditionally optimal parameter allocations with respect to fixed importance estimates, followed by a fine-grained pruning stage to meet strict budget constraints. We introduce the Compression Ratio Adherence Factor (CRAFT) to quantify budget fidelity, showing that while existing pruners deviate from target compression ratios by up to 33%, SNIPER achieves near-exact adherence with a CRAFT score of 0.98. Evaluations across four diverse architectures over a set of 18 tasks spanning five domains demonstrate SNIPER's consistent improvements in average performance retention and task-level stability over six state-of-the-art pruners. Across all pruning configurations, SNIPER achieves an excellent mean rank of 1.25, indicating its robust cross-architectural generalizability and excellent reliability.

## Metadata
- **Published**: 2026-08-13T08:32:18Z
- **Authors**: Palaash Goel, Ayan Sengupta, Akshay Nambi, Tanmoy Chakraborty
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12953v1)