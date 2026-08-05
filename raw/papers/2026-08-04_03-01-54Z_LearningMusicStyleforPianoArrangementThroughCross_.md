---
title: Learning Music Style for Piano Arrangement Through Cross-Modal Bootstrapping
published: 2026-08-04T03:01:54Z
authors: Jingwei Zhao, Gus Xia, Ziyu Wang, Ye Wang
url: http://arxiv.org/abs/2608.03050v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Music Style for Piano Arrangement Through Cross-Modal Bootstrapping

## Abstract
What is music style? Though often described using text labels such as "swing," "classical," or "emotional," the real style remains implicit and hidden in concrete music examples. In this paper, we introduce a cross-modal framework that learns implicit music styles from raw audio and applies them to symbolic music generation. Inspired by BLIP-2, our model leverages a Querying Transformer (Q-Former) to extract style representations from a large, pre-trained audio language model (LM), and further applies them to condition a symbolic LM for generating piano arrangements. We adopt a two-stage training strategy: contrastive learning to align auditory style with symbolic expression, followed by generative modeling for music arrangement. Our model generates piano performances jointly conditioned on a lead sheet (content) and a reference audio example (style), enabling controllable and stylistically faithful arrangement. Experiments demonstrate the effectiveness of our approach in piano cover generation, style transfer, and audio-to-MIDI retrieval, achieving substantial improvements in style-aware alignment and music quality.

## Metadata
- **Published**: 2026-08-04T03:01:54Z
- **Authors**: Jingwei Zhao, Gus Xia, Ziyu Wang, Ye Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03050v1)