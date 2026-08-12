---
title: Optimize Cheap, Deploy Strong: Cost-Aware Cross-Tier Transfer for Evolutionary Optimization
url: http://arxiv.org/abs/2608.10694v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_09-17-22Z_OptimizeCheap_DeployStrong_Cost_AwareCross_TierTra.md
generated_at: 2026-08-11 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a cost‑aware cross‑tier transfer strategy that separates the evaluation role of LLMs into cheap and strong tiers, enabling evolutionary search to use low‑cost answering on cheaper models while reserving high‑quality reasoning for rare operations. It shows that this decoupling can match or exceed same‑tier optimization while reducing total search cost by up to 54× in difficult tasks.

## Key Takeaways
- The framework runs the bulk of fitness evaluations on the cheapest LLM tier, saving most tokens and cost.
- It uses upward cross‑tier transfer so cheaply evolved prompts are applied to stronger models for final output.
- Search cost drops from 1.0× to 5.6–14× in easy tasks and up to 25–54× in reasoning‑heavy chains.

## Context
Evolutionary optimization of LLM prompts is limited by the high price of each fitness evaluation, which dominates total search expense. This work introduces a cost‑aware architecture that mitigates this bottleneck without sacrificing performance.

## Implications
Practitioners can lower training and inference expenses for prompt engineering pipelines while maintaining competitive results, especially as model tiers become more widely available. The approach also suggests a broader principle of tiered resource allocation in AI search tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10694v1)
