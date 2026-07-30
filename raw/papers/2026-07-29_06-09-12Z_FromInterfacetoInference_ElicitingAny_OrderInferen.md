---
title: From Interface to Inference: Eliciting Any-Order Inference from Any-Order Models
published: 2026-07-29T06:09:12Z
authors: Seunggeun Kim, Jaeyeon Kim, Taekyun Lee, Yuyuan Chen, Yilun Du, Sham Kakade, Sitan Chen
url: http://arxiv.org/abs/2607.26504v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Interface to Inference: Eliciting Any-Order Inference from Any-Order Models

## Abstract
Many discrete reasoning tasks, such as code generation, are inherently non-causal: programmers move between high-level structure and local details, a process we call any-order inference. For autoregressive language models, which lack a native any-order interface, non-causal abilities such as infilling and next-edit prediction require hand-designed mechanisms. Can we instead design models that natively support any-order inference? Masked diffusion models have recently emerged as compelling candidates, as their any-order training objective naturally offers an any-order prediction interface. This interface, however, does not automatically yield any-order inference. We demonstrate that this interface-inference gap stems from positional uncertainty: fixed-canvas, token-level models may know what semantic component should appear without knowing where to place it. In light of this, we propose two complementary approaches: (1) Insertion-based masked diffusion, building on FlexMDM (Kim et al, 2025), relaxes fixed-position commitments via insertions, enabling generation across non-contiguous regions. (2) Latent-space masked diffusion shifts prediction to coarser semantic segments, enabling search over latent generation orders. Empirically, we train a 7B FlexMDM for Python coding and a 125M LatentMDM for GSM8K and show that both approaches induce distinct any-order inference behaviors and improve downstream performance. We release our codebase at https://github.com/SeunggeunKimkr/genuine-any-order.

## Metadata
- **Published**: 2026-07-29T06:09:12Z
- **Authors**: Seunggeun Kim, Jaeyeon Kim, Taekyun Lee, Yuyuan Chen, Yilun Du, Sham Kakade, Sitan Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26504v1)