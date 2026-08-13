---
title: A Neighborhood Attention Transformer Network for Enhanced 3D Segmentation of the Left Anterior Descending Artery
url: http://arxiv.org/abs/2608.12274v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_17-13-59Z_ANeighborhoodAttentionTransformerNetworkforEnhance.md
generated_at: 2026-08-12 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces NA‑UNETR, a transformer‑based segmentation network that combines neighborhood attention and dilated neighborhood attention to capture both fine LAD details and long‑range context in 3D CT. The model is pretrained on large general coronary data and fine‑tuned with LoRA on limited free‑breathing scans, achieving superior Dice score, Hausdorff distance, and centerline stability compared with prior methods.

## Key Takeaways
- NA‑UNETR reaches a 45.64% Dice score and 38.16 mm HD95 on ImageCAS, improving Dice by 3.10 points over nnU‑Net and reducing Hausdorff distance by 2.96 mm relative to Swin UNETR.  
- The composite Dice‑Focal loss balanced with homoscedastic uncertainty yields the strongest boundary accuracy among all tested models.  
- Ablation studies confirm that residual blocks, variable kernels, and uncertainty‑weighted loss each contribute meaningfully to performance.

## Context
Segmenting small coronary arteries in low‑contrast CT remains a bottleneck for precise radiotherapy planning due to limited annotated data and inherent anatomical variability. Transformer architectures offer superior context modeling but often require large datasets or heavy computation; NA‑UNETR addresses these challenges with efficient attention mechanisms and parameter‑efficient fine‑tuning.

## Implications
The approach provides radiographers and physicists with a computationally feasible tool for substructure‑level LAD delineation, potentially reducing dose exposure by enabling more accurate treatment planning. As AI models become standard in medical imaging, such specialized architectures can improve clinical outcomes across cardiac and thoracic radiotherapy workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12274v1)
