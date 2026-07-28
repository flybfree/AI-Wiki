---
title: Controllable Diversity in Normalization-Based Implicit Ensembles via Softmax-Temperature Modulation
url: http://arxiv.org/abs/2607.23860v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_22-06-42Z_ControllableDiversityinNormalization_BasedImplicit.md
generated_at: 2026-07-27 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces σN‑Ens, a normalisation‑based implicit ensemble that treats each member as a task in a multi‑task architecture and modulates the shared backbone with sigmoid‑bounded scalers. It also adds a softmax‑temperature regulariser to shape sharing between members and trace accuracy‑calibration trade‑offs. Experiments on ResNet and transformer models show σN‑Ens matches or exceeds deep ensembles while using far fewer parameters, scales without collapse, and retains calibration under input corruption.

## Key Takeaways
- The ensemble quantifies uncertainty as modulation uncertainty by varying sigmoid‑bounded scalers across members.
- A softmax‑temperature term balances sharing between members, linking it to the accuracy‑calibration frontier observed in training.
- σN‑Ens achieves deep‑ensemble performance at a fraction of the parameter cost and scales with ensemble size without collapsing.

## Context
Implicit ensembles aim to reduce the linear cost of full deep ensembles by sharing a single backbone across many task‑like members. This work advances that goal by providing a principled way to control diversity during training, which is otherwise fixed or architectural. The integration of normalisation layers makes the method compatible with both convolutional and transformer architectures.

## Implications
For practitioners, σN‑Ens offers a lightweight alternative for reliable uncertainty estimates without sacrificing performance, enabling deployment on resource‑constrained devices. In industry, it supports faster prototyping and more robust model calibration across distribution shifts, fostering trustworthy AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23860v1)
