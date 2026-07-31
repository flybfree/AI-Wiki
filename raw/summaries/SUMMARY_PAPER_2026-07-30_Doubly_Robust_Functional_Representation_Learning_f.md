---
title: Doubly Robust Functional Representation Learning for Longitudinal Causal Inference with Irregular Histories
url: http://arxiv.org/abs/2607.28567v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-33-42Z_DoublyRobustFunctionalRepresentationLearningforLon.md
generated_at: 2026-07-30 23:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Doubly Robust Functional Representation Learning (DR-FRL) to handle longitudinal causal inference with irregular functional histories, extending doubly robust methods beyond scalar summaries to sequence learners that preserve nuisance information. It shows that when the learned state captures needed nuisance functions, representation error aligns with ordinary error and yields asymptotically linear mean estimators under explicit conditions. Simulations demonstrate gains in high-dimensional confounding, informative measurement, weak support, or heavy-tailed pseudo-outcomes.

## Key Takeaways
- DR-FRL converts irregular histories into estimand-targeted states using functional and temporal encoders, allowing sequence learners to incorporate nuisance functions rather than requiring scalar summaries.
- The method ensures representation error enters the second-order product remainder with ordinary nuisance error, preserving asymptotic linearity under overlap, calibration, stability, and explicit rate conditions.
- Catoni aggregation remains a bounded-influence point estimator separate from Wald inference, enabling both Wald and point estimates.

## Context
Longitudinal causal analysis often deals with irregularly sampled functional data such as lab values or sensor streams, where standard doubly robust estimators that rely on scalar summaries cannot fully exploit the information. This work addresses this gap by applying function representation learning to maintain nuisance functions throughout the estimation pipeline.

## Implications
For researchers and clinicians, DR-FRL enables more accurate causal inference from messy, high-dimensional functional data without discarding valuable temporal structure. Practitioners can apply the framework in healthcare settings where irregular measurements are common, improving decision support for outcomes like ICU disposition despite limited scalar summaries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28567v1)
