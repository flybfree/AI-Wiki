---
title: Momentum as Residual-Driven Multiplier Correction for Deep Learning Optimization
published: 2026-08-13T08:04:38Z
authors: Zhixin Ren, Yau Lyu, Congrong Li, Liping Zhang, Shengbo Eben Li
url: http://arxiv.org/abs/2608.12925v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Momentum as Residual-Driven Multiplier Correction for Deep Learning Optimization

## Abstract
Momentum-based optimizers are widely used in modern deep learning, yet the relations among momentum recursion, update geometry, and acceleration remain only partially understood. We develop an $\textbf{A}$DMM-$\textbf{I}$nspired $\textbf{M}$omentum (AIM) framework based on residual-penalty variable splitting, which interprets momentum as a multiplier-like correction driven by the splitting residual. AIM recovers the exponential moving average of gradients from an ADMM-style multiplier update and separates two mechanisms that are usually intertwined in practical optimizers: the residual penalty determines the update geometry, whereas the approximation of the objective-related subproblem determines the acceleration form. Building on AIM, we propose $\textbf{R}$elativistic $\textbf{A}$daptive gradient $\textbf{D}$escent with $\textbf{A}$ccelerated $\textbf{R}$esidual (RADAR), which combines relativistic adaptive geometry, decoupled residual correction, and second-order momentum filtering to improve the update direction and momentum estimation. We establish stochastic convergence through a variance-perturbed Lyapunov drift analysis. Experiments on supervised vision learning, language modeling, and reinforcement learning show that RADAR achieves consistent improvements over strong adaptive optimizer baselines.

## Metadata
- **Published**: 2026-08-13T08:04:38Z
- **Authors**: Zhixin Ren, Yau Lyu, Congrong Li, Liping Zhang, Shengbo Eben Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12925v1)