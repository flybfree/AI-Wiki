---
title: PATH-Bench: Path-Dependent Evaluation of Lifelong Agents
published: 2026-08-02T11:00:04Z
authors: Xidong Yang, Xingyi Zhang, Wenhao Li, Wenyan Liu, Junjie Sheng, Yun Hua, Wei Yin, Tao Fang, Chuyun Shen, Xiangfeng Wang
url: http://arxiv.org/abs/2608.01149v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PATH-Bench: Path-Dependent Evaluation of Lifelong Agents

## Abstract
Lifelong LLM agents increasingly adapt through external learning states that store past interactions as retrievable memories or reusable skills, yet existing benchmarks rarely account for how the path of accumulated experience shapes what agents transfer and retain. In this work, we establish PATH-Bench, a benchmark for path-dependent evaluation of lifelong agents. PATH-Bench estimates directed task relationships via multi-model in-context learning, constructs probe-centered sequences with controlled helpful and interfering histories, and repeatedly evaluates probe tasks to measure average performance, forward transfer, backward transfer, and forgetting. We evaluate eight representative agents on single-turn code generation and multi-turn tool-use tasks under positive- and negative-dominant histories. Benchmark results show that experience utility depends jointly on how experience is represented and on the task's interaction structure, that strong transfer does not ensure retention, and that later experience can reshape gains acquired earlier in the learning path. Based on these findings, we propose Selective Experience Use (SEU), an agent harness that regulates how path-accumulated experience influences each new task, admitting helpful items while filtering out potential interference. SEU consistently reduces forgetting while improving forward transfer in the majority of settings. The PATH-Bench provides both a controlled evaluation framework and actionable guidance for designing more selective and robust lifelong agents.

## Metadata
- **Published**: 2026-08-02T11:00:04Z
- **Authors**: Xidong Yang, Xingyi Zhang, Wenhao Li, Wenyan Liu, Junjie Sheng, Yun Hua, Wei Yin, Tao Fang, Chuyun Shen, Xiangfeng Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01149v1)