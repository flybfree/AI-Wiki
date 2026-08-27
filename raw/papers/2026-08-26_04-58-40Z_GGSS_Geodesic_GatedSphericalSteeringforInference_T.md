---
title: GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative Vision-Language Models
published: 2026-08-26T04:58:40Z
authors: Yiqun Sun, Junyu Chen, Pengfei Wei, Lawrence B. Hsieh
url: http://arxiv.org/abs/2608.25375v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative Vision-Language Models

## Abstract
Generative vision-language models (VLMs) are increasingly used in human-centered settings, yet they can produce demographically biased outputs even when images differ only in controlled attributes such as perceived race or gender. However, existing inference-time debiasers were largely designed for static embeddings or CLIP-like models rather than generative VLMs. We propose GGSS---Geodesic-Gated Spherical Steering---a norm-preserving intervention that discovers a counterfactual bias subspace on the unit hypersphere, steers visual tokens along geodesic arcs, and uses an adaptive gate to focus correction on tokens that carry stronger demographic signal. We evaluate four generative VLMs against ten adapted inference-time debiasing baselines and prompt-based mitigation under a single operating-point protocol across categorical, pairwise, and occupation-gender bias tests, while also measuring general visual-language capability. GGSS achieves the lowest average bias on all four models, significant on three of four backbones under paired permutation tests, while preserving MMStar accuracy within +/- 0.6 p.p. of the unsteered baseline. Code is available at https://github.com/dukesun99/GGSS.

## Metadata
- **Published**: 2026-08-26T04:58:40Z
- **Authors**: Yiqun Sun, Junyu Chen, Pengfei Wei, Lawrence B. Hsieh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25375v1)