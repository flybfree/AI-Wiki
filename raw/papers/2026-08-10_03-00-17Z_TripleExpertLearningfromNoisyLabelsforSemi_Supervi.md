---
title: Triple Expert Learning from Noisy Labels for Semi-Supervised Vision Foundation Model Adaptation
published: 2026-08-10T03:00:17Z
authors: Xuanyu Liu, Zheng Fang, Hongyang He, Yundi Hong, Daizong Liu
url: http://arxiv.org/abs/2608.09052v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Triple Expert Learning from Noisy Labels for Semi-Supervised Vision Foundation Model Adaptation

## Abstract
Semi-supervised adaptation of vision foundation models (VFMs) commonly freezes the pretrained backbone and updates lightweight modules such as LoRA. However, pseudo-labels have mixed reliability, and a single LoRA adapter must absorb reliable, ambiguous, and noisy gradients in the same low-rank space. This can make VFM adaptation sensitive to pseudo-label noise. We propose \textbf{TriNoL}, a \textbf{Tri}ple-expert learning framework from \textbf{No}isy \textbf{L}abels for semi-supervised VFM adaptation. TriNoL routes unlabeled samples into three confidence regions and assigns them to three LoRA experts: a Positive Expert for high-confidence pseudo-labels, an Alignment Expert for medium-confidence ambiguous samples, and a Negative Expert for low-confidence noisy samples. The VFM backbone remains frozen, and only the LoRA experts and classifier head are updated. By separating different pseudo-label reliability regions into specialized adaptation paths, TriNoL improves robustness to noisy supervision while keeping the training cost low.

## Metadata
- **Published**: 2026-08-10T03:00:17Z
- **Authors**: Xuanyu Liu, Zheng Fang, Hongyang He, Yundi Hong, Daizong Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09052v1)