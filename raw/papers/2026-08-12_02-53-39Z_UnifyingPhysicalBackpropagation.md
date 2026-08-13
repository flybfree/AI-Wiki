---
title: Unifying Physical Backpropagation
published: 2026-08-12T02:53:39Z
authors: Cyrill Bösch, Yigithan Gediz, Hakan Türeci
url: http://arxiv.org/abs/2608.11585v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unifying Physical Backpropagation

## Abstract
Physical computing systems exploit device dynamics for computation, but their gradient-based optimization is challenging: backpropagation through a digital twin suffers from model-reality gap. On-device gradient computation could resolve this issue, and a handful of theoretical and experimental studies have proposed ways to achieve it. Yet a unifying theory identifying when a physical system can compute the gradient of its own performance has been missing. Here we develop such a unification, based on the adjoint method: we identify sufficient conditions under which the adjoint field required for formally exact gradients can be generated on the same hardware that performs the computation. Linear and nonlinear systems obey fundamentally different conditions: for linear systems damping or gain is admissible provided reciprocity is preserved. For nonlinear trajectory systems the sufficient conditions are reciprocity of the linearized system and the existence of a time-reversal mirror. Algorithmically, the nonlinear case requires infinitesimal nudging, whereas linear systems admit a finite-amplitude experiment. We recover Equilibrium Propagation, Hamiltonian echo backpropagation, fully forward mode training and in situ gradient methods in integrated-photonic and free-space-optical systems. We further show that reciprocity is only the simplest instance of a more general intertwining condition, which extends exact on-device gradient computation to a class of non-Hermitian, non-reciprocal systems. Further generalizations include time-dependent parameters, Onsager-reciprocal dynamics and nonlinear, PT-symmetric Schrödinger equations. Our work provides a unified theoretical basis for formally exact physical learning algorithms and a template for constructing them across a range of physical systems.

## Metadata
- **Published**: 2026-08-12T02:53:39Z
- **Authors**: Cyrill Bösch, Yigithan Gediz, Hakan Türeci
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11585v1)