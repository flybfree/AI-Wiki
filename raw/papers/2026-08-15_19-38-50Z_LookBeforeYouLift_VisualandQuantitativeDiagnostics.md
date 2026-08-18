---
title: Look Before You Lift: Visual and Quantitative Diagnostics for Topological Deep Learning
published: 2026-08-15T19:38:50Z
authors: Mathilde Papillon, Guillermo Bernárdez, Álvaro Ballón Barreiro, Marco Montagna, Rémi Devaux, Antoine Jardin, Nina Miolane
url: http://arxiv.org/abs/2608.15388v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Look Before You Lift: Visual and Quantitative Diagnostics for Topological Deep Learning

## Abstract
Topological deep learning (TDL) methods rely on lifting raw data into higher-order discrete domains such as simplicial complexes, cell complexes, and hypergraphs. In practice, this lifting step is often treated as a black box: practitioners select a lifting and then tune architectures, with limited visibility into whether the induced higher-order connectivity is meaningful for the downstream task. To address this missing diagnostic layer, we propose a visualization technique called TopoExplorer that leverages the strictly augmented Hasse graph form of topological datasets for exploratory data analysis. For the first time, practitioners can easily visualize the incidence- and adjacency-based neighborhoods that define the lifted dataset, as well as read off key graph metrics that describe its structural and feature landscape. Via an extensive set of experiments across many datasets and liftings, we show that several of these metrics correlate with downstream model performance, suggesting they can help inform TDL preprocessing design. Our perspective reframes the TDL workflow from lift-train to lift-look-design-train, enabling more principled, interpretable, and efficient model development. TopoExplorer is hosted at https://topoexplorer.pagekite.me, and its source code is available at github.com/geometric-intelligence/topoexplorer.

## Metadata
- **Published**: 2026-08-15T19:38:50Z
- **Authors**: Mathilde Papillon, Guillermo Bernárdez, Álvaro Ballón Barreiro, Marco Montagna, Rémi Devaux, Antoine Jardin, Nina Miolane
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15388v1)