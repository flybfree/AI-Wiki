---
title: AutoPref: Automatic Discovery of Task-Specific Preference Objectives for Neural Combinatorial Optimization
published: 2026-07-30T10:01:21Z
authors: Shengda Gu, Kai Li, Xinyi Ke, Haobo Fu, Yifan Zhang, Jian Cheng
url: http://arxiv.org/abs/2607.27953v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoPref: Automatic Discovery of Task-Specific Preference Objectives for Neural Combinatorial Optimization

## Abstract
Combinatorial optimization problems (COPs) underpin many real-world decisions, but their exponentially large search spaces make high-quality solutions costly to obtain. Neural combinatorial optimization (NCO) learns fast construction policies, typically with reinforcement learning (RL), while preference-based NCO improves sample efficiency by learning from relative solution quality. However, existing preference objectives combine two distinct design choices in manually specified, one-size-fits-all formulations: what learning signal to extract from each solution pair and how to weight each pair relative to the sampled set. We present AutoPref, the first LLM-guided framework for automated preference-objective discovery in NCO. AutoPref factorizes the objective into a pairwise loss program, which defines the learning signal, and a set-aware weighting program, which determines each pair's relative contribution. Their composition forms a unified programmatic objective space containing existing preference objectives as special cases. To make its search tractable, we introduce a staged conditional search strategy with behavioral gates that filter inadmissible programs before short-horizon training and evaluation. Across TSP, CVRP, FFSP, and JSSP, AutoPref consistently outperforms strong hand-designed baselines across problem scales, demonstrating the benefits and scalability of automated objective discovery for NCO.

## Metadata
- **Published**: 2026-07-30T10:01:21Z
- **Authors**: Shengda Gu, Kai Li, Xinyi Ke, Haobo Fu, Yifan Zhang, Jian Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27953v1)