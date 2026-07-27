---
title: "Summary: Modular Manifolds"
date: 2025-09-26
type: source-note
tags: [thinking-machines, source-note, optimization, manifolds, training]
source_url: https://thinkingmachines.ai/blog/modular-manifolds/
---

# Summary: Modular Manifolds

**Source**: [Thinking Machines Lab](https://thinkingmachines.ai/blog/modular-manifolds/)

Saved: 2026-07-27 10:58

## Summary
The post explores a geometric way to constrain neural-network weights during training by keeping matrices on submanifolds. The goal is to co-design optimizer behavior with those constraints so training becomes more stable and predictable.

## Key Takeaways
- The post frames weight normalization as a design tool, not just a numeric fix.
- It introduces a manifold version of Muon and a broader idea of modular manifolds.
- The core benefit is better control over tensor scale, conditioning, and optimization behavior.

## Context
Large-scale training gets brittle when weights, activations, or gradients drift to extreme values.
Manifold constraints are one way to make the geometry of training more explicit and easier to manage.

## Implications
This is useful if you care about training stability, predictable optimization, and possible robustness guarantees.
It also fits Thinking Machines' broader theme of making model behavior more legible and engineerable.
