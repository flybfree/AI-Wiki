---
title: Background-Free Objectness Learning for Class-Agnostic Detection
published: 2026-08-29T12:39:23Z
authors: Dania Batool, Liliana Lo Presti, Marco La Cascia, Filippo Vella
url: http://arxiv.org/abs/2608.29232v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Background-Free Objectness Learning for Class-Agnostic Detection

## Abstract
Object detectors are typically trained under closed-set supervision, where unlabeled regions are implicitly treated as background. Under incomplete annotations, this assumption introduces objectness bias: visually valid but unlabeled objects are used as negatives, tying objectness to the annotated taxonomy rather than generic object structure. This limitation is particularly problematic for class-agnostic and open-world detection. This paper proposes Background-Free Objectness Learning (B-FOR), a dense class-agnostic detection framework that learns objectness without explicit background supervision on unlabeled regions. B-FOR formulates detection as the prediction of dense multi-scale object-center and scale fields, from which object hypotheses emerge as local spatial structures. Supervision is confined to reliable annotated regions through spatially structured soft targets, avoiding foreground-background discrimination. To support decoding from emergent local maxima, the paper further introduces displacement-aware scale fields that model object extent as a spatially varying property of the learned objectness field. Experiments on PASCAL VOC, MS-COCO, and Open Images demonstrate strong generalization to unseen categories and cross-dataset object distributions. B-FOR improves recall by more than +10 AR points over prior class-agnostic baselines. Ablation studies show that both localized objectness supervision and displacement-aware scale fields are critical for class-agnostic localization under incomplete annotations. Code available at: https://github.com/Daniaawan/B-FOR.

## Metadata
- **Published**: 2026-08-29T12:39:23Z
- **Authors**: Dania Batool, Liliana Lo Presti, Marco La Cascia, Filippo Vella
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29232v1)