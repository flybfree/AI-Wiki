---
title: SDO: Subspace Deconflicting Operator for Multi-Adapter Composition
published: 2026-08-13T23:13:39Z
authors: Zhongsheng Wang, Zhedong Lin, Qian Liu, Xinyu Zhang, Jiamou Liu
url: http://arxiv.org/abs/2608.13820v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SDO: Subspace Deconflicting Operator for Multi-Adapter Composition

## Abstract
Composing independently trained adapters within a shared diffusion backbone provides a modular approach to multi-character generation, but naive joint deployment often causes identity mixing, cross-character attribute leakage, and unstable scene composition. We study this interference from a parameter-space perspective and hypothesize that it arises partly from conflicts between overlapping dominant subspaces in shared layers. To address this issue, we propose \textbf{SDO}, a \textbf{S}ubspace \textbf{D}econflicting \textbf{O}perator for multi-adapter composition. SDO reconstructs layer-wise low-rank updates from the selected adapters, extracts compact subspace signatures, measures pairwise conflict through output-subspace overlap, and applies a permutation-equivariant transformation that suppresses harmful shared directions while retaining identity-specific characteristics. The resulting representations are mapped back to standard adapter updates and can be directly incorporated into existing diffusion inference pipelines. Experiments demonstrate that SDO consistently improves identity fidelity and compositional stability, with particularly clear gains as the number of jointly composed adapters increases.

## Metadata
- **Published**: 2026-08-13T23:13:39Z
- **Authors**: Zhongsheng Wang, Zhedong Lin, Qian Liu, Xinyu Zhang, Jiamou Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13820v1)