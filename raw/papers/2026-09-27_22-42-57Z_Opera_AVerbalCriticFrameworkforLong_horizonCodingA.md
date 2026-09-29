---
title: Opera: A Verbal Critic Framework for Long-horizon Coding Agents
published: 2026-09-27T22:42:57Z
authors: Kai Mei, Zhiyuan Hu, Yutong Dai, Juntao Tan, Yifan Zhang, Dingjie Song, Dimitris N. Metaxas, Silvio Savarese, Ran Xu, Zeyuan Chen
url: http://arxiv.org/abs/2609.33987v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Opera: A Verbal Critic Framework for Long-horizon Coding Agents

## Abstract
Long-horizon coding agents need timely corrections, yet feedback can be ineffective or even harmful when it misjudges ongoing work or fails to address the underlying problem. Existing critics focus on evaluating trajectories and generating feedback, but rarely track what happens after feedback is delivered. We present Opera, a verbal critic framework that treats each correction as a persistent note, followed until the diagnosed problem is resolved. Opera decides when to review through periodic and event-driven triggers, diagnoses issues with typed operators, audits feedback against visible evidence before delivery, and tracks the agent's subsequent actions to distinguish mere compliance from actual resolution. As a test-time critic, Opera improves the resolve rate of non-critic agents by up to 12.4, 15.0, and 8.9 percentage points on Terminal-Bench 2.1, a SWE-Bench Pro subset, and DeepSWE v1.1, respectively, across four policy models, and achieves the highest mean resolve rate among competitive critic baselines on all three benchmarks, and also improves policy models when the policy critiques itself. Beyond inference, Opera-guided rollouts provide approximately on-policy training data: fine-tuning Qwen3.5-9B on them improves its resolve rate on held-out SWE-Bench Pro repositories by 10.2 percentage points without a critic at inference time, matching fine-tuning on rollouts from a stronger model, while preserving its performance when switching harness, i.e., from Openhands to Terminus-2, which the latter substantially degrades.

## Metadata
- **Published**: 2026-09-27T22:42:57Z
- **Authors**: Kai Mei, Zhiyuan Hu, Yutong Dai, Juntao Tan, Yifan Zhang, Dingjie Song, Dimitris N. Metaxas, Silvio Savarese, Ran Xu, Zeyuan Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33987v1)