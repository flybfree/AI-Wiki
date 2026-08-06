---
title: LaPrune: Controllable Differentiable Sparsity at Million Scale
published: 2026-08-04T12:17:00Z
authors: Jakub Antczak, Joanna Wojciechowicz, Łukasz Struski, Jacek Tabor
url: http://arxiv.org/abs/2608.04057v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LaPrune: Controllable Differentiable Sparsity at Million Scale

## Abstract
Top-$k$ selection determines which components of a sparse model remain active. Hard selection blocks gradients, while continuous relaxations often couple mask hardness to the selected mass. We introduce LaPrune, a mathematically exact-budget differentiable layer that controls the normalized second moment while preserving the selected mass. A LapSum barrier preserves the selection mass, and a normalized second-moment constraint moves the mask from a dense equal-mass allocation toward hard top-$k$ at each budget. We derive a population prediction of the saturated fraction, a near-binary limiting law, and a tight worst-case guarantee on the near-zero fraction. The normalized hardness parameter is invariant to score scale, while a fixed LapSum temperature is not.

## Metadata
- **Published**: 2026-08-04T12:17:00Z
- **Authors**: Jakub Antczak, Joanna Wojciechowicz, Łukasz Struski, Jacek Tabor
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04057v1)