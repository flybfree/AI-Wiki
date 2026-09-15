---
title: LIMBO: Lifelong Inference-Time Memory and Budget Optimization for LLM Agents
published: 2026-09-12T20:39:45Z
authors: Siddharth Sharma, Nilesh Prasad Pandey, Onat Gungor, Tajana Rosing
url: http://arxiv.org/abs/2609.14138v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LIMBO: Lifelong Inference-Time Memory and Budget Optimization for LLM Agents

## Abstract
As LLM agents become integrated into increasingly complex workflows, they must continually acquire new capabilities while retaining competence on previously learned tasks. Lifelong agents address this through experience replay, injecting past interactions into the prompt to leverage prior experience during inference. However, replay is not free: every replayed trajectory competes with retrieval, reasoning, tool use, and verification for the same limited prompt and compute budget, making effective resource allocation essential. Existing approaches allocate these resources using fixed replay policies, regardless of whether replay is beneficial for the current task. We identify this as inference-time memory allocation, a distinct problem class for lifelong agents, and introduce LIMBO: the first online framework to our knowledge that treats memory as a controllable inference-time resource and jointly optimizes memory strategy and inference budget for each incoming task. Unlike prior approaches that fix the replay policy or require model weights, teacher supervision, or offline retraining, LIMBO learns this allocation online in a single pass, explicitly balancing task performance and inference cost without modifying the underlying agent. Across three LLM backbones on LifelongAgentBench, LIMBO achieves better cost-accuracy tradeoffs than state-of-the-art memory-augmented baselines and nearly matches all strongest such baselines at up to ~83% lower inference cost (~53% on average). LIMBO adapts its policy across models and environments without retraining, demonstrating that effective allocation can be learned online rather than manually specified.

## Metadata
- **Published**: 2026-09-12T20:39:45Z
- **Authors**: Siddharth Sharma, Nilesh Prasad Pandey, Onat Gungor, Tajana Rosing
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14138v1)