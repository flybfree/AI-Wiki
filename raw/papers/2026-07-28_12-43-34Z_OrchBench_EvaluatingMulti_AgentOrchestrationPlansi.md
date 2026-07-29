---
title: OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation
published: 2026-07-28T12:43:34Z
authors: Zhenzhen Ren, Jiyan He, Xinpeng Zhang, Zhenxing Qian, Ke Han, Shuxin Zheng, GuoBiao Li, Xiaoqing Zhang
url: http://arxiv.org/abs/2607.25656v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation

## Abstract
Complex tasks often decompose into parallelizable yet interdependent subtasks, making orchestration critical to the performance of multi-agent systems (MAS). Existing evaluations typically rely on end-to-end execution, which conflates orchestration-plan quality with worker capabilities, tool reliability, and environmental noise. Moreover, the time and token costs of real execution grow rapidly with workflow scale, making systematic evaluation expensive. We present OrchBench, a simulation-based benchmark for evaluating multi-agent orchestration plans in isolation. Starting from real-world tasks, OrchBench constructs directed acyclic graphs (DAGs) that encode task dependencies, with controlled sizes and degrees of parallelism. Given a DAG, a per-agent context limit, and an agent budget, the evaluated planner assigns subtasks to agents and specifies cross-agent information transfers and their retention ratios. A deterministic simulator evaluates the resulting plan without invoking worker agents and returns interpretable measures of result quality, makespan, and token cost. The simulated scores produced by OrchBench correlate strongly with quality scores from Claude Code executions, achieving a Pearson correlation of \(r=0.816\), while requiring only \(1.3\%\) of the tokens and \(10.3\%\) of the wall-clock time. Across diverse planners and workflow scales, we find that preserving task-critical information is more important than simply increasing the number of agents, and the benefits of parallelism diminish as coordination failures accumulate. These results establish OrchBench as an efficient and interpretable benchmark for comparing and diagnosing multi-agent orchestration plans.

## Metadata
- **Published**: 2026-07-28T12:43:34Z
- **Authors**: Zhenzhen Ren, Jiyan He, Xinpeng Zhang, Zhenxing Qian, Ke Han, Shuxin Zheng, GuoBiao Li, Xiaoqing Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25656v1)