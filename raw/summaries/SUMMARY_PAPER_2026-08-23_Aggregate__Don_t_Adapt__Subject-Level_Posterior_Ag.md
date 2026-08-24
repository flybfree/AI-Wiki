---
title: Aggregate, Don't Adapt: Subject-Level Posterior Aggregation and Transductive Calibration for Cross-Site Parkinsonian Gait Severity
url: http://arxiv.org/abs/2608.20587v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-20_21-49-52Z_Aggregate_Don_tAdapt_Subject_LevelPosteriorAggrega.md
generated_at: 2026-08-23 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a subject-level posterior aggregation method that improves Parkinsonian gait severity prediction by integrating multiple walk posteriors within each participant and applying label-free transductive calibration. It achieves a macro-F1 score of 0.6945 on the hidden test, surpassing all other entries including the runner‑up at 0.5807 and the baseline at 0.4289.

## Key Takeaways
- The system’s advantage stems from reproducing the exact benchmark head recipe, averaging per‑walk posteriors within subject groups, and performing a label‑free transductive calibration of feature means and decision operating points.
- Fine‑tuning the encoder yields no benefit; ten alternative encoders performed worse than the baseline.
- The largest gain comes from subject‑level aggregation, which is identified as the binding ceiling for this benchmark.

## Context
The work addresses a critical challenge in clinical AI: transferring performance across unseen medical sites while respecting patient heterogeneity. By focusing on subject‑level aggregation rather than model adaptation, it demonstrates that simple averaging can outperform complex fine‑tuning strategies.

## Implications
For practitioners, the findings suggest that robust cross‑site evaluation may be achieved without extensive retraining, reducing computational cost and data requirements. The approach could inform future Parkinsonian gait assessment tools where subject diversity is high but resources are limited.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20587v1)
