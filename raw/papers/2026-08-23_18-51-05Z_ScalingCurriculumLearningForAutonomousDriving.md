---
title: Scaling Curriculum Learning For Autonomous Driving
published: 2026-08-23T18:51:05Z
authors: Cevahir Koprulu, David Paz, Feng Tao, Yuliang Guo, Xinyu Huang, Ufuk Topcu, Liu Ren
url: http://arxiv.org/abs/2608.22549v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling Curriculum Learning For Autonomous Driving

## Abstract
Batched simulators for autonomous driving have recently enabled training reinforcement learning (RL) agents at scale, encompassing thousands of traffic scenarios and billions of interactions within a matter of days. Although such high-throughput feeds RL algorithms faster than ever, their sample-efficiency has not kept pace: As the standard training scheme, domain randomization uniformly samples scenarios, thereby consuming a vast number of interactions on cases that contribute little to learning. Curriculum learning offers a remedy by adaptively prioritizing scenarios that matter most to policy improvement. We present CL4AD, the first integration of curriculum learning into batched autonomous driving simulators by framing scenario selection as an unsupervised environment design problem. We introduce utility functions that shape curricula based on success rates and the realism of the agent's behavior, in addition to existing regret-estimation functions. Large-scale experiments in GPUDRIVE demonstrate that curriculum learning achieves a 99% success rate a billion steps earlier than domain randomization, reducing wall-clock time by 77%, and outperforms heuristic curricula with static and dynamic attributes, with only one exception at the largest scale. An ablation under limited compute shows that curriculum learning improves sample efficiency by 67%. We also investigate how utility functions behave at scale, and how prioritized scenarios evolve during training. We release an implementation of CLForAD in GPUDRIVE.

## Metadata
- **Published**: 2026-08-23T18:51:05Z
- **Authors**: Cevahir Koprulu, David Paz, Feng Tao, Yuliang Guo, Xinyu Huang, Ufuk Topcu, Liu Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22549v1)