---
title: Finite basis physics-informed neural networks with hard constraints for viscous fluid flow in highly perforated domains
published: 2026-08-08T12:54:16Z
authors: Jeeeun Lee, Denis Korolev, Miro Duhovic, Seong Su Kim
url: http://arxiv.org/abs/2608.08114v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Finite basis physics-informed neural networks with hard constraints for viscous fluid flow in highly perforated domains

## Abstract
In this work, viscous fluid flow governed by the Stokes equations in highly perforated domains is studied using physics-informed neural networks (PINNs). Perforated microstructures induce complex boundary conditions and fine-scale flow features that are difficult for standard neural networks to resolve. Conventional PINNs, even when combined with advanced training techniques, can suffer from a loss of accuracy and efficiency as the number of perforations increases. One important source of this difficulty is the soft enforcement of boundary conditions through penalty terms, which can lead to stiffness, gradient conflicts, and poor resolution of near-boundary flow structures. Hard constraints provide an alternative by encoding boundary conditions exactly into the network ansatz, but may introduce undesirable non-local effects due to the global nature of the approximation. To address these challenges, finite basis PINNs (FBPINNs), which are based on domain decomposition and localisation principles, are used together with hard boundary constraints that efficiently encode perforation-related boundary conditions. This approach helps mitigate spectral bias, improves overall accuracy, and exhibits convergence that is only weakly affected by the number of perforations, thereby providing an efficient and highly parallelisable neural network framework. The proposed approach is further supported with theoretical arguments, specifically focusing on the localisation and approximation properties of FBPINNs.

## Metadata
- **Published**: 2026-08-08T12:54:16Z
- **Authors**: Jeeeun Lee, Denis Korolev, Miro Duhovic, Seong Su Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08114v1)