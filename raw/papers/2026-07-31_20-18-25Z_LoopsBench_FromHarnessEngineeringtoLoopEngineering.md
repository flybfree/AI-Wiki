---
title: LoopsBench: From Harness Engineering to Loop Engineering in Benchmarking Coding Agent
published: 2026-07-31T20:18:25Z
authors: Han Li, Zhemin Fang, Rili Feng, Yingqi Zhao, Jiaheng Liu, Pengfei Gao, He Ye, Dayi Lin, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
url: http://arxiv.org/abs/2608.00267v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LoopsBench: From Harness Engineering to Loop Engineering in Benchmarking Coding Agent

## Abstract
Coding agent infrastructure is shifting from harness engineering toward loop engineering as coding agents are deployed for sustained long-horizon software development. Existing benchmarks often center on localized tasks or end-state outcomes, offering limited insight into sustained execution. We introduce LOOPSBENCH, a long-horizon benchmark for loop engineering in coding agent evaluation. Each task is a dependency DAG over separately testable development units with source-evidenced prerequisite edges. LOOPSBENCH comprises 112 tasks from authentic sources spanning 8 programming languages and 9 domains. Its flow-aware runtime releases tests along the ready frontier and retains completed nodes as regression obligations. We evaluate frontier coding agents paired with widely used loop implementations. The strongest configuration, Opus-4.7 with Claude Code and outer continuation, resolves 25.00% of tasks. Recorded plans recover only part of the source-recovered prerequisite DAG, and regression events remain visible across the evaluated loop profiles. We open source the benchmark data and code, including all tasks, more than 5,300 development units, and executable tests, at microsoft/Loopsbench.

## Metadata
- **Published**: 2026-07-31T20:18:25Z
- **Authors**: Han Li, Zhemin Fang, Rili Feng, Yingqi Zhao, Jiaheng Liu, Pengfei Gao, He Ye, Dayi Lin, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00267v1)