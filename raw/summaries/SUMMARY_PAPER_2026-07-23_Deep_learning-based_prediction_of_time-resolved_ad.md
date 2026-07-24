---
title: Deep learning-based prediction of time-resolved adhesive forces in viscoelastic Hertzian contacts
url: http://arxiv.org/abs/2607.19060v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_12-48-48Z_Deeplearning_basedpredictionoftime_resolvedadhesiv.md
generated_at: 2026-07-23 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This study introduces a deep learning model that predicts the full time‑resolved adhesive force trajectory of soft viscoelastic Hertzian contacts from a prescribed displacement history, eliminating the need for computationally expensive simulations. The best model, an LSTM architecture with concatenated conditioning, achieves a mean‑squared error of 5.0×10⁻⁴ and median pull‑off‑force errors within a few percent while requiring only 0.16 s inference time.

## Key Takeaways
- The model handles loading and unloading rates spanning four orders of magnitude by using a fixed‑measurement‑step representation that preserves physical time information.
- The LSTM with concatenated conditioning yields the lowest error metrics among tested architectures, demonstrating strong generalization across heterogeneous Tabor parameters (0.2–3.2).
- Inference is fast enough for real‑time control loops, making it suitable as a surrogate for repeated numerical evaluations.

## Context
The integration of neural networks into soft robotics and manipulation tasks aims to replace slow simulation pipelines with lightweight, data‑driven surrogates that can be updated online. This work exemplifies how sequence‑to‑sequence models can capture complex temporal dependencies in physical systems, offering a bridge between experimental data and real‑time decision making.

## Implications
For industry practitioners, the model reduces design iteration time by providing instant predictions of contact forces, enabling adaptive gripping strategies without recalibrating simulations each time. The approach also supports rapid prototyping of soft robotic grippers where safety and performance must be ensured in real time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19060v1)
