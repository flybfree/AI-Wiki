---
title: LieStoNet: Learning Lie Symmetries from Spatiotemporal Data for Stochastic Dynamical Systems
published: 2026-08-03T01:34:13Z
authors: Shida Liu, Abhishek Gupta, Sumit Sinha, L. Mahadevan
url: http://arxiv.org/abs/2608.01582v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LieStoNet: Learning Lie Symmetries from Spatiotemporal Data for Stochastic Dynamical Systems

## Abstract
Symmetry is central to modern machine learning and physics: invariances and equivariances improve sample efficiency, robustness, and out-of-distribution generalization, while symmetry principles guide scientific modeling. Yet for stochastic dynamical systems the relevant continuous symmetries are rarely known, and symmetry discovery for SDEs has remained essentially unexplored. We introduce \textit{LieStoNet}, an end-to-end, \emph{template-free} framework for discovering Lie-point symmetries of SDEs directly from spatiotemporal trajectories, without prespecifying symmetry groups, templates, or canonical coordinates. Building on the seminal SDE Lie-symmetry theory of Gaeta and Quintero (1999), which formalizes Lie-point SDE symmetries and their relation to Fokker-Planck symmetries, LieStoNet learns neural surrogates for drift and diffusion from increments, then learns projectable generators by enforcing the SDE determining equations, separately regularizing for closure under Lie brackets, adherence to the Lie algebra axioms (bilinearity, antisymmetry, Jacobi), and a non-redundant independent basis. The surrogate also defines an associated Fokker-Planck equation, enabling optional discovery of its Lie-point symmetries in parallel. Across multiple canonical SDEs with known analytic symmetries, LieStoNet recovers generators consistent with the ground-truth symmetry algebra, providing interpretable symmetry discovery for noisy dynamics. Code is available at \href{https://github.com/sumit-sinha-seas/LieStoNet_Final.git}{this link}.

## Metadata
- **Published**: 2026-08-03T01:34:13Z
- **Authors**: Shida Liu, Abhishek Gupta, Sumit Sinha, L. Mahadevan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01582v1)