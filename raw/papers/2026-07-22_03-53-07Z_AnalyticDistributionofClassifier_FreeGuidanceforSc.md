---
title: Analytic Distribution of Classifier-Free Guidance for Schedule Design
published: 2026-07-22T03:53:07Z
authors: Enze Jiang, Zheng Ma
url: http://arxiv.org/abs/2607.19725v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Analytic Distribution of Classifier-Free Guidance for Schedule Design

## Abstract
Classifier-free guidance (CFG) is the default mechanism for conditional generation in diffusion models, but the distribution sampled by its deterministic guided dynamics is not captured by the usual product-distribution heuristic $p_0^ωq_0^{1-ω}$. We analyze CFG through the probability flow ODE and derive exact analytic path-integral representations of the induced distributions for both constant and time-dependent guidance. The resulting formulas show that CFG modifies $p_{t_0}$ by an exponential path-integral correction, and that a time-dependent schedule enters this correction through the weight $ω(t)-1$. This characterization explains how score discrepancies accumulate along sampling trajectories and motivates Distribution-Guided CFG (DG-CFG), a schedule that balances timestep contributions while accounting for signal strength and low-noise score-error amplification. A toy model with analytic scores closely verifies the predicted distributions. On Stable Diffusion~1.5, DG-CFG improves generation and yields a stronger diversity--fidelity trade-off across guidance strengths, with especially clear gains when strong guidance causes saturation and quality degradation in constant and heuristic schedules. Across NFE budgets, DG-CFG reaches fixed image-quality targets with fewer sampling steps, reducing the sampling cost needed to achieve target metrics.

## Metadata
- **Published**: 2026-07-22T03:53:07Z
- **Authors**: Enze Jiang, Zheng Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19725v1)