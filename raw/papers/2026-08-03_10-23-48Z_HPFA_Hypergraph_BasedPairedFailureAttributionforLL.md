---
title: HPFA: Hypergraph-Based Paired Failure Attribution for LLM Reasoning
published: 2026-08-03T10:23:48Z
authors: Runchuan Zhu, Hongbin Lai, Bowen Jiang, Junrui Zhang, Zhangheng LI, Ostap Kilbasovych, Junyuan Hong
url: http://arxiv.org/abs/2608.02026v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HPFA: Hypergraph-Based Paired Failure Attribution for LLM Reasoning

## Abstract
Reflection is a powerful mechanism for LLM reasoning, yet its effectiveness hinges on accurately attributing failures to specific reasoning steps, a capability that current models notably lack. Existing failure attribution methods either require expensive step-by-step counterfactual testing that scales poorly with trajectory length, or treat reasoning traces as flat sequences that ignore the inherent non-linear logical dependencies. We propose a hypergraph-based paired failure attribution (HPFA) framework that attributes the failure root cause by comparing the hyperedges of the targeted failure reasoning path against a reference successful path. By reducing the search space, our method efficiently localizes root causes and enables scalable synthesis of attribution data for training a lightweight attributor model via supervised fine-tuning and reinforcement learning. Experiments on mathematical reasoning and agentic coding tasks demonstrate that HPFA can dramatically increase attribution accuracy and efficiency, and the trained attributor consistently improves reasoning accuracy at test time, outperforming baselines that lack graph structure or paired analysis.

## Metadata
- **Published**: 2026-08-03T10:23:48Z
- **Authors**: Runchuan Zhu, Hongbin Lai, Bowen Jiang, Junrui Zhang, Zhangheng LI, Ostap Kilbasovych, Junyuan Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02026v1)