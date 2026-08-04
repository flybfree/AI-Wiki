---
title: DAVET: Denoising-Aware Visual Evidence Trajectory Allocation for Diffusion Vision-Language Models
published: 2026-08-03T07:29:05Z
authors: Yongkang Zhou, Xiang Xia, Cheng Yan, Fan Xu, Wuyang Zhang
url: http://arxiv.org/abs/2608.01821v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DAVET: Denoising-Aware Visual Evidence Trajectory Allocation for Diffusion Vision-Language Models

## Abstract
Diffusion vision-language models (dVLMs) iteratively denoise masked responses while conditioning each denoising step on visual evidence, making visual conditioning a substantial recurring inference cost. Unlike autoregressive decoding, diffusion generation repeatedly revisits the entire response as uncertainty evolves. Our analysis reveals that visual evidence demand is strongly step-dependent, motivating adaptive allocation across denoising steps. Existing inference acceleration methods operate through decoding-side strategies or visual token compression via pruning and merging, but do not explicitly treat visual evidence as a resource whose demand evolves across the diffusion process. Therefore, we present Denoising-Aware Visual Evidence Trajectory Allocation (DAVET), a training-free framework that allocates visual evidence according to the evolving generation state. Starting from a phase-conditioned evidence trajectory, the proposed allocation policy uses operation demand to set an evidence reserve whose allocation at each denoising step is modulated by trajectory risk. DAVET realizes the resulting budgets through a hierarchy of evidence views constructed from a single visual encoding, separating when and how much evidence is needed from how the evidence views are constructed. Evaluated on two representative dVLMs, LLaDA-V and LaViDa, across multiple visual-understanding benchmarks, DAVET achieves an average speedup of 1.55$\times$ with an average relative performance drop of 1.86\%, showing that denoising-aware visual evidence allocation can reduce visual conditioning cost while largely preserving generation quality.

## Metadata
- **Published**: 2026-08-03T07:29:05Z
- **Authors**: Yongkang Zhou, Xiang Xia, Cheng Yan, Fan Xu, Wuyang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01821v1)