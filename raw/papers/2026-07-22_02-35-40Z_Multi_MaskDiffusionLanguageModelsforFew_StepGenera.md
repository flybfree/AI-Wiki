---
title: Multi-Mask Diffusion Language Models for Few-Step Generation
published: 2026-07-22T02:35:40Z
authors: Sijin Chen, Yinuo Ren, Heyang Zhao, Ziheng Cheng, Quanquan Gu, Lexing Ying
url: http://arxiv.org/abs/2607.19686v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Mask Diffusion Language Models for Few-Step Generation

## Abstract
Masked diffusion models (MDMs) are a promising family of language generators, but achieving high-quality few-step generation remains challenging. In MDMs, all forward trajectories collapse to a single fully masked state, leaving no terminal entropy for consistency-style few-step generation. While recent few-step alternatives based on uniform-state diffusion avoid this degeneracy, it becomes harder to distinguish clean tokens from noise than MDMs, which usually harms modeling quality and training efficiency. In this work, we propose a multi-mask diffusion model (MultiMDM) that preserves the masking structure towards few-step generation. In the forward process, each clean token is first pushed towards a designated mask and then gradually mixes over the mask set. As a result, the backward process has a drafting capability by predicting a designated mask before refining to a clean token. We derive a closed-form ELBO training objective for MultiMDM that supports continual training from pretrained MDMs. In addition, we formulate a purely discrete-state consistency distillation scheme, with a shared-Gumbel coupling to reduce pathwise entropy. Experiments on pretraining and distillation show that MultiMDM provides an effective foundation for principled few-step generation.

## Metadata
- **Published**: 2026-07-22T02:35:40Z
- **Authors**: Sijin Chen, Yinuo Ren, Heyang Zhao, Ziheng Cheng, Quanquan Gu, Lexing Ying
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19686v1)