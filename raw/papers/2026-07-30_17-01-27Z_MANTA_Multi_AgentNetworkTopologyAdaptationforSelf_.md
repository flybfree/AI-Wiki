---
title: MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems
published: 2026-07-30T17:01:27Z
authors: Mao-xun Huang, Jerry Wang, Yi-Cheng Lai, Zhengxin Zhang, Claire Cardie, Hen-Hsen Huang
url: http://arxiv.org/abs/2607.28527v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems

## Abstract
Large language model-based multi-agent systems improve complex problem solving through task decomposition, agent specialization, information exchange, and intermediate validation. However, existing systems typically treat communication topology as a fixed design choice or an offline optimization target. We introduce MANTA, a framework for Multi-Agent Network Topology Adaptation that enables communication structures to self-evolve at inference time. Before execution, MANTA initializes a task-conditioned topology from prior structural experience. During deployment, it monitors collaboration traces and applies bounded structural updates when the current organization becomes insufficient. These updates can modify agent roles, communication links, execution order, information visibility, and validation pathways while preserving the task interface and agent budget. We evaluate MANTA against representative single-agent and multi-agent baselines on five benchmarks spanning information seeking, tool use, planning, workflow execution, and mathematical reasoning. MANTA achieves the highest average score of 74.0, outperforming the strongest baseline by 5.8 percentage points and obtaining the best result on PlanCraft. These results show that inference-time self-improvement can extend to the architecture of collaboration itself.

## Metadata
- **Published**: 2026-07-30T17:01:27Z
- **Authors**: Mao-xun Huang, Jerry Wang, Yi-Cheng Lai, Zhengxin Zhang, Claire Cardie, Hen-Hsen Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28527v1)