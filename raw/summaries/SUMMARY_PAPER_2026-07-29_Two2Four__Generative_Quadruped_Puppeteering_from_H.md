---
title: Two2Four: Generative Quadruped Puppeteering from Human Motion
url: http://arxiv.org/abs/2607.26108v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_13-23-10Z_Two2Four_GenerativeQuadrupedPuppeteeringfromHumanM.md
generated_at: 2026-07-29 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a two‑stage generative diffusion model that converts ordinary human motion data into realistic quadruped locomotion without requiring animal performers or complex retargeting setups. The framework supports diverse actions such as walking, running, jumping, sitting and lying while allowing fine‑grained control of head movement and individual limb puppeteering. Experiments show higher realism and controllability than existing methods.

## Key Takeaways
- The model generates quadruped motion directly from human data using a diffusion architecture rather than relying on motion capture or manual retargeting.
- It employs structured conditioning and inpainting to handle multiple actions, including walking, running, jumping, sitting, and lying.
- Fine‑grained intuitive control is possible for head movement and individual limb puppeteering.

## Context
Generative models are increasingly used to create realistic synthetic data for robotics and virtual production. This work demonstrates how diffusion techniques can be applied to motion synthesis, bridging the gap between human intent and animal locomotion.

## Implications
The approach reduces reliance on expensive animal performers and complex rigs, making high‑quality quadruped animation more accessible. Practitioners in film, gaming, and robotics can integrate this model into pipelines for realistic virtual animals with controllable behavior. This integration streamlines workflows and enables real‑time adjustments for dynamic scenes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26108v1)
