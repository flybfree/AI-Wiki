---
title: SWE-Pruner Pro: The Coder LLM Already Knows What to Prune
published: 2026-07-20T17:47:44Z
authors: Yuhang Wang, Yuling Shi, Shaoqiu Zhang, Jialiang Liang, Shilin He, Siyu Ye, Yuting Chen, Kai Cai, Xiaodong Gu
url: http://arxiv.org/abs/2607.18213v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SWE-Pruner Pro: The Coder LLM Already Knows What to Prune

## Abstract
Pruning long context for coding agents has been a vital technology for efficient context management. While existing context pruning methods such as SWE-Pruner realize this by attaching a separate code classifier, we find the agent itself encodes internal representations indicating the relevance of code context when reading tool output. Based on this finding, we propose SWE-Pruner Pro, which prunes tool outputs directly inside the agent. Concretely, a small head turns the agent's own internal representations into a keep-or-prune label for each line, with a length-aware embedding keyed to each tool output's line count. Across two open-weight backbones and four multi-turn benchmarks, SWE-Pruner Pro saves up to 39% of prompt and completion tokens while preserving task quality, with bounded inference overhead. Notably, on MiMo-V2-Flash SWE-Pruner Pro additionally raises the SWE-Bench Verified resolve rate by +3.8% and the long-context Oolong accuracy by +2.2 points.

## Metadata
- **Published**: 2026-07-20T17:47:44Z
- **Authors**: Yuhang Wang, Yuling Shi, Shaoqiu Zhang, Jialiang Liang, Shilin He, Siyu Ye, Yuting Chen, Kai Cai, Xiaodong Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18213v1)