---
title: Conformal risk control for model-form uncertainty in parametric non-intrusive reduced-order models
url: http://arxiv.org/abs/2608.03360v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_09-08-16Z_Conformalriskcontrolformodel_formuncertaintyinpara.md
generated_at: 2026-08-05 01:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a conformal risk control framework that quantifies model‑form uncertainty in non‑intrusive reduced‑order models (NIROMs) by coupling stochastic perturbations on the discarded basis modes with distribution‑free conformal methods. The approach yields posterior variance estimates that separate basis truncation from regression uncertainty, enabling calibrated prediction sets with coordinate miscoverage guarantees.

## Key Takeaways
- The framework uses random perturbations defined on the Stiefel manifold to model basis‑induced variance while keeping regression variance separate through a transport approximation.
- A closed‑form posterior variance is obtained without retraining Gaussian processes, allowing efficient uncertainty quantification for NIROMs.
- Conformal risk control produces prediction sets with coordinate miscoverage guarantees and provides an interpretable scalar calibration factor that reflects the quality of the uncertainty estimate.

## Context
Non‑intrusive reduced‑order models are widely used to approximate parametric PDEs from experimental data, but their predictive reliability is limited by model‑form uncertainty. Existing methods often rely on Gaussian process assumptions or require costly re‑training, which hampers real‑time applications in engineering and AI.

## Implications
This work offers a practical tool for engineers and researchers who need reliable uncertainty estimates without sacrificing computational efficiency. By delivering calibrated prediction sets, the methodology improves trust in NIROM predictions across both benchmark PDEs and industrial processes like tire calendering.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03360v1)
