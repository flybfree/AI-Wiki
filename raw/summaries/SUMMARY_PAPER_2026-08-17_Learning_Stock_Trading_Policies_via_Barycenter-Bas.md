---
title: Learning Stock Trading Policies via Barycenter-Based Adversarial Inverse Reinforcement Learning
url: http://arxiv.org/abs/2608.15770v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_14-45-28Z_LearningStockTradingPoliciesviaBarycenter_BasedAdv.md
generated_at: 2026-08-17 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BRaG, a barycenter-based adversarial inverse reinforcement learning method for stock trading that learns from multiple heterogeneous expert strategies. It aggregates demonstrations into a stable pseudo‑expert representation and pretrains a policy via imitation learning before fine‑tuning with true market rewards. The approach also uses control barrier functions to enforce risk constraints such as drawdown limits, resulting in stronger performance than classical rules or recent deep RL methods across four global equity markets.

## Key Takeaways
- BRaG aggregates diverse expert trading demonstrations using a performance‑weighted Wasserstein barycenter to create a stable pseudo‑expert that captures common patterns.  
- The method pretrains a trading policy through adversarial imitation learning, reducing exploration instability before fine‑tuning with real market rewards.  
- Control barrier functions are integrated to enforce risk constraints like drawdown limits, ensuring the learned policy remains within safe boundaries.

## Context
Inverse reinforcement learning seeks to infer policies from observed behavior without explicit reward signals, which is especially valuable in finance where rewards are delayed and noisy. This work advances that field by providing a scalable aggregation technique for heterogeneous experts and embedding risk‑aware constraints directly into the learning pipeline.

## Implications
The results suggest that combining barycenter aggregation with adversarial pretraining can yield robust trading policies that balance performance and risk, offering practitioners a practical framework for deploying RL in real‑time market environments. This could inspire future research on multi‑expert policy synthesis and safety‑constrained reinforcement learning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15770v1)
