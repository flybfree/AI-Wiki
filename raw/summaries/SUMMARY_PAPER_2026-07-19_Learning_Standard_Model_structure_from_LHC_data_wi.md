---
title: Learning Standard Model structure from LHC data with Riemannian flow matching
url: http://arxiv.org/abs/2607.16144v1
type: paper-summary
date: 2026-07-19
source_paper: 2026-07-17_17-23-22Z_LearningStandardModelstructurefromLHCdatawithRiema.md
generated_at: 2026-07-19 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents ShellFlow, a transformer‑based generative model that learns to reproduce Standard Model particle structures from LHC data alone. By enforcing only the on‑shell condition and invariant‑mass formula as priors, it generates events across five decades of invariant mass without external training signals. The model recovers intra‑particle kinematics, dilepton resonances, leptonic angle, W and top masses, and inter‑particle correlations.

## Key Takeaways
- ShellFlow uses a Riemannian conditional flow to enforce the on‑shell condition for each particle, allowing generation of full Standard Model structures from raw event data. - The model learns all SM parameters such as dilepton resonance positions, leptonic angle, W and top masses directly from training without additional priors. - Inter‑particle correlations that are not part of any loss function are reproduced, showing the model captures hidden structure.

## Context
This work illustrates how deep generative models can infer complex physical laws from observational data alone, moving beyond supervised learning to unsupervised discovery. It highlights a paradigm where AI acts as a surrogate for theoretical physics, extracting quantitative predictions from limited experimental records.

## Implications
For particle physicists, ShellFlow offers a tool to test SM consistency and explore parameter space without large datasets. For industry, the approach demonstrates scalable AI methods that can be applied to any physical model governed by simple constraints, potentially accelerating discovery in other fields.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.16144v1)
