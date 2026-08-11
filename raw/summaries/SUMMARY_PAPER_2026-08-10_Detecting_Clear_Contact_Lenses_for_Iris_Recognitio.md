---
title: Detecting Clear Contact Lenses for Iris Recognition: A Two-Stage Mask-Guided Attention Approach
url: http://arxiv.org/abs/2608.08977v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_00-44-37Z_DetectingClearContactLensesforIrisRecognition_ATwo.md
generated_at: 2026-08-10 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how clear prescription contact lenses affect iris recognition and proposes a two‑stage detection framework to improve verification accuracy. Experiments on four datasets show that clear lenses cause slight score degradation but can be mitigated with calibration. The full pipeline achieves 90–98.8 % accuracy.

## Key Takeaways
- Clear lenses degrade match scores marginally, increasing verification error despite being transparent.
- A two‑stage approach using a PAD model followed by a ConvNeXt‑Base with Mask‑Guided Spatial Attention detects both patterned and clear lenses accurately.
- Z‑score calibration reduces EER by up to 28.3 % when clear lenses are present.

## Context
Iris recognition systems rely on visual cues that can be altered by contact lens wear, yet most research focuses on patterned attacks leaving clear lenses understudied. This work bridges that gap by introducing a specialized detection module for transparent lenses within an existing verification pipeline.

## Implications
Accurate detection of clear lenses will enhance reliability of iris‑based authentication in real‑world deployments such as mobile banking and access control. Practitioners can integrate the proposed calibration to maintain high match scores without sacrificing user experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08977v1)
