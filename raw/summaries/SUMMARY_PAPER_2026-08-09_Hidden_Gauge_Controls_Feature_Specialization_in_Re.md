---
title: Hidden Gauge Controls Feature Specialization in ReLU Networks
url: http://arxiv.org/abs/2608.06766v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_03-39-09Z_HiddenGaugeControlsFeatureSpecializationinReLUNetw.md
generated_at: 2026-08-09 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how a hidden gauge parameter influences specialization of neurons in overparameterized ReLU networks, showing that the choice of gauge determines which neuron becomes the owner of a teacher feature while others become redundant. It demonstrates deterministic selection among duplicate students and proves functional pruning occurs without changes to the initial predictor's parameters.

## Key Takeaways
- The identity of a neuron’s feature ownership is controlled by an invisible positive‑homogeneous scaling gauge, not by the network’s overall architecture.
- Among any fixed number of initially identical neurons, assigning the favorable gauge to one neuron deterministically selects it as the owner and drives the remaining functional contribution to zero.
- A reaction–transport decomposition explains the effect through different mobilities for changing a feature’s coefficient versus its direction.

## Context
This work extends understanding of overparameterized models by revealing that internal specialization can be driven by subtle parameter choices, challenging assumptions about when and where features emerge. It provides a theoretical framework that links gauge invariance to functional pruning in deep networks.

## Implications
For practitioners, the findings suggest that regularization strategies might inadvertently bias feature learning toward certain neurons, potentially limiting model diversity. Researchers should consider gauge‑aware initialization to promote balanced specialization across network units.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06766v1)
