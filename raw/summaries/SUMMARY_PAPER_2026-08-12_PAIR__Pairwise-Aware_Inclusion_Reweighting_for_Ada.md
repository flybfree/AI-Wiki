---
title: PAIR: Pairwise-Aware Inclusion Reweighting for Adaptive Rollout Allocation in RLVR
url: http://arxiv.org/abs/2608.11368v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_19-24-59Z_PAIR_Pairwise_AwareInclusionReweightingforAdaptive.md
generated_at: 2026-08-12 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PAIR, a Pairwise-Aware Inclusion Reweighting method for adaptive rollout allocation in RLVR. The authors show that unclipped leave‑one‑out gradients are second‑order U‑statistics over pairs of rollouts, and their estimator is design‑unbiased when treating rollout prefixes as vertices and pair‑gradient terms as edges in a contrast graph.

## Key Takeaways
- The unclipped leave‑one‑out group‑relative score gradient is not additive but a second‑order U‑statistic that depends on the joint inclusion of every pair of completed rollouts.  
- PAIR models these pair‑gradient terms as edges in a contrast graph, assigning each edge an inverse weight based on its logged joint inclusion probability to correct for statistical mismatch.  
- Experiments on Qwen3‑1.7B/4B demonstrate that PAIR boosts average accuracy by 1.2–1.4 points while cutting token generation by roughly half compared with the best pointwise allocator.

## Context
RLVR systems generate long reasoning trajectories to verify rewards, incurring high compute costs. Pointwise allocators attempt to reduce this cost by assigning budgets based on local difficulty or utility, but they ignore the inter‑rollout dependencies that affect gradient estimates. PAIR addresses this gap by recognizing that each completed rollout provides contrast information with every other rollout.

## Implications
For practitioners developing efficient RLVR pipelines, PAIR offers a principled way to allocate compute without sacrificing reward verification accuracy. The method’s design‑unbiased estimator can be integrated into adaptive allocation frameworks, potentially lowering token usage and improving model performance across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11368v1)
