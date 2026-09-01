---
title: Learning the Geometry of Admissible Hypotheses through Inductive Bias in Training Distributions
published: 2026-08-31T16:09:41Z
authors: James Crowley, Faez Ahmed, Anton van Beek
url: http://arxiv.org/abs/2608.31028v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning the Geometry of Admissible Hypotheses through Inductive Bias in Training Distributions

## Abstract
Scientific discovery often requires reasoning over competing hypotheses that are consistent with experimental observations. For mixed-variable and combinatorial hypothesis spaces, however, constructing probabilistic representations remains challenging because both the active model components and their associated parameters are unknown. In this work, we present a framework for learning continuous latent representations of admissible partial differential equations (PDEs) by embedding a scientific inductive bias directly into the training distribution. Progressively richer structural principles (e.g., sparsity, logical dependencies, common PDE families, and physical admissibility) are used to generate a structured distribution of hypotheses from which a gated variational autoencoder learns a continuous latent manifold. Experimental results show that the resulting 11-dimensional representation accurately reconstructs a broad collection of representative PDEs, while exhibiting smooth geometric transitions both within and across equation families. Through an ablation study we further demonstrate that introducing scientific principles reduces both structural misclassifications of equation forms and parameter estimation errors when reconstructing a representative benchmark set of admissible partial differential equations. These results show that embedding a scientific inductive bias in the training distribution enables the learning of compact and geometrically meaningful hypothesis manifolds, providing a principled foundation for future inference over competing governing equations.

## Metadata
- **Published**: 2026-08-31T16:09:41Z
- **Authors**: James Crowley, Faez Ahmed, Anton van Beek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.31028v1)