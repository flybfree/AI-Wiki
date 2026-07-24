---
title: The Quadrilateral Loss: Additivity as a Measurable Behavior of Dense Neural Networks
url: http://arxiv.org/abs/2607.20201v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_14-23-37Z_TheQuadrilateralLoss_AdditivityasaMeasurableBehavi.md
generated_at: 2026-07-23 23:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes the quadrilateral loss, a differentiable penalty that quantifies how well a neural network respects additivity by measuring second‑order mixed differences when training points are swapped in one coordinate. It shows that this loss vanishes exactly when a feature carries no interaction and aligns with the per‑coordinate interaction mass from an interventional Shapley‑GAM model, turning additivity into an observable metric that can be optimized online.

## Key Takeaways
- The quadrilateral loss is a second‑order mixed difference on pairs of training points swapping one coordinate, which measures whether feature interactions exist and vanishes only when no interaction is present. 
- It provides a per‑feature surrender curve that reveals how much interaction mass each coordinate contributes before regularization removes it, showing pre‑regularization magnitude does not predict what remains after regularization. 
- The loss can be used to improve both accuracy and additivity on small datasets by applying a moderate penalty, making additivity a dial that is largely removable without affecting structure.

## Context
In deep learning, achieving interpretable models often relies on enforcing additive relationships between features, yet most neural networks learn complex interactions. This work offers a principled way to measure and penalize non‑additive behavior directly from the data, bridging the gap between theoretical additivity constraints and practical model performance.

## Implications
For practitioners seeking transparent AI, the quadrilateral loss provides an online, differentiable objective that can be integrated into training loops without requiring structural masks. It challenges existing methods like weight decay or backfitting by offering a behavioral guarantee that is more sensitive to data regime, potentially guiding better design of regularization strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20201v1)
