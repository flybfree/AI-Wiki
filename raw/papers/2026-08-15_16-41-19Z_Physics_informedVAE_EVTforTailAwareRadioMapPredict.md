---
title: Physics-informed VAE-EVT for Tail Aware Radio Map Prediction
published: 2026-08-15T16:41:19Z
authors: Amanda Sheron Gamage, Niloofar Mehrnia, James Gross
url: http://arxiv.org/abs/2608.15314v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Physics-informed VAE-EVT for Tail Aware Radio Map Prediction

## Abstract
Ultra-reliable low-latency communication (URLLC) requires precise identification of spatial regions where the signal-to-noise ratio (SNR) falls below an outage threshold. In this context, an outage refers to instances in which SNR falls below a specified threshold, which, for URLLC, can be as stringent as the 0.1% quantile of the SNR distribution. Traditional generative radio map models tend to focus on reconstructing average signal levels, often overlooking the low SNR that is crucial for accurate outage prediction. To address this limitation, we introduce a physics- and tail-informed VAE-EVT (variational autoencoder-extreme value theory) framework that distinctly models both the bulk and tail distribution of SNR. Our approach begins with a physics-informed preprocessing stage that extracts deterministic features, including line-of-sight, shadowing, and distance, from the scene geometry. A dual-latent encoder then captures the bulk SNR using a Gaussian mixture and the tail using a generalized Pareto distribution (GPD). By employing a modified variational objective, the model is trained to jointly supervise both regimes, ensuring focused attention on extreme fading events. Evaluated on the RadioMapSeer dataset, our method achieves an SNR RMSE of 4.83 dB in the outage region defined by the low threshold of 0.1% SNR quantile. This significantly outperforms the state-of-the-art GAN-based model, which records an SNR RMSE of 21.90 dB, with the performance gap widening as the outage threshold becomes more stringent.

## Metadata
- **Published**: 2026-08-15T16:41:19Z
- **Authors**: Amanda Sheron Gamage, Niloofar Mehrnia, James Gross
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15314v1)