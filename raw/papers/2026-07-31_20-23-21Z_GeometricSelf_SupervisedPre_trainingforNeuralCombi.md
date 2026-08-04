---
title: Geometric Self-Supervised Pre-training for Neural Combinatorial Optimization
published: 2026-07-31T20:23:21Z
authors: David Aguado, Daniel Fuertes, Carlos R. del-Blanco, Fernando Jaureguizar
url: http://arxiv.org/abs/2608.00270v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Geometric Self-Supervised Pre-training for Neural Combinatorial Optimization

## Abstract
Neural Combinatorial Optimization (NCO) techniques have emerged as a highly efficient alternative to traditional exact algorithms for solving routing problems such as the Traveling Salesman Problem (TSP). However, the generalization capabilities of these Reinforcement Learning-based models are severely hindered when scaling to high-dimensional instances. This issue has been mitigated in other domains, like computer vision and natural language processing, by adopting a self-supervised pre-training strategy. Nevertheless, its application to routing graphs, which lack complex topological attributes beyond 2D spatial coordinates, remains a challenge. In this paper, we propose a geometric self-supervised pre-training framework specifically designed to capture spatial invariance and global relative distance distributions. By applying isometric transformations, such as rotations and axial reflections, the model learns robust structural representations prior to the policy optimization phase. Empirical results demonstrate that this strategy consistently outperforms models trained from scratch (baselines), achieving a 7.23\% improvement in tour length for massive zero-shot extrapolation scenarios (TSP1,000). Furthermore, the proposed model exhibits remarkable computational efficiency, delivering speedups of up to two orders of magnitude over the exact solver Concorde at massive scales.   The source code and pre-trained models are publicly available at https://github.com/davidaguadocosano/TSP-GeoPretrain.git.

## Metadata
- **Published**: 2026-07-31T20:23:21Z
- **Authors**: David Aguado, Daniel Fuertes, Carlos R. del-Blanco, Fernando Jaureguizar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00270v1)