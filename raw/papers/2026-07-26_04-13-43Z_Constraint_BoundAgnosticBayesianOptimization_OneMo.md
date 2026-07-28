---
title: Constraint-Bound Agnostic Bayesian Optimization: One Model for All Thresholds
published: 2026-07-26T04:13:43Z
authors: Jin Wang, Xi Lin, Handing Wang
url: http://arxiv.org/abs/2607.23448v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Constraint-Bound Agnostic Bayesian Optimization: One Model for All Thresholds

## Abstract
Expensive constrained optimization problems in real-world industry design often involve constraint thresholds that are difficult to determine in advance. Engineers may need to adjust constraint thresholds to explore different feasibility-performance trade-offs, requiring solutions under a wide range of threshold settings. However, existing constrained Bayesian optimization methods treat each threshold configuration independently, leading to repeated optimization and failing to exploit the shared relationship among continuously varying thresholds. To address this challenge, we propose constraint-bound agnostic Bayesian optimization (CBA-BO), a learning-based framework that learns a parametric constraint model mapping thresholds to optimal solutions. Once learned, CBA-BO directly predicts solutions for arbitrary unseen threshold configurations without additional optimization, with a one-step Bayesian optimization refinement further improving solution quality. Experiments on benchmark and engineering problems demonstrate that CBA-BO learns a transferable threshold-solution mapping, enabling efficient prediction and optimization for arbitrary threshold queries. An intent-guided constraint-bound recommendation mechanism is further developed to improve objective performance while satisfying user-specified constraint preferences.

## Metadata
- **Published**: 2026-07-26T04:13:43Z
- **Authors**: Jin Wang, Xi Lin, Handing Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23448v1)