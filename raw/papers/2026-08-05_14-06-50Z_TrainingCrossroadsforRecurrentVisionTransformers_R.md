---
title: Training Crossroads for Recurrent Vision Transformers: Recurrence, Neural ODEs, and Deep Supervision
published: 2026-08-05T14:06:50Z
authors: Grzegorz Gruszczynski, Pawel Olszowiec, Michal Byra, Grzegorz Stefanski, Alberto Presta
url: http://arxiv.org/abs/2608.04879v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Crossroads for Recurrent Vision Transformers: Recurrence, Neural ODEs, and Deep Supervision

## Abstract
Vision Transformers (ViTs) achieve strong image-recognition performance, but their parameter count grows linearly with depth when each block is independently parameterized. Single-block recurrent ViTs (bViT) remove this growth by repeatedly applying one shared block. Rather than proposing a new architecture, we fix a bViT and provide a controlled empirical characterization of three training and inference regimes under a common CIFAR-100 protocol, asking: (i)~when does recurrence beat independently parameterized depth---at matched FLOPs or at matched parameter memory? (ii)~when a residual recurrent block is trained through an ODE solver, does solver order act as numerical refinement or as an architectural bias? and (iii)~what does robustness beyond the training horizon cost in nominal accuracy? We find that standard ViTs remain preferable when FLOPs are the primary constraint, whereas recurrent ViTs offer a better accuracy--parameter trade-off under memory constraints. Consistent with the standard view of residual networks as Euler discretizations of ODEs, the continuous-time analogue of a residual recurrent block is the state-subtracted vector field $\dot{z}=F_θ(z)-z$; although known in principle, this distinction is easy to violate when the block is wrapped as a black-box vector field, and we qualify the cost at few accuracy points. Because the vector field is learned jointly with the solver, higher-order solvers act as a solver-induced architectural bias rather than a numerical-accuracy improvement, and their gains are not uniform. Finally, stage-wise deep supervision traces an accuracy--robustness frontier: it does not improve nominal accuracy, but degrades gracefully far beyond the training horizon, where naive recurrence collapses to near-random performance.

## Metadata
- **Published**: 2026-08-05T14:06:50Z
- **Authors**: Grzegorz Gruszczynski, Pawel Olszowiec, Michal Byra, Grzegorz Stefanski, Alberto Presta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04879v1)