---
title: Training Advisors for LLM Agents from Task Outcomes
url: http://arxiv.org/abs/2610.09858v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_11-14-26Z_TrainingAdvisorsforLLMAgentsfromTaskOutcomes.md
generated_at: 2026-10-07 21:09
model: qwen3.8-flash-next-iq3_xxs
---

## Summary

This paper introduces Caddie, a method for training natural-language critics that provide real-time advice to LLM agents during multi-step task execution. Rather than relying on step-level labels or human-written reference critiques, Caddie trains the critic through reinforcement learning using only the final task outcome—whether the agent ultimately succeeds after receiving the critic's feedback. The resulting Qwen3-4B critic demonstrates strong generalization, improving success rates across multiple base models and transferring to out-of-domain benchmarks without additional training.

## Key Takeaways

- Caddie trains critics using outcome-based reinforcement learning, meaning the critic is optimized purely on whether the agent succeeds after receiving its advice, rather than requiring expensive step-level annotations or reference critiques. This makes the training pipeline significantly more scalable and practical, as it only needs a binary success signal from the environment rather than detailed human-labeled reasoning traces.

- A single trained critic (Qwen3-4B) generalizes across four different base models of varying scales and architectures, including three models never seen during critic training. On the MuSiQue multi-hop question answering benchmark, the critic boosts Qwen3-4B's success rate by over 25 percentage points, even surpassing the performance of the much larger Kimi K3 model operating without any critic assistance.

- The trained critic transfers to entirely out-of-domain interactive benchmarks such as τ³ and DeepDive with no additional fine-tuning, and agents can autonomously decide when to seek the critic's help at inference time. This demonstrates that outcome-based critic training produces genuinely transferable guidance rather than domain-specific memorization.

## Context

LLM agents increasingly operate in complex, multi-step environments where they interleave reasoning with tool calls and must adapt to environmental observations. Prior research has explored natural-language feedback loops to help agents revise decisions mid-task, but these approaches typically depend on hand-crafted critiques or supervised step-level labels that are costly to obtain. Caddie addresses this bottleneck by showing that a critic can learn effective advisory behavior from the sparse signal of task success alone, aligning with the broader trend in AI research toward reinforcement learning from outcomes rather than dense supervision.

## Implications

For practitioners building agentic systems, Caddie offers a practical path to improving agent reliability without retraining or modifying the base model, since the critic operates as a frozen, plug-in component that can be swapped across different agent architectures. For the broader field, the cross-model and cross-domain transferability of a single outcome-trained critic suggests that advisory knowledge can be decoupled from the agent's own reasoning capabilities, potentially enabling shared critic services across heterogeneous agent ecosystems. This could reduce the engineering burden of building bespoke feedback mechanisms for each new agent deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09858v1)
