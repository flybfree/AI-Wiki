---
title: What Moves? Localized Motion Representations for Compositional Scene Control
url: http://arxiv.org/abs/2609.04383v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-03_18-44-53Z_WhatMoves_LocalizedMotionRepresentationsforComposi.md
generated_at: 2026-09-06 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a promptable localized motion representation that creates persistent embeddings for user‑defined spatial regions within videos, enabling precise control of individual object dynamics while preserving global context. By processing the full video and conditioning encoding on queried masks instead of cropping or masking features, the method produces temporally consistent, region‑addressable vectors. Experiments show improved scene composition and action classification compared with traditional global embeddings.

## Key Takeaways
- The model generates persistent motion embeddings for any spatial mask without altering input data, preserving context needed to interpret local dynamics.
- Motion is encoded relative to a global reference frame, allowing disambiguation between different entities moving in the same scene.
- The approach enables object‑level motion transfer and localized action classification, demonstrating superior controllability over cropping or post‑hoc masking methods.

## Context
Current video representation systems treat motion as a single global signal, which limits their ability to isolate individual agents. This limitation hampers applications requiring precise control of complex scenes where multiple moving objects interact. The proposed method addresses this by providing region‑specific embeddings that retain the broader scene context.

## Implications
For interactive entertainment and robotics, localized motion representations could allow users to direct specific characters or objects with fine‑grained commands. Practitioners can integrate these embeddings into generative control pipelines, enhancing realism and reducing computational cost compared with full‑scene modeling.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04383v1)
