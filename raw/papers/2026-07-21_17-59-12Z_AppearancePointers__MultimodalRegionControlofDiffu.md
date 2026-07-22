---
title: Appearance Pointers -- Multimodal Region Control of Diffusion Transformers
published: 2026-07-21T17:59:12Z
authors: Rahul Sajnani, Yulia Gryaditskaya, Radomír Měch, Srinath Sridhar, Matheus Gadelha
url: http://arxiv.org/abs/2607.19344v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Appearance Pointers -- Multimodal Region Control of Diffusion Transformers

## Abstract
Controllable image generation remains challenging for creative professionals, who often require precise regional control over materials, object identities, and spatial arrangements that cannot be reliably achieved through text prompting alone. Diffusion Transformers (DiTs) can natively ingest heterogeneous tokens stemming from texts and images, but they lack mechanisms for determining where and how these tokens should influence the output. We introduce appearance pointers, compact tokens that guide DiTs toward the correct appearance cues at the correct spatial locations by aligning text or image inputs with user-specified masks. Appearance pointers are produced by a region correspondence network and refined through a spatial aggregation mechanism, enabling the model to handle multiple regional descriptions without significantly increasing token load. Our approach introduces the first modality-agnostic interface for localized multimodal control in a DiT without retraining the base model from scratch. Across a range of metrics, our single model reaches or surpasses the performance of modality-specific state of the art methods, offering a simple and extensible path toward precise, region-aware, multimodal guidance in generative image synthesis.

## Metadata
- **Published**: 2026-07-21T17:59:12Z
- **Authors**: Rahul Sajnani, Yulia Gryaditskaya, Radomír Měch, Srinath Sridhar, Matheus Gadelha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19344v1)