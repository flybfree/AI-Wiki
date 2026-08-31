---
title: Conditional Diffusion Models for Energy-Efficient Driving
published: 2026-08-28T10:04:31Z
authors: Hemanth Neelgund Ramesh, André Snoeck, Chyi-Fu Hong, Shijing Sun
url: http://arxiv.org/abs/2608.28142v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conditional Diffusion Models for Energy-Efficient Driving

## Abstract
Electrification of commercial delivery fleets is shifting fleet routing from distance- and time-based optimization toward energy-aware decision-making. Existing sequence models primarily provide deterministic point estimates or limited uncertainty summaries, which do not capture the range of plausible energy-consumption trajectories required for operational decision-making. In this work, we introduce a conditional diffusion framework that generates EV battery-current profiles conditioned on route features such as vehicle velocity and ambient temperature. The model combines a latent conditioning encoder with a temporal 1D U-Net denoising backbone that enables trip-related conditions to be mapped into a shared representation and guides the reverse diffusion process. We evaluate the framework on an open-access commercial EV telemetry dataset containing 12k trips from 9 vehicles. The proposed latent-conditioned diffusion model generates realistic cur- rent trajectories that capture both the dominant temporal envelope and sharp transient events. The model achieves a Wasserstein distance of 0.0029 between generated and measured current distributions below the real vs real reference distance of 0.0085 indicating that generated samples lie within the empirical variability of the test set. We further demonstrate that learned latent conditioning substantially improves performance over direct condition injection, reducing the Wasserstein distance by 89.1% and MAE by 52.8%. This work demonstrates a generative modeling framework for characterizing EV energy consumption under real-world operating conditions, providing an essential foundation for uncertainty-aware fleet planning in large-scale operational settings.

## Metadata
- **Published**: 2026-08-28T10:04:31Z
- **Authors**: Hemanth Neelgund Ramesh, André Snoeck, Chyi-Fu Hong, Shijing Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28142v1)