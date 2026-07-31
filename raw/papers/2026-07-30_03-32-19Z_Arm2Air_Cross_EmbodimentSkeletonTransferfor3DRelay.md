---
title: Arm2Air: Cross-Embodiment Skeleton Transfer for 3D Relay Formation
published: 2026-07-30T03:32:19Z
authors: Dohun Lee, Kyeonghyun Yoo, Seokmin Kim, Byongho Lee, Seungjoo Oh, Hwangnam Kim
url: http://arxiv.org/abs/2607.27627v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Arm2Air: Cross-Embodiment Skeleton Transfer for 3D Relay Formation

## Abstract
Unmanned aerial vehicle (UAV) relay networks can restore connectivity after communication infrastructure is damaged. Urban relay placement is difficult because line-of-sight blockage, communication range, altitude, and three-dimensional obstacles must be considered jointly. Arm2Air transfers obstacle-avoidance skeletons from robot arms to UAV relay placement through cross-embodiment transfer. Source-domain robot-arm motions from a pretrained Neural MP model are converted into ordered skeletons that pretrain a transformer-based transfer platform, which is then adapted to the UAV domain using limited target data and Low-Rank Adaptation. The transferred skeleton initializes a relay chain that is refined for connectivity, bottleneck capacity, delay, and movement cost. On nine held-out high-clutter 3D urban maps, Arm2Air reduced median end-to-end planning runtime by 64.9 percent relative to the fastest conventional planner. On the high-obstruction group of a separate 30-map dense urban holdout, it increased bottleneck capacity by 32.6 percent, reduced capacity variance by 74.7 percent, reduced maximum hop distance by 13.2 percent, reduced hop-distance variance by 75.2 percent, and reduced relay displacement by 16.9 percent relative to IMPC-MD. With only three target-domain training maps, Arm2Air reduced relay-position root mean square error by 53.6 percent relative to training from scratch while updating 0.134 million parameters, compared with 1.383 million for Scratch and Full Fine-tuning. These results demonstrate computationally and data-efficient UAV relay placement and suggest a broader principle for transferring ordered structural priors across heterogeneous embodied tasks.

## Metadata
- **Published**: 2026-07-30T03:32:19Z
- **Authors**: Dohun Lee, Kyeonghyun Yoo, Seokmin Kim, Byongho Lee, Seungjoo Oh, Hwangnam Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27627v1)