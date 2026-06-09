---
title: Topological Neural Operators
published: 2026-06-08T17:54:33Z
authors: Lennart Bastian, Samuel Leventhal, Mustafa Hajij, Tolga Birdal
url: http://arxiv.org/abs/2606.09806v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Topological Neural Operators

## Abstract
We introduce Topological Neural Operators (TNOs), a principled framework for operator learning on cell complexes that lifts neural operators (NOs) from functions on points and/or edges to topological domains. TNOs represent data as features defined on cells of varying dimension and model their interactions through Discrete Exterior Calculus, enabling explicit cross-dimensional coupling via gradient-, curl-, and divergence-type operators. The key design principle is to decouple where information flows, as governed by fixed topological operators, from how it is transformed (which is learned), yielding models that respect the geometric support of physical quantities and expose conservation and compatibility structure. We further propose Hierarchical TNOs (HTNOs), which incorporate learned coarse complexes to propagate long-range and topology-dependent information. Our framework subsumes existing NOs as a special case, providing a unified perspective on operator learning across discretizations. Across a range of PDE benchmarks, including irregular-geometry flow problems, TNOs and HTNOs improve accuracy; controlled studies further isolate the benefits of native higher-rank and topological structure. Project page: https://circle-group.github.io/research/TNO

## Metadata
- **Published**: 2026-06-08T17:54:33Z
- **Authors**: Lennart Bastian, Samuel Leventhal, Mustafa Hajij, Tolga Birdal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.09806v1)