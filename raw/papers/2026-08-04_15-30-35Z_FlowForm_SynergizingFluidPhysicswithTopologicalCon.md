---
title: FlowForm: Synergizing Fluid Physics with Topological Consistency for Satellite Flood Synthesis
published: 2026-08-04T15:30:35Z
authors: Zhang Weihui, Wang Ruizhi, Xu Hongye, Wang Huiqiong, Sun Li, Song Mingli
url: http://arxiv.org/abs/2608.03822v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FlowForm: Synergizing Fluid Physics with Topological Consistency for Satellite Flood Synthesis

## Abstract
Developing robust flood assessment models requires high-quality paired satellite imagery, yet such data remain scarce for flood-specific image generation. Although generative models provide a promising means of data augmentation, existing methods often yield implausible spatial layouts of flooded regions and distort scene structures. We propose FlowForm, a framework for satellite flood synthesis that integrates SWE-inspired latent regularization with structure-aware conditioning. The Flood Descriptor Module (FDM) imposes differentiable penalties on residuals of the steady-state Shallow Water Equation in auxiliary latent fields at the diffusion bottleneck. The Terrain Anchor Adapter (TAA) injects depth, semantic, and edge features at four encoder scales of the U-Net. We further curate FloodScape, a large-scale, high-resolution dataset comprising paired satellite images acquired before and after disasters. In addition to standard image-generation metrics, we evaluate the consistency of flooded regions, zero-shot generalization to a geographically held-out flood event, and sensitivity to individual components. Across all reported comparisons, FlowForm achieves higher visual fidelity, greater similarity between paired images, and stronger consistency of flooded regions.

## Metadata
- **Published**: 2026-08-04T15:30:35Z
- **Authors**: Zhang Weihui, Wang Ruizhi, Xu Hongye, Wang Huiqiong, Sun Li, Song Mingli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03822v1)