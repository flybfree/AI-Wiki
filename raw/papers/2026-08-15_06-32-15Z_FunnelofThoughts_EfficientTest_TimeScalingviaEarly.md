---
title: Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning
published: 2026-08-15T06:32:15Z
authors: Chanhee Park, Sungbin Han, Jeongho Yoon, Seongtae Hong, Heuiseok Lim
url: http://arxiv.org/abs/2608.15065v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning

## Abstract
Large Reasoning Models produce diverse, sometimes inconsistent answers across repeated queries on the same problem, so multi-sample inference is a prerequisite for reliable deployment. Majority voting at k rollouts is the standard solution and the de facto accuracy target for this regime, but it is prohibitively expensive at the scale LRMs require. We introduce Funnel of Thoughts (FoT), an inference-time method that preserves the full 32-trajectory voted accuracy while halving its attention FLOPs, a 28.8% reduction in full-model inference cost. Across 115K reasoning trajectories from six LRMs, we find that unproductive trajectories often reveal themselves through repeated hesitation markers such as "Wait", "Actually", and "perhaps." These trajectories are less likely to reach the correct answer and consume disproportionate attention FLOPs, degenerating into no-answer loops in the worst case. Built on this training-free lexical signal, FoT identifies the vocabulary that captures these pathological patterns and prunes affected trajectories before completion, reducing online generation attention FLOPs by 56.1% and wall time by 37.6% without any additional model inference; the same signal transfers without retuning across held-out architectures and out-of-domain tasks.

## Metadata
- **Published**: 2026-08-15T06:32:15Z
- **Authors**: Chanhee Park, Sungbin Han, Jeongho Yoon, Seongtae Hong, Heuiseok Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15065v1)