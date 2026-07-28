---
title: WISERouter: LLM Routing with Workload Budget Constraint
published: 2026-07-26T17:20:39Z
authors: Yifei Li, Zihui Gao, Laks V. S. Lakshmanan
url: http://arxiv.org/abs/2607.23765v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WISERouter: LLM Routing with Workload Budget Constraint

## Abstract
Large language models (LLMs) achieve impressive performance across multiple domains, but using the most capable model for every query is prohibitive at scale. LLM routing exploits diversity in model capability and cost by assigning each query to a suitable model to balance utility and budget. Current methods have two limitations: (i) they either use heuristics that do not always enforce the budget constraint or impose a fixed per-query budget that cannot adapt across the workload and leads to suboptimal performance; (ii) they require supervised learning on a dense dataset with statistics for every query-model pair, which is expensive to collect. To address these challenges, we formulate LLM routing as a constrained contextual multi-armed bandit problem and introduce WISERouter (WR for short), a framework that supports offline learning from historical interactions as well as online learning with exploration. We further prove that WR-Online achieves a sublinear regret bound of $O(\sqrt{T})$ over a time horizon $T$. Empirical results on RouterBench and SWE-Bench demonstrate that (i) WR-Offline surpasses existing baselines in performance under a fixed budget and adheres more closely to budget constraints, and (ii) WR-Online achieves comparable performance to the baselines, while using substantially less exploration data.

## Metadata
- **Published**: 2026-07-26T17:20:39Z
- **Authors**: Yifei Li, Zihui Gao, Laks V. S. Lakshmanan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23765v1)