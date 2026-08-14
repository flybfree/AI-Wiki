---
title: CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Representation
url: http://arxiv.org/abs/2608.12944v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_08-21-06Z_CardioState_JEPA_Delay_AwareCross_ModalLearningofa.md
generated_at: 2026-08-13 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CardioState-JEPA, a foundation model that learns a shared cardiac representation from electrocardiography, photoplethysmography, and phonocardiography. By predicting masked latent cardiac states across modalities with a delay‑aware alignment, the encoder achieves significant gains in downstream classification tasks.

## Key Takeaways
- The model maps heterogeneous waveforms into a common token space using a single shared Transformer encoder.
- A learned delay aligner synchronizes ECG, PPG, and PCG signals at corresponding cardiac time points for cross‑modal prediction.
- Downstream performance improves by 8.2 AUROC on PPG classification, 18.8 AUROC on PCG murmur detection, and 15.5 AUROC on ECG classification over self‑supervised baselines.

## Context
Cardiac signal fusion remains limited to single‑sensor models that ignore the complementary information across modalities. This work demonstrates how joint learning can unlock mutual supervision of diverse cardiac signals without requiring synchronized recordings.

## Implications
The findings suggest a path toward unified cardiac foundation models that can be applied across multiple sensing platforms, reducing reliance on privileged clinical text or large labeled datasets and accelerating research in wearable health monitoring.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12944v1)
