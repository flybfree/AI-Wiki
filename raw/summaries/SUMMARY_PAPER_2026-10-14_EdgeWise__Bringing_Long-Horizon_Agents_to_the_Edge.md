---
title: EdgeWise: Bringing Long-Horizon Agents to the Edge via Selective Cloud Delegation
url: http://arxiv.org/abs/2610.17560v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_01-32-16Z_EdgeWise_BringingLong_HorizonAgentstotheEdgeviaSel.md
generated_at: 2026-10-14 00:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
EdgeWise is an edge-cloud collaboration framework that addresses the high inference cost of running frontier LLMs for every step of long-horizon agent tasks. The authors demonstrate that delegating only a small subset of critical steps to a cloud LLM while using a smaller language model (SLM) locally can match or exceed full LLM performance, achieving up to 62% cost reduction on SWE-Rebench and 34% on Terminal-Bench 2.1. The framework introduces a step-level reinforcement learning method that jointly optimizes task solving and delegation decisions with fine-grained credit assignment, enabling autonomous delegation without additional models at inference time.

## Key Takeaways
- The core finding is that not all steps in a long-horizon agent trajectory require frontier-level model capability; selectively allocating the LLM to only key steps achieves performance comparable to full LLM execution while dramatically reducing inference cost. This challenges the assumption that uniform model capability across all steps is necessary for strong agent performance.
- EdgeWise introduces a step-level RL method that jointly optimizes task solving and delegation decisions, incorporating fine-grained credit assignment for individual delegation choices. This enables the system to autonomously decide when to delegate to the cloud without requiring additional classifier or routing models at inference time, reducing architectural complexity.
- The authors systematically investigate critical design choices in edge-cloud collaboration through an external judge-based delegation strategy, examining when to delegate, how delegation decisions should be made, what context should be shared between edge and cloud, and how frequently the cloud LLM should be invoked. These ablations provide a principled understanding of the tradeoffs involved in hybrid agent architectures.

## Context
This work sits at the intersection of efficient inference, agentic AI systems, and edge computing—three rapidly growing areas where cost and latency constraints increasingly limit deployment. As long-horizon agents for software engineering, terminal operations, and complex planning become mainstream, the per-step inference cost of frontier models becomes a practical bottleneck for on-device and privacy-sensitive applications. EdgeWise contributes a principled framework for hybrid model routing that could inform how the broader community designs cost-aware agent pipelines without sacrificing task performance.

## Implications
For practitioners deploying agentic systems in resource-constrained environments—such as local workstations, mobile devices, or privacy-sensitive enterprise settings—EdgeWise offers a concrete blueprint for reducing cloud inference costs by up to 62% while maintaining competitive task performance. The systematic ablation study of delegation strategies provides actionable guidance for engineers designing hybrid edge-cloud agent architectures, and the RL-based delegation mechanism suggests a path toward self-optimizing agent systems that learn their own cost-performance tradeoffs over time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17560v1)
