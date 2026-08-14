---
title: Efficient Hessian-Free Methods for Multi-Objective Bilevel Optimization with Nonconvex Lower Level
published: 2026-08-13T01:37:49Z
authors: Yicong Jiang, Feihu Huang
url: http://arxiv.org/abs/2608.12704v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient Hessian-Free Methods for Multi-Objective Bilevel Optimization with Nonconvex Lower Level

## Abstract
Multi-objective bilevel optimization has wide applications in the AI area such as automated learning and multi-task meta-learning. Although recently some works have been begun to study the multi-objective bilevel optimization, the proposed methods rely on the (strongly) convex lower level problems. In fact, these multi-objective bilevel learning problems are generally nonconvex, and particularly their lower level problems are nonconvex. To fill this gap, we propose a class of Multi-Objective Moreau Envelope based Hessian-free Algorithms (MOMEHA) to solve the multi-objective bilevel learning problems with nonconvex lower level. Specifically, our method uses the Moreau envelope to convert the original problem into a multi-objective single-level optimization with an envelope constraint. In particular, our method retains computational advantages of being single-loop and Hessian-free in the multi-objective setting by incorporating a smooth weighted Tchebycheff scalarization. Furthermore, we propose a momentum-based variant of MOMEHA (i.e., MB-MOMEHA) method to solve the stochastic multi-objective bilevel learning problems. In theory, we provide the convergence properties of our algorithms under both deterministic and stochastic setting. Some experiments on few-shot meta-learning and neural architecture search demonstrate that our methods outperform the existing approaches in Pareto front, validating its effectiveness and robustness.

## Metadata
- **Published**: 2026-08-13T01:37:49Z
- **Authors**: Yicong Jiang, Feihu Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12704v1)