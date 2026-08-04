---
title: FL-OA: A Byzantine-Robust Federated Learning Framework with Outsourced Auditing for Intelligent Devices
published: 2026-08-02T08:50:52Z
authors: Hongliang Zhang, Zhongyuan Yu, Fenghua Xu, Teng Hu, Jian Meng, Jiguo Yu
url: http://arxiv.org/abs/2608.01095v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FL-OA: A Byzantine-Robust Federated Learning Framework with Outsourced Auditing for Intelligent Devices

## Abstract
Federated learning (FL) enables multiple intelligent devices to collaboratively train a high-accuracy model without sharing raw data. However, due to its distributed nature, FL is vulnerable to Byzantine attacks. Existing defense methods rely on strong assumptions, such as the proportion of malicious devices not exceeding 50\%, or the server having an additional root dataset that matches the training task. Moreover, they show limited efficacy as they overlook $(i)$ the divergence among benign updates and $(ii)$ the curse of dimensionality involved in comparing two high-dimensional updates. To solve these concerns, we propose FL-OA, a Byzantine-robust federated learning framework utilizing outsourced auditing. In FL-OA, the server collaborates with third-party organization that holds an additional root dataset to perform outsourced auditing, thereby enabling the server to achieve robust aggregation without strong assumptions. Additionally, FL-OA introduces a gradient ascent step and a correction term during local training to mitigate the divergence among benign updates, and designs a parameter importance indicator to extract critical parameters for auditing, alleviating the curse of dimensionality. We further provide a detailed theoretical analysis of FL-OA. Extensive experiments demonstrate that FL-OA outperforms existing defense methods against Byzantine attacks.

## Metadata
- **Published**: 2026-08-02T08:50:52Z
- **Authors**: Hongliang Zhang, Zhongyuan Yu, Fenghua Xu, Teng Hu, Jian Meng, Jiguo Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01095v1)