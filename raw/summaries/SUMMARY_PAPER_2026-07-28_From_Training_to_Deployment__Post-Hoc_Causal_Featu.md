---
title: From Training to Deployment: Post-Hoc Causal Feature Identification via Sensitivity Ratios
url: http://arxiv.org/abs/2607.25546v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_10-26-09Z_FromTrainingtoDeployment_Post_HocCausalFeatureIden.md
generated_at: 2026-07-28 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces a post‑hoc diagnostic called the Normalised Sensitivity Ratio that identifies which features drive model predictions causally versus spuriously when environments differ mainly in spurious feature means. It proves exact identification under a linear structural causal model with three or more non‑degenerate environments and provides quantitative failure modes.

## Key Takeaways  
- NSR equals the squared coefficient of variation of per‑environment sensitivity, so it remains constant for causal features while increasing for spurious ones.  
- Weak shifts cause an O(ε^4) collapse that makes identification unreliable.  
- Proxy attenuation yields an O((1‑α)^4) error that reduces finite‑sample rates.

## Context  
In AI fairness and model interpretability, distinguishing causal from spurious drivers is crucial because training pipelines are often inaccessible after deployment. This work offers a method that works even when only the trained model is available.

## Implications  
Practitioners can now evaluate model reliance without retraining, supporting trustworthy deployment in multi‑site clinical or genomics settings. The method’s finite‑sample rates guide sample size planning and highlight when the structured‑shift regime may break.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25546v1)
