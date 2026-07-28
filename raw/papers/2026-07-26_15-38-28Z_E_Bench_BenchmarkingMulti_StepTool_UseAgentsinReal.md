---
title: E-Bench: Benchmarking Multi-Step Tool-Use Agents in Real-World Product Scenarios
published: 2026-07-26T15:38:28Z
authors: Weihuang Zheng, Tianyuan Zou, Eileen Ye, Alphet Liu, Youyong Kong, Ya-Qin Zhang, Duran Zheng, Maxm Pan
url: http://arxiv.org/abs/2607.23722v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# E-Bench: Benchmarking Multi-Step Tool-Use Agents in Real-World Product Scenarios

## Abstract
Large Language Models (LLMs) are increasingly deployed as agents that interact with stateful environments over multiple steps: gathering hidden information, composing tool calls, and committing state changes. We refer to this capability as multi-step tool use. Existing benchmarks have advanced tool-use agent evaluation, but often focus on isolated API calls, short trajectories, or settings that are difficult to scale or control. We introduce E-Bench, a fully synthetic benchmark with 323 state-changing tasks across three product domains: Honor of Kings, QQ Music, and Tencent Meeting. E-Bench decouples environment synthesis from task synthesis: graph-guided database filling builds reusable, orphan-free product environments, while generator-solver asymmetry creates tasks with both an information gap and a tool gap, requiring agents to discover hidden data and compose multiple tool calls before changing state. Outcomes are graded deterministically by database-state diffs. Since both environments and tasks are synthetic, E-Bench is controllable at the environment level and scalable at the task level. Benchmarking 11 cutting-edge LLMs shows that multi-step tool use remains challenging: Pass^3 stays below 60% for the strongest models, and even with code execution in the E-Bench-Code extension, reliability (Pass^3) remains below 70%.

## Metadata
- **Published**: 2026-07-26T15:38:28Z
- **Authors**: Weihuang Zheng, Tianyuan Zou, Eileen Ye, Alphet Liu, Youyong Kong, Ya-Qin Zhang, Duran Zheng, Maxm Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23722v1)