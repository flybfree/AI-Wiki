---
title: SCOPE: Entanglement Frontier Escape for Source-Free Class Unlearning
url: http://arxiv.org/abs/2608.02058v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_10-56-46Z_SCOPE_EntanglementFrontierEscapeforSource_FreeClas.md
generated_at: 2026-08-03 23:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SCOPE, a source‑free class unlearning method that erases entire classes by conditioning the erasure on input features rather than using a fixed projection. It proves that any fixed projection incurs a retain cost at least equal to the readout energy along the forget discriminant subspace and that this lower bound is tight. The proposed approach achieves this bound with a single gate, no training, and minimal computational cost.

## Key Takeaways
- SCOPE conditions erasure on input scores of the frozen head’s weight scores for the forget class, thereby suppressing only the forget subspace without affecting retained classes.
- It attains the theoretical lower bound on retain‑readout energy for any fixed projection, showing that no better performance is possible with a single projection.
- The method requires no retain data, gradient training, or additional parameters, delivering orders of magnitude less cost than retraining.

## Context
Source‑free class unlearning remains an open challenge in representation learning because existing erasers rely on fixed projections that cannot simultaneously erase and retain overlapping classes. This limitation hampers applications where memory efficiency is crucial across diverse datasets and model architectures.

## Implications
SCOPE provides a scalable, zero‑gradient solution for large‑scale systems where frequent forgetting is needed, potentially reducing training time and hardware costs. Practitioners can integrate it into existing pipelines without retraining, offering a practical path toward more efficient AI models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02058v1)
