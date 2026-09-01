---
title: AOI-Net: Structural Face AOI-Guided Eye-Gaze Track Representation Learning for Autism Spectrum Disorder Detection
url: http://arxiv.org/abs/2608.29289v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_14-26-12Z_AOI_Net_StructuralFaceAOI_GuidedEye_GazeTrackRepre.md
generated_at: 2026-08-31 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AOI-Net a framework that combines temporal eye-gaze dynamics with structural Area of Interest organization to detect autism spectrum disorder. Experiments on a large clinical dataset show it outperforms existing methods and provides interpretable gaze modeling for ASD screening.

## Key Takeaways
- AOI-Net jointly models short‑term temporal dynamics and AOI‑level structural organization to capture both rapid attention shifts and semantic grouping of gaze points.
- The network gating mechanism adaptively blends these complementary representations based on their contribution to behavior classification.
- Class‑distribution‑aware learning mitigates the imbalance between ASD and typically developing participants, enabling robust embedding for skewed data.

## Context
Eye‑movement analysis is a growing non‑invasive tool for mental health diagnostics, yet most models treat gaze as isolated sequences. This work bridges that gap by respecting the natural AOI structure of visual attention and integrating it with temporal modeling, offering a more biologically informed representation.

## Implications
The framework can be deployed in real‑world screening tools, reducing reliance on invasive measures while maintaining high accuracy. Practitioners may adopt AOI‑guided models to personalize ASD assessments and scale AI support for clinicians across diverse settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29289v1)
