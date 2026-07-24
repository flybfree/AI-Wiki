---
title: Efficient and Interpretable Body-Based Emotion Recognition with Lightweight Temporal Convolutional Networks
published: 2026-07-23T01:12:39Z
authors: Christian Arzate Cruz, Stefanos Gkikas, Houshyar Asadi
url: http://arxiv.org/abs/2607.20820v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient and Interpretable Body-Based Emotion Recognition with Lightweight Temporal Convolutional Networks

## Abstract
Body-based emotion recognition is important for real-time affective systems, but graph-based skeleton models can be computationally expensive. This paper studies whether lightweight temporal convolutional networks (TCNs) can provide an efficient and interpretable alternative for body-based emotion classification. We evaluate a family of TCN models on DIEM-A and compare them with a graph-based time-series graph (G-TSG) baseline using accuracy, macro-F1, parameter count, and inference latency. Although G-TSG achieves the highest mean performance, TCN-Base remains within $1.58$ accuracy points and $1.25$ macro-F1 points while using $79.18\%$ fewer parameters and reducing classifier latency by approximately $12.5\times$. We also analyze body-region contributions using region-specific TCN models, zero-based occlusion, and G-TSG gradient saliency. The results show that upper-body motion provides the strongest standalone regional cue, that the usefulness of body regions varies across emotions, and that different interpretability methods capture distinct aspects of model behavior. These findings suggest that lightweight TCNs can support efficient body-based emotion recognition while also providing practical insight into how motion cues contribute to classification.

## Metadata
- **Published**: 2026-07-23T01:12:39Z
- **Authors**: Christian Arzate Cruz, Stefanos Gkikas, Houshyar Asadi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20820v1)