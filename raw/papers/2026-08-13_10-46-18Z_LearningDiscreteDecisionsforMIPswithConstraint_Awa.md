---
title: Learning Discrete Decisions for MIPs with Constraint-Aware Diffusion
published: 2026-08-13T10:46:18Z
authors: Vincenzo Di Vito, Mehdi Taghizadeh, Deepjyoti Deka, Kaarthik Sundar, Ferdinando Fioretto
url: http://arxiv.org/abs/2608.13079v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Discrete Decisions for MIPs with Constraint-Aware Diffusion

## Abstract
This paper proposes a novel learning-based approach to approximately solve instances of mixed-integer optimization problems. These problems are computationally challenging, as they require jointly determining discrete and continuous decisions while satisfying complex combinatorial constraints. The proposed method relies on a graph-based generative diffusion model that learns the discrete component of mixed-integer optimization problems while integrating a training-free feasibility projection operator directly into the reverse diffusion process to steer intermediate samples toward the feasible set throughout generation. Once the discrete decisions are generated, the remaining optimization reduces to a continuous problem that can be solved efficiently (relative to the original problem) using existing numerical methods. The resulting framework named Constrained Graph Diffusion (CGD), is problem-agnostic and can accommodate a broad class of mixed-integer optimization problems through suitable projection operators. We evaluate CGD on optimal transmission switching for ACOPF and discrete portfolio optimization, demonstrating substantial improvements in feasibility and solution quality over learning-based baselines while achieving speedups of up to $425\times$ over state-of-the-art numerical solvers for MINLPs.

## Metadata
- **Published**: 2026-08-13T10:46:18Z
- **Authors**: Vincenzo Di Vito, Mehdi Taghizadeh, Deepjyoti Deka, Kaarthik Sundar, Ferdinando Fioretto
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13079v1)