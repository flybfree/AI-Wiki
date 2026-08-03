---
title: Frugal Bayesian Optimization: Scalable Surrogates for Data- and Resource-Limited Discovery
published: 2026-07-31T09:55:38Z
authors: Panagiotis Krokidas, Christoforos Rekatsinas, Vassilis Sioros, Grigorios M. Chatziathanasiou, Efi-Maria Papia, George Giannakopoulos
url: http://arxiv.org/abs/2607.29225v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Frugal Bayesian Optimization: Scalable Surrogates for Data- and Resource-Limited Discovery

## Abstract
Bayesian Optimization (BO) is widely adopted for data-efficient optimization in scientific and engineering applications, yet its computational cost is rarely evaluated alongside optimization performance. Here we present a systematic, compute-aware study of BO that evaluates surrogate models along two axes: optimization quality and computational frugality. Across eight benchmark functions and nine real-world datasets spanning materials science, mechanics, robotics, chemistry, and machine learning, we benchmark four surrogate models: Gaussian Processes, Random Forests, NGBoost, and Bayesian Adaptive Spline Surfaces. We show that Gaussian Process-based BO consistently incurs the highest time and memory overhead without delivering superior optimization or sample efficiency. In contrast, scalable alternatives achieve equal or better performance at a fraction of the computational cost. Motivated by these findings, we introduce a surrogate-recommendation framework that predicts the most suitable BO surrogate from inexpensive dataset characteristics. Together, these results establish FruBO as a reproducible, compute-aware baseline for Bayesian Optimization and provide practical guidance for surrogate selection under limited computational and experimental budgets.

## Metadata
- **Published**: 2026-07-31T09:55:38Z
- **Authors**: Panagiotis Krokidas, Christoforos Rekatsinas, Vassilis Sioros, Grigorios M. Chatziathanasiou, Efi-Maria Papia, George Giannakopoulos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29225v1)