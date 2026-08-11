---
title: Learning from Consensus and Disagreement: Unsupervised On-Policy Self-Distillation with Minority-Trajectory Contrast
url: http://arxiv.org/abs/2608.08764v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_15-23-25Z_LearningfromConsensusandDisagreement_UnsupervisedO.md
generated_at: 2026-08-10 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CoDA, a fully unsupervised on-policy self-distillation method that leverages both consensus and disagreement in model rollouts to improve reasoning without external supervision. The framework extracts answer‑level consensus as stable guidance while using minority trajectories to correct errors through a KTO‑style calibration objective. Experiments show significant gains over baselines on competition‑level math benchmarks.

## Key Takeaways
- Answer‑level consensus is used to condition a frozen teacher, providing dense distributional guidance but risking amplification of correlated errors.
- Minority trajectories are penalized via a reference‑anchored KTO‑style objective, offering unpaired binary feedback that regularizes without assuming consensus is ground truth.
- The combined positive and negative branches create reliable privileged information from the model’s own latent uncertainty structure.

## Context
Current on‑policy self‑distillation relies heavily on external verifiers or gold solutions to break teacher‑student symmetry. This work demonstrates that internal uncertainty can be harnessed, reducing dependency on costly supervision while preserving strong reasoning performance.

## Implications
The approach offers a scalable path for improving language models in settings where ground truth is unavailable, such as real‑time deployment or large‑scale training pipelines. Practitioners can adopt CoDA to stabilize training and enhance factual accuracy without additional labeling resources.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08764v1)
