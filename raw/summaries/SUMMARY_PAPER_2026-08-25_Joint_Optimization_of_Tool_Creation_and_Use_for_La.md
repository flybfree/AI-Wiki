---
title: Joint Optimization of Tool Creation and Use for Large Language Model Agents
url: http://arxiv.org/abs/2608.24571v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_13-59-34Z_JointOptimizationofToolCreationandUseforLargeLangu.md
generated_at: 2026-08-25 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SMITH, a reinforcement learning framework that jointly optimizes the creation and use of tools for large language model agents. The authors demonstrate that their approach achieves state‑of‑the‑art performance on procedural reasoning tasks, surpassing both larger models and untrained baselines.

## Key Takeaways
- SMITH trains tool generation and invocation within a single policy, eliminating the need for separate frozen LLMs to write tools and use them.  
- The framework uses three reward axes—schema, code, and outcome—to capture failures independently, providing clear gradient signals for each failure mode.  
- On 13 procedural reasoning tasks with exact verifiers, SMITH reaches a macro‑average accuracy of 79.8%, the highest score among all evaluated methods and ahead of an untrained 30B‑A3B tool writer.

## Context
Tool‑augmented language models face limitations because human‑written APIs constrain what can be invoked, and existing systems often separate model components, leading to misaligned schemas. This paper addresses that gap by integrating tool creation and use in a unified training loop, reflecting broader efforts toward self‑improving agents.

## Implications
The results suggest that joint optimization can unlock higher reasoning capabilities without requiring massive visual or tabular data, encouraging industry adoption of more efficient, modular tooling for LLM deployment. Practitioners may leverage SMITH’s framework to reduce development time and improve performance across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24571v1)
