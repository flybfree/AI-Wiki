---
title: LaGSplat: Inferring Physics-Governed Interactive Simulation from Monocular Video Using Latent Lagrangian Gaussian Splatting
published: 2026-08-17T09:29:12Z
authors: Louen Pottier
url: http://arxiv.org/abs/2608.16324v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LaGSplat: Inferring Physics-Governed Interactive Simulation from Monocular Video Using Latent Lagrangian Gaussian Splatting

## Abstract
We present LaGSplat (Latent Lagrangian Gaussian Splatting), a framework that infers interactive, physics-governed dynamics from one or a few monocular videos. At inference it lets a user push on the filmed object, rigid or deformable, with an external force that was never measured, annotated, or seen during training. This is possible because a low-dimensional latent state $\mathbf{q} \in \mathbb{R}^d$ plays two roles at once: it is the generalised coordinate of a learned dissipative Lagrangian and the conditioning variable of a Gaussian Splatting decoder. The inductive bias of this decoder, whose primitives are explicit points $μ_i(\mathbf{q})$ that move with the object, is what lets a force $f$ applied in the image pull back into a latent generalised force $J(\mathbf{q})^\top f$ and enter the equations of motion, which pixel-space (CNN) or neural-field (NeRF) decoders cannot do. We validate LaGSplat on test cases of increasing difficulty, from rigid to deformable and from autonomous to forced real systems, combining monocular video and sensor measurements. We further demonstrate interactive use: forces of arbitrary magnitude and direction can be applied to the reconstructed object at any time, its response rendered in real time, in 2D or 3D. Assuming a dissipative Euler-Lagrange equation over a few generalised coordinates trades generality for a bounded, plausible response to unseen forces, where an unconstrained predictor diverges.

## Metadata
- **Published**: 2026-08-17T09:29:12Z
- **Authors**: Louen Pottier
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16324v1)