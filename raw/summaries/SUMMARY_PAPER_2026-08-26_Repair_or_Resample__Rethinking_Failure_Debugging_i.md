---
title: Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems
url: http://arxiv.org/abs/2608.25920v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_15-33-47Z_RepairorResample_RethinkingFailureDebugginginLLMMu.md
generated_at: 2026-08-26 20:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether existing repair methods for large language model multi‑agent systems (MAS) causally fix failures or merely rely on random sampling. It introduces SymTrace, a framework that records execution trajectories and intervenes only at designated anchors to reproduce failures reliably. The study evaluates three MAS frameworks using the SymFail dataset, showing that unguided rerun methods have low success rates while a symptom‑driven approach improves repair by 191.89% over state‑of‑the‑art.

## Key Takeaways
- Existing unguided rerun methods are unreliable, reproducing only about 67.97% of failures and achieving merely 6.90% repair rates.
- The SymTrace framework reconstructs the pre‑anchor portion using logs while regenerating downstream steps, enabling faithful failure reproduction.
- A symptom‑driven intervention method repairs 20.15% of failed cases, representing a substantial improvement over prior approaches.

## Context
LLM multi‑agent systems promise scalable solutions for complex tasks but suffer from unpredictable failures that hinder deployment. Current debugging relies on costly full reruns, which are inefficient and often fail to capture root causes due to stochastic sampling. This work addresses the gap by providing a systematic way to isolate and repair specific failure points.

## Implications
For researchers, SymTrace offers a reusable toolkit for diagnosing MAS issues without exhaustive retraining. Practitioners can adopt symptom‑driven repairs to reduce downtime in production systems, making large‑scale AI deployments more robust and trustworthy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25920v1)
