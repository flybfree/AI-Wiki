---
title: Fluid-DiT: Graph-Free Diffusion Transformers for Fluid Flow Simulations Learning
published: 2026-08-07T12:28:45Z
authors: Shentong Mo, Guolin Ke
url: http://arxiv.org/abs/2608.07161v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fluid-DiT: Graph-Free Diffusion Transformers for Fluid Flow Simulations Learning

## Abstract
Simulating complex fluid flows requires capturing full equilibrium distributions rather than just mean trajectories, yet high-fidelity solvers remain computationally prohibitive. Recent advances, such as Diffusion Graph Networks (DGNs), have combined diffusion models with graph neural networks to sample equilibrium states directly from unstructured meshes, enabling distributional accuracy even from short simulations. However, graph-based diffusion approaches suffer from hand-crafted architectural constraints, limited receptive fields in message passing, and costly multi-scale designs, which restrict scalability to larger and more complex domains. We propose Fluid-DiT, a Graph-Free Diffusion Transformer that replaces graph message passing with attention-based denoising, eliminating explicit graph design while preserving the ability to model distributions of chaotic flows. Our framework introduces a latent-space formulation that disentangles geometric fidelity from distributional learning, reducing high-frequency artifacts and accelerating sampling. By leveraging the transformer's global receptive field, Fluid-DiT naturally captures both local flow structures and long-range correlations without requiring hierarchical graph coarsening. On canonical benchmarks including laminar cylinder wakes, ellipse-flow systems, and turbulent 3D wing experiments, Fluid-DiT consistently outperforms graph-based diffusion baselines in both sample quality and distributional accuracy, achieving higher $R^2$ correlations and lower Wasserstein distances. Moreover, it generalizes robustly from short, incomplete trajectories to unseen Reynolds numbers and geometries, demonstrating strong scalability.

## Metadata
- **Published**: 2026-08-07T12:28:45Z
- **Authors**: Shentong Mo, Guolin Ke
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07161v1)