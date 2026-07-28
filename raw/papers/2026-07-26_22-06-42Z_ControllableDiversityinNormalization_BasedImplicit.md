---
title: Controllable Diversity in Normalization-Based Implicit Ensembles via Softmax-Temperature Modulation
published: 2026-07-26T22:06:42Z
authors: Mihai Suteu, Ovidiu Serban
url: http://arxiv.org/abs/2607.23860v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Controllable Diversity in Normalization-Based Implicit Ensembles via Softmax-Temperature Modulation

## Abstract
Deep ensembles provide the most reliable uncertainty estimates in deep learning, but their cost grows linearly with the number of members. Implicit ensembles lower this cost by sharing a single backbone across members. Member diversity is a primary determinant of ensemble quality, yet no implicit ensemble can shape it during training; existing methods fix it at initialisation or build it into the architecture. We introduce $σ$N-Ens, a normalisation-based implicit ensemble that treats each member as a task in a multi-task architecture and modulates the shared backbone through sigmoid-bounded scalers. We also introduce a softmax-temperature regulariser, which shapes the equilibrium level of sharing between members and traces the accuracy-calibration frontier. Because only normalisation layers are replicated, the mechanism can wrap convolutional and transformer backbones alike, also allowing pretrained models to be adapted through a short fine-tune. We frame the epistemic uncertainty such an ensemble expresses as modulation uncertainty, and explain why its calibration holds under input corruption, and why its out-of-distribution detection is weaker. Our method is evaluated across ResNets and transformers on CIFAR-10/100, ImageNet and SST-2. $σ$N-Ens matches or outperforms deep ensembles at a fraction of their parameter cost, scales with ensemble size where partitioning methods collapse, and maintains calibration under distribution shift.

## Metadata
- **Published**: 2026-07-26T22:06:42Z
- **Authors**: Mihai Suteu, Ovidiu Serban
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23860v1)