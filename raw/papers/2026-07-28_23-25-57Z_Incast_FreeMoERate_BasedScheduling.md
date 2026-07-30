---
title: Incast-Free MoE Rate-Based Scheduling
published: 2026-07-28T23:25:57Z
authors: Evyatar Cohen, Jose Yallouz, Alexander Shpiner, Mark Silberstein, Sylvia Ratnasamy, Isaac Keslassy
url: http://arxiv.org/abs/2607.26340v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Incast-Free MoE Rate-Based Scheduling

## Abstract
Mixture of Experts (MoE) architectures have become key to large language models; however, their typical round-robin (RR) scheduling introduces significant bottlenecks.   In this paper, we demonstrate that RR causes a previously-undiscovered exponential incast phenomenon with MoE traffic. We propose an alternative proactive fair scheduling framework tailored for MoE workloads, which effectively prevents fabric oversubscription. We also outline how it can be implemented in NICs. Finally, through extensive simulations with real and synthetic workloads, we demonstrate that this framework consistently eliminates incast, maintains a near-100% link utilization, and reduces Collective Completion Time (CCT).

## Metadata
- **Published**: 2026-07-28T23:25:57Z
- **Authors**: Evyatar Cohen, Jose Yallouz, Alexander Shpiner, Mark Silberstein, Sylvia Ratnasamy, Isaac Keslassy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26340v1)