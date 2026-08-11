---
title: Constrained Learning with Universally Learnable Concept Classes
published: 2026-08-09T02:13:57Z
authors: Herlock SeyedAbolfazl Rahimi, Spyridon Pougkakiotis, Dionysis Kalogerias
url: http://arxiv.org/abs/2608.08414v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Constrained Learning with Universally Learnable Concept Classes

## Abstract
We study constrained statistical learning over infinite-dimensional hypothesis classes in the fully nonconvex setting, and establish universal PACC learnability of the solutions of dual algorithms: Probably Approximately Correct on Constraints, guaranteeing optimality and constraint satisfaction at once. This strengthens near-PACC results, whose feasibility residual no amount of data can remove. Optimality is caught between generalization, governed by Rademacher complexity and favoring small classes, and strong Lagrangian duality, which rests on Lyapunov convexity for vector measures and needs decomposability, a demand pulling the other way. We reconcile the two by posing the population problem over a universal RKHS $\mathcal{H}_K$, dense in a decomposable envelope, and learning over norm balls of growing radius. This yields the Tikhonov complexity $\mathfrak{T}^{\varepsilon}_{n}$, the least RKHS norm reaching an $\varepsilon$-optimal Lagrangian level set; we prove it finite, obtain exact learnability of the optimal value, and make the sample threshold explicit and polynomial in $1/\varepsilon$ under a source condition. Feasibility is harder: absent convexity the Lagrangian may not attain its infimum, and dual information pins down only an averaged constraint-risk vector, not the risks of any returned predictor. We introduce the closure-realization gap $\varepsilon^\star_\infty$, an index of how well $\mathcal{H}_K$ retrieves feasible solutions from dualization; it is a property of the problem, not of a modeling choice. Learnability is exact when $\varepsilon^\star_\infty=0$, in particular under dual differentiability, and near-PACC with residual exactly $\varepsilon^\star_\infty$ otherwise. Finally, no distribution-free threshold exists already in the unconstrained specialization, so universality is the canonical frame for dual algorithms over large hypothesis classes.

## Metadata
- **Published**: 2026-08-09T02:13:57Z
- **Authors**: Herlock SeyedAbolfazl Rahimi, Spyridon Pougkakiotis, Dionysis Kalogerias
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08414v1)