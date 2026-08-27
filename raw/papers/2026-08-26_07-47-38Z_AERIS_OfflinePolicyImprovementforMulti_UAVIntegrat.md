---
title: AERIS: Offline Policy Improvement for Multi-UAV Integrated Sensing and Communication
published: 2026-08-26T07:47:38Z
authors: Ziyuan Wang, Yifan Sui, Wei Wei, Wenjie Xin, Zekai Zhang, Xiangwang Hou,  Xiao-Ping,  Zhang
url: http://arxiv.org/abs/2608.25477v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AERIS: Offline Policy Improvement for Multi-UAV Integrated Sensing and Communication

## Abstract
Unmanned aerial vehicle (UAV)-enabled integrated sensing and communication (ISAC) is a promising 6G paradigm, but dynamic multi-UAV ISAC control must jointly balance communication quality, sensing reliability, and flight safety under stochastic mobility. Existing optimization methods often require repeated global non-convex solving, while online reinforcement learning (RL) depends on risky trial-and-error flights that may cause sensing loss or collision-risk events.   This paper proposes AERIS, an offline policy improvement framework for multi-UAV ISAC. AERIS learns from fixed flight logs under centralized training and decentralized execution, so each UAV acts from local histories while training uses logged global information to assess team-level effects. We further design STAR-CRDT, an offline multi-agent RL algorithm that performs support-aware local action rectification and distills only trusted improvements into the decentralized actor. We prove an offline-support policy improvement guarantee. Experiments show that STAR-CRDT improves the main ISAC objective return by 29.3% over the strongest baseline. It further improves communication sum rate, sensing pass rate, and sensing margin by 3.4%, 4.8%, and 69.1%, while reducing collision-risk events by 54.2%. On unseen real-road maps built from OpenStreetMap data, STAR-CRDT still obtains the best return.

## Metadata
- **Published**: 2026-08-26T07:47:38Z
- **Authors**: Ziyuan Wang, Yifan Sui, Wei Wei, Wenjie Xin, Zekai Zhang, Xiangwang Hou,  Xiao-Ping,  Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25477v1)