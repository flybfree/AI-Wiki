---
title: An Open-Source Two-Stage Computer Vision Pipeline for Fine-Grained Vehicle Classification using Vision Transformers
url: http://arxiv.org/abs/2606.05149v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-03_17-53-33Z_AnOpen_SourceTwo_StageComputerVisionPipelineforFin.md
generated_at: 2026-06-11 10:52
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an open-source two-stage pipeline that first detects vehicles with RT-DETR and then classifies their body types using a fine-tuned Vision Transformer. On in-distribution data it reaches 94% accuracy across six categories, while handling out-of-distribution cases with confidence abstention.

## Key Takeaways
- The pipeline uses a confidence threshold of 0.60 to abstain rather than misclassify, reducing false predictions when model uncertainty is high.
- Performance degrades for minivan due to higher abstention rates but avoids incorrect labels, showing honest uncertainty handling.
- All models and scripts are released as open-source, enabling reproducibility in roadside video analysis.

## Context
Fine-grained vehicle classification from naturalistic video remains underexplored, limiting automated safety tools. Vision Transformers offer promising alternatives to traditional CNNs for such tasks.

## Implications
This work provides a deployable framework that can be integrated into cycling safety monitoring systems, improving risk assessment without overconfident errors. Open-source availability accelerates adoption across research and industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.05149v1)
