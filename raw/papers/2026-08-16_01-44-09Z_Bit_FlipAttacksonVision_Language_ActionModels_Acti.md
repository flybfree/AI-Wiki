---
title: Bit-Flip Attacks on Vision-Language-Action Models: Action-Decoding Architecture Shapes the Vulnerability
published: 2026-08-16T01:44:09Z
authors: Yudong Gao, Linghan Chen, Wenhan Wu, Mia Zhou, Jiyao Wang, Kaiyan Ji, Mingyu Guo, Honglong Chen
url: http://arxiv.org/abs/2608.15475v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bit-Flip Attacks on Vision-Language-Action Models: Action-Decoding Architecture Shapes the Vulnerability

## Abstract
Quantized Vision-Language-Action (VLA) models expose a weight-fault surface: Rowhammer-style faults can corrupt deployed INT8 bits. We present the first bit-flip attack on a VLA: a few gradient-selected flips reduce closed-loop success to $0\%$, while hundreds of random flips are harmless. Across four model variants spanning three action-head families, damaging bits concentrate in a few action-generating layers, but the empirical budget depends sharply on the head: direct regression and token policies fall in $1$--$5$ flips, whereas the evaluated flow-matching policies require ${\sim}100$--$300$. Our fixed-direction manifold-escape loss cuts \pizero{}'s budget from ${\sim}1000$ to ${\sim}100$ flips, and a matched five-direction sweep shows that the attack is not specific to an all-positive direction. On a direct head, protecting $3.1\%$ of weights preserves $60\%$ success at $K{=}100$, and protecting $5.3\%$ moves the open-loop break threshold from 3 to 100 flips. Finally, task-calibrated emulated $K{=}100$ flips yield $0/20$ real-robot successes, versus $14/20$ clean and $16/20$ global-random. Weight integrity is therefore a security boundary for embodied foundation models. Code is included as ancillary material.

## Metadata
- **Published**: 2026-08-16T01:44:09Z
- **Authors**: Yudong Gao, Linghan Chen, Wenhan Wu, Mia Zhou, Jiyao Wang, Kaiyan Ji, Mingyu Guo, Honglong Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15475v1)