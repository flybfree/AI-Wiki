---
title: Don't Solve, Just Compare: Tiny Advisors for Runtime Intervention in LLM Agents
published: 2026-08-21T12:20:14Z
authors: Yanze Jiang, Mingxuan Li, Yuhao Wang, Shengfang Zhai, Jiaheng Zhang
url: http://arxiv.org/abs/2608.21027v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Don't Solve, Just Compare: Tiny Advisors for Runtime Intervention in LLM Agents

## Abstract
LLM agents are emerging as an important paradigm for real-world tasks that require reasoning, tool use, and sequential decision-making. As these agents operate over longer horizons, runtime intervention offers a way to improve reliability without retraining the underlying actor. Failure detection alone is insufficient. Effective intervention must also provide a useful direction for recovery. Existing approaches often rely on an expert solver or a critic that generates task-specific corrections, incurring either the cost of another capable solver or the capacity demands of a task-capable critic. We introduce Comparison-Only Tiny Advisor (COTA), a comparison-only framework for constructive runtime intervention. In COTA, a tiny comparator judges whether sampled alternatives lead to better continuations than the actor's proposal, and repeated comparisons determine when intervention is warranted. We train the comparator using pairwise supervision constructed from same-prefix counterfactual branches. Preferred alternatives are returned as non-binding advice, leaving the original actor to replan. Across WebShop, ALFWorld, and tau^3-Retail with three actors, COTA improves all nine evaluation settings and outperforms the compared baselines. These results show that constructive runtime intervention can remain effective even when the auxiliary model has substantially weaker task-solving capability than the actor.

## Metadata
- **Published**: 2026-08-21T12:20:14Z
- **Authors**: Yanze Jiang, Mingxuan Li, Yuhao Wang, Shengfang Zhai, Jiaheng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21027v1)