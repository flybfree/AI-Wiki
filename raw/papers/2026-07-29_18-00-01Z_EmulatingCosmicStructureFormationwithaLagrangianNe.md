---
title: Emulating Cosmic Structure Formation with a Lagrangian Neural Cellular Automaton
published: 2026-07-29T18:00:01Z
authors: Cooper Jacobus, Beatriz Tucci, Oliver Philcox
url: http://arxiv.org/abs/2607.27320v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Emulating Cosmic Structure Formation with a Lagrangian Neural Cellular Automaton

## Abstract
Field-level inference of cosmological initial conditions from galaxy surveys requires a forward model that is simultaneously accurate in the non-linear regime, computationally efficient, and fully differentiable. Traditional N-body simulations are accurate but computationally prohibitive for iterative inference, while approximate solvers like Lagrangian Perturbation Theory (LPT) fail to capture the knotty halo-forming dynamics of the cosmic web at late times. We introduce the \textit{Lagrangian Neural Cellular Automaton} (LNCA), a hybrid deep learning framework that can be applied to emulate structure formation as a local, iterative dynamical process on a comoving lattice. Unlike standard Eulerian Convolutional Neural Networks (CNNs) which map fixed density fields, the LNCA operates in the Lagrangian frame, advecting the computational graph itself to follow the flow of mass. By training the network to learn only the \textit{residual} displacement corrections to the Zeldovich approximation, we achieve high-fidelity emulation of the non-linear physics while guaranteeing accuracy at large scales. We further constrain our model to produce complete trajectories, not just final states, by adopting an equivariant cellular automaton architecture, which recurrently iterates on its internal states to yield a dynamic history. The resulting model is strictly local, translationally and rotationally equivariant, and naturally supports continuous time integration, making it a reliable differentiable forward model for reconstructing the initial conditions of the universe from lightcone data. Our trained model supports percent-level precision in the power and cross spectra well into the non-linear regime ($k \lesssim 0.5 \, h \text{Mpc}^{-1}$), while requiring $\sim10^4$ times fewer learned parameters than comparable models which take the form of an interpretable internal dynamic rule set.

## Metadata
- **Published**: 2026-07-29T18:00:01Z
- **Authors**: Cooper Jacobus, Beatriz Tucci, Oliver Philcox
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27320v1)