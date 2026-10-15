---
title: EvoProbe: Evaluation-Driven Benchmark Evolution for LLM Agents
published: 2026-10-14T02:27:06Z
authors: Qianhong Guo, Wei Xie, Xiaofang Cai, Shuoyoucheng Ma, Chengxin Hu, Baosheng Wang
url: http://arxiv.org/abs/2610.19433v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvoProbe: Evaluation-Driven Benchmark Evolution for LLM Agents

## Abstract
Static benchmarks for large language model (LLM) agents face saturation and data contamination risks, motivating continual updates to evaluation tasks. However, aggregate scores and success rates offer limited insight into specific problem-solving bottlenecks and provide limited guidance for subsequent task design. We propose EvoProbe, an evaluation-driven benchmark evolution framework that integrates task generation, diagnostic evaluation, and feedback-driven regeneration into a closed loop. It combines verifiable subtask outcome scoring with evidence-supported multi-judge trajectory evaluation and distills phase-level bottlenecks, success patterns, and failure patterns into diagnostic feedback for generating new executable tasks. Across two rounds of cybersecurity experiments, evaluations of eight models on 66 tasks reveal phase-level performance differences and common failure patterns beyond aggregate scores. In a cross-round comparison with the Examiner model set and solver configuration held fixed, all eight models achieve lower Outcome scores on the updated tasks, with relative decreases of 11.8\% in mean Outcome and 40.0\% in mean Pass\textasciicircum{}3. These results support using fine-grained diagnostics to guide iterative task updates and probe agents' current capabilities and limitations.

## Metadata
- **Published**: 2026-10-14T02:27:06Z
- **Authors**: Qianhong Guo, Wei Xie, Xiaofang Cai, Shuoyoucheng Ma, Chengxin Hu, Baosheng Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19433v1)