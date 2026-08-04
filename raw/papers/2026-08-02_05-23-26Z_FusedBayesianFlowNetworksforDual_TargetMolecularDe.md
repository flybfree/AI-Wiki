---
title: Fused Bayesian Flow Networks for Dual-Target Molecular Design
published: 2026-08-02T05:23:26Z
authors: Jingyuan Zhou, Shikui Tu, Lei Xu
url: http://arxiv.org/abs/2608.01007v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fused Bayesian Flow Networks for Dual-Target Molecular Design

## Abstract
Dual-target drug design aims to generate 3D molecules that can simultaneously interact with two target proteins, offering a promising route for discovering polypharmacological compounds against complex diseases. While recent generative models have shown encouraging performance in single-target drug design, existing dual-target approaches either focus on sequence generation or introduce an additional predictive drift term into the diffusion-based generative trajectory, which limits their ability to fully integrate feature information from both targets. We propose FusedBFN, a fused Bayesian flow network (BFN) for dual-target molecular design. FusedBFN formulates dual-target generation as distribution fusion in a unified continuous parameter space and employs a product-of-experts formulation to incorporate dual-target information throughout the generative process. To address the scarcity of dual-target structural data, we leverage a pretrained target-aware BFN model as the shared backbone. We further introduce a chemically aware prior-based alignment method and a prior-free pocket alignment strategy to construct aligned dual-target contexts. Extensive experiments demonstrate that FusedBFN generates molecules with strong binding affinity toward dual targets while maintaining favorable molecular properties.

## Metadata
- **Published**: 2026-08-02T05:23:26Z
- **Authors**: Jingyuan Zhou, Shikui Tu, Lei Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01007v1)