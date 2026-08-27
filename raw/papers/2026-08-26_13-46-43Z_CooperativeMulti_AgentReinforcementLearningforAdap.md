---
title: Cooperative Multi-Agent Reinforcement Learning for Adaptive Aggregation in Semi-Supervised Federated Learning with non-IID Data
published: 2026-08-26T13:46:43Z
authors: Rene Glitza, Luca Becker, Rainer Martin
url: http://arxiv.org/abs/2608.25794v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cooperative Multi-Agent Reinforcement Learning for Adaptive Aggregation in Semi-Supervised Federated Learning with non-IID Data

## Abstract
Federated Learning (FL) enables distributed training of machine learning models while preserving data privacy. However, FL struggles with heterogeneous, non-IID client data distributions, resulting in sub-optimal and biased global models. In this paper, we propose pFedMARL, a novel approach leveraging Multi-Agent Reinforcement Learning (MARL) with Twin Delayed Deep Deterministic Policy Gradient (TD3) to dynamically adapt aggregation strategies in FL settings. Our method employs a server-side agent adjusting client contributions to optimize global model robustness and client-side agents balancing global and local updates to personalize models effectively without pre-training. We demonstrate superior performance of pFedMARL for training a semi-supervised audio spectrogram transformer, matching or outperforming FedAvg, Ditto, and local training approaches across multiple non-IID scenarios and in the presence of adversarial clients. Our results indicate that pFedMARL actively improves accuracy, robustness, and fairness, making it suitable for real-world deployments.

## Metadata
- **Published**: 2026-08-26T13:46:43Z
- **Authors**: Rene Glitza, Luca Becker, Rainer Martin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25794v1)