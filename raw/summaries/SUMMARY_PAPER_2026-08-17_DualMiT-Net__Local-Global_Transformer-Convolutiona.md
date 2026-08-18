---
title: DualMiT-Net: Local-Global Transformer-Convolutional Fusion for Breast Mass Segmentation in Mammographic Regions of Interest
url: http://arxiv.org/abs/2608.15019v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_04-08-26Z_DualMiT_Net_Local_GlobalTransformer_ConvolutionalF.md
generated_at: 2026-08-17 21:40
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DualMiT-Net, a dual-branch network designed to segment breast masses from mammograms by combining local mass details with broader tissue context. The model achieves high segmentation performance measured by Dice and Intersection over Union scores on the CBIS-DDSM dataset.

## Key Takeaways
- The model uses Mix Transformer encoder MiT-B5 for the local branch, learning detailed mass shape, texture, and boundary information.
- EfficientNet-B5 encodes the global context of surrounding breast tissue, with a spatial gate that controls how much this information is added during decoding.
- Trained on patient-level splits from CBIS-DDSM, DualMiT-Net reaches Dice 0.9375 and IoU 0.8834, outperforming six standard encoder-decoder baselines.

## Context
Breast mass segmentation remains challenging due to low contrast and irregular shapes in mammographic images. Current methods often rely on single-branch encoders that miss the broader tissue context needed for accurate boundaries.

## Implications
Integrating local detail with global context can boost accuracy and consistency in medical imaging AI tasks. The spatial gate mechanism provides a practical way to balance information flow, offering a template for future segmentation models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15019v1)
