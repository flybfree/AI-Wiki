---
title: HetGPS: Scalable Graph Multi-Agent Reinforcement Learning with Physics-Anchored Adaptive Safety for EV Charging
published: 2026-08-01T13:59:49Z
authors: Xiangwei Wang, Nanduni Nimalsiri, Yu Xia, Peng Wang, Saman Halgamuge
url: http://arxiv.org/abs/2608.00679v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HetGPS: Scalable Graph Multi-Agent Reinforcement Learning with Physics-Anchored Adaptive Safety for EV Charging

## Abstract
Safety interventions for large populations of network-coupled agents must protect shared constraints without unnecessarily overriding task-oriented policy decisions. We present HetGPS, a hybrid graph-control framework synergizing learned graph risk with physics-anchored correction by separating intervention magnitude from corrective direction. An action-conditioned graph residual model schedules state-dependent intervention authority, while a physics model determines its direction. For electric vehicle (EV) charging, we couple this filter with a parameter-shared heterogeneous graph soft actor-critic policy, enabling topology-aware coordination with a learned model size independent of fleet size. Across five nested distribution networks with 200--3,218 EVs and 100 evaluation days, Adaptive Authority reduces bus--step voltage violations from 3.93--7.74\% without filtering to 0.52--3.44\%, while maintaining 99.06--100\% departure success. Relative to the same physics-directed projection with fixed authority, it improves mean reward on all five networks and lowers the mean safety score on four. The deployed policy-and-risk model contains 383,702 learned parameters at every scale; at 3,218 EVs, a matched centralized SAC actor is about $170\times$ larger. A policy trained on the eight-transformer system transfers zero-shot to the 16- and 32-transformer systems, attaining 0.57--0.75\% violation rates and at least 99.99\% departure success. These results show that learned graph risk can allocate intervention authority at scale while feeder physics anchors corrective action.

## Metadata
- **Published**: 2026-08-01T13:59:49Z
- **Authors**: Xiangwei Wang, Nanduni Nimalsiri, Yu Xia, Peng Wang, Saman Halgamuge
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00679v1)