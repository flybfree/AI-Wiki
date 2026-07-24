---
title: Reinforcement Learning for Delivery Drone-Based Participatory Sensing in Dynamic Environments
published: 2026-07-21T09:06:23Z
authors: Xin Ouyang, Songxin Lei, Xusen Guo, Yutian Jiang, Sijie Ruan, Yuxuan Liang
url: http://arxiv.org/abs/2607.18874v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reinforcement Learning for Delivery Drone-Based Participatory Sensing in Dynamic Environments

## Abstract
Using Unmanned Aerial Vehicle (UAV) for urban sensing has emerged as a powerful paradigm to monitor the status of the city, e.g., air quality and noise levels, through agile aerial crowdsourcing. Despite this potential, existing UAV-based sensing approaches overlook environmental disturbances like wind that drastically impact drone velocity and energy efficiency. Consequently, directly applying existing methods to this joint delivery and sensing paradigm in dynamic environments faces two severe challenges: (1) scalability bottlenecks as fleet sizes expand; and (2) multi-timescale decision heterogeneity between macro task dispatching and micro velocity control. To tackle these, we formalize the problem as SensUAV and propose a Two TimeScale Reinforcement Learning framework (TSRL). Specifically, TSRL separates decision-making into two cooperative layers. At the macro level, a task-embedding sensing dispatcher handles scalability by separately encoding distinct task features and sequentially evaluating UAV suitability before task selection. At the micro level, a wind-aware velocity controller learns fine-grained velocity scheduling to adapt to dynamic environmental variations. Extensive experiments on real-world datasets demonstrate that TSRL significantly outperforms baselines, achieving average system profit improvements of 20.1% in Hangzhou and 46.6% in Shanghai.

## Metadata
- **Published**: 2026-07-21T09:06:23Z
- **Authors**: Xin Ouyang, Songxin Lei, Xusen Guo, Yutian Jiang, Sijie Ruan, Yuxuan Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18874v1)