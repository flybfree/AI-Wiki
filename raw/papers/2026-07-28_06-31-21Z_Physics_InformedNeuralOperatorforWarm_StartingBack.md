---
title: Physics-Informed Neural Operator for Warm-Starting Background-Decomposed and Preconditioned PSFD: Enabling Scalable 3-D EUV Mask Simulation
published: 2026-07-28T06:31:21Z
authors: Doyun Kim, Werner Gillijns
url: http://arxiv.org/abs/2607.25330v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Physics-Informed Neural Operator for Warm-Starting Background-Decomposed and Preconditioned PSFD: Enabling Scalable 3-D EUV Mask Simulation

## Abstract
We present a physics-informed neural operator (PINO) trained with pseudo-spectral frequency-domain (PSFD) equations for electromagnetic (EM) scattering problems in EUV lithography. The Fourier neural operator is factorized into a two-dimensional lateral ($xy$) branch and a one-dimensional axial ($z$) branch and is trained self-consistently with background decomposition.Thus, the full-vector coupling between the mask and the multilayer response is retained without invoking a finite-order Born approximation. In this way, the computational domain size is significantly reduced, thereby lowering the computational cost. The PINO is trained on approximately 16,000 mask designs from the LithoBench library sampled randomly at each training iteration without using precomputed EM field solutions. The PINO surrogate model yields predictions with a mean absolute error of about $7 \times 10^{-3}$ for the scattered intensity of held-out mask patterns relative to the reference PSFD solution. Combined with spectral damping, the PINO warm-start initialization accelerates the background-decomposed PSFD solver on finer discretizations.

## Metadata
- **Published**: 2026-07-28T06:31:21Z
- **Authors**: Doyun Kim, Werner Gillijns
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25330v1)