---
title: Similarity Weighted Aggregation with Global Differential Privacy for Federated Brain Lesion Segmentation
url: http://arxiv.org/abs/2608.00872v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_21-23-32Z_SimilarityWeightedAggregationwithGlobalDifferentia.md
generated_at: 2026-08-03 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DP‑SimAgg, a federated learning framework that combines similarity‑weighted aggregation with server‑side differential privacy to train brain lesion segmentation models across hospitals without sharing raw data. The method limits update magnitude via L2 clipping, assigns weights based on similarity between local and global models, and adds calibrated Gaussian noise at the central server, achieving per‑round (ε, δ)-DP guarantees under a known sensitivity bound. Experiments on the FeTS 2022 dataset show Dice scores of 0.6357, 0.5305, and 0.5274 for enhancing tumor, tumor core, and whole tumor regions with ε=1 per round.

## Key Takeaways
- The framework mitigates non‑IID data distribution effects by using similarity‑based aggregation weights while preserving privacy through calibrated Gaussian noise.
- L2 clipping caps collaborator updates to bound sensitivity, enabling a strict per‑round privacy budget of ε=1 with cumulative ε_total=20 over 20 rounds.
- Performance remains competitive (Dice ≈0.63) even under tight privacy constraints, approaching non‑private baselines when the per‑round budget is relaxed.

## Context
Federated learning offers a way to train deep models on medical images without moving patient data across institutions, addressing both heterogeneity and privacy concerns. Recent work has focused on integrating differential privacy into federated settings, yet few methods combine similarity weighting with calibrated server‑side noise for brain segmentation tasks.

## Implications
DP‑SimAgg demonstrates that privacy‑preserving federated training can maintain high clinical utility in medical imaging, encouraging adoption by hospitals seeking to collaborate securely. Practitioners can leverage this approach to deploy robust lesion segmentation tools while complying with data protection regulations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00872v1)
