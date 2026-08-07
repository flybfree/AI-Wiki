---
title: Big, Bright, or Invisible: A Frozen-Feature Benchmark of 3D CT Foundation Models
url: http://arxiv.org/abs/2608.05960v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_12-34-17Z_Big_Bright_orInvisible_AFrozen_FeatureBenchmarkof3.md
generated_at: 2026-08-06 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a benchmark evaluating ten frozen CT foundation models on thoracic scans using multiple methods to assess diagnostic breadth. It finds no single model dominates across all evaluation contexts and highlights that small low‑contrast lesions remain hard for all encoders.

## Key Takeaways
- The study shows rankings vary widely depending on the evaluation context, indicating no universal SOTA among frozen CT encoders.
- Models with fine‑grained image tokenization and vision‑language alignment generally outperform others, suggesting that explicit labels can substitute for scale in performance.
- Detectability of findings is limited by contrast against tissue and spatial extent; widespread or high‑contrast abnormalities are reliably recovered while small low‑contrast focal lesions persist.

## Context
Foundation models aim to provide generalizable representations from medical imaging, but their ability to capture subtle pathologies remains unproven. This benchmark reveals that performance is heavily influenced by the physical properties of the anomaly rather than model architecture alone.

## Implications
Practitioners should prioritize lesion‑level pretraining for low‑contrast findings and consider multimodal alignment strategies when selecting CT foundation models. The results guide future research toward architectures that better represent small structures in medical scans.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05960v1)
