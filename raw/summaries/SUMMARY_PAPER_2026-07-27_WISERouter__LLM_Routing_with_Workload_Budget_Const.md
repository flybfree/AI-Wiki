---
title: WISERouter: LLM Routing with Workload Budget Constraint
url: http://arxiv.org/abs/2607.23765v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_17-20-39Z_WISERouter_LLMRoutingwithWorkloadBudgetConstraint.md
generated_at: 2026-07-27 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces WISERouter, a framework for routing large language model queries to models that balance utility and cost within a budget constraint. It solves the problem as a constrained contextual multi‑armed bandit and shows that its online version has sublinear regret O(√T). Experiments on RouterBench and SWE‑Bench show offline learning outperforms baselines under fixed budgets while adhering more closely to constraints, and online learning matches performance with far less exploration data.

## Key Takeaways
- WISERouter treats LLM routing as a constrained contextual multi‑armed bandit problem, allowing both offline historical data and online exploration without violating budget limits.  
- The offline version WR‑Offline exceeds existing baselines in performance while staying within the fixed per‑query budget and enforcing constraints more strictly.  
- The online version WR‑Online achieves comparable performance to baselines but uses substantially less exploration data, reducing training cost.

## Context
LLM deployment at scale requires efficient use of model capacity and computational resources. Current routing methods either ignore strict budgets or need exhaustive pairwise statistics, limiting scalability. This work advances the field by providing a principled algorithmic solution that integrates learning with budget enforcement.

## Implications
For practitioners deploying LLMs in production, WISERouter offers a cost‑effective strategy to maximize utility while controlling expenses. The sublinear regret guarantee assures long‑term performance stability, and its low exploration requirement reduces data collection overhead, making large‑scale routing feasible.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23765v1)
