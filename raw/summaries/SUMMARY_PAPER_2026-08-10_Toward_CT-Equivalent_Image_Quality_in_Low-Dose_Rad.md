---
title: Toward CT-Equivalent Image Quality in Low-Dose Radiotherapy Planning: Conditional Diffusion-Based CBCT-to-CT Synthesis and the Impact of CBCT Input Representation
url: http://arxiv.org/abs/2608.08919v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_21-15-08Z_TowardCT_EquivalentImageQualityinLow_DoseRadiother.md
generated_at: 2026-08-10 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a conditional diffusion‑based deep learning framework that synthesizes high‑quality CT images from low‑dose CBCT scans for radiotherapy planning, aiming to reduce cumulative X‑ray dose while preserving image fidelity. The authors evaluate how different CBCT representations—raw clinical DICOM images versus filtered back‑projection reconstructions—impact the synthesis performance and whether physics‑aware inputs can achieve CT‑equivalent quality.

## Key Takeaways
- The conditional denoising diffusion probabilistic model (DDPM) can generate CT‑like images from low‑dose CBCT, enabling accurate patient registration and dose calculation without extra scans.  
- Using filtered back‑projection reconstructions as input yields superior synthesis results compared to standard clinical DICOM CBCT images, suggesting a more physics‑aware representation improves quality.  
- The study demonstrates that the chosen input representation directly influences the realism of the synthesized CT, highlighting its importance in radiotherapy workflow optimization.

## Context
The integration of AI for image synthesis addresses a growing need to minimize patient radiation exposure while maintaining diagnostic accuracy in medical imaging. Diffusion models have become a powerful tool for generating realistic images from noisy or incomplete inputs, and their application to clinical data is an emerging frontier that could streamline treatment planning.

## Implications
For radiotherapy centers, this approach offers a practical way to cut dose by leveraging existing low‑dose CBCT scans instead of high‑resolution CTs. Practitioners can adopt the chosen input representation to balance image quality and radiation safety, potentially reducing treatment time and patient discomfort.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08919v1)
