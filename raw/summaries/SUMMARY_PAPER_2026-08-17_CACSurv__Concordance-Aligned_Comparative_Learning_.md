---
title: CACSurv: Concordance-Aligned Comparative Learning with Large Language Models for Cancer Survival Prediction
url: http://arxiv.org/abs/2608.16594v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_13-51-29Z_CACSurv_Concordance_AlignedComparativeLearningwith.md
generated_at: 2026-08-17 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CACSurv, a report‑centric survival prediction framework that leverages large language models to order patient prognostic rankings rather than predict exact event times. By reformulating survival modeling as comparative reasoning and using concordance‑aligned rewards, the method handles censored data naturally. On the TCGA‑SurvReport benchmark, CACSurv achieves the highest C‑index across six cohorts, outperforming existing methods by up to 6.5 percentage points.

## Key Takeaways
- The framework treats survival prediction as mini‑cohort comparative reasoning, allowing LLMs to predict relative orderings instead of exact times.
- Concordance‑aligned rewards incorporate right censoring, so censored patients still provide ranking supervision without requiring precise event‑time targets.
- CACSurv reaches the top performance on TCGA‑SurvReport with an average C‑index of 0.722, surpassing both strong survival models and LLM time‑regression baselines.

## Context
Current AI research often focuses on predicting continuous outcomes or binary labels, but many medical tasks involve ordering information under uncertainty such as censored survival data. This paper bridges that gap by applying LLMs to comparative reasoning, demonstrating how language models can be guided with alignment rewards to solve problems where exact targets are unavailable.

## Implications
For clinicians and researchers, CACSurv offers a practical way to incorporate patient narratives into prognostic assessments without sacrificing ranking consistency. The approach could improve risk stratification tools, support personalized treatment planning, and set a precedent for applying LLMs to other ordering‑based medical tasks like tumor progression sequencing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16594v1)
