---
title: Physics-informed distribution of relaxation times estimation and latent-space condition monitoring of solid oxide fuel and electrolysis cells from electrochemical impedance spectroscopy
url: http://arxiv.org/abs/2608.13305v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_14-33-33Z_Physics_informeddistributionofrelaxationtimesestim.md
generated_at: 2026-08-16 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a physics‑informed convolutional autoencoder that directly estimates the distribution of relaxation times from electrochemical impedance spectroscopy data without requiring spectrum‑specific regularisation. The model reconstructs experimental spectra with range‑normalised errors below 1.1% and resolves overlapping relaxation processes in synthetic two‑ZARC measurements. Moreover, the latent representation is organised by relaxation timescales, allowing distances to reflect operating changes, hydrogen‑shortage events, and long‑term degradation.

## Key Takeaways
- The autoencoder learns a direct mapping from EIS spectra to DRT distributions, eliminating the need for separate tuning per relaxation process.  
- Reconstruction errors are consistently under 1.1% across three independent datasets, demonstrating high accuracy without spectrum‑specific constraints.  
- Latent space distances capture both short‑term operational shifts and long‑term degradation signals, providing a unified metric for condition monitoring.

## Context
This work advances physics‑informed neural networks by embedding physical relations directly into the training objective rather than relying on post‑hoc regularisation. It addresses an ill‑posed inverse problem in electrochemistry where traditional methods struggle with overlapping relaxation processes and require extensive manual tuning, highlighting a broader trend toward integrating domain knowledge into deep learning architectures.

## Implications
For fuel and electrolysis cell operators, this lightweight model offers real‑time DRT estimation that can be applied uniformly across different cell types without modification. The interpretable latent space enables early detection of performance degradation, supporting predictive maintenance and extending the operational life of solid oxide systems in renewable energy applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13305v1)
