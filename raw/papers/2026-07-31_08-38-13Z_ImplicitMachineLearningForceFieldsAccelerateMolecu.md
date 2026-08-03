---
title: Implicit Machine Learning Force Fields Accelerate Molecular Dynamics Simulations
published: 2026-07-31T08:38:13Z
authors: Johannes Maeß, Leon Werner, J. Thorben Frank, Winfried Ripken, Martin Michajlow, Joshua Futterer, Klaus-Robert Müller, Stefan Chmiela
url: http://arxiv.org/abs/2607.29158v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Implicit Machine Learning Force Fields Accelerate Molecular Dynamics Simulations

## Abstract
We introduce implicit machine learning force fields (I-MLFFs), which replace explicit stacks of neural network layers with self-consistent fixed-point equations. In molecular simulations, this formulation enables intermediate representations to be reused across successive timesteps, thereby warm-starting force evaluation. The resulting models effectively combine the computational footprint of a shallow, single-layer MLFF with the representational capacity and accuracy of a deep neural network. Our approach unlocks architecture-agnostic efficiency gains that are inaccessible when force prediction and trajectory integration are considered separately. We demonstrate this across three major classes of graph neural networks: invariant, equivariant Cartesian tensor, and SO(3)-equivariant spherical-tensor architectures. Each yields a two- to five-fold reduction in compute and memory footprint. Crucially, these gains are achieved while retaining full atomistic resolution and the original integration timestep, avoiding spatial or temporal coarse graining. Our contribution therefore advances the scaling frontier of quantum-mechanically faithful molecular simulation, enabling longer trajectories and larger atomistic systems within fixed GPU memory and compute budgets, and thereby opening access to new insights across biomolecular and material systems.

## Metadata
- **Published**: 2026-07-31T08:38:13Z
- **Authors**: Johannes Maeß, Leon Werner, J. Thorben Frank, Winfried Ripken, Martin Michajlow, Joshua Futterer, Klaus-Robert Müller, Stefan Chmiela
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29158v1)