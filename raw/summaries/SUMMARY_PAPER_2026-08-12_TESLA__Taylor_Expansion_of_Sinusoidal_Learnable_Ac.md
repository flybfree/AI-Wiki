---
title: TESLA: Taylor Expansion of Sinusoidal Learnable Activations
url: http://arxiv.org/abs/2608.11970v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_11-57-23Z_TESLA_TaylorExpansionofSinusoidalLearnableActivati.md
generated_at: 2026-08-12 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TESLA, a learnable activation based on sine and cosine terms that can control polynomial degree and selectively amplify high-order components, achieving strong performance on the parity problem despite linear inseparability. It provides theoretical bounds showing Lipschitz and Rademacher complexity constraints when coefficients are constrained, and empirical results show robust generalization with 100K samples and tolerance to 30% label noise.

## Key Takeaways
- TESLA's activation uses a learnable combination of sine and cosine terms that can be tuned to emphasize higher-frequency structure while controlling the effective polynomial degree.
- Theoretical analysis shows that constraining coefficients yields Lipschitz and Rademacher complexity bounds, shaping training dynamics toward higher-order components.
- Empirically, TESLA achieves high accuracy on parity with 100K samples (≈0.002% of input space) and remains robust under up to 30% label noise.

## Context
The parity problem exemplifies the difficulty of separating linear patterns in deep networks due to global interactions, highlighting a need for activation functions that can model higher-order structure without sacrificing expressivity. This work demonstrates that activation-level degree control can improve generalization beyond simple periodic or Fourier-based baselines.

## Implications
By enabling explicit control over polynomial degree at the activation level, TESLA offers a pathway to design networks that are both expressive and well-behaved under noise, potentially leading to more stable training and better robustness in vision tasks like ImageNet-100. The approach may inspire future research into adaptive activations for complex, non-linear problems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11970v1)
