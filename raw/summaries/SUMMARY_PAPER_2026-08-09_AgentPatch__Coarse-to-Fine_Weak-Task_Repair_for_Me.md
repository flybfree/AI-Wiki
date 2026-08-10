---
title: AgentPatch: Coarse-to-Fine Weak-Task Repair for Merging Agentic Multimodal Large Language Models
url: http://arxiv.org/abs/2608.06699v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_01-52-45Z_AgentPatch_Coarse_to_FineWeak_TaskRepairforMerging.md
generated_at: 2026-08-09 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AgentPatch, a training-free repair method for merging agentic multimodal large language models that suffers from uneven capability preservation and behavior-critical forgetting. It restores weak-task-specific signals using Weak-Task Unique Residual Recovery and recovers decisive actions via an Agent-Guided Behavior-Critical Patch, yielding a single static checkpoint.

## Key Takeaways
- The framework addresses asymmetric capability preservation by selectively preserving tasks with high interaction complexity while mitigating degradation of weaker tasks.
- It employs Weak-Task Unique Residual Recovery to restore diluted weak-task signals without retraining the merged model.
- An Agent-Guided Behavior-Critical Patch protects decisive behaviors and recovers lost actions under explicit capability protection.

## Context
Agentic multimodal models aim to combine vision, language, and planning into a unified agent but current approaches create fragmented performance across tools. This work advances consolidation research by providing a repair strategy that maintains both perception and reasoning capabilities in a single checkpoint.

## Implications
For practitioners seeking generalist agents, AgentPatch offers a practical solution to merge specialized components without costly fine-tuning. The method could enable scalable deployment of multimodal agents across diverse environments while preserving critical decision-making abilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06699v1)
