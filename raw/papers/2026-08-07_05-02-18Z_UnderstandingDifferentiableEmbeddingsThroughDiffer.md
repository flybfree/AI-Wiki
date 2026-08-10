---
title: Understanding Differentiable Embeddings Through Differential and Integral Geometry
published: 2026-08-07T05:02:18Z
authors: Xinyu Zhang, Klaus Mueller
url: http://arxiv.org/abs/2608.06809v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding Differentiable Embeddings Through Differential and Integral Geometry

## Abstract
How can an analyst decide whether a nonlinear dimensionality reduction embedding can be trusted? Existing diagnostics provide only partial answers: projection glyphs characterize local sensitivity, map-continuity scores measure local conditioning, and transport-based analyses reveal path-dependent inconsistencies. However, these methods appear unrelated and provide no common framework for understanding when they agree or not. We show that they are all derived from a single geometric object induced by every differentiable embedding, whether defined implicitly through optimization or explicitly by a learned mapping. This framework provides two complementary geometric views of an embedding. The differential view explains local behavior: its first-order term recovers projection glyphs, while its second-order curvature quantifies how far their linear approximation remains reliable. The integral view follows the same geometry along high dimensional paths and determines whether an embedding depends only on the current state or also on the path taken to reach it. We further show that map-continuity is a prerequisite for the other analyses. The framework is theoretically complete for diagnostics derived from the embedding geometry, and we prove the integral view irreducible: no amount of local measurement at any number of points, to any order of derivative, reproduces what it detects. Classical rank-based metrics form a complementary class based on finite-scale neighborhood relationships. Experiments on synthetic and real datasets validate theoretical predictions, demonstrate accurate curvature-based trust estimates on single-cell embeddings, and show that the integral analysis distinguishes single-valued embeddings from path-dependent optimization-based embeddings in ways that existing pointwise diagnostics cannot.

## Metadata
- **Published**: 2026-08-07T05:02:18Z
- **Authors**: Xinyu Zhang, Klaus Mueller
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06809v1)