---
title: Hybrid Lagrangian-Eulerian Model for Lagrangian Fluid Simulation
published: 2026-08-02T11:36:08Z
authors: Ruoyan Li, Wei Wang, Yizhou Sun
url: http://arxiv.org/abs/2608.01164v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hybrid Lagrangian-Eulerian Model for Lagrangian Fluid Simulation

## Abstract
Pure Lagrangian neural simulators offer geometric flexibility and exact advection, making them well-suited for modeling moving domains and free surfaces. However, the absence of a fixed global reference frame introduces two severe limitations: a spatial bottleneck, in which model capacity is wasted on uniform regions because the dense particle neighborhoods required for stable gradients are applied indiscriminately, and rapid temporal drift, caused by purely local message passing that lacks a global anchor. Inspired by classical hybrid numerical solvers, we propose a Hybrid Lagrangian-Eulerian neural simulator that augments Lagrangian dynamics with an Eulerian representation. To address the spatial bottleneck, we introduce adaptive downsampling that eliminates kinematic redundancy, preserving micro-scale details on particles while aggregating compressed features onto Eulerian nodes to resolve large-scale dynamics. To counter temporal drift, we employ a cross-attention mechanism that queries these Eulerian features, using the fixed grid as a stable spatial anchor to correct trajectory deviations at every timestep. Comprehensive experiments show that this hierarchical, cross-attended design substantially suppresses error accumulation, establishing a new state-of-the-art for accuracy and rollout stability in Lagrangian fluid simulation.

## Metadata
- **Published**: 2026-08-02T11:36:08Z
- **Authors**: Ruoyan Li, Wei Wang, Yizhou Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01164v1)