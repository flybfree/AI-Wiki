---
title: TRACE: Spatiotemporal Contact Memory Graph Network Simulator for Granular Dynamics
published: 2026-09-02T15:30:41Z
authors: Changjian Zhou, Negin Yousefpour, Jie Qi, Junfeng Fang, Guillermo A. Narsilio, Hans Petter Jostad
url: http://arxiv.org/abs/2609.02991v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACE: Spatiotemporal Contact Memory Graph Network Simulator for Granular Dynamics

## Abstract
Learned graph simulators provide an efficient alternative to high-fidelity solvers for granular dynamics. However, granular motion depends strongly on inter-granular contact history, which is difficult to preserve when particle contacts form, break, and rearrange. Existing simulators mainly store temporal information in node features or node-level memory. Here we introduce TRACE, a graph-network simulator that stores interaction history directly on contact edges. Each edge maintains a persistent memory updated by attention-based message passing and a gated recurrent unit, while an edge-identity dictionary preserves this memory as the contact graph changes. A physics-structured decoder predicts inter-granular normal and tangential contact forces, enforces the Coulomb friction limit, and applies equal-and-opposite internal forces. The model is trained with single-step pretraining followed by autoregressive rollout fine-tuning. We evaluate TRACE on 2D and 3D granular column-collapse benchmarks. In both cases, TRACE produces stable, physically consistent long-horizon rollouts, closely reproducing the final deposit geometry and the kinetic energy released during collapse. Compared with graph network simulator (GNS) and node-memory graph neural simulator (NMGNS), TRACE reduces long-rollout position error by 31-62% and final-deposit error by 58-89% across the two benchmarks, while using fewer parameters and maintaining near-zero particle interpenetration. TRACE also achieves 12.2$\times$ and 8.9$\times$ speedups over the material point method (MPM) reference solver in 2D and 3D, respectively. Our code is available at https://github.com/Data-Driven-Computational-Geotechnics/TRACE.

## Metadata
- **Published**: 2026-09-02T15:30:41Z
- **Authors**: Changjian Zhou, Negin Yousefpour, Jie Qi, Junfeng Fang, Guillermo A. Narsilio, Hans Petter Jostad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02991v1)