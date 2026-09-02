---
title: SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers
url: http://arxiv.org/abs/2609.01343v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-52-57Z_SMELT_ScalingLawsforCompute_MatchedMoELoopedTransf.md
generated_at: 2026-09-01 22:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates Looped Transformers by matching the per-token FLOPs, total non‑embedding parameters, and KV cache of a baseline Mixture-of-Experts model while looping the middle half of layers twice. It introduces SMELT, a recipe that yields loss reductions comparable to extra compute but saves 6.8–18 % of training FLOPs on the optimal frontier. The advantage is especially strong on Code and grows with sample length.

## Key Takeaways
- Looping the middle half of layers twice can match the performance of an unlooped baseline while keeping all three budget constraints (FLOPs, parameters, KV cache) identical.  
- SMELT reduces training FLOPs by up to 18 % on the compute‑optimal frontier, demonstrating that depth reuse yields measurable efficiency gains.  
- The second visit of layers mitigates attention sink and redirects token mass toward content‑relevant tokens, providing an inductive bias that explains the observed performance boost.

## Context
Looped Transformers aim to increase effective depth without proportionally increasing model size or compute, a challenge highlighted by recent scaling studies on Mixture-of-Experts architectures. This work provides empirical evidence that architectural tricks can be optimized under strict budget matching, aligning with broader efforts to improve training efficiency in large language models.

## Implications
For practitioners, SMELT offers a practical recipe for reducing FLOPs without sacrificing performance, encouraging the adoption of depth‑reuse strategies in model design. The findings suggest that future scaling laws may incorporate architectural reuse as a factor, potentially reshaping how we allocate compute budgets across training and inference phases.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01343v1)
