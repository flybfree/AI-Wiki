---
title: Staying on the Attack Path: Structured State for Long-Horizon Automated Penetration Testing
published: 2026-09-07T11:09:01Z
authors: Weizhe Wang, Yitong Zhang, Yao Zhang, Xiaoqiang Di, Zhigang Li, Bin Wu, Guangquan Xu
url: http://arxiv.org/abs/2609.07344v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Staying on the Attack Path: Structured State for Long-Horizon Automated Penetration Testing

## Abstract
Large language model (LLM) based agents are increasingly applied to cybersecurity tasks such as vulnerability discovery and automated penetration testing. On long-horizon security tasks, however, such agents remain limited by context forgetting and intent drift: early critical facts and causal reasoning chains are lost over extended interactions, and the agent falls into aimless, repetitive exploration. This paper proposes Intentest, an intent-graph-guided automated penetration testing agent that externalizes long-horizon state from the LLM's context window onto a persistent fact-intent directed acyclic graph (DAG), thereby substantially reducing invalid transitions. We evaluate Intentest on automated penetration testing of web applications, a representative long-tail task in cybersecurity. In the DAG, verified network states are stored as immutable fact nodes, and exploration directions are constrained as intent edges bounded by predecessor facts. The system adopts a three-layer architecture, in which the fact-intent mapping layer maintains the global state, the task scheduling and allocation layer ensures execution stability through two-phase degradation recovery and multi-dimensional adaptive load balancing, and the intent retrieval and prediction layer provides tactical priors through a top-down five-stage filtering algorithm. On a benchmark of real CTF challenges covering more than ten vulnerability types across three difficulty levels, Intentest achieves an overall success rate of 88.2% and a success rate of 75.0% on hard tasks, improving over the baseline by approximately 44 and 50 percentage points. Ablation experiments further show that the intent retrieval and prediction reduce the average number of rounds on successful medium and hard tasks by about 33% and 48%, respectively, without changing the set of solvable tasks.

## Metadata
- **Published**: 2026-09-07T11:09:01Z
- **Authors**: Weizhe Wang, Yitong Zhang, Yao Zhang, Xiaoqiang Di, Zhigang Li, Bin Wu, Guangquan Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07344v1)