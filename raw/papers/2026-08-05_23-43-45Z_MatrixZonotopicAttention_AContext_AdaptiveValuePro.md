---
title: Matrix Zonotopic Attention: A Context-Adaptive Value Projection for Set Transformers
published: 2026-08-05T23:43:45Z
authors: Zhen Zhang, Amr Alanwar
url: http://arxiv.org/abs/2608.05472v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Matrix Zonotopic Attention: A Context-Adaptive Value Projection for Set Transformers

## Abstract
Multi-head attention combines an input-dependent softmax routing with an input-independent linear value projection, so the per-sample operator mapping aggregated values to outputs is the same for every input set. We study the consequences of this asymmetry for permutation-invariant set targets. We introduce the Transformation Degrees of Freedom (TDOF) of a target operator, a complexity measure counting the input-dependent directions an exact representation requires, and present a depth-separation analysis showing that context-rigid attention needs depth proportional to the target's TDOF, whereas a single layer with a context-adaptive value family can represent the same target. Building on this analysis, we propose Matrix Zonotopic Attention (MZAttn), which replaces the fixed value projection with a context-adaptive matrix-zonotope family: a centre matrix plus a sum of generator matrices weighted by input-dependent gates. The construction reduces to standard multi-head attention at initialisation, preserves permutation equivariance, and admits a data-driven reachability interpretation. Experiments on a range of set-prediction tasks are consistent with the TDOF prediction that the architectural advantage is selective: it appears on targets that depend on the input set in a high-rank, sparsely combinatorial way, and is small on aggregate-statistic targets where parameter-matched standard attention is already competitive.

## Metadata
- **Published**: 2026-08-05T23:43:45Z
- **Authors**: Zhen Zhang, Amr Alanwar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05472v1)