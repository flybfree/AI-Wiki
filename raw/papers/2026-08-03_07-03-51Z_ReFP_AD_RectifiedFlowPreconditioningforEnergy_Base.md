---
title: ReFP-AD: Rectified Flow Preconditioning for Energy-Based Anomaly Detection
published: 2026-08-03T07:03:51Z
authors: Camile Lendering, Erkut Akdag, Joaquín Figueira, Egor Bondarev
url: http://arxiv.org/abs/2608.01793v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReFP-AD: Rectified Flow Preconditioning for Energy-Based Anomaly Detection

## Abstract
Unified anomaly detection requires modeling highly heterogeneous normal data without access to anomalous samples. While foundation models like DINOv2 provide rich token representations, leveraging these spaces for explicit density estimation remains challenging. Energy-Based Models (EBMs) offer a principled formulation, but their training in high-dimensional token spaces is unstable due to anisotropy and strong cross-dimensional correlations, which degrades finite-step Markov Chain Monte Carlo (MCMC) sampling. We identify this instability as fundamentally geometric and introduce ReFP-AD (Rectified Flow Preconditioning for Anomaly Detection), which learns a geometric reparameterization that maps high-dimensional embeddings into a well-conditioned latent space via an optimal transport (OT)-coupled rectified flow. This preconditioning enables stable persistent contrastive divergence with preconditioned Stochastic Gradient Langevin Dynamics (SGLD) in full-dimensional token spaces. Anomaly scores are then derived from the learned energy landscape using gradient norms. Under a strict unified protocol on the MVTec-AD and VisA datasets, ReFP-AD achieves 98.6%/97.9% Image/Pixel AUROC on MVTec-AD and 97.3%/99.0% on VisA, outperforming prior unified EBM baselines by up to +10.8% in Image AUROC. Ablation experiments demonstrate that geometric reparameterization is critical for finite-step MCMC and accurate anomaly localization in high-dimensional token spaces. Code is available at https://github.com/CLendering/ReFP-AD

## Metadata
- **Published**: 2026-08-03T07:03:51Z
- **Authors**: Camile Lendering, Erkut Akdag, Joaquín Figueira, Egor Bondarev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01793v1)