---
title: Representational separation between unitary and channel quantum generative models via shared classical randomness at shallow depth
url: http://arxiv.org/abs/2608.05110v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_17-44-36Z_Representationalseparationbetweenunitaryandchannel.md
generated_at: 2026-08-05 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether stochasticity introduced into shallow unitary quantum circuits can create a representational gap from purely unitary models. It demonstrates that shared classical randomness enables a channel model to generate long‑range correlations unattainable by bounded‑connectivity unitary circuits, and that this separation holds for arbitrarily large systems.

## Key Takeaways
- Shared classical randomness, derived from measurement outcomes, is sufficient to produce output distributions that no shallow unitary model with limited connectivity can replicate. 
- The channel model’s depth remains constant while the classical random bit controls spatially separated Pauli operations, creating correlations that require linear depth in unitary models. 
- For one‑dimensional nearest‑neighbour architectures, reproducing such long‑range patterns would need Ω(N) depth, showing a strict scalability advantage.

## Context
Quantum generative modeling aims to approximate probability distributions using quantum circuits, but hardware constraints limit circuit depth and connectivity. Understanding which resources—such as entanglement or classical randomness—can overcome these limits is crucial for designing scalable algorithms.

## Implications
The results suggest that modest amounts of classical randomness can dramatically improve the expressiveness of shallow quantum models without increasing physical depth, offering a practical path to more efficient generative circuits. Practitioners may integrate measurement‑based randomness into hardware pipelines to unlock previously inaccessible output spaces.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05110v1)
