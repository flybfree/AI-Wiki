---
title: Few-Shot Concept Prompt Learning for Segmentation Foundation Models via Visual Grounding
url: http://arxiv.org/abs/2608.01663v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_03-54-17Z_Few_ShotConceptPromptLearningforSegmentationFounda.md
generated_at: 2026-08-03 23:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Few-Shot Concept Prompt Learning (FS-CPL), a method that learns a continuous visual prompt embedding from a small set of image-mask pairs while keeping the segmentation backbone frozen. The approach replaces traditional natural‑language prompts with visually grounded concepts and achieves up to +0.62 absolute Dice improvement over standard text prompts across multiple medical imaging benchmarks.

## Key Takeaways
- FS-CPL learns a continuous concept prompt embedding p* from K image-mask pairs using mask supervision without retraining the encoder-decoder backbone.
- It delivers absolute Dice improvements of up to +0.62 over canonical text prompts on ultrasound and endoscopy datasets such as BUSI, HC18, TN3K, and CVC-Clinic.
- The method is backbone‑agnostic, lifting both vanilla SAM3 and Medical SAM3 performance.

## Context
Few-shot prompt learning aims to enable interactive segmentation with minimal labeled data. In medical imaging, paired image-text supervision is often scarce, limiting the effectiveness of existing text‑based prompting. Visual grounding offers a promising alternative that can be learned directly from the target distribution.

## Implications
FS-CPL reduces reliance on large annotated datasets and costly model retraining, making it accessible to clinicians and developers alike. By providing high‑quality interactive segmentation without additional training, it could accelerate adoption of AI tools in clinical workflows across diverse imaging modalities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01663v1)
