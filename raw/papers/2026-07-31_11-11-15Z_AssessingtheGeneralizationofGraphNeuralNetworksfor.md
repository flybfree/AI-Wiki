---
title: Assessing the Generalization of Graph Neural Networks for Fault Location Across Increasing Distributed Energy Resource Penetration Levels
published: 2026-07-31T11:11:15Z
authors: Burak Karabulut, Olayiwola Arowolo, Carlo Manna, Chris Develder, Jochen L. Cremer
url: http://arxiv.org/abs/2607.29293v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Assessing the Generalization of Graph Neural Networks for Fault Location Across Increasing Distributed Energy Resource Penetration Levels

## Abstract
Accurate fault location is critical for distribution network reliability. However, increasing distributed energy resource (DER) penetration complicates fault location due to intermittent generation and bidirectional power flows that reshape fault signatures. Spatio-Temporal Graph Neural Networks (STGNNs) have shown promise by jointly modeling spatial and temporal dependencies, but their behavior under increasing DER penetration has not been studied rigorously. In this paper, we (i) systematically benchmark spatio-temporal graph attention network (STGATv2) against purely temporal (gated recurrent unit, GRU), purely spatial (GATv2) and traditional machine learning baselines, and (ii) evaluate how well models generalize across increasing DER penetration levels (10%, 25%, 50%) on a reconfigured IEEE 123-bus feeder with multiple DER injection points and moderate-to-high impedance faults. Results show that STGATv2 consistently outperforms neural baselines, achieving 92-94% macro F1 in-distribution. Notably, generalization across penetration levels is asymmetric: training at 50% penetration retains near in-distribution F1 score at lower levels, whereas training at 10% degrades considerably at 50% - with STGATv2 retaining 81-84% F1 under these drastic shifts, substantially higher than GATv2 and GRU which drop to 69-74% F1 and 73-75% F1 respectively. Under realistic measurement noise, STGATv2 maintains > 85% F1, while GRU drops as low as 33.5% F1, highlighting the critical role of topological awareness for robust fault location in active distribution networks.

## Metadata
- **Published**: 2026-07-31T11:11:15Z
- **Authors**: Burak Karabulut, Olayiwola Arowolo, Carlo Manna, Chris Develder, Jochen L. Cremer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29293v1)