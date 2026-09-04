---
title: EPIC: Explicit Posterior Item Conditioning for Semantic ID Diffusion Recommendation
published: 2026-09-03T08:21:50Z
authors: Tuan-Binh Tran, Thanh Tam Nguyen, Quoc Viet Hung Nguyen, Dung D. Le, Tung Kieu, Thanh Trung Huynh
url: http://arxiv.org/abs/2609.03522v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EPIC: Explicit Posterior Item Conditioning for Semantic ID Diffusion Recommendation

## Abstract
Semantic ID (SID) generative recommendation predicts the next item by generating a short tuple of discrete tokens. Recent masked-diffusion methods improve this process through bidirectional context and flexible decoding, yet recommendation ultimately requires selecting among complete catalog items. At each denoising step, a partial SID can correspond to multiple feasible items, while existing methods primarily reason through position-wise token predictions. We propose Explicit Posterior Item Conditioning (EPIC), which introduces explicit item-level competition into SID denoising. EPIC constructs a personalized posterior over feasible candidate items using the current generation context and the user's recent interactions, then projects this distribution back to unresolved SID positions to guide subsequent token decisions. The pretrained backbone remains frozen and requires no additional decoder forward pass. Experiments on four Amazon benchmarks show consistent improvements over strong baselines, while diagnostic analyses indicate that the gains primarily arise from personalized transition evidence that preserves promising item hypotheses during denoising.

## Metadata
- **Published**: 2026-09-03T08:21:50Z
- **Authors**: Tuan-Binh Tran, Thanh Tam Nguyen, Quoc Viet Hung Nguyen, Dung D. Le, Tung Kieu, Thanh Trung Huynh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03522v1)