---
title: Dual-Domain Cross-Modal Decoding for Clinical Text-Guided Medical Image Segmentation
published: 2026-08-11T18:40:52Z
authors: Md Maklachur Rahman, Tracy Hammond
url: http://arxiv.org/abs/2608.11335v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dual-Domain Cross-Modal Decoding for Clinical Text-Guided Medical Image Segmentation

## Abstract
Clinical text can narrow down what to segment, but recent text-guided designs emphasize spatial alignment while overlooking frequency content that governs texture and boundaries. We propose Dual-Domain Cross-Modal Decoding (DD-CMD) for clinical text-guided pulmonary infection segmentation, integrating two complementary forms of language guidance during decoding. In the spatial domain, Text-Guided Spatial Cross-Attention (TGSA) aligns multi-scale visual tokens with text semantics and updates features through gated residual fusion. In the frequency domain, Spectral-Text Adaptive Modulation (STAM) applies a 2D DCT to compute learnable band-energy statistics and predicts text-conditioned FiLM parameters to recalibrate decoder channels for frequency-aware decoding. DD-CMD embeds TGSA and STAM into a coarse-to-fine decoder (7x7 to 56x56) and restores full-resolution masks using a lightweight two-stage refinement module. Experiments on QaTa-COV19 and MosMedData+ show that DD-CMD achieves 91.46% Dice / 84.26% mIoU and 81.95% Dice / 69.42% mIoU, respectively, with average gains of +1.96 Dice and +2.67 mIoU over the strongest prior baselines. Code: https://github.com/maklachur/DD-CMD.

## Metadata
- **Published**: 2026-08-11T18:40:52Z
- **Authors**: Md Maklachur Rahman, Tracy Hammond
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11335v1)