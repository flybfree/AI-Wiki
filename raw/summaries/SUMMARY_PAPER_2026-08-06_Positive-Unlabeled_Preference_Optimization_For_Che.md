---
title: Positive-Unlabeled Preference Optimization For Chest X-ray Report Generation
url: http://arxiv.org/abs/2608.05341v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_18-59-23Z_Positive_UnlabeledPreferenceOptimizationForChestX_.md
generated_at: 2026-08-06 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PU-DPO, a preference optimization method for generating chest X-ray reports that mitigates omission noise caused by retrospective training data. By treating absent findings as unlabeled rather than negative examples, the framework uses contrastive pairs where one response mentions a specific finding and the other omits it, enabling the model to learn from visual evidence. Experiments on semi‑synthetic data and real benchmarks show consistent improvements in detection rates and recovery of hidden positives compared with prior approaches.

## Key Takeaways
- PU-DPO reframes omission noise as unlabeled data, allowing preference supervision without relying on true negative labels.
- The method constructs contrastive pairs by editing model responses to either include or exclude a target finding, making the inclusion version naturally preferred when aligned with visual evidence.
- Real‑world chest radiograph benchmarks demonstrate that PU-DPO yields higher detection rates and better recovery of hidden positives than standard methods.

## Context
Vision‑language models for medical report generation often inherit omissions from retrospective reports, which can degrade performance. This work addresses the challenge by designing a preference‑based optimization loop that leverages contrastive learning to prioritize clinically relevant mentions over omitted ones.

## Implications
For radiology AI developers, PU-DPO offers a practical way to improve diagnostic accuracy without requiring large labeled datasets of negative examples. Practitioners can adopt this framework to generate more complete reports, potentially reducing missed findings and enhancing patient care.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05341v1)
