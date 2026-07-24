---
title: Generating Bearing Vibration Signals at User-Specified Fault Probabilities Using PR-GAN and Counterfactual Methods
url: http://arxiv.org/abs/2607.19455v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_14-45-57Z_GeneratingBearingVibrationSignalsatUser_SpecifiedF.md
generated_at: 2026-07-23 23:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper tackles the scarcity of intermediate fault‑probability samples in bearing vibration datasets by generating synthetic signals that match target probabilities of 0.25, 0.50 and 0.75. Two methods are compared: a training‑based Probability‑Regularized Generative Adversarial Network (PR‑GAN) and a per‑sample counterfactual (CF) approach. The CF method achieves near‑perfect probability alignment with minimal signal alteration, while PR‑GAN performs less reliably but runs faster.

## Key Takeaways
- CF reaches the target fault probability with a mean absolute error of 0.005–0.008 and a success rate of 1.000 on retained samples, demonstrating high precision in probability generation.
- PR‑GAN’s mean absolute error is larger (0.046–0.059) and its success rates drop between 0.501 and 0.680, indicating less stable probability control despite lower runtime.
- The CF procedure requires only small average L1 changes to the original signal, preserving time‑domain fidelity while achieving accurate probability matching.

## Context
Generating signals with controlled fault probabilities is crucial for training decision‑making models in predictive maintenance, where intermediate probabilities reflect realistic maintenance thresholds. This work addresses a common data imbalance problem by creating synthetic samples that fill the “gray zone,” enabling more robust evaluation of classification boundaries and risk assessment algorithms.

## Implications
Practitioners can rely on CF to produce near‑ideal fault probability signals without extensive retraining, reducing computational overhead while maintaining signal integrity. The findings suggest that targeted counterfactual generation is a practical solution for improving model training in industrial vibration monitoring systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19455v1)
