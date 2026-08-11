---
title: Toward CT-Equivalent Image Quality in Low-Dose Radiotherapy Planning: Conditional Diffusion-Based CBCT-to-CT Synthesis and the Impact of CBCT Input Representation
published: 2026-08-09T21:15:08Z
authors: Alzahra Altalib, Chunhui Li, Christopher Hamill Taylor, Sankar Pillai, Alessandro Perelli
url: http://arxiv.org/abs/2608.08919v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Toward CT-Equivalent Image Quality in Low-Dose Radiotherapy Planning: Conditional Diffusion-Based CBCT-to-CT Synthesis and the Impact of CBCT Input Representation

## Abstract
During standard radiotherapy planning, repeated CT acquisitions are often required for patient registration, verification, and adaptive planning, resulting in increased cumulative X-ray dose. To mitigate this, low-dose cone-beam CT (CBCT) is routinely acquired during treatment delivery. However, CBCT image quality remains insufficient for accurate dose calculation and adaptive radiotherapy planning due to increased scatter, noise, beam hardening, and reconstruction related artifacts. This study develops a supervised deep learning based CBCT to CT synthesis framework using a conditional denoising diffusion probabilistic model (DDPM), where the generation of a CT-based planning for accurate positioning and dose calculation is obtained using generative models with low dose CBCT imaging. Beyond demonstrating CBCT to CT synthesis, the primary objective is to investigate how the representation of CBCT input data, either standard clinical DICOM CBCT images or filtered back-projection (FDK) reconstructions from raw projection data, affects the performance of diffusion based CT synthesis. The overarching aim is to assess whether physics aware CBCT representations better support CT-equivalent image quality while maintaining reduced imaging dose in radiotherapy workflows.

## Metadata
- **Published**: 2026-08-09T21:15:08Z
- **Authors**: Alzahra Altalib, Chunhui Li, Christopher Hamill Taylor, Sankar Pillai, Alessandro Perelli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08919v1)