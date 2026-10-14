---
title: Full-duplex Spoken Language Modeling with Discrete Diffusion
published: 2026-10-13T06:05:54Z
authors: Chen Chen, Pin-Jui Ku, Ankita Pasad, Ante Jukić, Zhehuai Chen, Boris Ginsburg
url: http://arxiv.org/abs/2610.17780v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Full-duplex Spoken Language Modeling with Discrete Diffusion

## Abstract
We introduce Diffuplex, a full-duplex spoken language model based on discrete diffusion that achieves an unprecedented balance between linguistic intelligence and response efficiency. With thinking mode, Diffuplex delivers 13.0 tokens per forward pass, reaching an average of 1872 tokens per second and substantially surpassing the frontier autoregressive (AR) models in decoding speed. Without thinking, Diffuplex matches the first-audio latency of existing full-duplex models while achieving markedly stronger linguistic intelligence. This capability is enabled by separating when to say from what to say at the training level, rather than compressing both into a single autoregressive timeline. During inference, Diffuplex continuously tracks the user speech through an AR interaction policy, while independently generating and refining response content through parallel diffusion. Consequently, semantic computation is no longer bounded by the perception audio frame rate, allowing intelligence and responsiveness to improve simultaneously. Taken together, these results establish a new paradigm for spoken agents that can sustain real-time dialogue while devoting parallel computation to intelligent response generation. Training code and checkpoints will be avaliable soon.

## Metadata
- **Published**: 2026-10-13T06:05:54Z
- **Authors**: Chen Chen, Pin-Jui Ku, Ankita Pasad, Ante Jukić, Zhehuai Chen, Boris Ginsburg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17780v1)