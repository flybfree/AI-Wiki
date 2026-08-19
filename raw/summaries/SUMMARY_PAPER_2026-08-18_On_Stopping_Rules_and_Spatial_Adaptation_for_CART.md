---
title: On Stopping Rules and Spatial Adaptation for CART
url: http://arxiv.org/abs/2608.15649v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-16_09-28-49Z_OnStoppingRulesandSpatialAdaptationforCART.md
generated_at: 2026-08-18 20:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the statistical role of stopping rules in CART regression trees and shows that a specific rule yields minimax pointwise rates. Under spatially heterogeneous and anisotropic smoothness, CART with the minimum impurity decrease stopping rule achieves rates up to logarithmic factors, while the common minimum leaf size rule cannot provide spatial adaptation.

## Key Takeaways
- The minimum impurity decrease (MID) stopping rule yields pointwise minimax rates that are optimal up to logarithmic factors in domains with spatially varying smoothness and anisotropy.
- The widely used minimum leaf size stopping rule fails to achieve spatial adaptation, meaning its performance does not improve on local data heterogeneity.
- These results clarify the statistical importance of the MID rule while exposing a limitation of simpler stopping criteria.

## Context
In machine learning theory, understanding how algorithmic choices affect statistical efficiency is crucial for designing robust models. This work bridges theoretical analysis with practical tree-based methods and highlights that empirical success of CART can be linked to rigorous statistical guarantees.

## Implications
For practitioners, the result suggests selecting stopping rules carefully to avoid degraded performance on complex data. It also guides future research on adaptive learning algorithms in high-dimensional settings and can inform regularization strategies that respect local smoothness patterns.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15649v1)
