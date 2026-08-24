---
title: Neural-Primitive: An Efficient End-to-end Local Planner with Primitive-based Imitation Learning for Autonomous Flight
url: http://arxiv.org/abs/2608.20948v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_10-13-44Z_Neural_Primitive_AnEfficientEnd_to_endLocalPlanner.md
generated_at: 2026-08-23 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Neural‑Primitive, an end‑to‑end local planner that combines primitive‑based imitation learning with a compact neural network to generate safe, collision‑free trajectories in unknown cluttered environments. The method achieves ultra‑fast computation (under 1 ms on a desktop and about 3.7 ms during flight) while using less than 1.5 MiB of memory, outperforming traditional planners in both latency and trajectory quality.

## Key Takeaways
- A lightweight offline primitive collection framework creates safe, high‑quality trajectory primitives that work well even in non‑convex settings.
- The compact neural network maps raw sensory inputs directly to polynomial coefficients, which naturally encode higher‑order dynamical information without extra processing.
- The planner runs at sub‑millisecond speed on standard hardware and consumes minimal memory, enabling zero‑shot deployment from simulation to real flight.

## Context
Autonomous flight in cluttered environments is constrained by the computation‑quality‑memory trilemma, a challenge that has driven research toward efficient perception‑action loops. Neural‑Primitive addresses this trilemma by integrating primitive‑based learning with a fast neural mapper, aligning with recent advances in model‑based planning and low‑resource imitation learning.

## Implications
For industry, the approach reduces reliance on heavy onboard compute, lowering hardware costs and power consumption for autonomous aircraft. For practitioners, it provides a template for building efficient, real‑time planners that can be trained offline and deployed without extensive simulation fidelity matching, fostering broader adoption of safe, scalable autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20948v1)
