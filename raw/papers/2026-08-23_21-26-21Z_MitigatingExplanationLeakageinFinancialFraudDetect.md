---
title: Mitigating Explanation Leakage in Financial Fraud Detection Systems
published: 2026-08-23T21:26:21Z
authors: Muhammad Waleed Gul, Elaheh Homayounvala
url: http://arxiv.org/abs/2608.22607v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mitigating Explanation Leakage in Financial Fraud Detection Systems

## Abstract
Financial fraud detection relies heavily on centralized machine learning models. This creates serious data privacy risks. Federated Learning (FL) decentralizes data processing, but financial regulations still require models to be transparent. This means using Explainable AI (XAI) tools such as TreeSHAP. Recent cybersecurity research shows a problem with this approach. Sharing high-fidelity SHAP explanations exposes the federated network to Membership Inference Attacks (MIAs). This dissertation proposes and evaluates DP-FedSHAP. It is a new architecture that applies client-level differential privacy only to post-hoc TreeSHAP vectors. It is compared against a Weight-Level DP baseline, which perturbs the trained model directly instead. Using the highly imbalanced IEEE-CIS Fraud Detection dataset, this study measures the trade-off between explanation fidelity, privacy preservation, and the model's Area Under the Precision-Recall Curve (AUPRC).

## Metadata
- **Published**: 2026-08-23T21:26:21Z
- **Authors**: Muhammad Waleed Gul, Elaheh Homayounvala
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22607v1)