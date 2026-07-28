---
title: Physics-Informed Neural Networks for Discovering Periodic Orbits in the Gravitational Three-Body Problem
url: http://arxiv.org/abs/2607.23501v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_07-07-29Z_Physics_InformedNeuralNetworksforDiscoveringPeriod.md
generated_at: 2026-07-27 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a method using physics-informed neural networks to discover periodic orbits in the gravitational three-body problem without relying on initial conditions or gradient searches. Trained on sparse noisy observations, the network can recover orbit families that were not present in the training data. Experiments show convergence to genuine periodic solutions such as the figure-eight and Broucke-Hadjidemetriou-Hénon orbits.

## Key Takeaways
- The method recovers periodic orbits from data alone, demonstrating that PINNs can find solution families absent from the dataset.
- Changing the source of training data significantly alters which orbit families emerge, indicating a strong influence of data distribution rather than random seed.
- Despite slower performance on well‑posed initial‑value problems compared to conventional integrators, the recovered orbits are verified as true periodic solutions.

## Context
This work extends PINNs from static function approximation to dynamical system exploration, showing that neural networks can be guided by physics constraints to solve inverse problems in celestial mechanics. It highlights a new application area where data‑driven models complement traditional numerical methods.

## Implications
For researchers, the approach offers a flexible tool for discovering hidden periodic motions without exhaustive parameter sweeps. Practitioners could use it to generate candidate orbits for satellite design or spacecraft rendezvous planning where precise periodicity is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23501v1)
