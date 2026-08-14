---
title: Dual Spatial-Temporal Attribution: Architecture-Aligned Post-Hoc Explainability for Recurrent Graph Anomaly Detection
url: http://arxiv.org/abs/2608.12441v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_15-58-27Z_DualSpatial_TemporalAttribution_Architecture_Align.md
generated_at: 2026-08-13 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces X‑AddGraph, a post‑hoc explainability framework for the AddGraph model that detects anomalies in dynamic graphs. It provides three aligned attributions: spatial relevance from gradients, short‑term temporal attention weights, and long‑term hidden‑state rollback. The detector’s performance is unchanged (ΔAUC=0) while explanations are added.

## Key Takeaways
- X‑AddGraph adds a Dual Spatial‑Temporal Attribution mechanism that combines gradient‑based spatial relevance, zero‑cost short‑term attention weights, and long‑term hidden‑state rollback for edge‑level anomaly explanations.
- The framework is strictly post‑hoc; the original AddGraph model remains frozen, preserving detection performance with ΔAUC=0 verified to ten decimal places.
- Long‑term attribution reveals historical snapshots carry more counterfactual signal than random samples (0.127 vs 0.074), a capability absent in spatially blind explainers.

## Context
Explainability is essential for auditable AI decisions, especially in regulated information systems where automated graph anomaly detection is used. Existing detectors lack transparent attributions, limiting trust and compliance. This work bridges that gap by providing interpretable explanations without sacrificing model performance.

## Implications
For industry practitioners, X‑AddGraph enables regulators to audit edge‑level predictions with concrete reasons, enhancing stakeholder confidence. The method demonstrates that high‑accuracy models can be both performant and explainable, setting a benchmark for future graph anomaly detection systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12441v1)
