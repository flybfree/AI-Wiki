---
title: When Does Trace-Driven Evaluation Mislead MoE Expert Caching? Replay Semantics, Workload Contamination, and Operating Regimes
url: http://arxiv.org/abs/2608.07911v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_04-29-20Z_WhenDoesTrace_DrivenEvaluationMisleadMoEExpertCach.md
generated_at: 2026-08-11 12:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how trace‑driven evaluation can mislead the performance of MoE expert caching policies by exposing three hidden factors: replay semantics, workload contamination, and operating regimes. Using a fused‑event simulator across models with 40, 64, and 128 experts, it shows that inconsistent per‑access replay inflates recency‑based policies while other policies remain stable, workloads can be altered to reverse cache‑friendliness rankings, and normalized miss fractions do not transfer between models.

## Key Takeaways
- Replay semantics cause a 27–29 % inflation of recency‑based policy scores under fused‑event traffic contracts, inverting the ranking compared with frequency‑ or static policies.  
- Workload contamination via instruction templates yields verbatim identical generation prefixes; matched‑pair rendering shifts early‑window effects by 19.4–31.9 points and flips which workloads appear most cache‑friendly.  
- Normalized miss fractions are model‑specific; permuting the temporal order of an identical event stream changes the offline‑optimal gap from 44.9 % to 30.8 %, indicating that only frozen workload compositions preserve a stable gap.

## Context
MoE models increasingly offload expert weights to host memory, making cache management critical for efficiency. Evaluating caching policies is essential because traffic reduction directly impacts latency and energy use in large‑scale AI systems.

## Implications
Practitioners must account for replay consistency and workload heterogeneity when designing lightweight eviction mechanisms; otherwise they may overestimate gains from causal predictors that only recover a fraction of the offline optimum.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07911v1)
