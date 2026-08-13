---
title: Dual-Domain Cross-Modal Decoding for Clinical Text-Guided Medical Image Segmentation
url: http://arxiv.org/abs/2608.11335v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_18-40-52Z_Dual_DomainCross_ModalDecodingforClinicalText_Guid.md
generated_at: 2026-08-12 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Dual-Domain Cross-Modal Decoding (DD-CMD) to improve clinical text-guided segmentation of pulmonary infections by integrating spatial and frequency-based language guidance. It combines Text-Guided Spatial Cross-Attention for aligning visual tokens with text semantics and Spectral-Text Adaptive Modulation for recalibrating decoder channels using learned band-energy statistics. The method achieves higher Dice and mIoU scores than prior baselines on QaTa-COV19 and MosMedData+.

## Key Takeaways
- Text-Guided Spatial Cross-Attention aligns multi-scale visual tokens with text semantics and updates features through gated residual fusion, enabling precise spatial decoding. 
- Spectral-Text Adaptive Modulation computes learnable band-energy statistics via a 2D DCT and predicts FiLM parameters to recalibrate decoder channels for frequency-aware decoding. 
- DD-CMD embeds both modules into a coarse-to-fine decoder and uses a lightweight two-stage refinement module to restore full-resolution masks, resulting in average gains of +1.96 Dice and +2.67 mIoU.

## Context
Current text-guided segmentation models focus on spatial alignment but ignore frequency content that influences texture and boundaries, limiting their ability to capture fine-grained anatomical details. This work addresses the gap by adding a frequency domain component that leverages learned spectral statistics for more accurate channel recalibration.

## Implications
The integration of frequency-aware decoding could improve diagnostic precision in medical imaging applications where subtle patterns matter. Practitioners may adopt DD-CMD to reduce false positives and enhance treatment planning, especially in infection detection where early signs are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11335v1)
