---
title: Router Sensitivity Under Lightweight Fine-Tuning Identifies Prunable Experts in Mixture-of-Experts Models
url: http://arxiv.org/abs/2608.07890v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_03-36-41Z_RouterSensitivityUnderLightweightFine_TuningIdenti.md
generated_at: 2026-08-10 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how lightweight fine‑tuning of mixture‑of‑experts (MoE) models can reveal which experts are most sensitive to router changes, enabling one‑shot pruning without full retraining. By applying a parameter‑efficient adapter that only modifies the router weights and ranking experts by their induced ℓ₂ router change, the authors achieve significant compression while preserving or even improving MMLU‑Pro accuracy. The results show that router‑only LoRA outperforms all‑module LoRA at matched rank with fewer experts, delivering 27.54% accuracy versus 24.42%, and that memory usage drops by 49% with latency reduced by 37%.

## Key Takeaways
- Router sensitivity under lightweight fine‑tuning can identify prunable experts in MoE models without requiring full fine‑tuning of all parameters.  
- Applying a router‑only LoRA adapter and pruning the least‑changed experts yields higher MMLU‑Pro scores (27.54%) than methods that remove more experts or use random magnitude‑based pruning.  
- The compression ratio improves memory by 49% and per‑token latency by 37%, while router‑guided accuracy remains competitive with full activation statistics at 25% compression.

## Context
Mixture‑of‑experts models promise to decouple total parameters from compute, but practical deployment often stores all experts, limiting efficiency. Recent work on pruning assumes full fine‑tuning, which is costly and impractical for large systems. This study bridges that gap by showing how a minimal adapter can expose router‑driven sensitivity, making expert removal feasible at scale.

## Implications
For industry practitioners, this approach enables cost‑effective model compression without sacrificing performance, supporting deployment of MoE systems on limited hardware. It also provides a principled metric for pruning decisions that can be integrated into automated model optimization pipelines, fostering broader adoption of efficient large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07890v1)
