---
title: JPO: Juris Policy Optimization for Structured Legal Reasoning in Criminal Judgment Prediction
url: http://arxiv.org/abs/2608.29616v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_07-14-02Z_JPO_JurisPolicyOptimizationforStructuredLegalReaso.md
generated_at: 2026-08-31 20:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Juris Policy Optimization (JPO), a post‑training method that enhances Chinese criminal judgment prediction by aligning model outputs with a structured four‑step legal reasoning process. Experiments on multiple language models and three benchmarks show JPO improves both prediction accuracy and reasoning quality compared to supervised fine‑tuning and reinforcement learning baselines.

## Key Takeaways
- The framework leverages teacher‑generated rationales to enforce a standardized four‑step reasoning pipeline, ensuring statutes match facts, charges follow from statutes, and sentencing aligns with charges.  
- JPO uses reinforcement learning with a composite reward that jointly scores legal prediction quality, completeness of reasoning structure, and consistency across steps, avoiding model‑biased rubrics.  
- Token‑level advantage reweighting and adaptive clipping are applied to the most legally salient segments, allowing fine‑grained optimization without destabilizing training.

## Context
Legal judgment prediction is a challenging task that demands logical coherence rather than simple classification, reflecting the need for models to reason over complex statutes and precedents. Current methods often treat reasoning as an afterthought or rely on external rubrics, limiting their ability to capture genuine legal consistency.

## Implications
This work demonstrates that structured reward design can significantly boost both output accuracy and internal reasoning quality in AI systems handling rule‑based domains. Practitioners can adopt JPO’s token‑level reweighting to fine‑tune models for high‑stakes applications where logical correctness is paramount.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29616v1)
