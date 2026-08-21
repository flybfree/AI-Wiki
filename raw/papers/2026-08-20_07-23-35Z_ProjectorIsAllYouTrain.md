---
title: Projector Is All You Train
published: 2026-08-20T07:23:35Z
authors: Nyx Iskandar, Saathvik Selvan, Slater Victoroff
url: http://arxiv.org/abs/2608.19726v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Projector Is All You Train

## Abstract
The typical training process of a multimodal large language model (MLLM) involves adapting both the language model backbone and the projector between the backbone and a modality-specific encoder. We ask whether fine-tuning the backbone of an MLLM is necessary to adapt it to a new modality. Through experiments on 3D MLLMs, we find that training only the projector is sufficient to achieve strong multimodal performance relative to existing baseline models and our jointly trained MLLMs with the same encoder and backbone. We also show that joint training leads to undesirable drift in existing capabilities of the language model, which projector-only training avoids by definition. Furthermore, projector-only training has approximately twice the training sample throughput of joint training. We validate our findings across different language model backbones via 3D classification and captioning benchmarks as well as standard benchmarks evaluating language, vision, and spatial reasoning capabilities.

## Metadata
- **Published**: 2026-08-20T07:23:35Z
- **Authors**: Nyx Iskandar, Saathvik Selvan, Slater Victoroff
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19726v1)