---
title: A Computational Comparison of Fourier Spectral Differentiation and Spatial Automatic Differentiation in Periodic Physics-Informed Neural Networks
url: http://arxiv.org/abs/2609.02110v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_04-52-26Z_AComputationalComparisonofFourierSpectralDifferent.md
generated_at: 2026-09-02 20:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper compares Fourier spectral differentiation with spatial automatic differentiation in periodic physics‑informed neural networks, holding all other experimental conditions constant. Across five benchmark equations and training frameworks, the Fourier method achieves substantial speedups and memory savings while keeping solution errors comparable to spatial AD.

## Key Takeaways
- Fourier spectral differentiation reduces GPU peak memory usage by up to 94 % compared with spatial automatic differentiation.
- The method yields end‑to‑end training speedups ranging from 2.9× to 18.5×, depending on the equation and framework.
- Both techniques produce L₂ errors of similar magnitude, indicating no consistent accuracy advantage.

## Context
Physics‑informed neural networks rely heavily on automatic differentiation for residual evaluation, which can become computationally expensive in periodic settings where high‑order derivatives are needed. This work addresses that bottleneck by introducing a spectral alternative that leverages the fast Fourier transform.

## Implications
The findings suggest that structured spatial grids enable efficient training of PINNs without sacrificing accuracy, offering practitioners a path to scalable deep learning for complex PDEs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02110v1)
