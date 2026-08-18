---
title: Eigenanalysis framework for autoregressive neural emulators of multi-scale chaotic dynamics
published: 2026-08-17T04:30:03Z
authors: Conrad Ainslie, Pedram Hassanzadeh, Michael W. Mahoney, Ashesh Chattopadhyay
url: http://arxiv.org/abs/2608.16084v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Eigenanalysis framework for autoregressive neural emulators of multi-scale chaotic dynamics

## Abstract
Neural autoregressive models have rapidly emerged as powerful emulators of high-dimensional chaotic systems, yet their long-term instability and error growth remain poorly understood, leading to ad-hoc solutions. Here, we develop an eigenanalysis framework that reveals the dynamical origin of this error growth. By analyzing the Jacobian of the learned one-step update map with respect to the state, we show how inference-time error growth, and thus model stability, is governed by its spectral radius. Direct-step architectures (models that predict the next state from the previous one) generically admit unstable eigenvalues with magnitudes exceeding one, explaining the rapid divergence of these widely used models. In contrast, integration-constrained models (where the time derivative is estimated and integrated with a higher-order integrator) collapse their eigenspectrum onto the unit circle, yielding neutral stability and a universal linear error-scaling law. The largest eigenvalue of this Jacobian provides an architecture-agnostic, a priori diagnostic of short-term skill, long-term stability, and spectral bias, without requiring an expensive rollout. Leveraging this theory, we introduce a stability-promoting loss that explicitly regularizes Jacobian-driven error amplification, improving both forecast accuracy and dynamical robustness. Demonstrated across $29$ models spanning two architectures, several explicit and implicit integrators, and multiple loss functions on the Kuramoto-Sivashinsky system, our results establish a theoretical foundation for the design and evaluation of neural emulators of chaotic multi-scale dynamics. More broadly, our framework is a step toward the kind of a priori stability analysis that numerical analysis provides for discretizations of differential equations and that scientific machine learning currently lacks.

## Metadata
- **Published**: 2026-08-17T04:30:03Z
- **Authors**: Conrad Ainslie, Pedram Hassanzadeh, Michael W. Mahoney, Ashesh Chattopadhyay
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16084v1)