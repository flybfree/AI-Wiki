---
title: FBID: Adaptive Personalized Federated Learning for Robust Out-of-Distribution Attack Detection in IoT Networks
url: http://arxiv.org/abs/2608.04073v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_15-59-33Z_FBID_AdaptivePersonalizedFederatedLearningforRobus.md
generated_at: 2026-08-05 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Federated Bandit Intrusion Detection (FBID), an adaptive personalized federated learning framework that uses a server-side multi-armed bandit to control client training intensity and a trust-based blending mechanism for interpolation coefficients. Experiments on CICIoT2023 show FBID raises individual client OOD detection rate by up to 7.66% and F1-score by up to 5.08% relative to the best stable baseline, while enhancing robustness to unseen attack classes.

## Key Takeaways
- The server-side bandit dynamically adjusts each client's training intensity based on observed behavior and update quality to prevent over-personalization.
- A trust-based blending mechanism computes client-specific interpolation coefficients between global and local models, preserving global knowledge while allowing specialization.
- FBID achieves significant gains in OOD detection metrics (7.66% DR increase, 5.08% F1 increase) compared with the strongest stable baseline.

## Context
Federated learning enables collaborative model training across distributed IoT devices without sharing raw data, but non-IID client distributions and out-of-distribution attacks challenge performance. Personalized approaches aim to adapt locally yet risk overfitting to individual clients, reducing overall robustness.

## Implications
This work demonstrates that server-controlled personalization can improve OOD detection in heterogeneous IoT networks, offering a scalable solution for security systems. Practitioners can adopt FBID's blending and bandit mechanisms to balance global knowledge with local adaptation, enhancing system resilience against novel attacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04073v1)
