---
title: DPS: Dual-Mode Precision LLM Serving with Semi-Unified Memory
url: http://arxiv.org/abs/2609.34380v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_05-55-33Z_DPS_Dual_ModePrecisionLLMServingwithSemi_UnifiedMe.md
generated_at: 2026-09-28 23:10
model: qwen3.6-35b-a3b
---

## Summary
DPS is a novel LLM serving system that dynamically adjusts model precision based on workload demands to optimize memory utilization, specifically addressing the limitations of fixed weight storage in existing architectures. By implementing Semi-Unified Memory (SUM), DPS allows weight memory to be repurposed for KV-cache blocks during traffic spikes, switching between full-accuracy and lower-precision modes without compromising overall system performance or accuracy. Evaluations demonstrate that this approach significantly boosts sustained throughput by up to 3

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34380v1)
