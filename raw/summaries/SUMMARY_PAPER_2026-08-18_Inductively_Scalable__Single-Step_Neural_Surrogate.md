---
title: Inductively Scalable, Single-Step Neural Surrogates for Wave-Scattering Inverse Problems
url: http://arxiv.org/abs/2608.17344v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_04-07-53Z_InductivelyScalable_Single_StepNeuralSurrogatesfor.md
generated_at: 2026-08-18 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a method to train neural network surrogates that can handle up to 41,772 controllable variables in two‑dimensional wave scattering and later scale inductively to over three million variables without retraining. By generating training examples where the surrogate disagrees with a full‑wave simulator, using gradient ascent on refractive index and source configurations, and normalizing with an evolving replay dataset, they achieve high accuracy and massive speedups compared to FDTD. The approach enables fast forward simulation and inverse design of complex structures such as beam splitters and GRIN lenses.

## Key Takeaways
- The surrogate is trained using gradient ascent on cases where it disagrees with a full‑wave simulator, allowing it to learn configurations that improve its performance.
- It normalizes both source and ground‑truth data with an evolving replay dataset, which stabilizes learning across diverse examples.
- The model can be inductively scaled to more than 3 million controllable variables, delivering speedups up to 26.5 times faster than FDTD.

## Context
Neural network surrogates aim to replace computationally expensive physics‑based simulators with fast inference models for inverse problems in optics and acoustics. This work addresses the scalability limit of single‑step networks by dynamically generating training data, a technique that could be applied beyond wave scattering into other domains requiring high‑dimensional control.

## Implications
For photonics design engineers, this method means rapid prototyping of complex optical components without waiting for simulation cycles, accelerating R&D pipelines. The ability to handle millions of variables opens possibilities for adaptive metamaterials and real‑time inverse optimization in large systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17344v1)
