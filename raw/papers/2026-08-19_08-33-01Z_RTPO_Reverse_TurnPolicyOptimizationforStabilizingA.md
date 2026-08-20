---
title: RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training
published: 2026-08-19T08:33:01Z
authors: Yugu Li, Jimmy Cao, Jianglin Qiao, Siyi Hu
url: http://arxiv.org/abs/2608.18682v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training

## Abstract
Training multi-turn agentic workflows with reinforcement learning (RL) enables large language models to perform complex reasoning, use external tools, and conduct iterative search beyond single-turn settings. Yet multi-turn RL training remains highly unstable, often causing severe performance degradation as the number of turns increases. Through theoretical analysis, we identify three tightly coupled sources of instability: rollout-training context mismatch, weak turn-level credit assignment under sparse terminal rewards, and asynchronous policy drift when short and long trajectories are optimized under different policy versions. We show that these issues share a common structural origin in flattened trajectory optimization and address them through a unified reverse-turn formulation. We propose Reverse-Turn Policy Optimization (RTPO), which organizes multi-turn rollouts as sparse reverse trees and performs turn-level policy updates in temporal reverse order, aligning each decision with its downstream continuation. RTPO enables causally consistent turn-level credit assignment and on-policy continuation to control asynchronous drift. We provide theoretical guarantees showing that RTPO eliminates context mismatch and asynchronous drift under the proposed turn-level formulation, reduces credit bias, and converges to recursive optimality. Experiments on multi-turn agentic RL benchmarks show that RTPO improves upon trajectory- and turn-level baselines by 21.50% and 10.76%, respectively, highlighting its potential to support more stable training for tool-using agents.

## Metadata
- **Published**: 2026-08-19T08:33:01Z
- **Authors**: Yugu Li, Jimmy Cao, Jianglin Qiao, Siyi Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18682v1)