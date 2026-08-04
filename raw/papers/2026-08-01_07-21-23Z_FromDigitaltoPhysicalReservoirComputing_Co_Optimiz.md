---
title: From Digital to Physical Reservoir Computing: Co-Optimizing Soft Robotic Reservoirs via Dynamics Matching
published: 2026-08-01T07:21:23Z
authors: Nicola Visentin, Maximilian Stölzle, Mariano Ramírez Montero, Francesco Braghin, Daniela Rus, Cosimo Della Santina
url: http://arxiv.org/abs/2608.00484v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Digital to Physical Reservoir Computing: Co-Optimizing Soft Robotic Reservoirs via Dynamics Matching

## Abstract
Soft robotic substrates are promising for Physical Reservoir Computing (PRC) because their compliant nonlinear dynamics can provide temporal memory, high-dimensional state transformations, and efficient inference. However, physical reservoirs are often adopted as-is rather than pretrained or co-optimized, potentially limiting soft robotic PRC performance relative to digital reservoirs. We investigate whether a physical reservoir can instead be pretrained against high-performing digital reference dynamics. Our formulation jointly optimizes physical parameters, a diffeomorphic physical-reference state map, and feedforward-feedback control using a differentiable physical model and an acceleration-level equation-error objective that avoids temporal integration. As a proof of concept, we instantiate the formulation with simulated soft robots, a Random Oscillators Network (RON) reference, and parallel multi-start gradient descent. We evaluate the optimized reservoirs on classification (sMNIST and ADIAC) and forecasting (Mackey-Glass and Lorenz96) tasks across four reservoir dimensions. Compared with unoptimized soft robot reservoirs, the optimized reservoirs achieve a mean relative improvement of 33.7% across all tasks and datasets, while remaining close to the digital reference. These results demonstrate the feasibility of dynamics-level co-optimization for the simulated soft robotic reservoirs considered here.

## Metadata
- **Published**: 2026-08-01T07:21:23Z
- **Authors**: Nicola Visentin, Maximilian Stölzle, Mariano Ramírez Montero, Francesco Braghin, Daniela Rus, Cosimo Della Santina
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00484v1)