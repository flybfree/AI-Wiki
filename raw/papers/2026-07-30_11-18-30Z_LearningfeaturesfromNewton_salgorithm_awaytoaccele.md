---
title: Learning features from Newton's algorithm: a way to accelerate nonlinear parametrized PDE solvers
published: 2026-07-30T11:18:30Z
authors: Rémy Vallot, Florian de Vuyst, Thibault Dairay, Mathilde Mougeot
url: http://arxiv.org/abs/2607.28036v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning features from Newton's algorithm: a way to accelerate nonlinear parametrized PDE solvers

## Abstract
It is well known that Newton's method converges faster when the initial guess is closer to a root of a system of nonlinear equations. In this paper, a two-stage Newton initial guess strategy is proposed by learning features from a parameter-space sampling and a database of precomputed solutions. The method uses discrete Newton trajectories to construct two complementary reduced spaces: a solution feature space, built from converged states, and a corrective search direction feature space, built from intermediate Newton increments. For an unseen parameter, a regression model is used to predict a surrogate solution approximation. Then, in a second step, a residual-minimizing correction is computed using a dedicated GMRES-based approach. The resulting state is then used as an initial guess for the high-fidelity Newton method, which completes convergence. The corrective step is computationally inexpensive since it only requires residual evaluations and the solution of a small least-squares problem. The methodology is weakly intrusive once the high-fidelity residual fields and a script-based programming interface are available. This strategy reduces the number of Newton iterations and decreases the overall CPU time. Numerical experiments on representative PDE problems show quantifiable speedups compared with standalone surrogate initialization. Significant speedups are observed. This generic approach can be applied to a broad class of large-scale nonlinear problems.

## Metadata
- **Published**: 2026-07-30T11:18:30Z
- **Authors**: Rémy Vallot, Florian de Vuyst, Thibault Dairay, Mathilde Mougeot
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28036v1)