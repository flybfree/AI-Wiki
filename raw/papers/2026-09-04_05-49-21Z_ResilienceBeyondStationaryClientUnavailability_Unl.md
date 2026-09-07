---
title: Resilience Beyond Stationary Client Unavailability: Unlocking Efficient and Unbiased Federated Learning
published: 2026-09-04T05:49:21Z
authors: Ming Xiang, Stratis Ioannidis, Edmund Yeh, Carlee Joe-Wong, Lili Su
url: http://arxiv.org/abs/2609.04763v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Resilience Beyond Stationary Client Unavailability: Unlocking Efficient and Unbiased Federated Learning

## Abstract
Due to resource constraints or external and internal uncertainties, clients in real-world federated learning systems are often intermittently available edge devices. In highly dynamic environments, the parameter server lacks prior real-time knowledge of clients' availability, making it challenging to adapt traditional federated learning algorithms to be resilient to uncertainties in client availability. If not carefully addressed, complex client availability can introduce significant bias, potentially harming the performance of the trained model. Most prior work either fails to account for non-stationary client availability dynamics or demands significant memory and computational overhead. This paper aims to develop efficient federated learning algorithms that are provably resilient to heterogeneous and non-stationary stochastic client availability. We propose FedSWE, which admits novel algorithmic structures to (i) compensate for missed computations, (ii) stabilize and diffuse the global updates over rounds, and (iii) evenly mix the local updates through implicit gossiping, despite being agnostic to non-stationary dynamics. Compared with the standard FedAvg, FedSWE introduces light additional memory and computation overhead. We show that FedSWE converges to a stationary point of non-convex objectives while achieving the desired linear speedup property in certain special cases. We corroborate our analysis with numerical experiments over diversified client unavailability dynamics on real-world data sets.

## Metadata
- **Published**: 2026-09-04T05:49:21Z
- **Authors**: Ming Xiang, Stratis Ioannidis, Edmund Yeh, Carlee Joe-Wong, Lili Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04763v1)