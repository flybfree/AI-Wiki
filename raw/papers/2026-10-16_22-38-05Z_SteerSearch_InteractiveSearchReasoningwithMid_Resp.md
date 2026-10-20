---
title: SteerSearch: Interactive Search Reasoning with Mid-Response Steering
published: 2026-10-16T22:38:05Z
authors: Udit Thakur, Baohao Liao, Matteo Nulli, Stefan Vasilev, Seyyed Hadi Hashemi, Shahram Khadivi, Christof Monz
url: http://arxiv.org/abs/2610.24287v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SteerSearch: Interactive Search Reasoning with Mid-Response Steering

## Abstract
Search-augmented language models increasingly serve as long-horizon research agents, yet most open training methods assume a fixed user goal throughout search. We study mid-response steering, where users redirect a model during ongoing reasoning or retrieval. We identify answer-target anchoring, a failure mode in which fixed-query search agents retrieve evidence for the updated request but still answer an earlier question. We introduce SteerSearch, an RL framework that trains on interactive search trajectories with injected interventions to enable context-preserving target reassignment, and SteerSearch-Bench, a benchmark adapted from multi-hop QA datasets. We also investigate Contrastive Context Reward (CCR), an auxiliary signal for aligning post-intervention reasoning with the updated goal. Without CCR, SteerSearch improves average steering accuracy over Search-R1 from 11.1% to 31.3% on Qwen2.5-3B and from 36.6% to 44.6% on Qwen3-4B, while preserving standard single-query performance. Gains also extend to larger Qwen2.5 models and natural multi-turn conversations.

## Metadata
- **Published**: 2026-10-16T22:38:05Z
- **Authors**: Udit Thakur, Baohao Liao, Matteo Nulli, Stefan Vasilev, Seyyed Hadi Hashemi, Shahram Khadivi, Christof Monz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24287v1)