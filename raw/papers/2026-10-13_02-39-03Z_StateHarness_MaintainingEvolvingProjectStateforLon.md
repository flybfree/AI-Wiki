---
title: StateHarness: Maintaining Evolving Project State for Long-Horizon Coding Agents
published: 2026-10-13T02:39:03Z
authors: Chuan Zou, Yujun Zhou, Xiaonan Luo, Xiangliang Zhang
url: http://arxiv.org/abs/2610.17616v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StateHarness: Maintaining Evolving Project State for Long-Horizon Coding Agents

## Abstract
Long-horizon coding requires agents to maintain an evolving view of the project they are changing: what problem is currently being solved, what has already been learned or modified, which other artifacts may be affected, and what work remains unresolved. When this information is scattered across a growing interaction history, local edits can become disconnected from their later consequences and progress can be difficult to carry forward. We introduce StateHarness, a runtime framework that maintains evolving project state without updating model parameters. The working agent records its current problem and hypothesis, important findings and decisions, discovered repository relationships, and unfinished work. Runtime support prompts record updates, searches for callers, tests, and documentation that may be affected by a change, and maintains a compact working brief for subsequent decisions. When behavioral signals accumulate, a separate diagnostic session revisits the recorded history and surfaces overlooked evidence. Across three repository-level evaluations, StateHarness improves task completion and several measures of change consistency. On RefactorBench, full-chain completion increases from 29.4% to 35.3% and cleanup-check accuracy from 87.0% to 95.4%. On five LHTB software-engineering tasks, mean reward improves from 0.427 to 0.576, exceeding LongHorizon-Harness at substantially lower recorded execution cost. On ChainSWE, bug-fix rate increases from 35.1% to 39.5% and residual debt decreases from 60 to 43 items, although pass-to-pass regressions increase. These results show that maintaining project state can improve long-horizon coding while introducing measurable execution and regression trade-offs.

## Metadata
- **Published**: 2026-10-13T02:39:03Z
- **Authors**: Chuan Zou, Yujun Zhou, Xiaonan Luo, Xiangliang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17616v1)