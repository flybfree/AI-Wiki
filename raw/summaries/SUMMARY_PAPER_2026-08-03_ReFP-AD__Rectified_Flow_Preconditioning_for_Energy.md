---
title: ReFP-AD: Rectified Flow Preconditioning for Energy-Based Anomaly Detection
url: http://arxiv.org/abs/2608.01793v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_07-03-51Z_ReFP_AD_RectifiedFlowPreconditioningforEnergy_Base.md
generated_at: 2026-08-03 23:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ReFP‑AD, a method that maps high‑dimensional token embeddings into a well‑conditioned latent space using an optimal transport coupled rectified flow. This geometric reparameterization stabilizes finite‑step MCMC and SGLD training for energy‑based anomaly detection. On MVTec‑AD and VisA datasets the approach reaches 98.6% image AUROC and 97.3% pixel AUROC, beating prior unified EBM baselines by up to ten point eight percent.

## Key Takeaways
- The instability of standard EBM training in token spaces is identified as a geometric problem caused by anisotropy and cross‑dimensional correlations.
- ReFP‑AD solves this by learning an optimal transport rectified flow that reparameterizes embeddings into a well‑conditioned space, enabling stable persistent contrastive divergence.
- Anomaly scores are derived from gradient norms of the learned energy landscape, allowing accurate anomaly localization.

## Context
Energy‑based models provide a principled framework for density estimation but struggle with high‑dimensional data due to poor conditioning. Recent advances in foundation models like DINOv2 create rich token representations that can be leveraged for detection tasks. This work bridges the gap between representation learning and EBM training by addressing geometric conditioning.

## Implications
The method offers a practical solution for practitioners seeking reliable anomaly scores without anomalous samples, improving model robustness on diverse datasets. By stabilizing MCMC and SGLD, ReFP‑AD could become a standard component in unified anomaly detection pipelines across computer vision and other high‑dimensional domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01793v1)
