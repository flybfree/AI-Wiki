---
title: Physics-informed VAE-EVT for Tail Aware Radio Map Prediction
url: http://arxiv.org/abs/2608.15314v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_16-41-19Z_Physics_informedVAE_EVTforTailAwareRadioMapPredict.md
generated_at: 2026-08-17 21:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a physics‑informed variational autoencoder‑extreme value theory (VAE‑EVT) model that jointly predicts the bulk and tail of radio signal‑to‑noise ratio (SNR) to improve outage detection for ultra‑reliable low‑latency communication. Trained on the RadioMapSeer dataset, it achieves an SNR RMSE of 4.83 dB in the extreme low‑threshold region (0.1% quantile), far outperforming a state‑of‑the‑art GAN model with an RMSE of 21.90 dB.

## Key Takeaways
- The framework explicitly separates bulk SNR modeling via a Gaussian mixture and tail modeling via a generalized Pareto distribution, ensuring accurate capture of extreme fading events.
- A physics‑informed preprocessing stage extracts deterministic features such as line‑of‑sight, shadowing, and distance to ground the generative model on physical constraints.
- The modified variational objective jointly supervises both regimes, resulting in significantly lower RMSE compared with GAN‑based approaches when outage thresholds are stringent.

## Context
The demand for URLLC services demands precise prediction of low‑SNR regions where communication fails. Traditional models often ignore the tail distribution, leading to inaccurate outage estimates. This work bridges that gap by integrating extreme value theory into a deep generative model, offering a more robust solution for real‑world radio map generation.

## Implications
Accurate outage prediction is critical for network planning and resource allocation in 5G/6G deployments. By delivering reliable low‑SNR forecasts, the VAE‑EVT approach can enable proactive optimization of coverage and reduce user impact during extreme fading events.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15314v1)
