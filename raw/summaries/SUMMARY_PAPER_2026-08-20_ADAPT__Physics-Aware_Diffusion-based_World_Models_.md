---
title: ADAPT: Physics-Aware Diffusion-based World Models for Adaptive Predictive Transferable HVAC Control
url: http://arxiv.org/abs/2608.19804v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_08-58-28Z_ADAPT_Physics_AwareDiffusion_basedWorldModelsforAd.md
generated_at: 2026-08-20 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ADAPT, a physics‑aware conditional diffusion model that predicts short‑horizon thermal baselines for HVAC control while respecting building inertia and multi‑zone heat balance without explicit geometry or calibrated parameters. Experiments on Simulators show it cuts energy use by 7.3 % and discomfort by 30.2 % versus state‑of‑the‑art, and retains performance under out‑of‑distribution conditions with only marginal degradation.

## Key Takeaways
- ADAPT predicts a short‑horizon held‑action thermal baseline that captures latent building thermal inertia without needing explicit geometry or manually tuned parameters.
- The diffusion backbone generates plausible HVAC trajectories while a learnable multi‑zone heat‑balance regularizer enforces thermodynamic consistency across zones.
- Credit assignment is designed for downstream reinforcement learning, enabling robust transfer to unseen seasons and climate regions with minimal performance loss.

## Context
Generative models are increasingly used to approximate complex physical systems in control applications. However, most HVAC controllers rely on static or limited data, leading to poor generalization when environmental conditions change. ADAPT addresses this gap by integrating physics‑informed diffusion learning, offering a more adaptable alternative to conventional reinforcement approaches.

## Implications
This work demonstrates that AI can improve energy efficiency and occupant comfort while handling real‑world variability without costly sensor networks. Practitioners can adopt the framework to create self‑learning HVAC systems that generalize across climates, reducing operational costs and supporting sustainability goals.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19804v1)
