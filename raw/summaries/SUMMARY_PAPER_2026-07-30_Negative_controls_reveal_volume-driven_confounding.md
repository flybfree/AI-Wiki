---
title: Negative controls reveal volume-driven confounding in radiomics and imaging foundation model features
url: http://arxiv.org/abs/2607.28423v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_16-02-49Z_Negativecontrolsrevealvolume_drivenconfoundinginra.md
generated_at: 2026-07-30 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces READII-2-ROQC, an open-source framework that uses volume-preserving negative controls to test whether radiomic and deep imaging features capture independent spatial signals. Applied to three cancer cohorts, it processed 3552 tumour volumes with matched controls, finding that some models retain performance when spatial structure is destroyed while others are sensitive, indicating volume-driven confounding.

## Key Takeaways
- The framework generates voxel‑perturbed images across tumour, background and whole‑image regions using configurable randomization strategies to compare feature behaviour between original and control images.
- Reproducing published survival and HPV‑status signatures, the study shows that multiple models retain performance after spatial structure is destroyed, revealing volume‑driven or contextual confounding.
- Other models show perturbation‑sensitive signal, indicating that some radiomic and foundation‑model features are not robust to volume changes.

## Context
Radiomics and imaging foundation models have become central in cancer biomarker discovery, yet their predictive power often depends on artefacts such as tumour size rather than true biological signals. This work addresses the need for rigorous quality control by providing a scalable method to separate genuine spatial information from volume‑driven noise.

## Implications
Practitioners can use READII-2-ROQC to validate that their biomarker models are not merely reflecting tumour volume, leading to more reliable clinical predictions. The framework supports reproducible workflows and helps regulatory bodies assess the independence of imaging features for diagnostic use.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28423v1)
