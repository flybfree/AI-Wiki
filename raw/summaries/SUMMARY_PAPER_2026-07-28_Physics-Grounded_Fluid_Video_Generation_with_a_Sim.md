---
title: Physics-Grounded Fluid Video Generation with a Simulation Dataset and Dual-Stream Optical-Flow Supervision
url: http://arxiv.org/abs/2607.25321v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_06-13-18Z_Physics_GroundedFluidVideoGenerationwithaSimulatio.md
generated_at: 2026-07-28 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses physics violations in video diffusion models for fluid scenes by introducing a simulation dataset and a dual-stream architecture that incorporates optical flow supervision. The method improves both physical commonsense scores and visual quality compared to prior approaches. Human evaluation shows preference over competitors.

## Key Takeaways
- The authors create a large physics-simulation fluid dataset of 1,638 MPM videos combined with real stock footage, enabling training on genuine motion dynamics rather than appearance alone.
- A lightweight optical-flow decoder branch is fused into the diffusion model’s RGB stream using zero‑initialized convolutions, allowing only decoders to be updated while the encoder remains frozen.
- The approach raises VideoPhy‑2 Physical‑Commonsense scores by up to 8.75 points and Video‑Quality scores by 4.65 points on test sets, outperforming open competitors.

## Context
Current video diffusion models excel at generating realistic images but often produce physically implausible fluid behavior because they lack explicit motion supervision. This work bridges the gap by integrating simulation data with optical flow constraints to teach coherent dynamics.

## Implications
For industry practitioners, this method offers a practical way to embed physics into generative pipelines without retraining massive encoders. It could be adopted in content creation tools that require realistic fluid effects, such as game asset generation or virtual production.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25321v1)
