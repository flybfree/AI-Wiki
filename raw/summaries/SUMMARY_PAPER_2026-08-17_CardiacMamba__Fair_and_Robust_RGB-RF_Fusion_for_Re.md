---
title: CardiacMamba: Fair and Robust RGB-RF Fusion for Remote Heart Rate Estimation via State Space Modeling
url: http://arxiv.org/abs/2608.15831v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_16-05-24Z_CardiacMamba_FairandRobustRGB_RFFusionforRemoteHea.md
generated_at: 2026-08-17 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
CardiacMamba introduces a fair and robust RGB‑RF fusion framework for remote heart rate estimation that mitigates illumination changes, motion artifacts, and skin‑tone dependent optical reflectance. By integrating optical facial cues with radio‑frequency cardiac motion cues through state space modeling, the model achieves state‑of‑the‑art performance on the EquiPleth dataset with a mean absolute error of 0.96 bpm, root‑mean‑square error of 3.06 bpm, and Pearson correlation of 0.97.

## Key Takeaways
- The Temporal Difference Mamba Module (TDMM) captures subtle RF temporal variations that are critical for accurate heart rate inference.
- A bidirectional state space model aligns heterogeneous RGB‑RF dynamics, ensuring consistent representation across modalities.
- Channel‑wise Fast Fourier Transform (CFFT) refines spectral information per channel, reducing the light‑dark skin‑tone MAE gap to 0.26 bpm.

## Context
Remote photoplethysmography relies on AI models that fuse visual and physiological signals to estimate heart rate without contact sensors. Recent advances in transformer architectures have enabled such fusion, yet illumination and motion remain persistent challenges. CardiacMamba’s state space modeling approach offers a principled way to handle these heterogeneous data streams.

## Implications
For wearable health devices, this work demonstrates that non‑contact HR monitoring can be both fair across skin tones and robust under sensor degradation. Practitioners can adopt the TDMM and CFFT modules to improve real‑world deployment of rPPG systems in diverse environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15831v1)
