---
title: Training-Free Human-in-the-Loop Anomaly Detection via Memory Bank Correction
url: http://arxiv.org/abs/2608.17775v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_13-39-21Z_Training_FreeHuman_in_the_LoopAnomalyDetectionviaM.md
generated_at: 2026-08-18 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a training-free human-in-the-loop anomaly detection system that corrects a PatchCore detector by directly editing its memory bank using domain expert feedback without retraining or gradients. The framework inserts normal patches into the detector’s memory via a self‑calibrating novelty gate, improving performance on 12 of 15 MVTec AD categories while preserving accuracy for others.

## Key Takeaways
- A median 66% gap to an uncorrected fully trained bank is closed using only ten golden samples and operator corrections.  
- Corrections improve 12 of 15 MVTec AD categories with no harm, outperforming hundreds of samples without them.  
- Passive and active querying are statistically indistinguishable, but a matched‑label‑budget control shows gains at 43% of exhaustive review cost.

## Context
The work addresses the challenge of deploying anomaly detectors where labeled data is scarce, such as in production environments with limited golden samples. It demonstrates that human feedback can effectively augment memory banks without requiring costly retraining pipelines, aligning with trends toward low‑data, on‑device AI solutions.

## Implications
For industry practitioners, this approach reduces reliance on large training datasets and expensive engineering resources, enabling rapid deployment of anomaly detection in real time. Practitioners can leverage expert corrections to maintain high accuracy while minimizing false positives, supporting safer and more efficient manufacturing processes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17775v1)
