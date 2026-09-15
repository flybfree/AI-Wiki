---
title: DynSTEER: Dynamic Stage-wise Trajectory Evaluation and Execution-time Review for Agents
published: 2026-09-13T16:18:03Z
authors: Zhichao Shi, Wenjie Zhang, Xuhui Jiang, Xiaojun Wu, Cehao Yang, Chengjin Xu, Jian Guo, Yuanzhuo Wang
url: http://arxiv.org/abs/2609.14637v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DynSTEER: Dynamic Stage-wise Trajectory Evaluation and Execution-time Review for Agents

## Abstract
Large language model agents are increasingly deployed for long-horizon task execution. However, current evaluation paradigms face three major limitations: terminal-only assessment ignores intermediate processes and struggles to localize errors efficiently and accurately, single-reference matching penalizes valid alternative solution paths, and post-hoc trajectory judging incurs high costs without the ability to halt failed runs early. To address these issues, we propose DynSTEER, a dynamic stage-wise trajectory evaluation framework for agents. DynSTEER segments rollouts into stages anchored by key completed actions, focusing evaluation on essential milestones with adequate context while enabling targeted strategy adjustments. It compiles a path-tolerant milestone graph from public task views to respect diverse legitimate strategies without leaking ground truth. Furthermore, it adaptively routes evaluation queries across multi-tier judges and halts unrecoverable executions online to curb resource waste. Experiments demonstrate that DynSTEER improves evaluation discriminability across LLM agents by 85.2\% over native evaluation, separates all model pairs with statistical significance, and saves 34.51\% of execution steps on failed rollouts.

## Metadata
- **Published**: 2026-09-13T16:18:03Z
- **Authors**: Zhichao Shi, Wenjie Zhang, Xuhui Jiang, Xiaojun Wu, Cehao Yang, Chengjin Xu, Jian Guo, Yuanzhuo Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14637v1)