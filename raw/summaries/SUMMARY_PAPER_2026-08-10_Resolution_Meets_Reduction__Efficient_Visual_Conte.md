---
title: Resolution Meets Reduction: Efficient Visual Context for 3D Radiology Report Generation
url: http://arxiv.org/abs/2608.08713v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_13-57-50Z_ResolutionMeetsReduction_EfficientVisualContextfor.md
generated_at: 2026-08-10 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how to allocate a fixed number of vision tokens across input field of view, spatial resolution, and projection compression when generating radiology reports from 3D CT scans. It finds that anatomy‑guided cropping combined with the PerceiverResampler projector yields the highest clinical performance, achieving state‑of‑the‑art macro F1 scores on two benchmark datasets.

## Key Takeaways
- Anatomy‑guided region of interest cropping consistently improves clinical macro F1 by up to 3.7 points across most configurations, especially with the 3D ViT Primus encoder.
- The PerceiverResampler projector paired with higher‑resolution Curia features provides the strongest performance in both resolution and compression studies on CT‑RATE and Merlin datasets.
- Increasing input resolution is highly dependent on the chosen projector; without a suitable compressor, higher resolutions lead to diminishing returns or severe loss of detail.

## Context
Vision‑language models are increasingly used for automated medical report generation, yet 3D volumetric data generate massive visual token streams that strain downstream language models. Efficiently compressing these sequences while preserving clinically relevant information is a critical bottleneck in deploying such systems at scale.

## Implications
Efficient token allocation enables faster inference and broader deployment of AI radiology assistants without sacrificing diagnostic quality. The findings guide researchers toward practical architectures that balance resolution, compression, and clinical relevance for real‑world medical imaging pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08713v1)
