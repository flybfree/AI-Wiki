---
title: Online Variance Reduction for Domain Adaptation on Streaming Data
url: http://arxiv.org/abs/2607.20374v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_17-04-29Z_OnlineVarianceReductionforDomainAdaptationonStream.md
generated_at: 2026-07-23 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Adaptive vaRiance Reduction via Online reWeighting (ARROW), an online variance reduction algorithm for the maximum mean discrepancy (MMD) and correlation alignment (CORAL) loss functions on streaming data. It maintains moving average references of the alignment statistics, adaptively reweights incoming minibatches so that the minibatch and reference statistics are aligned, and uses a relaxed weight‑optimisation scheme to keep computation tractable. The method also supports distributed implementations where each node maintains its own moving averages. Experiments show competitive runtime, variance reduction, and target domain accuracy compared with offline algorithms.

## Key Takeaways
- ARROW uses adaptive reweighting to keep minibatch and reference statistics aligned in an online setting.
- A relaxed weight‑optimisation scheme makes the problem tractable for streaming data.
- Results demonstrate comparable performance to offline SVR algorithms in terms of speed, variance reduction, and target accuracy.

## Context
Online learning requires methods that update incrementally without recomputing full references. Variance reduction techniques are usually batch‑oriented, limiting their applicability. ARROW bridges this gap by providing an online variant for MMD and CORAL.

## Implications
Practitioners can apply ARROW to real‑time domain adaptation tasks such as recommendation systems or sensor fusion where data arrives continuously. The algorithm’s efficiency makes it suitable for distributed environments with limited compute resources. Future work could extend ARROW to other loss functions beyond MMD and CORAL.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20374v1)
