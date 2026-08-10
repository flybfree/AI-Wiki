---
title: Machine Learning-Based Inter-Crystal Scatter Recovery for Ultra-High Resolution PET Imaging
url: http://arxiv.org/abs/2608.07155v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_12-21-17Z_MachineLearning_BasedInter_CrystalScatterRecoveryf.md
generated_at: 2026-08-09 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a feed‑forward neural network designed to recover inter‑crystal scatter (ICS) events in ultrahigh‑resolution PET detectors that are fully pixelated and segmented. By inferring the line‑of‑response from the first Compton interaction, the method recovers previously discarded data without sacrificing spatial resolution.

## Key Takeaways
- The neural network achieves a 70% to 106% increase in sensitivity compared with conventional rejection or suboptimal positioning methods.
- Spatial resolvability is preserved down to 1.6 mm, maintaining the ultrahigh‑resolution capability of UHR‑PET.
- Validation was performed using both Monte Carlo simulations and experimental data from LabPET‑II based preclinical and brain scanners.

## Context
This work addresses a growing challenge in AI‑driven medical imaging: recovering low‑probability events that are essential for high‑resolution reconstruction. The integration of deep learning into PET detector readout demonstrates how machine learning can complement traditional signal processing to overcome hardware limitations.

## Implications
Practitioners can reduce scan times and radiation doses while keeping image quality intact, making UHR‑PET more accessible. The approach also sets a precedent for applying neural networks to other imaging modalities where event recovery is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07155v1)
