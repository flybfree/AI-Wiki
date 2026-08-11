---
title: Classical $\mathrm{SU}(2)$ Models Match or Exceed Shallow Variational Quantum Circuits on Vision Benchmarks
url: http://arxiv.org/abs/2608.07822v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-07_23-50-09Z_Classical__mathrm_SU__2__ModelsMatchorExceedShallo.md
generated_at: 2026-08-11 13:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether quaternion‑valued neural networks and shallow variational quantum circuits can perform as well or better than each other on classic vision benchmarks such as MNIST, FashionMNIST, and CIFAR-10. Experiments show that quaternion classifiers match or exceed real‑valued MLPs while deeper VQCs underperform, especially when pretrained CNN features are used.

## Key Takeaways
- Quaternion networks retain 94–97% of the accuracy achieved by real‑valued models on CIFAR-10 and provide stable performance even after a 32‑fold increase in bottleneck dimensionality.  
- Product‑state VQCs show lower classification accuracy than quaternion classifiers and suffer from higher computational cost, while entanglement only yields modest grayscale gains that disappear with pretrained features.  
- The Friedman test on MNIST detects significant differences between models (χ²=12.796, p=0.0051) indicating that shallow quantum circuits cannot reliably outperform quaternion alternatives.

## Context
The study addresses a longstanding question in classical machine learning: whether the geometric structure of SU(2) can be leveraged to build efficient quantum‑inspired models without requiring deep entanglement or large circuits. By comparing architectures on standard datasets, it highlights limitations of shallow VQCs when faced with realistic feature representations.

## Implications
For practitioners developing hybrid classical‑quantum systems, quaternion networks offer a practical alternative that avoids the pitfalls of shallow entanglement and measurement noise. This suggests that quantum advantage may be limited to tasks with intrinsic quantum structure rather than general vision problems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07822v1)
