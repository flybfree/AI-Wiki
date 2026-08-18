---
title: Layers Matter: Why Continual Learning Regularization Should Be Layer-Adaptive
published: 2026-08-16T19:37:38Z
authors: Brian B. Moser, Ahmed Anwar, Tobias Christian Nauen, Shishir Muralidhara, Federico Raue, René Schuster, Stanislav Frolov, Andreas Dengel
url: http://arxiv.org/abs/2608.15901v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Layers Matter: Why Continual Learning Regularization Should Be Layer-Adaptive

## Abstract
Continual learning regularizers like EWC fight forgetting by penalizing changes from previous-task parameters with per-parameter importance, typically diagonal Fisher values. Per-parameter looks more flexible than per-layer, but each layer's diagonal Fisher is a weak summary of its actual curvature, missing the top-eigenvalue information that controls forgetting. Adversarial bit-flip attacks and Hessian-spectrum studies show that this missing per-layer sensitivity spans orders of magnitude in neural networks. Under a block-diagonal Hessian assumption, the layer-level analogue of EWC's existing diagonal assumption, we prove three things. Forgetting decomposes as a sum of per-layer terms weighted by each layer's top Hessian eigenvalue. Diagonal-Fisher weights cannot recover this eigenvalue. For instance, two layers with identical Fisher averages can have top eigenvalues differing by a factor as large as the layer width. For the same level of forgetting, uniform regularization loses new-task performance by an amount scaling with the layer condition number. Our theoretical analysis leads to a simple recipe: protect early layers strongly, let deeper layers move. We apply this recipe to EWC and SLCA and show clear improvements in average performance and forgetting metrics.

## Metadata
- **Published**: 2026-08-16T19:37:38Z
- **Authors**: Brian B. Moser, Ahmed Anwar, Tobias Christian Nauen, Shishir Muralidhara, Federico Raue, René Schuster, Stanislav Frolov, Andreas Dengel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15901v1)