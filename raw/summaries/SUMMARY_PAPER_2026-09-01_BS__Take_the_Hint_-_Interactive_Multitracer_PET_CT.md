---
title: BS: Take the Hint - Interactive Multitracer PET/CT Lesion Segmentation with a Scribble-Conditioned ResEnc U-Net
url: http://arxiv.org/abs/2609.01554v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_17-19-34Z_BS_TaketheHint_InteractiveMultitracerPET_CTLesionS.md
generated_at: 2026-09-01 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a scribble-conditioned residual encoder U-Net that segments PET/CT lesions using user-provided foreground and background scribbles. On the autoPET/CT V challenge it achieves Dice 0.751 and F1 0.733 after five correction rounds, improving over unaided models.

## Key Takeaways
- The model uses four input channels (CT, PET, scribble foreground, scribble background) with zero‑initialised scribble channels to preserve pretrained weights.
- Normalising PET against a per‑scan aorta blood‑pool reference removes tracer and centre scaling without lesion labels.
- Ensembling five fold models via sliding‑window averaging and Gaussian stitching yields higher Dice scores.

## Context
Interactive segmentation is crucial for clinical whole‑body scans where manual marking guides AI, yet prior methods often ignore scribbles or use static priors. This work demonstrates how conditioning on user input can dramatically boost performance across diverse folds.

## Implications
Clinicians and radiologists will benefit from more accurate lesion maps that reduce false positives/negatives, supporting faster diagnosis and treatment planning. The approach also offers a template for future multimodal AI pipelines in medical imaging.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01554v1)
