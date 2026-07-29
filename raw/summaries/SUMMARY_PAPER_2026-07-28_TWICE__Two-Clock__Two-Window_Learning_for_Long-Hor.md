---
title: TWICE: Two-Clock, Two-Window Learning for Long-Horizon Conversion Prediction in Online Advertising
url: http://arxiv.org/abs/2607.25404v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_08-02-41Z_TWICE_Two_Clock_Two_WindowLearningforLong_HorizonC.md
generated_at: 2026-07-28 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TWICE, a framework for predicting long‑horizon conversion rates in online advertising where feedback arrives late. By treating the problem as two clocks—one for clicks and one for conversions—TWICE learns both a target‑window conversion probability and a cumulative delay distribution function to generate monotone predictions without needing historical lookups or convolutions.

## Key Takeaways
- The click clock supplies timely but only partially observed supervision, allowing the model to estimate current status likelihoods over the short base observation window.  
- Newly arrived conversions on the longer conversion clock train a delay model that captures how delays are weighted by historic click cohorts with varying traffic and conversion rates.  
- TWICE uses fixed click‑time predicted CVR as cohort exposure in an arrival‑conditioned likelihood, producing self‑contained aggregate records that enable single CDF generation for any horizon up to the target window.

## Context
Long‑horizon prediction under delayed feedback remains a challenge because traditional models rely on full historical data or convolutions that are computationally heavy. TWICE’s two‑clock approach separates short‑term click information from long‑term conversion delays, offering a more efficient and interpretable solution for real‑time serving.

## Implications
For advertisers, TWICE can boost revenue by accurately forecasting conversions even when feedback is delayed, leading to better budget allocation. Practitioners should adopt this framework as it reduces latency in prediction pipelines while maintaining high accuracy across diverse traffic patterns.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25404v1)
