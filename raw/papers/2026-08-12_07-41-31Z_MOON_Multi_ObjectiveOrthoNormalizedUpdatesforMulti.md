---
title: MOON: Multi-Objective OrthoNormalized Updates for Multitask Learning
published: 2026-08-12T07:41:31Z
authors: Shiji Zhou, Kunlin Lyu, Lei Zhang, Ruodong Wang, Yifan Sun
url: http://arxiv.org/abs/2608.11749v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MOON: Multi-Objective OrthoNormalized Updates for Multitask Learning

## Abstract
Multi-objective optimization (MOO) has demonstrated significant success in multi-task learning by mitigating task conflicts through gradient manipulation. However, most existing methods flatten model parameters into vectors and perform gradient manipulation under Euclidean geometry, thereby overlooking the matrix structure prevalent in modern architectures such as Transformers. In this paper, we show that gradient manipulation in Euclidean space does not generally yield the steepest descent direction under matrix geometry, potentially limiting optimization efficiency. Drawing from the theory of steepest descent for matrix-valued parameters, we propose MOON (Multi-Objective OrthoNormalized Updates), which performs gradient manipulation under spectral--nuclear norm geometry and uses the orthonormalized manipulated gradient for parameter updates. Theoretically, for smooth non-convex objectives, we establish convergence of the averaged Pareto-stationarity measure at rates of $\mathcal{O}(T^{-1/2})$ in the deterministic setting and $\mathcal{O}(T^{-1/4})$ under stochastic gradients. Empirical results across various benchmarks show that MOON consistently improves both optimization efficiency and final multi-task performance. Our code is available at https://github.com/KunlinLyu/MOON.

## Metadata
- **Published**: 2026-08-12T07:41:31Z
- **Authors**: Shiji Zhou, Kunlin Lyu, Lei Zhang, Ruodong Wang, Yifan Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11749v1)