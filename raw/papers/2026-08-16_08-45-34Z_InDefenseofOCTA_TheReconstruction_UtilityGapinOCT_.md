---
title: In Defense of OCTA: The Reconstruction-Utility Gap in OCT-to-OCTA Synthesis
published: 2026-08-16T08:45:34Z
authors: Michael Chertok, Alon Tiosano, Orly Gal-Or, Lior Kramarski, Einav Baharav Shlezinger, Irit Bahar, Lior Wolf
url: http://arxiv.org/abs/2608.15626v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# In Defense of OCTA: The Reconstruction-Utility Gap in OCT-to-OCTA Synthesis

## Abstract
Optical coherence tomography angiography (OCTA) images retinal blood flow, giving capillary-perfusion and foveal-avascular-zone biomarkers that grade diabetic-retinopathy ischemia. Because OCTA hardware is less common than structural OCT, recent work synthesizes it from OCT, reporting strong reconstruction (3D PSNR > 31 dB, SSIM > 0.9). We ask not whether the synthetic image looks similar, but whether it supports the measurements OCTA is acquired for. A frozen real-OCTA segmenter, applied as a probe to two synthesizers (XOCT, TransPro), shows downstream Dice falling with structural fineness: large vessels survive (0.862 -> 0.831) while the fine capillary network collapses (0.798 -> 0.635, five times the large-vessel loss; paired Wilcoxon p < 1e-3), TransPro worse throughout. A matched-blur control shows this detail is fabricated, not blurred. Retrained on a private Spectralis dataset, neither synthesizer reproduces the neovascular lesion (qualitative, n=3). Reconstruction fidelity is not clinical utility; we establish downstream-task fidelity as the evaluation OCT-to-OCTA synthesis needs.

## Metadata
- **Published**: 2026-08-16T08:45:34Z
- **Authors**: Michael Chertok, Alon Tiosano, Orly Gal-Or, Lior Kramarski, Einav Baharav Shlezinger, Irit Bahar, Lior Wolf
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15626v1)