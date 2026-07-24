---
title: Are Diversity Metrics Measuring Diversity? A Capability-Controlled Audit of Majority-Vote Gain in LLM Ensembles
url: http://arxiv.org/abs/2607.20768v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_22-34-57Z_AreDiversityMetricsMeasuringDiversity_ACapability_.md
generated_at: 2026-07-23 22:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether commonly used diversity metrics in LLM ensembles actually capture true diversity or merely reflect model capability. By auditing five measures across 31,900 subsets of 30 models on MMLU‑Pro and TruthfulQA, the authors find that most diversity indicators are tightly linked to capability rather than genuine complementarity.

## Key Takeaways
- latent complementarity is rare: majority voting only outperforms the best model in a small fraction (9.98%) of size‑3 subsets despite positive oracle gains.
- strict diversity is almost collinear with one minus mean accuracy, showing that raw diversity‑gain associations are strongly capability‑entangled and unstable under explicit controls.
- pairwise co‑failure statistics reveal a modest residual association where higher shared error reduces gain, a direction that holds but varies with configuration.

## Context
LLM ensembles rely on diversity metrics to select models that complement each other, aiming for better collective performance. However, existing measures often conflate capability differences with genuine diversity, leading to suboptimal ensemble design and limited empirical insight into the trade‑offs between accuracy and variety.

## Implications
For practitioners, this work warns against treating diversity scores as reliable proxies for ensemble benefit, urging a shift toward capability‑controlled evaluation. The field should develop metrics that separate true complementarity from correlated accuracy, ensuring ensembles truly leverage model diversity rather than merely stacking similar strengths.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20768v1)
