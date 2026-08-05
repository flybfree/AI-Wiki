---
title: FedRings: A Scalable and Topology-Aware Federated Learning Framework for LEO Satellite Constellations
published: 2026-08-04T10:31:58Z
authors: Ziwu Liu, Inês Pinto Gouveia, Rehana Yasmin, Paulo Esteves-Verissimo, Ali Shoker
url: http://arxiv.org/abs/2608.03436v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedRings: A Scalable and Topology-Aware Federated Learning Framework for LEO Satellite Constellations

## Abstract
Federated learning over low Earth orbit (LEO) satellite networks is limited by frequent link changes, short contact times, and a highly dynamic topology, making centralized or synchronized training inefficient and hard to scale. To address this, we propose FedRings, a decentralized framework that organizes satellites into ring-based communication structures. It uses a spatio-temporal routing strategy with link-aware communication scheduling to align model exchange with actual visibility windows and time-varying connectivity patterns in LEO. Model updates are propagated along the ring using adaptive sparse incremental aggregation, which reduces communication overhead by progressively combining and compressing updates. To handle communication interruptions, a historical compensation mechanism maintains training continuity. By combining topology-aware routing, communication scheduling, and efficient aggregation, FedRings enables stable and efficient learning in dynamic LEO networks while reducing communication cost, and experiments show it consistently outperforms existing methods in realistic settings.

## Metadata
- **Published**: 2026-08-04T10:31:58Z
- **Authors**: Ziwu Liu, Inês Pinto Gouveia, Rehana Yasmin, Paulo Esteves-Verissimo, Ali Shoker
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03436v1)