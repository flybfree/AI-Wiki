---
title: The Weight Is Over - Interactive Diffusion on Consumer GPUs
published: 2026-09-18T14:42:55Z
authors: Frieder Ganz, Maximilian Müller
url: http://arxiv.org/abs/2609.21849v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Weight Is Over - Interactive Diffusion on Consumer GPUs

## Abstract
On-device inference is booming, but the momentum is almost all in language models. Diffusion pipelines are memory hungry, latency-sensitive, and require orchestrating an embedder, a transformer, a decoder, and often further postprocessing that is not as standardized as LLM inference loops are. We navigate the trade-off between performance, quality, and model footprint to reach as many client devices in the wild as possible. We make three contributions: an embedding translator that maps a small text encoder into a large encoder space to cut weight and latency; a reproducible sweep recipe for navigating the speed/quality/memory triangle in diffusion pipelines; and an interactive on-device image generation editor achieving sub-second TTFI on recent GPUs.

## Metadata
- **Published**: 2026-09-18T14:42:55Z
- **Authors**: Frieder Ganz, Maximilian Müller
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21849v1)