---
title: MiSS: A Logic-Driven Explanation of Minimal Sufficient Coalitions for Point Cloud Classifiers
published: 2026-07-27T07:17:04Z
authors: Mengda Xing, Jean-Marie Lagniez
url: http://arxiv.org/abs/2607.24074v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MiSS: A Logic-Driven Explanation of Minimal Sufficient Coalitions for Point Cloud Classifiers

## Abstract
We present MiSS, a black-box, query-based framework for explaining 3D point cloud classifiers through perturbation-relative sufficiency reasoning. MiSS treats a superpoint partition as an interpretable abstraction layer and asks whether the original prediction can be certified from a minimal coalition of geometric regions under a specified perturbation distribution. Unlike abductive explainers that require Boolean feature spaces or white-box logical encodings of the predictor, MiSS separates candidate proposal from verification: a weighted MaxSAT procedure proposes coalitions using a heuristic adaptive cardinality floor, certified exact-size fallback, a safely tightened upper bound, blocking clauses, and a surrogate acquisition heuristic learned from previous oracle evaluations, while a blackbox statistical oracle decides sufficiency from prediction queries. The system returns a statistically verified sufficient coalition as a binary attribution, with minimum cardinality guaranteed when certified search completes. Experiments on ModelNet40 and ShapeNet with PointNet and PointMLP classifiers show higher precision and coverage than rule-based baselines in most settings, with lower explanation time than exhaustive search.

## Metadata
- **Published**: 2026-07-27T07:17:04Z
- **Authors**: Mengda Xing, Jean-Marie Lagniez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24074v1)