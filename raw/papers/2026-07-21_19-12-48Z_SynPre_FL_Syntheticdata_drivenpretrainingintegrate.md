---
title: SynPre-FL: Synthetic data-driven pretraining integrated Federated Learning training framework
published: 2026-07-21T19:12:48Z
authors: Akarsh K Nair, Muhammad Arifur Rahman, Nicholas Shopland, Andy Burton, Jun He, Yuan Shen, David Baldwin, Emma O'Dowd, Amna Burzic, Mufti Mahmud, David J. Brown
url: http://arxiv.org/abs/2607.19524v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SynPre-FL: Synthetic data-driven pretraining integrated Federated Learning training framework

## Abstract
Federated learning (FL) offers a promising approach to privacy-preserving clinical risk prediction, but its deployment remains limited by restricted data sharing, client heterogeneity, class imbalance, and the lack of realistic tabular electronic health record (EHR) benchmarks. Synthetic data generation may alleviate data scarcity, yet its integration with federated optimisation has received limited systematic study. We propose SynPre-FL, a unified framework combining high-fidelity synthetic EHR generation with synthetic-pretrained FL for robust prediction under non-IID conditions. A latent autoencoder-diffusion model generates privacy-preserving synthetic cohorts, which are used to warm-start federated training. This pretraining is followed by heterogeneity-aware optimisation using class-balanced local objectives, proximal regularisation, and adaptive server aggregation. Post-hoc calibration and federated-safe explainability support reliable and interpretable risk estimates. Experiments show that the synthetic generator preserves univariate, bivariate, and multivariate structure while protecting against membership-inference and reconstruction attacks. The generated data achieve strong downstream utility under TSTR, TRTS, and model-based evaluations. Across federated settings with 5, 10, and 15 heterogeneous clients, SynPre-FL consistently improves robustness and scalability over baseline methods, especially under severe non-IID fragmentation. Calibration improves probability reliability, while SHAP analysis produces stable and clinically coherent feature attributions across federation sizes. SynPre-FL therefore provides a practical and reproducible framework for combining synthetic data with FL to enable privacy-aware, interpretable, and robust clinical prediction from distributed tabular EHR data.

## Metadata
- **Published**: 2026-07-21T19:12:48Z
- **Authors**: Akarsh K Nair, Muhammad Arifur Rahman, Nicholas Shopland, Andy Burton, Jun He, Yuan Shen, David Baldwin, Emma O'Dowd, Amna Burzic, Mufti Mahmud, David J. Brown
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19524v1)