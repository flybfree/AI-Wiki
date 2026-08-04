---
title: AOS: Adaptive Optimizer Switching via Training-State Signals for Faster Convergence and Better Generalization
url: http://arxiv.org/abs/2608.01997v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_09-57-50Z_AOS_AdaptiveOptimizerSwitchingviaTraining_StateSig.md
generated_at: 2026-08-03 23:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AOS-R, a rule‑based controller that selects among AdamW, SGD‑M, and Lion based on six online gradient signals to improve convergence and generalization. On CIFAR‑100/WRN‑28x10 it reaches 78% top‑1 accuracy in 81 epochs, beating each optimizer by a large margin. Across eight benchmarks AOS‑R obtains the best result on six combinations with a mean gain of 0.4 percentage points and an 0.8× speedup over AdamW.

## Key Takeaways
- The controller monitors gradient noise scale, Hutchinson curvature trace, loss stagnation, update stability ratio, gradient stability index, and loss improvement ratio to decide optimizer switches.
- State‑preserving momentum transfer and a 400‑step learning‑rate bridge keep accuracy stable at each transition point.
- AOS‑R reduces training epochs by up to 43% compared with AdamW while improving top‑1 accuracy.

## Context
Deep neural network optimization often requires different strategies for early noisy gradients versus later flat minima, yet most methods use a single optimizer throughout. This mismatch limits both speed and performance across diverse tasks.

## Implications
The results show that lightweight adaptive switching can deliver substantial gains without sacrificing hyperparameter simplicity, encouraging practitioners to adopt rule‑based controllers in production pipelines where efficiency matters more than marginal accuracy improvements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01997v1)
