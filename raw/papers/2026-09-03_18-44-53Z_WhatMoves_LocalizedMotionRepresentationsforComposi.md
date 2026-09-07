---
title: What Moves? Localized Motion Representations for Compositional Scene Control
published: 2026-09-03T18:44:53Z
authors: Frank Fundel, Malek Ben Alaya, Thomas Ressler-Antal, Stefan Andreas Baumann, Björn Ommer
url: http://arxiv.org/abs/2609.04383v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Moves? Localized Motion Representations for Compositional Scene Control

## Abstract
Real-world dynamics are inherently compositional: multiple entities move simultaneously within a shared scene, each exhibiting distinct motion patterns. Yet most existing video representations encode motion globally, without explicitly capturing localized motion for individual entities. Crucially, motion is defined relative to a global reference frame, including camera motion and scene layout. However, localized embeddings are often computed from cropped images or obtained by masking features after encoding, discarding the context needed to interpret motion. To address this, we introduce a promptable localized motion representation that produces persistent embeddings for user-specified regions defined by spatial masks. Rather than cropping the input or masking features, our model processes the full video and conditions motion encoding directly on the queried region. This yields temporally consistent, region-addressable embeddings that isolate local dynamics while retaining the global context required for disambiguation. We demonstrate object-level motion transfer, enabling controlled composition of dynamic scenes. Beyond generative control, our embeddings support localized action classification in multi-actor videos. Across both tasks, our approach improves controllability and outperforms global representations localized through cropping or post-hoc masking. Project Page: https://compvis.github.io/WhatMoves

## Metadata
- **Published**: 2026-09-03T18:44:53Z
- **Authors**: Frank Fundel, Malek Ben Alaya, Thomas Ressler-Antal, Stefan Andreas Baumann, Björn Ommer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04383v1)