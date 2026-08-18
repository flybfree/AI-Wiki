---
title: LaGSplat: Inferring Physics-Governed Interactive Simulation from Monocular Video Using Latent Lagrangian Gaussian Splatting
url: http://arxiv.org/abs/2608.16324v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_09-29-12Z_LaGSplat_InferringPhysics_GovernedInteractiveSimul.md
generated_at: 2026-08-17 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
LaGSplat proposes a method that infers interactive, physics‑governed dynamics from one or few monocular videos without any prior force annotations. By encoding object motion in a low‑dimensional latent state that simultaneously serves as generalized coordinates and decoder conditioning, the system can translate an unseen external push into corresponding latent forces that drive Euler‑Lagrange equations.

## Key Takeaways
- The latent state q acts as both the coordinate of a dissipative Lagrangian and the input to a Gaussian Splatting decoder.  
- A force applied in pixel space is mapped back through J(q)ᵀf, allowing the model to predict how the object will respond.  
- This approach limits response to plausible, bounded motions instead of diverging unconstrained predictions.

## Context
The work advances monocular video understanding by integrating physics‑based reasoning with neural rendering techniques such as Gaussian Splatting and NeRFs. It demonstrates that latent variables can serve dual roles, bridging perception and simulation in a single framework.

## Implications
For developers building interactive AR/VR experiences, LaGSplat offers a way to generate realistic object responses without costly sensor data. Practitioners may leverage the method to create adaptive simulations where user inputs are naturally reflected by learned physics constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16324v1)
