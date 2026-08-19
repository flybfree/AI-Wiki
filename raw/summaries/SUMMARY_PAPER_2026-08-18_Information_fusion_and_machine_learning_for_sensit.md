---
title: Information fusion and machine learning for sensitivity analysis using physics knowledge and experimental data
url: http://arxiv.org/abs/2608.17248v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_01-07-59Z_Informationfusionandmachinelearningforsensitivitya.md
generated_at: 2026-08-18 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of estimating system sensitivity when both a physics‑based model and experimental observations are available, using global sensitivity analysis (GSA). It proposes physics‑informed machine learning strategies that fuse deep neural networks (DNN) and Gaussian processes (GP) with simulation data or loss functions to improve the accuracy of sensitivity estimates. The study finds that DNN‑based approaches yield tighter bounds on sensitivity than GP models.

## Key Takeaways
- Incorporating physics constraints into ML loss functions steers model outputs toward physically plausible regions, enhancing reliability.
- Pre‑training an ML model with simulation data and then fine‑tuning it using experimental measurements reduces uncertainty in the final sensitivity estimate.
- Deep neural networks provide smaller sensitivity bounds compared to Gaussian processes when global sensitivity analysis is performed.

## Context
Fusing heterogeneous sources of information—experimental data and theoretical physics—is a central challenge for AI‑driven engineering. Physics‑informed learning helps mitigate overfitting by constraining model behavior, making it more robust in high‑dimensional settings where traditional ML may fail. This work exemplifies how machine learning can be guided by domain knowledge to produce reliable quantitative insights.

## Implications
Accurate sensitivity analysis is crucial for designing safe and efficient systems such as additive manufacturing processes and environmental monitoring of lake temperatures. By delivering tighter bounds on uncertainty, the proposed methods enable engineers to make informed decisions with reduced risk of failure or costly rework.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17248v1)
