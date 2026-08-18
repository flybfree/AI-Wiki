---
title: CG-GLORE: A Conjugate Gradient-Based Global-Local Regularization Network for Sparse-View CT Reconstruction
url: http://arxiv.org/abs/2608.15246v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_14-08-44Z_CG_GLORE_AConjugateGradient_BasedGlobal_LocalRegul.md
generated_at: 2026-08-17 21:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CG-GLORE, a deep reconstruction framework that uses conjugate gradient unrolling to solve the ill‑posed sparse‑view CT problem while preserving physics‑based curvature. It combines a Global‑Local Regularization Network that captures anatomical details through convolutional local features and long‑range dependencies via patchified attention. Experiments on AAPM and DeepLesion demonstrate improved quantitative metrics, lower noise power, and better visual quality compared with existing methods.

## Key Takeaways
- CG-GLORE replaces first‑order updates with a second‑order inspired conjugate gradient approach that solves structured Hessian surrogates for the data term while approximating regularization with identity.  
- The GLORE module employs sparse patchification and Nyström attention to model long‑range anatomical dependencies, enabling non‑local feature capture without exploding complexity.  
- Quantitative results show lower noise power and improved visual fidelity across multiple sparse‑view and noise conditions.

## Context
This work advances AI‑driven medical imaging by integrating second‑order optimization principles into deep learning pipelines, moving beyond first‑order gradient methods that often fail in ill‑conditioned inverse problems. By preserving the curvature of the data fidelity term through structured Hessian surrogates, CG-GLORE offers a more stable and accurate reconstruction framework.

## Implications
The convergence stability and reduced noise of CG‑GLORE translate into clinically viable reconstructions that can be deployed in real‑time scanners with limited projection views. Practitioners benefit from a method that maintains high fidelity without requiring massive regularization networks, lowering computational overhead and enabling broader adoption in resource‑constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15246v1)
