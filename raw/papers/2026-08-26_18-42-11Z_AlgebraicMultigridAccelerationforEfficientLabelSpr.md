---
title: Algebraic Multigrid Acceleration for Efficient Label Spreading
published: 2026-08-26T18:42:11Z
authors: Antonia van Betteray, Jonathan Klees, Miriam Schäfers, Matthias Rottmann
url: http://arxiv.org/abs/2608.26309v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Algebraic Multigrid Acceleration for Efficient Label Spreading

## Abstract
Modern machine learning models rely on large amounts of labeled data. However, manual annotation of large-scale datasets is expensive and time-consuming. Label spreading is a semi-supervised learning technique that addresses this challenge by propagating information from a few labeled examples to a larger pool of unlabeled data. Despite its effectiveness, its application to large-scale, high-dimensional datasets is limited by computational costs and memory constraints. To address these limitations, we propose Algebraic Multigrid Acceleration for Efficient Label Spreading (AMELS), an efficient label spreading framework that improves scalability by fast construction of neighborhood graphs and the incorporation of algebraic multigrid solvers. The latter is an iterative solver that replaces the ordinary random walk iteration typically performed in label spreading. Due to the multilevel nature of algebraic multigrid solvers, AMELS spreads given label information across a graph of any size in a single multigrid cycle. We demonstrate that AMELS achieves significant runtime reductions compared to existing implementations while also being more robust to hyperparameter choices in terms of both runtime and classification accuracy. Our framework therefore enables efficient label spreading on large-scale image datasets and produces accurate labels even when only a few labeled samples are available.

## Metadata
- **Published**: 2026-08-26T18:42:11Z
- **Authors**: Antonia van Betteray, Jonathan Klees, Miriam Schäfers, Matthias Rottmann
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26309v1)