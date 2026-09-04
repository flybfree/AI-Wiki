---
title: Mesh-Native Physics-Informed Graph Surrogates for TCAD-in-the-Loop Design Space Exploration
published: 2026-09-02T15:15:29Z
authors: Leonid Popryho, Ayoub Sadeghi, Inna Partin-Vaisband
url: http://arxiv.org/abs/2609.02988v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mesh-Native Physics-Informed Graph Surrogates for TCAD-in-the-Loop Design Space Exploration

## Abstract
High-fidelity TCAD simulation of drift-diffusion transport remains the workhorse of emerging FinFET device design, but it is computationally expensive, especially for 3D structures where runtime escalates steeply with mesh complexity. This sharply limits multi-objective design space exploration. Existing machine-learning surrogates map a fixed set of design parameters to a few scalar device metrics, discarding the underlying physics and losing transferability across device geometries and families. A physics-informed graph attention network (GAT) surrogate is proposed. It operates directly on the tetrahedral TCAD mesh and predicts, at every mesh node, the electrostatic potential together with the electron and hole quasi-Fermi levels, the fundamental unknowns of the drift-diffusion system. Training combines a data loss with finite-volume current-continuity residuals, embedding carrier-transport physics into the objective. Operating on the mesh as a graph, the surrogate inherits size generalization: a model trained on few-fin meshes applies unchanged to substantially larger arrays, bounded at inference only by GPU memory. Per-node uncertainty from a deep ensemble drives an active-learning loop that screens large candidate pools in seconds and forwards only the most informative designs for full simulation. Benchmarked against Sentaurus Device on multi-fin tri-gate FinFETs, the surrogate reproduces the three drift-diffusion fields with sub-volt per-field RMSE and reaches a per-design throughput orders of magnitude higher than the full simulator. The advantage grows with device size: on large multi-fin arrays that are prohibitively slow to simulate directly, inference still completes in under a second per device, enabling Pareto-front exploration across device scales infeasible for direct TCAD sweeps.

## Metadata
- **Published**: 2026-09-02T15:15:29Z
- **Authors**: Leonid Popryho, Ayoub Sadeghi, Inna Partin-Vaisband
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02988v1)