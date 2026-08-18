---
title: CrevasseSeg: A Label-Efficient UAV Crevasse Segmentation Framework
url: http://arxiv.org/abs/2608.15790v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_15-13-36Z_CrevasseSeg_ALabel_EfficientUAVCrevasseSegmentatio.md
generated_at: 2026-08-17 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents CrevasseSeg, a label-efficient binary segmentation framework that learns crevasse boundaries from unlabelled UAV orthomosaic tiles using self‑supervised objectives. The method achieves high performance with minimal labelled data and outperforms traditional machine learning baselines on the Borebreen glacier.

## Key Takeaways
- DINOv3 features are weak under linear probing but strong under a non‑linear XGBoost classifier, indicating readout choice influences feature strength.
- A UMAP analysis reveals that DINOv3 fragments pixels into many small clusters with interleaved classes, while O‑Net and O‑Net++ embed them onto a single class‑sorted manifold.
- The label‑efficient pipeline reaches 75.33 mDSC / 61.28 mIoU, surpassing standard ML baselines trained on the same 24 labelled images.

## Context
Self‑supervised learning enables models to exploit large unlabeled datasets, reducing reliance on costly expert annotations in remote sensing. This work demonstrates that such approaches can deliver state‑of‑the‑art segmentation without extensive supervision.

## Implications
For glaciological research, CrevasseSeg offers a practical tool for mapping crevasses safely and accurately with limited field data. Practitioners can adopt label‑efficient pipelines to improve model performance while minimizing annotation costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15790v1)
