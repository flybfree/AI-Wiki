---
title: BRiG-AFA: Bellman Risk-to-Go Learning for Non-Myopic Active Feature Acquisition
url: http://arxiv.org/abs/2608.02305v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_14-30-44Z_BRiG_AFA_BellmanRisk_to_GoLearningforNon_MyopicAct.md
generated_at: 2026-08-03 23:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BRiG‑AFA, a supervised method for active feature acquisition that learns candidate‑conditioned risk‑to‑go functions using Bellman targets. It improves classification accuracy over greedy baselines on non‑myopic benchmarks, especially at budgets two and three. The approach leverages a Bellman target that propagates risk from the terminal classification to earlier acquisition decisions, enabling myopic‑free learning.

## Key Takeaways
- At budget two the method gains 4.84±2.17 points versus one‑step ablation.
- At budget four it gains 10.20±0.74 points on Fashion‑MNIST with twenty candidate pixels.
- The mean paired gain across budgets {2,4,8,12,16} is 3.50±0.37 points.

## Context
Active feature acquisition seeks to select informative measurements that boost downstream classification performance while respecting a limited measurement budget. This work provides a principled Bellman‑based framework that avoids the optimization challenges of reinforcement learning or generative models.

## Implications
Practitioners can adopt BRiG‑AFA to guide sensor placement or camera focus without retraining the entire model, preserving inference speed and reducing compute cost. The method offers a deployable, supervised alternative that can be integrated into real‑time pipelines in resource‑constrained settings such as mobile vision systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02305v1)
