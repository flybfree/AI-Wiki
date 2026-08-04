---
title: The Condition-Number Barrier in Sparse Least Squares
published: 2026-08-03T17:57:01Z
authors: Honghao Lin, Vahab Mirrokni, David P. Woodruff
url: http://arxiv.org/abs/2608.02588v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Condition-Number Barrier in Sparse Least Squares

## Abstract
In [AS21], Axiotis and Sviridenko conjectured that the linear dependence on the restricted condition number in sparse convex optimization cannot be improved by a polynomial-time algorithm. We establish their conjectured lower bound for least-squares objectives, conditional on the randomized exact-volume Small-Set Expansion Hypothesis in the weighted regular-graph formulation of Raghavendra, Steurer, and Tulsiani [RST12]. Concretely, for every fixed $γ\in(0,1]$, there is no randomized polynomial-time algorithm that, with probability at least $2/3$, returns a vector $x$ such that, writing $s=\lVert x\rVert_0$, \[   \lVert Ax-b\rVert_2^2   \leq   \min_{\lVert z\rVert_0\leq k}\lVert Az-b\rVert_2^2+\varepsilon   \quad\text{and}\quad   s=O\!\left(k\,κ_{s+k}^{\,1-γ}\right), \] where $κ_r$ is the restricted condition number at sparsity level $r$. The result holds even on rational instances with $A$ of full column rank.   The proof was first obtained using a fully automated Gemini-based agentic system developed internally at Google. The authors have verified the proof and edited it for clarity of presentation.

## Metadata
- **Published**: 2026-08-03T17:57:01Z
- **Authors**: Honghao Lin, Vahab Mirrokni, David P. Woodruff
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02588v1)