---
title: Spine-Branch Coordination for Multi-agent Computer Use
published: 2026-08-22T18:48:37Z
authors: Mian Zhang, Manasi Sharma, Sheng Zhang, Minglai Yang, Kejian Shi, Ying Liu, Zhiyu Zoey Chen, Daniel Yue Zhang
url: http://arxiv.org/abs/2608.22077v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spine-Branch Coordination for Multi-agent Computer Use

## Abstract
Computer use agents (CUAs) are increasingly deployed as multi-agent systems that decompose a task into multiple subtasks executed across parallel virtual machines (VMs). However, a critical physical bottleneck is that the state of two VMs cannot be merged. Previous systems handle this ad-hoc rather than treating it as a first-class concern. We propose Spine-Branch Coordination for multi-agent computer use, a framework that decomposes a task into a "spine-branch" graph, where the spine carries the main task flow with continuous VM state and branch tasks execute in parallel to collect information the spine needs to complete the task. Branch VMs are discarded once their tasks finish, so no VM merging ever occurs. Experiments show that on 200 long-horizon tasks from Odysseys and across three CUA backbones, Spine-Branch improves success rate over the baseline system by 6.0% to 16.5%, while reducing per-task cost by 34% to 70%, indicating that explicitly modeling VM-state merging constraint enables multi-agent computer use to scale efficiently.

## Metadata
- **Published**: 2026-08-22T18:48:37Z
- **Authors**: Mian Zhang, Manasi Sharma, Sheng Zhang, Minglai Yang, Kejian Shi, Ying Liu, Zhiyu Zoey Chen, Daniel Yue Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22077v1)