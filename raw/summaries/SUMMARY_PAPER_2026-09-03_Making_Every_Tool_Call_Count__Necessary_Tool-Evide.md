---
title: Making Every Tool Call Count: Necessary Tool-Evidence Path Rewards for Agentic Vision-Language Models
url: http://arxiv.org/abs/2609.03493v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_07-52-56Z_MakingEveryToolCallCount_NecessaryTool_EvidencePat.md
generated_at: 2026-09-03 20:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces NTEP, a new annotation scheme that defines the necessary external evidence and required tool calls for each image-grounded query in agentic vision-language models. It also proposes NTEP‑R, a reward function that ensures every tool invocation directly advances reasoning toward the final answer. Experiments show that an 8B‑parameter model using NTEP improves both accuracy on search tasks and efficiency of tool use.

## Key Takeaways
- Models often issue redundant or off‑target tool calls because training rewards only final correctness, not evidence gathering.
- Even when appropriate tools are called, models may fail to extract the needed information from observations.
- The non‑repeated‑goal regularizer penalizes repeated calls that revisit already satisfied NTEP goals.

## Context
Agentic vision-language models aim to combine visual perception with external knowledge retrieval. Current training pipelines treat tool use as a black box, leading to inefficient or inaccurate evidence acquisition. This work provides a principled supervision method that aligns tool behavior with the underlying reasoning pipeline.

## Implications
Fine‑grained tool‑evidence path supervision can make agentic VLMs more reliable and cost‑effective in real applications. Practitioners can adopt NTEP as a training framework to reduce redundant calls and improve performance across diverse benchmarks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03493v1)
