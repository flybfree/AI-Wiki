---
title: Particle-Based Conformal Prediction for Contact-Aware Uncertainty Calibration in Stratified Configuration Spaces
published: 2026-08-10T06:22:10Z
authors: Luís Marques, Kristian Popov, Dmitry Berenson
url: http://arxiv.org/abs/2608.09166v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Particle-Based Conformal Prediction for Contact-Aware Uncertainty Calibration in Stratified Configuration Spaces

## Abstract
Reliable uncertainty representation is essential for deploying autonomous systems that interact with their environment, as robots must reason about how uncertainty arising from both stochasticity and model mismatch is impacted by contacts with obstacles (e.g., when navigating through a cluttered environment or inserting a part into an assembly). We propose Calibrated Particle-sets for Trans-dimensional Uncertainty Representation (CaPTURe), a geometry-aware, conformal prediction-based algorithm that generates probabilistically valid prediction regions of the unknown future system configuration using particle-based models of arbitrary fidelity. While calibrated uncertainty predictions are essential for safe and efficient planning, analytical or learned motion models are often inaccurate - due to limited data, simplifying assumptions, unmodeled effects, etc. - which can lead to unsafe executions or task failure. Additionally, when a robot contacts an obstacle, the distribution of its future configurations can become multimodal or disjoint, or lie along manifolds of lower intrinsic dimension than the space of possible robot configurations. Our method uses a calibration dataset of system transitions to locally calibrate motion uncertainty estimates, constructing regions guaranteed to contain the future robot configuration at a user-set probability. Our calibration procedure captures how motion uncertainty varies between contact-rich and contactless motions, leading to sufficient coverage in both cases. We evaluate our method on two simulated planning tasks: controlling a marble around a labyrinth and performing tight-tolerance peg-in-hole insertion with a manipulator. Compared to relevant baselines, CaPTURe achieves the user-specified coverage requirement both in and out of contact and achieves up to a 30% absolute improvement in task success rate over the best baseline.

## Metadata
- **Published**: 2026-08-10T06:22:10Z
- **Authors**: Luís Marques, Kristian Popov, Dmitry Berenson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09166v1)