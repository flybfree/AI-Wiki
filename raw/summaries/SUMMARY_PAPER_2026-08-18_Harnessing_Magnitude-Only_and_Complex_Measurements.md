---
title: Harnessing Magnitude-Only and Complex Measurements for Improved Dynamic MRI Reconstruction with Learned Priors
url: http://arxiv.org/abs/2608.18036v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_17-31-07Z_HarnessingMagnitude_OnlyandComplexMeasurementsforI.md
generated_at: 2026-08-18 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a new reconstruction method that combines complex-valued k-space data with magnitude-only measurements to accelerate steady-state dynamic MRI. Experiments show improved artifact suppression and sharper anatomy compared to standard deep learning approaches.

## Key Takeaways
- The authors demonstrate that k-space magnitudes are consistent across time-frames, providing reliable auxiliary information for reconstruction.
- Their method uses an ADMM unrolling framework with a magnitude‑aware data fidelity formulation that handles non‑differentiable constraints via smoothing and momentum updates.
- Compared to conventional PD‑DL methods, the proposed C+Mag reconstruction yields better artifact suppression, sharper anatomical recovery, and more faithful phase preservation.

## Context
MRI reconstruction traditionally relies on complex k-space samples, but acquiring them is time‑consuming. Recent AI advances enable sparse sampling, yet practical settings lack non‑invasive magnitude measurements. This work bridges that gap by showing how simple magnitude data can enhance model fidelity without extra scans.

## Implications
For clinical practice, the method could reduce scan time and improve image quality for dynamic studies such as cine MRI or phase‑contrast flow imaging. Practitioners may adopt C+Mag reconstruction to obtain faster, higher‑quality diagnostic images, supporting earlier diagnosis and reduced patient burden.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.18036v1)
