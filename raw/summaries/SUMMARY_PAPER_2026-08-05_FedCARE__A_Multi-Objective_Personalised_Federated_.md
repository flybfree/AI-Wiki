---
title: FedCARE: A Multi-Objective Personalised Federated Learning Framework for Smart Healthcare
url: http://arxiv.org/abs/2608.03498v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_11-37-03Z_FedCARE_AMulti_ObjectivePersonalisedFederatedLearn.md
generated_at: 2026-08-05 01:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FedCARE a multi-objective personalised federated learning framework for smart healthcare that learns a shared global backbone and then fine-tunes it locally. Experiments on MIMIC-III and Diabetes 130-US Hospitals show FedCARE improves AUROC by up to 12.5% and reduces MAE by 32.0% compared with existing methods.

## Key Takeaways
- FedCARE separates global feature learning from client-specific objective adaptation using Pareto-driven multi-objective optimisation.
- The two-stage training avoids extra communication overhead while still personalising models to each institution's private features and objectives.
- Results demonstrate superior performance over standard FL, multi‑objective FL and personalised FL baselines.

## Context
Federated learning is gaining traction in healthcare because it protects patient privacy but struggles with non-IID data and divergent clinical goals. Existing approaches either ignore personalisation or fail to handle multiple competing objectives simultaneously.

## Implications
This framework enables hospitals to collaborate on shared models while respecting local clinical priorities, fostering scalable AI solutions that improve diagnostic accuracy without compromising data security. Practitioners can adopt FedCARE to deliver more effective and equitable health services across diverse settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03498v1)
