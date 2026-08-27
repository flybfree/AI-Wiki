---
title: DeMMO: Longitudinal and Cross-Disease Modelling of Digital Mobility Outcomes via Multi-Task Learning
url: http://arxiv.org/abs/2608.25073v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-25_19-07-32Z_DeMMO_LongitudinalandCross_DiseaseModellingofDigit.md
generated_at: 2026-08-26 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper proposes DeMMO a framework for longitudinal multi‑disease multi‑outcome modelling of digital mobility outcomes. It outperforms baselines on the Mobilise‑D dataset achieving best prediction performance and identifies reliable DMO patterns.

## Key Takeaways  
- DeMMO models each disease‑outcome pair with its own longitudinal coefficient matrix, allowing multivariate DMO relationships across diseases without requiring shared participants.  
- The framework combines temporal regularisation with stable visit‑specific feature selection to improve stability of predictions.  
- Evaluation on the large‑scale Mobilise‑D dataset shows DeMMO achieves superior overall and outcome‑specific performance compared to nine strong baselines.

## Context  
Temporal multi‑task learning is a growing area in AI that seeks to predict multiple related outcomes from sequential data. Existing methods either focus on single diseases or assume participant overlap, limiting applicability in real‑world clinical monitoring where disease cohorts are often distinct.

## Implications  
DeMMO provides clinicians with interpretable longitudinal DMO patterns that can be used for ongoing disease monitoring and treatment evaluation. By enabling cross‑disease insight without paired data, it supports personalized care strategies across complex health conditions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25073v1)
