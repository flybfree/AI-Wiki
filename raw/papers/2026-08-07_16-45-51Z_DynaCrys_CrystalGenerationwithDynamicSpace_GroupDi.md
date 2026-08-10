---
title: DynaCrys: Crystal Generation with Dynamic Space-Group Diffusion
published: 2026-08-07T16:45:51Z
authors: Zhuotao Jin, Xiaoyun Wang, Nicholas Brawand, Roman Zubatyuk, Atul Thakur, Eric Qu, Boris Kozinsky, Justin Smith
url: http://arxiv.org/abs/2608.07401v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DynaCrys: Crystal Generation with Dynamic Space-Group Diffusion

## Abstract
The search for new crystalline materials spans an enormous compositional and structural space. Generating candidates in this space requires jointly modeling discrete crystallographic symmetry, elemental composition, and continuous geometry. We introduce DynaCrys, a generative model for crystals in which the space group co-evolves with Wyckoff occupations and elements through a coupled symbolic diffusion process. The structured space-group transitions follow crystallographic group-subgroup relations. As the space group changes, a shared, pretrained symmetry codebook provides both the legality-constrained stochastic decoder and the symmetry-constrained crystal-geometry model with a common representation of the corresponding Wyckoff vocabulary. Across large-scale evaluations using two independent relaxation-and-evaluation engines, DynaCrys achieves best-in-class performance in symmetry-aware discovery of stable, unique, and novel crystals, both overall and under the additional requirement of nontrivial post-relaxation symmetry. It also enables fast sampling while generating structures with consistently low relaxation-induced structural displacements.

## Metadata
- **Published**: 2026-08-07T16:45:51Z
- **Authors**: Zhuotao Jin, Xiaoyun Wang, Nicholas Brawand, Roman Zubatyuk, Atul Thakur, Eric Qu, Boris Kozinsky, Justin Smith
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07401v1)