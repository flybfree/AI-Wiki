---
title: MIRAGE: Multi-scale Lesion-Informed Representation with Auxiliary Guidance for MRI Contrast Enhancement
url: http://arxiv.org/abs/2607.19137v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_14-26-59Z_MIRAGE_Multi_scaleLesion_InformedRepresentationwit.md
generated_at: 2026-07-23 23:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MIRAGE, a residual 2D U-Net that synthesizes realistic post‑contrast breast MRI images from a single pre‑contrast slice while preserving lesion fidelity. It achieves state‑of‑the‑art performance on the MAMA‑SYNTH dataset across multiple metrics and improves downstream lesion localization compared to baselines.

## Key Takeaways
- The method uses an asymmetric penalty that discourages missing tumor enhancement, ensuring lesions are not omitted in generated images.
- Multi‑scale auxiliary tumor segmentation provides fine‑grained supervision at different resolutions, capturing subtle changes during contrast administration.
- Guidance from a frozen nnU‑Net post‑contrast segmentation helps align the synthetic appearance with realistic lesion boundaries.

## Context
Current MRI synthesis tasks face a trade‑off between realistic appearance and accurate lesion representation. Existing approaches often prioritize one objective over another, limiting clinical utility. MIRAGE addresses this by integrating lesion‑aware losses that directly target both fidelity and utility.

## Implications
For radiologists and AI developers, MIRAGE demonstrates that task‑specific loss functions can outperform generic adversarial objectives in medical imaging synthesis. This encourages the design of synthetic data pipelines that align with downstream diagnostic needs rather than raw visual realism alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19137v1)
