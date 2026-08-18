---
title: HyMem: Hierarchical Context Management for Long-Horizon Agents via Information Isolation
published: 2026-08-16T12:15:01Z
authors: XinQi Wang, Jinwei Xiao, Sijia Cui, Hongming Zhang, Yanna Wang, Qingyang Zhang, Bo Xu
url: http://arxiv.org/abs/2608.15703v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HyMem: Hierarchical Context Management for Long-Horizon Agents via Information Isolation

## Abstract
Large language model (LLM) agents often perform poorly on complex, long-horizon tasks because their context becomes increasingly cluttered over time. As interactions accumulate, detailed execution traces and intermediate outputs dominate the context, making it difficult for the model to retain and use high-level planning information. Most existing methods address this issue through compression or retrieval applied to a single, flat context, which does not clearly separate different types of context information and often leads to degraded reasoning. To address this challenge, we propose HyMem, a hierarchical framework that explicitly separates the agent's context into distinct functional layers. HyMem organizes context by function to separate high-level planning from execution and complex analysis. Its isolated reasoning module handles complex subtasks without adding intermediate reasoning traces to the persistent planning context, while its memory management module preserves task progress across context refreshes through structured summaries. These components reduce redundant context accumulation, retain task-critical information, and support coherent long-horizon reasoning within a limited context window. Experiments on GAIA and Browsecomp-plus show that, with DeepSeek-V4, HyMem achieves average Pass@1 scores of 66.7% and 61.3%, outperforming the strongest baseline by 6.1 and 4.7 percentage points, respectively. Further analysis indicates that HyMem effectively controls the growth of the reasoning context, allowing the model to maintain focus and accuracy across complex, long-horizon tasks.

## Metadata
- **Published**: 2026-08-16T12:15:01Z
- **Authors**: XinQi Wang, Jinwei Xiao, Sijia Cui, Hongming Zhang, Yanna Wang, Qingyang Zhang, Bo Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15703v1)