---
title: On a joint simultaneous learning of relevant feature subsets and subspaces in regression-like problems
published: 2026-07-30T11:51:29Z
authors: Illia Horenko
url: http://arxiv.org/abs/2607.28080v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On a joint simultaneous learning of relevant feature subsets and subspaces in regression-like problems

## Abstract
We extend a recently introduced Entropy-Optimal Manifold Clustering (EOMC) to allow for a joint simultaneous identification of subsets and subspaces of relevant features in nonstationary and nonlinear regression problems. It is shown that the proposed extension - that we coin as Entropy-Optimal Manifold Regression (EOMR) - allows a robust learning with linearly-scaling iteration and memory complexities. EOMR is compared to the most complete set of state-of-the-art tools from the Artificial Intelligence (AI) and Machine Learning (ML) that is available to the author, on the very challenging problems from chaotic and fluid dynamics: (i) on predicting the Lorenz-96 systems dynamics in strongly- and very-strongly chaotic regimes (with forcing parameter being $F=8$ and $F=12$, respectively); and, (ii) on a data from the Hasegawa-Wakatani model on the edge of the tokamak plasma. It is demonstrated that the proposed benchmarks (i) and (ii), indeed, are the very challenging problems for the state of the art ML and AI tools - since both the general-purpose gradient boosted random forests and deep neuronal networks, as well as transformer-based AI tools like TabPFN v.03 (more spezialised for large-dimensional small data learning problems) - result in orders of magnitude inferior root mean squared prediction errors, and orders of magnitude larger model complexities, when compared to the EOMR. For a Hasegawa-Wakatani example, EOMR distills a very simple entropy-optimal and skilful description of the leading Essential Orthogonal Function (EOF) dynamics, given by linear, causal and weakly-stationary autoregressive process described by just 8 parameters.

## Metadata
- **Published**: 2026-07-30T11:51:29Z
- **Authors**: Illia Horenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28080v1)