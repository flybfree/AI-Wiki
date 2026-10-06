---
title: MemTrace: State-Consistent Memory for Long-Horizon Coding Agents
published: 2026-10-04T00:45:37Z
authors: Hongming Xu, Le Zhou, ZhongHe Jin, Xiang Zhang, Bo Tang, Zhiyu Li, Xuanhe Zhou, Juncheng Zhang
url: http://arxiv.org/abs/2610.04838v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemTrace: State-Consistent Memory for Long-Horizon Coding Agents

## Abstract
As coding agents take on long-horizon software evolution tasks spanning multiple files and stages, longer execution trajectories introduce two coupled challenges: (1) accumulated histories strain context budgets, and (2) repository changes can invalidate earlier execution evidence. Existing approaches address these challenges through techniques like larger context windows, compression, retrieval, or repository representations, but often fail to reconstruct a consistent task state after a context refresh or verify whether recalled evidence remains valid. Thus, we introduce MemTrace, a provenance-aware memory system that preserves execution history and aligns its reuse with the evolving task (e.g., iterative cross-file repair) and repository state. MemTrace stores history as immutable Memory Traces anchored to key information (e.g., files, symbols, tests), and organizes their execution order and dependencies in a Memory Trace Graph. When context is constrained, working memory retains only compact Memory Anchors, from which the agent can reconstruct the latest execution state and locate evidence relevant to its next action. Before restoring historical evidence, MemTrace checks its validity against the current repository state and retrieves only what the next action requires. Across three complementary long-horizon coding benchmarks, MemTrace consistently outperforms all fully evaluated baselines under the same backbone and harness, improving DeepSWE pass@1 by 21.2 points, SWE-EVO Resolved Rate by 4.4 points, and SWE-Milestone Score by 17.8 points under Codex CLI.

## Metadata
- **Published**: 2026-10-04T00:45:37Z
- **Authors**: Hongming Xu, Le Zhou, ZhongHe Jin, Xiang Zhang, Bo Tang, Zhiyu Li, Xuanhe Zhou, Juncheng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04838v1)