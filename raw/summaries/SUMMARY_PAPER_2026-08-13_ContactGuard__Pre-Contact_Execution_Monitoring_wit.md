---
title: ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models
url: http://arxiv.org/abs/2608.13438v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_16-25-54Z_ContactGuard_Pre_ContactExecutionMonitoringwithAct.md
generated_at: 2026-08-13 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
ContactGuard is a pre-contact execution monitor for chunked visuomotor policies that predicts short‑horizon consequences in latent visual space and aborts when failure is likely. The model uses an unsupervised latent world model trained on robot trajectories to generate compact multi‑view embeddings under planned actions, avoiding pixel‑level video prediction. A lightweight probe trained on a small labeled set of pre‑contact clips provides the final decision.

## Key Takeaways
- ContactGuard predicts failure before contact by forecasting latent visual states rather than raw pixels, enabling early abort.
- The latent world model is trained from unlabeled trajectories to produce compact multi‑view embeddings that capture the effect of actions without video prediction.
- A small labeled set of pre‑contact clips trains a lightweight probe that translates the model’s predictions into an actionable abort signal.

## Context
In robotics, detecting manipulation failures only after contact occurs limits safety and efficiency. Current methods rely on pixel‑level video analysis or corrupted‑action ablations which are computationally heavy or misleading. ContactGuard shifts focus to latent representations, offering a faster, policy‑agnostic monitoring mechanism that can be integrated without altering the underlying policy.

## Implications
This approach reduces false positives by predicting failure before it happens, improving safety in real‑world tasks. By leveraging unsupervised training and lightweight probes, ContactGuard offers a scalable solution for industry robots where high‑resolution video is impractical. Practitioners can adopt pre‑contact abort signals to enhance reliability without retraining the main policy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13438v1)
