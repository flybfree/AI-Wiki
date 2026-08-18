---
title: ER-KANs: Efficient and Robust Kolmogorov-Arnold Networks for Data-Scarce Scientific Machine Learning
url: http://arxiv.org/abs/2608.14773v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_16-15-37Z_ER_KANs_EfficientandRobustKolmogorov_ArnoldNetwork.md
generated_at: 2026-08-17 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ER‑KANs, a new type of Kolmogorov‑Arnold Network designed for noisy and scarce scientific data. It demonstrates that ER‑KAN maintains performance comparable to standard MLP while handling moderate noise, unlike other KAN variants that degrade sharply. The authors also propose the noise degradation ratio as a metric.

## Key Takeaways
- ChebyKAN's test MSE rises 10.6x under sigma=0.1 noise compared with clean ground truth, indicating poor robustness.
- Vanilla KAN degrades by 7.9x while ER‑KAN only increases by 1.4x, showing superior performance in noisy settings.
- The proposed ER‑KAN uses shared Gaussian RBF bases, curriculum noise injection, and entropy-weighted adaptive regularisation to achieve a 595‑parameter network that matches MLP accuracy at moderate noise.

## Context
Efficient KANs have traditionally been evaluated on clean data, which masks their true capability differences. This study addresses the gap by benchmarking architectures under realistic noisy conditions in scientific machine learning tasks such as physics‑informed neural networks for harmonic oscillators and Burgers' equation.

## Implications
For researchers and practitioners, ER‑KAN offers a practical alternative to traditional KANs when data are limited or corrupted. The noise degradation ratio provides a clear benchmark that can guide model selection and improve reproducibility in scientific AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14773v1)
