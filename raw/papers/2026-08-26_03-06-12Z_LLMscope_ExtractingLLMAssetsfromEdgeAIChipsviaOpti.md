---
title: LLMscope: Extracting LLM Assets from Edge AI Chips via Optical Probing
published: 2026-08-26T03:06:12Z
authors: Dev Mehta, Lily Dukette, William Folan, Olivia Kochol, Noah Solomon, Shahin Tajik, Fatemeh Ganji
url: http://arxiv.org/abs/2608.25321v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLMscope: Extracting LLM Assets from Edge AI Chips via Optical Probing

## Abstract
The move of LLM inference to edge AI accelerators introduces new physical vulnerabilities. During execution, model parameters and intermediate inference states are repeatedly loaded into and processed on the chip, making them suscep- tible to physical side-channel attacks. In this work, by deploying laser voltage imaging, we show that one can extract LLM assets during inference, namely embeddings, attention, and quantized MLP weights, activations, and other inference states, from localized memories and compute subcircuits. To validate our claims, we perform an attack on an FPGA-based LLM accelerator. Since such accelerators reuse the same buffers and compute subcircuits across addresses, tiles, modules, and layers, reading asset values comes down to probing different memories during inference. We demonstrate full recovery of the targeted values; however, we also establish a methodology to recover asset values even if some weights or bits remain unread. We further derive lower bounds that relate imaging effort to asset dimensions and show that even direct recovery scales linearly with the size of the targeted asset

## Metadata
- **Published**: 2026-08-26T03:06:12Z
- **Authors**: Dev Mehta, Lily Dukette, William Folan, Olivia Kochol, Noah Solomon, Shahin Tajik, Fatemeh Ganji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25321v1)