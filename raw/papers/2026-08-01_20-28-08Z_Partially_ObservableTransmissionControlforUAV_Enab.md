---
title: Partially-Observable Transmission Control for UAV-Enabled Federated Learning in IoT Networks
published: 2026-08-01T20:28:08Z
authors: Masoud Ghazikor, Zhou Ni, Morteza Hashemi
url: http://arxiv.org/abs/2608.00855v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Partially-Observable Transmission Control for UAV-Enabled Federated Learning in IoT Networks

## Abstract
Uncrewed aerial vehicle (UAV)-enabled federated learning (FL) can provide flexible, on-demand edge intelligence for large-scale IoT deployments, but operating in shared unlicensed bands makes uplink update delivery interference-coupled and unreliable. In this paper, we develop a packet-level transmission framework that captures buffer overflow, delay violations, and transmission errors, and uses the resulting packet delivery ratio (PDR) to represent partial-update reception through a packetized, Bernoulli-masked FL aggregation process. We then formulate a fairness-consensus bilevel (FCB) optimization that jointly controls (i) transmission thresholds to maximize the average PDR while reaching consensus under partial observability and (ii) transmission powers to improve the worst PDR and enforce fairness across IoT learners. To solve this problem, we propose an alternating FCB optimizer composed of a consensus-based threshold controller (CTC), which drives the IoT learners toward a PDR-efficient consensus on transmission thresholds, and a fairness-based power controller (FPC), which updates transmission powers to improve the worst PDR and ensure fairness under the resulting consensus thresholds. Numerical results on CNN-based FL tasks show that the FCB optimizer improves FL aggregation and training performance by enhancing packet-level update delivery, consistently outperforming baseline transmission policies.

## Metadata
- **Published**: 2026-08-01T20:28:08Z
- **Authors**: Masoud Ghazikor, Zhou Ni, Morteza Hashemi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00855v1)