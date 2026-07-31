---
title: Negative controls reveal volume-driven confounding in radiomics and imaging foundation model features
published: 2026-07-30T16:02:49Z
authors: Katy L. Scott, Sejin Kim, Joshua Siraj, Caryn Geady, Matthew Boccalon, Mattea Welch, Mogtaba Alim, Andrew J. Hope, Benjamin Haibe-Kains
url: http://arxiv.org/abs/2607.28423v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Negative controls reveal volume-driven confounding in radiomics and imaging foundation model features

## Abstract
Radiomics and imaging foundation models promise non-invasive biomarkers of tumour biology, yet predictive signatures may reflect tumour volume or acquisition artifacts rather than meaningful image structure. We introduce READII-2-ROQC, an open-source framework that uses volume-preserving negative controls to assess whether radiomic and deep imaging features capture independent spatial signals. READII-2-ROQC generates voxel-perturbed images across tumour, background and whole-image regions using configurable randomization strategies, then compares feature behaviour and model performance between original and control images. Applied to three public cancer imaging cohorts, the framework processed 3,552 tumour volumes and extracted PyRadiomics and foundation-model features from original images and nine matched controls. Reproducing published survival and HPV-status signatures, we show that multiple models retain performance after spatial structure is destroyed, revealing volume-driven or contextual confounding, whereas others show perturbation-sensitive signal. READII-2-ROQC provides a scalable quality-control strategy for developing interpretable, biologically grounded imaging biomarkers and reproducible radiomics workflows.

## Metadata
- **Published**: 2026-07-30T16:02:49Z
- **Authors**: Katy L. Scott, Sejin Kim, Joshua Siraj, Caryn Geady, Matthew Boccalon, Mattea Welch, Mogtaba Alim, Andrew J. Hope, Benjamin Haibe-Kains
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28423v1)