---
title: TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories
published: 2026-08-06T17:51:20Z
authors: Yunjia Qi, Zehua Yin, Xintong Shi, Hao Peng, Songyuanyi Lu, Yixian Liu, Richeng Xuan, Yuhong Liu, Zhichao Hu, Xiaozhi Wang, Lei Hou, Bin Xu, Juanzi Li
url: http://arxiv.org/abs/2608.06346v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories

## Abstract
LLM-based agentic systems have shown remarkable capabilities in complex domains, while suffering from cascading errors and difficulty in debugging. Critical error detection aims to locate the earliest error step in a failed trajectory that is responsible for the final failure. However, progress faces two main challenges. First, long trajectories make it difficult to identify individual errors, since the evidence for judging a step may be scattered across distant instructions, observations, and prior context. Second, failed trajectories often contain multiple local errors with different downstream effects, only some of which remain responsible for the final failure. In this work, we propose TrajDebug, an error-lifecycle tracing framework that addresses long-trajectory error discovery with multi-granularity history compression and evidence-based error identification, and supports critical attribution by tracing each error's resolution status and terminal impact. We further construct TrajErrBench, a benchmark of 486 manually annotated failed trajectories from Tau2Bench and SWE-Bench Pro, covering realistic tool-use and coding scenarios. Experiments across diverse agent benchmarks show that TrajDebug achieves the best overall performance over existing baselines, and application studies further demonstrate that its diagnoses provide actionable feedback for improving downstream agent success. We will release the codes and data to facilitate further research.

## Metadata
- **Published**: 2026-08-06T17:51:20Z
- **Authors**: Yunjia Qi, Zehua Yin, Xintong Shi, Hao Peng, Songyuanyi Lu, Yixian Liu, Richeng Xuan, Yuhong Liu, Zhichao Hu, Xiaozhi Wang, Lei Hou, Bin Xu, Juanzi Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06346v1)