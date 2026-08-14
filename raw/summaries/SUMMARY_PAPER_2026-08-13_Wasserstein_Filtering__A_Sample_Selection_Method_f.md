---
title: Wasserstein Filtering: A Sample Selection Method for Robust Distribution Learning
url: http://arxiv.org/abs/2608.13418v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_16-12-28Z_WassersteinFiltering_ASampleSelectionMethodforRobu.md
generated_at: 2026-08-13 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Wasserstein Filtering (WF), a sample selection method that removes contaminated data by selecting the subset whose empirical distribution maximizes its Wasserstein distance to the fully corrupted distribution. It proves minimax optimality under the Far Exclusion and Local Projection (FELP) model and demonstrates strong performance on synthetic, benchmark, and diffusion‑model datasets.

## Key Takeaways
- WF discards a fraction of suspicious samples by maximizing the geometric Wasserstein distance to the contaminated empirical measure, isolating outliers that are geometrically influential.  
- The method uses three algorithms: marginal screening (SinkMarg), joint optimization with entropic optimal transport (SinkWF), and sliced Wasserstein approximation (SlicedWF).  
- Under the FELP contamination model, WF achieves minimax optimality for distribution families with bounded covariance.

## Context
In AI, learning from noisy or corrupted data is a persistent challenge that can degrade model performance. This work addresses this by providing a principled, model‑agnostic preprocessing step that separates genuine samples from outliers without requiring explicit anomaly detectors. The theoretical grounding in optimal transport and Wasserstein geometry makes the approach robust to various corruption patterns.

## Implications
For practitioners, WF offers an efficient way to clean datasets before training generative or discriminative models, reducing downstream errors caused by outliers. In industry, this can lead to higher‑quality predictions and lower computational cost for large‑scale AI pipelines. The method’s theoretical optimality also provides a benchmark for future research on robust distribution learning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13418v1)
