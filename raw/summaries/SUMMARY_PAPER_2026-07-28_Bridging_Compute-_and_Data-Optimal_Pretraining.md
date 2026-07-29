---
title: Bridging Compute- and Data-Optimal Pretraining
url: http://arxiv.org/abs/2607.25271v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_04-18-49Z_BridgingCompute_andData_OptimalPretraining.md
generated_at: 2026-07-28 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Compute-Data (CD) scaling laws to address the growing gap between compute availability and high‑quality pretraining data, extending classical compute‑optimal models with a token‑effectiveness function η that measures how valuable derived tokens are compared to fresh ones. Experiments across model sizes 14M–600M parameters show η varies with model size, token‑per‑parameter ratio, and amount of repeated or paraphrased data, eventually saturating as the corpus expands.

## Key Takeaways
- The token‑effectiveness function η is not constant; it depends jointly on model size, tokens‑per‑parameter ratio, and derived‑data volume, indicating diminishing returns when substituting compute for data.  
- CD scaling identifies three operational regimes—compute‑bound, data‑bound, and model‑bound—revealing that classical compute‑optimal allocation is suboptimal in most practical settings.  
- The functional form of η suggests a saturation point where further data expansion yields negligible gains, highlighting the need to balance compute investment with effective token value.

## Context
In AI research, scaling laws traditionally assume unlimited high‑quality data, but real‑world pretraining pipelines often face constraints on both compute and data quality. This paper’s CD framework provides a more realistic view of how these resources interact as models grow larger.

## Implications
For practitioners, the CD model encourages strategic allocation of compute toward tasks that generate tokens with high effectiveness rather than simply increasing raw training time. It also signals that future large‑model development may need to prioritize data curation and effective token reuse over brute‑force scaling alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25271v1)
