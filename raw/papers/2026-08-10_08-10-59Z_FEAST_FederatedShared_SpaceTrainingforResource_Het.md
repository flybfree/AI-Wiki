---
title: FEAST: Federated Shared-Space Training for Resource-Heterogeneous Clients
published: 2026-08-10T08:10:59Z
authors: Bostan Khan, Masoud Daneshtalab
url: http://arxiv.org/abs/2608.09250v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FEAST: Federated Shared-Space Training for Resource-Heterogeneous Clients

## Abstract
Federated learning (FL) must serve devices with varying computational capabilities. A fixed model cannot suit all devices, while training one model per deployment limit is costly. Federated supernet training instead learns one elastic model with differently sized subnetworks, then deploys a suitable one to each device. When client inference budgets differ, however, parameters exclusive to high-cost subnetworks are reachable by fewer clients. We propose FEAST, a federated shared-space training framework that counters this imbalance by jointly training multiple subnetworks within each client's limit. Budget-tailored sub-supernet routing sends only the relevant supernet portion, and sparse aggregation merges the returned parameter slices. The trained supernet directly serves the subnetworks used during federation and supports post-hoc extraction of additional subnetworks without federated retraining. We further show that independently assigning clients' training-data volumes and inference budgets can distort accuracy--inference-cost comparisons in heterogeneous FL simulations, and introduce a one-parameter $γ$-allocation protocol to control this coupling. In our experimental setup, the SuperFedNAS and DeepFedNAS supernet training procedures remain near chance at 25M and reach at most $17.09\%$ at $596$M inference MACs; FEAST reaches $71.06\%$ at $596$M, $2.4$ points above the strongest model-heterogeneous weight-sharing baseline at its largest tier. Across CIFAR-100, CINIC-10, and TinyImageNet-200, FEAST achieves the highest population-averaged accuracy among the evaluated weight-sharing methods when each client receives its largest affordable subnetwork. Sub-supernet routing reduces aggregate model-parameter traffic by $6.8\times$ relative to full-supernet transmission.

## Metadata
- **Published**: 2026-08-10T08:10:59Z
- **Authors**: Bostan Khan, Masoud Daneshtalab
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09250v1)