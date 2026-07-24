---
title: Procedural Memory Distillation: Online Reflection for Self-Improving Language Models
published: 2026-07-01T21:20:57Z
authors: Ye Liu, Srijan Bansal, Bo Pang, Yang Li, Zeyu Leo Liu, Yifei Ming, Zixuan Ke, Shafiq Joty, Semih Yavuz
url: http://arxiv.org/abs/2607.01480v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Procedural Memory Distillation: Online Reflection for Self-Improving Language Models

## Abstract
Reinforcement learning with verifiable rewards (RLVR), along with recent selfdistillation variants such as SDPO, evaluates each rollout against a verifier and updates the policy from that episode-level signal. However, the richer procedural information in the rollout is rarely retained or reused. Across episodes and epochs, the model repeatedly encounters related problems under a changing policy, producing cross-episode signals that episode-local updates cannot capture: which strategies consistently pass verification, which failure modes persist, which patterns recur. We propose Procedural Memory Distillation (PMD), which converts these crossepisode signals into reusable procedural memory and distills it into the policy's weights during training. This memory functions as a training scaffold, absorbed into the policy itself, yielding a memory-free model at inference. PMD organizes the memory at three levels of abstraction: raw trajectories, self-reflected strategies and lessons, and higher-level behavioral patterns that recur across problems, all extracted online from the model's own trajectories. A memory-conditioned self-teacher draws on the accumulated experience to supervise the student on its own rollouts, enabling student to progressively internalize procedural knowledge within its parameters. The central design principle is co-evolution: the policy generates rollouts that update the memory, and memory shapes the supervision that updates the policy. Empirically, across Qwen3-8B and OLMo3-Instruct-7B, PMD improves over SDPO by 3.8-5.5% on SCIKNOWEVAL and 7.9-13.6% on LIVECODEBENCH. Co-evolution powers these gains: freezing either the memory or the policy trails PMD by more than 10% across SCIKNOWEVAL domains.

## Metadata
- **Published**: 2026-07-01T21:20:57Z
- **Authors**: Ye Liu, Srijan Bansal, Bo Pang, Yang Li, Zeyu Leo Liu, Yifei Ming, Zixuan Ke, Shafiq Joty, Semih Yavuz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.01480v1)