---
title: Multimodal Semantic-Probabilistic Objectness for Open World Object Detection
published: 2026-07-27T04:12:04Z
authors: Weijun Tian, Rui Liu
url: http://arxiv.org/abs/2607.23981v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multimodal Semantic-Probabilistic Objectness for Open World Object Detection

## Abstract
Open-world object detection (OWOD) requires a detector to recognize known categories, discover unnamed objects from unseen categories, and incrementally learn newly annotated classes. PROB improves unknown discovery by modeling class-agnostic probabilistic objectness in the decoder-query space. However, visual objectness alone cannot determine whether an object-like query corresponds to a hard known instance, an unseen-category object, or background clutter, resulting in an ambiguous known-unknown decision boundary. We propose MSPO, a lightweight semantic calibration framework that augments PROB with task-aware known-category language priors while preserving its detector architecture and incremental learning protocol. For each currently known category, MSPO constructs an extended text description covering category attributes, visual appearance, typical scenes, and functional usage, and encodes it using a frozen CLIP text encoder. Decoder query features are projected into the same semantic space to estimate their support from the current known-category semantics. This semantic evidence is fused with PROB's visual objectness to calibrate known and unknown predictions without turning OWOD into open-vocabulary classification. Importantly, MSPO never uses future-category names, and all unseen categories remain unnamed during evaluation. Experiments on M-OWODB and S-OWODB show that MSPO improves the strong PROB baseline on the main aggregate metrics while retaining competitive unknown recall. It also improves early unknown-confusion metrics and raises PASCAL VOC final mAP by up to 2.7 points. These results demonstrate that known-category language semantics provide an effective calibration signal for probabilistic objectness under the standard OWOD setting.

## Metadata
- **Published**: 2026-07-27T04:12:04Z
- **Authors**: Weijun Tian, Rui Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23981v1)