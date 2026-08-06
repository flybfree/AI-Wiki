---
title: NeuroPB: Scaling Neural Decoding with Pretrained Behavioral Representations
published: 2026-08-05T02:45:14Z
authors: Luyao Jin, Yonghao Song, Huan Zhao, Vincent C. K. Cheung, Wei-Hsin Liao
url: http://arxiv.org/abs/2608.04389v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NeuroPB: Scaling Neural Decoding with Pretrained Behavioral Representations

## Abstract
Decoding continuous motor trajectories from neural activity is essential for developing practical brain-computer interfaces (BCIs). However, current neural decoders are constrained by the limited scale and heterogeneity of neural recordings. In contrast, behavioral data can be collected more readily and at substantially larger scale from humans, animals, simulations, and robotic systems. Here, we introduce NeuroPB, a framework that scales neural decoding by transferring knowledge from pretrained behavioral representations. NeuroPB first pretrains a motor encoder on large-scale motor behavior data and then aligns neural activity with the resulting behavioral representation space using a limited set of paired neural-behavioral recordings. A neural encoder and lightweight motor decoder are subsequently optimized to reconstruct continuous movement from the aligned neural representations. Across multiple macaque motor datasets, behavioral pretraining improves trajectory decoding, including an 11% $R^2$ increase on center-out and 8% on random-target compared with training the motor encoder from scratch. Notably, pretraining on robotic trajectories achieves performance comparable to pretraining on macaque trajectories, demonstrating that transferable kinematic structure is shared across biological and artificial models. Moreover, decoding performance improves as the scale and diversity of robotic pretraining data increase, when the amount of neural data is fixed. Pretraining also enhances generalization across recording sessions, subjects, and motor tasks, with only 10% calibration needed to match training from scratch. Overall, these results establish behavioral pretraining as a scalable source for neural decoding and provide a promising route toward high-performance and calibration-efficient BCIs under limited neural data.

## Metadata
- **Published**: 2026-08-05T02:45:14Z
- **Authors**: Luyao Jin, Yonghao Song, Huan Zhao, Vincent C. K. Cheung, Wei-Hsin Liao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04389v1)