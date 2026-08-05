---
title: Operationally Feasible Synthetic Power-Grid Scenarios via Learning the AC-Operable Joint Distribution
published: 2026-08-04T16:17:15Z
authors: Chenhan Xiao, Xinyu He, Haoran Li, Hanghang Tong, Yang Weng
url: http://arxiv.org/abs/2608.03878v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Operationally Feasible Synthetic Power-Grid Scenarios via Learning the AC-Operable Joint Distribution

## Abstract
Synthetic power-grid scenarios are essential for planning, resilience assessment, contingency analysis, and data-driven power-system applications. Recent synthetic grid generation methods have improved structural realism and operational feasibility by incorporating engineering knowledge through post-generation validation, optimization, or physics-aware generation. However, generated scenarios may still exhibit low AC feasibility and robustness, limiting their practical value for downstream power-system studies. This paper proposes a feasibility-aware distribution-learning framework that learns the AC-operable joint distribution of network topology, branch electrical parameters, and time-varying load profiles. Instead of enforcing feasibility after generation, the proposed framework incorporates AC power-flow convergence and operational constraints into hierarchical diffusion-based distribution learning. This enables the generator itself to produce operationally feasible grid scenarios through efficient diffusion sampling. The hierarchical architecture decomposes the high-dimensional generation task into three engineering-motivated stages: topology and bus-attribute generation, branch-parameter generation conditioned on the generated structure, and load-profile generation conditioned on both network structure and electrical characteristics. Experiments on benchmark systems demonstrate that the proposed framework significantly improves operational feasibility and contingency robustness while maintaining strong statistical fidelity and eliminating optimization-based post-processing.

## Metadata
- **Published**: 2026-08-04T16:17:15Z
- **Authors**: Chenhan Xiao, Xinyu He, Haoran Li, Hanghang Tong, Yang Weng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03878v1)