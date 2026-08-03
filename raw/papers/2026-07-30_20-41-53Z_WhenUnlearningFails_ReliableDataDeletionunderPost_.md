---
title: When Unlearning Fails: Reliable Data Deletion under Post-Training in Agent Networks
published: 2026-07-30T20:41:53Z
authors: Zihao Ding, Jun Huang, Liang Dong
url: http://arxiv.org/abs/2607.28829v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Unlearning Fails: Reliable Data Deletion under Post-Training in Agent Networks

## Abstract
Self-improving federated agent networks keep training after deployment by collecting new trajectories with the current policy and feeding them back into later rounds. This closed loop makes unlearning harder than a one-time model repair. When a data owner requests deletion, the target data may have already shaped later retained trajectories, so retraining or model-side unlearning can leave an influence echo that returns as the network continues to operate. We show that this echo survives retained-data retraining, grows with the amount of forget-shaped retained data, and can be traced from deployment, collection, and aggregation records. To address this problem, we propose MUTE, a Muting Unlearned Trajectories' Echoes method for reliable deletion in self-improving federated agent networks. MUTE estimates downstream influence from a lightweight server ledger, removes the current residue through a forget-retain update, contains high-influence retained trajectories through quarantine or down-weighting, and audits later behavior to schedule additional erasure under an uplink budget. Experiments on LIBERO with two vision-language-action backbones, three deletion granularities, and a physical Jetson-based edge testbed show that MUTE keeps behavioral leakage and influence regeneration low while preserving task utility and using much less communication than full retraining.

## Metadata
- **Published**: 2026-07-30T20:41:53Z
- **Authors**: Zihao Ding, Jun Huang, Liang Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28829v1)