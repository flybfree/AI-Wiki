---
title: Rethinking the Generation Order of Block Diffusion Language Models
published: 2026-07-27T11:49:50Z
authors: Kai Syun Hou, James Kwok
url: http://arxiv.org/abs/2607.24306v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking the Generation Order of Block Diffusion Language Models

## Abstract
Diffusion language models enable flexible arbitrary-order generation, but existing sampling methods are mostly designed for early masked diffusion models (MDMs). In this work, we study sampling for recent block diffusion language models (BDLMs). We show empirically and analytically that these models are naturally more aligned with left-to-right decoding than MDMs. Based on this observation, we propose Parallel Autoregressive Decoding (PARD), a simple training-free sampling method that preserves left-to-right unmasking structure while allowing parallel token commitment. Extensive experiments show that PARD consistently outperforms existing parallel samplers in generation quality, while achieving substantial speedups over pure AR decoding with only a small quality gap.

## Metadata
- **Published**: 2026-07-27T11:49:50Z
- **Authors**: Kai Syun Hou, James Kwok
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24306v1)