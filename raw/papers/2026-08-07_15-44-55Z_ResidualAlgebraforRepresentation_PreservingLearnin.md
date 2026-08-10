---
title: Residual Algebra for Representation-Preserving Learning
published: 2026-08-07T15:44:55Z
authors: Yao Wu
url: http://arxiv.org/abs/2608.07349v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Residual Algebra for Representation-Preserving Learning

## Abstract
Learning from heterogeneous representations is usually reduced to feature concatenation, which erases which representation produced an error. We instead algebraize the residual: a representation is a typed object that owns both a coordinate system and the residual it leaves unresolved, and learning is an ordered composition of operators that preserve or deliberately erase that type. Fold realizes the objects as point-in-time conditional-mean fields on 10x10 rank grids. FPRC-PQ realizes the algebra as relax-aggregate-close: each field is relaxed by a correction fitted to its own residual in its own coordinates; corrected fields meet at a fixed mean that is the sole identity-erasure boundary; and a shared learner closes only the aggregate's fresh residual. The composition telescopes exactly into representation, local residual estimate, and residual-of-residual estimate. Its aggregate is a learned control-variate interface with population variance reduction, while refitting the closer along perturbations of the backbone yields first-order coupled-path mean orthogonality. As an analytical extension, a reflective rumination operator reads the displacement of a global reconstruction from the aggregate anchor, reflects it, and fixes its gain by a unique orthogonal projection rather than return-tuned grid search. On 3.67M Chinese A-share stock-day observations (2023-2026) under a frozen point-in-time protocol, the evaluated base algebra raises net-of-cost return from 13.52% to 19.10% and Sharpe from 1.42 to 2.09. Matched-capacity, unified-residual, identity-free two-stage, and pairwise-only controls all trail it. The gain is therefore not explained by more features or more trees, but by making residual ownership and composition explicit while representation identity is still available.

## Metadata
- **Published**: 2026-08-07T15:44:55Z
- **Authors**: Yao Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07349v1)