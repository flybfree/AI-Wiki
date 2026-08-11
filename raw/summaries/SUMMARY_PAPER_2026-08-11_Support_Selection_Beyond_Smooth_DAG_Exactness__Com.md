---
title: Support Selection Beyond Smooth DAG Exactness: Completion Geometry,Score Margins, and Selective Certificates
url: http://arxiv.org/abs/2608.08103v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_12-33-13Z_SupportSelectionBeyondSmoothDAGExactness_Completio.md
generated_at: 2026-08-11 13:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses how to select support changes that satisfy smooth DAG constraints, focusing on the geometry near the boundary where exactness fails. It shows that minimal cycle completions create a monomial ideal containing all restricted Taylor jets of an exact representation, leading to response orders proportional to the number of edges in the smallest completion. Experiments confirm these theoretical predictions and provide statistical evidence.

## Key Takeaways
- Minimal cycle completions generate a squarefree monomial ideal that includes every restricted Taylor jet of an exact representation when a DAG boundary is approached.
- The first possible response order equals q for vector residuals and 2q for nonnegative scalar residuals, where q is the number of edges in the smallest completion.
- A truth-free separation statistic predicts selection times with high accuracy on official NOTEARS/DAGMA trajectories, achieving Spearman correlations below -0.5.

## Context
This work bridges theoretical analysis of smooth DAG constraints and practical support selection in causal inference. By isolating the role of exactness versus degeneracy, it clarifies why certain constraint formulas behave differently near boundary points, a nuance relevant to algorithm design for network reconstruction.

## Implications
For practitioners building scalable graph learning models, understanding these response orders helps predict computational costs of cycle completions and informs the choice of regularization strategies. The findings also support more reliable separation between feasibility checks and causal labeling, improving trust in AI-driven inference systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08103v1)
