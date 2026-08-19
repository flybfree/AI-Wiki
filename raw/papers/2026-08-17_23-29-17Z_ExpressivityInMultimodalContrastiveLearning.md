---
title: Expressivity In Multimodal Contrastive Learning
published: 2026-08-17T23:29:17Z
authors: Andrew Stuart, Florian Wolf
url: http://arxiv.org/abs/2608.17203v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Expressivity In Multimodal Contrastive Learning

## Abstract
Contrastive learning has become a cornerstone of modern representation learning, powering CLIP-style models that underpin text-to-image generation, vision-language models, and retrieval across a rapidly growing range of modalities. Despite this empirical success, the expressive power of these architectures remains poorly understood. To gain insight, we study expressivity by adopting a population-level, density-estimation viewpoint: each architecture comprises a parameterized set of densities whose parameters may be chosen to approximate the joint distribution of the modalities. This isolates a question of pure representational capacity: which joint distributions can a given contrastive family of parameterizations approximate to arbitrary accuracy? We show that expressivity is sharply architecture-dependent. For two modalities, the simple two-tower CLIP architecture is a universal approximator. A natural generalization of CLIP, widely used in practice when three or more modalities are present, is based on a loss found by summing over all pairwise similarities. This provably cannot represent arbitrary joint distributions, although we prove that it remains expressive enough to match all pairwise conditionals. Motivated by this gap, we propose Hadamard-CLIP, which adds a single learned weight vector on top of the existing encoders and restores universal approximation of the joint for any number of modalities while preserving CLIP's fast, precomputable-embedding retrieval.

## Metadata
- **Published**: 2026-08-17T23:29:17Z
- **Authors**: Andrew Stuart, Florian Wolf
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17203v1)