---
title: Matrix-Free Photoacoustic Image Reconstruction via Sensor-Token Self-Attention
url: http://arxiv.org/abs/2607.25576v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_11-00-28Z_Matrix_FreePhotoacousticImageReconstructionviaSens.md
generated_at: 2026-07-28 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Sensor Attention Network (SAN), a transformer that reconstructs photoacoustic images directly from sensor time series without using the system matrix. It achieves high fidelity metrics compared to existing methods and reduces reconstruction time by an order of magnitude.

## Key Takeaways
- SAN treats each full time series as a token, mapping raw measurements directly to image without H-matrix inference.
- The network attains mean per-sensor Pearson correlation 0.919 with k-space apodization and Gaussian damping improving mismatch reduction by 49%.
- SAN outperforms LISTA and other solvers on SSIM, PSNR, NMSE, confirming superiority via statistical tests.

## Context
This work addresses the computational bottleneck of iterative compressive‑sensing based reconstruction in photoacoustic tomography. By replacing matrix‑dependent steps with attention mechanisms, it aligns deep learning with real‑time clinical needs.

## Implications
Clinicians can deploy PAT scanners that generate images instantly, expanding the utility of non‑invasive imaging for diagnostics. The method also sets a benchmark for transformer‑based inverse problems in medical imaging research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25576v1)
