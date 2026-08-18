---
title: CETalk: Continuous Valence-Arousal Control for Audio-Driven 3D Talking Head Generation
published: 2026-08-15T08:22:50Z
authors: Peng Jia, Li Dai, Zhen Xiao, Xueliang Liu, Jia Li
url: http://arxiv.org/abs/2608.15110v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CETalk: Continuous Valence-Arousal Control for Audio-Driven 3D Talking Head Generation

## Abstract
Emotional 3D talking head generation aims to synthesize expressive facial animations with accurate lip synchronization. However, existing methods often rely on discrete emotion categories, which fail to capture the continuous evolution of affect. They also overlook the temporal frequency mismatch between audio articulation and emotional expression. In this paper, we propose CETalk, an audio-driven 3D facial animation framework conditioned on continuous Valence--Arousal (VA) representations for fine-grained emotion control. CETalk predicts a sequence of FLAME parameters through three key components: a Dynamic Emotion Modulation Module that adaptively scales emotional intensity using audio-derived cues; a Multi-Scale Temporal Modeling mechanism that employs parallel branches to decouple high-frequency articulatory movements from low-frequency emotional dynamics; and a Dynamic Fusion Mechanism that integrates these multi-scale features via an adaptive gating network. To support training and evaluation, we construct 3D-VA-MEAD, a large-scale dataset with automatically estimated VA annotations and reconstructed 3D facial motions. Extensive experiments demonstrate that CETalk outperforms state-of-the-art methods in both lip-sync accuracy and emotional expressiveness, while enabling smooth and controllable emotion transitions.

## Metadata
- **Published**: 2026-08-15T08:22:50Z
- **Authors**: Peng Jia, Li Dai, Zhen Xiao, Xueliang Liu, Jia Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15110v1)