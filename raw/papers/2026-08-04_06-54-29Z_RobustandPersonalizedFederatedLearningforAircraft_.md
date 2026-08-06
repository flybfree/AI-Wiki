---
title: Robust and Personalized Federated Learning for Aircraft-Engine Prognostics under Benign and Adversarial Client Heterogeneity
published: 2026-08-04T06:54:29Z
authors: Chinmoy Mitra, Md. Mehedi Hasan Nipu, Mohammad Sakib Mahmood, Md. Rakibul Islam, M. F. Mridha
url: http://arxiv.org/abs/2608.04045v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robust and Personalized Federated Learning for Aircraft-Engine Prognostics under Benign and Adversarial Client Heterogeneity

## Abstract
Federated learning (FL) enables aircraft fleet operators to jointly train remaining-useful-life (RUL) models from engine sensor telemetry without sharing raw data. This study examines two complementary challenges: benign heterogeneity, where honest operators observe different operating conditions and fault modes, and adversarial heterogeneity, where compromised operators submit poisoned updates. We conduct a controlled, safety-oriented evaluation using a multi-task one-dimensional convolutional neural network and a structurally non-IID partition of the Commercial Modular Aero-Propulsion System Simulation (C-MAPSS) benchmark. We compare four remedies for benign heterogeneity and evaluate five attacks against four aggregation methods, including a physically motivated sensor-value backdoor designed to mask engine degradation.   Shared-representation personalization closes approximately 70% of the local-to-centralized root-mean-square-error gap, compared with 21% for proximal regularization and 10% for server-side reweighting. The backdoor achieves a 94.9% attack success rate against standard averaging while leaving clean accuracy statistically unchanged, demonstrating that accuracy alone cannot certify model safety and that attack success must be evaluated explicitly. Krum reduces attack success by an order of magnitude and is the only evaluated aggregator that withstands coordinated attackers, whereas personalization alone provides no protection. Combining personalization with robust aggregation restores robustness (2.8% attack success) with only a small accuracy cost, revealing a trade-off between robust update selection and collaborative representation learning. Results remain consistent across client counts and on a harder six-condition dataset. Code and data partitions are released for reproducibility.

## Metadata
- **Published**: 2026-08-04T06:54:29Z
- **Authors**: Chinmoy Mitra, Md. Mehedi Hasan Nipu, Mohammad Sakib Mahmood, Md. Rakibul Islam, M. F. Mridha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04045v1)