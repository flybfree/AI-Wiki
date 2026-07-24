---
title: Censoring-Aware In-Context Learning for Generalized Supplier Lead Time Estimation in Supply Chain Planning
url: http://arxiv.org/abs/2607.18530v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_21-45-43Z_Censoring_AwareIn_ContextLearningforGeneralizedSup.md
generated_at: 2026-07-23 23:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LeadTime-ICL, a censoring‑aware in‑context learning model for forecasting supplier lead times. The authors show that the model beats standard methods on 24 real supply‑chain datasets and achieves the lowest point and probabilistic errors on many of them.

## Key Takeaways
- The model leverages a transformer backbone with a conditional normalizing‑flow head to output a full predictive distribution over lead times, preserving right‑censored information. - It is pretrained on synthetic censored data so that new industrial datasets can be adapted without updating any parameters. - Theoretical analysis bounds the excess CRPS by prior misspecification and amortized approximation errors.

## Context
In AI for supply chain planning, most forecasting approaches ignore the fact that some orders have not yet arrived, leading to biased estimates. This work demonstrates how in‑context learning can be combined with survival‑type modeling to handle censored data without task‑specific retraining.

## Implications
Practitioners can deploy a single pretrained model across multiple industries, reducing development cost and improving planning accuracy. The approach encourages the industry to adopt probabilistic forecasts that account for uncertainty inherent in right‑censored lead times.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18530v1)
