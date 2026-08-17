---
title: Connected Subspace Clustering: Hardness, a Scalable Heuristic, and an Application to Sea Level Geodesy
url: http://arxiv.org/abs/2608.14215v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_11-45-05Z_ConnectedSubspaceClustering_Hardness_aScalableHeur.md
generated_at: 2026-08-16 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Connected Subspace Clustering, a method for partitioning high‑dimensional measurements into exactly k connected clusters while fitting low‑dimensional affine subspaces to each cluster. It proves the problem is NP‑hard even with simple connectivity constraints and provides a scalable heuristic that alternates subspace fitting and merging steps. On sea level geodesy data the approach yields fewer disconnected fragments than unconstrained methods.

## Key Takeaways
- The problem of partitioning points into k connected clusters minimizing squared distance to m′‑dimensional affine subspaces is NP‑hard for any ε>0, even when m′=0 and the graph has holes. 
- The proposed heuristic combines Lloyd’s subspace fitting with an iterative merging procedure that guarantees exactly k connected regions by construction. 
- In experiments on 160 sea level configurations the method outperforms four strategies in 73.75 % of cases, especially compared to Ward’s method.

## Context
This work addresses a longstanding challenge in machine learning where spatial coherence must be preserved alongside dimensionality reduction. By integrating graph connectivity as a hard constraint, it bridges unsupervised clustering and constrained optimization, offering a principled way to handle spatially embedded data such as climate fields or neuroimaging slices.

## Implications
For geodesy the method enables reliable identification of contiguous regions that align with natural climate patterns like El Niño‑Southern Oscillation. Practitioners can apply the same framework to remote sensing networks or sensor arrays where connectivity and subspace fitting are both important, improving signal isolation without sacrificing computational scalability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14215v1)
