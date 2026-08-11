---
title: Predicting blood clot growth from sparse post-onset measurements with latent neural differential equations
url: http://arxiv.org/abs/2608.08165v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_14-47-28Z_Predictingbloodclotgrowthfromsparsepost_onsetmeasu.md
generated_at: 2026-08-10 22:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a latent neural differential equation framework that infers missing biochemical parameters from few early clot measurements and predicts future growth of blood clots. Using a multiphysics model with four known inputs and sparse observations, the authors show that stochastic neural ordinary differential equations (SNODE) best recover the unknown tissue-factor parameter while also forecasting trajectories.

## Key Takeaways
- SNODE outperforms seven alternative probabilistic methods in both inferring the missing input and predicting clot growth. 
- The model’s accuracy improves with more sparse measurements but deteriorates when forecasts are made far into the future. 
- SNFDE, a stochastic neural functional differential equation approach, provides comparable performance to SNODE.

## Context
This work advances AI‑driven medical modeling by integrating uncertainty quantification with parameter inference from limited clinical data. It demonstrates how latent representations can bridge gaps in sparse biomedical measurements, a challenge that limits personalized thrombosis prediction.

## Implications
Clinicians could use the framework to tailor clot growth forecasts without invasive monitoring, reducing reliance on dense datasets. The method also offers a template for other rare‑parameter estimation tasks where differential equations model complex physiological processes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08165v1)
