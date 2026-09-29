---
title: The Right Lesson at the Right Step: Deriving Control Updates for Self-Evolving Agents
url: http://arxiv.org/abs/2609.34988v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_11-59-22Z_TheRightLessonattheRightStep_DerivingControlUpdate.md
generated_at: 2026-09-28 22:53
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces EvoCUE, a framework that enables self-evolving agents to learn and apply localized control updates rather than relying on global memory mechanisms. By representing agent workflows as explicit state-machine controllers, EvoCUE derives precise instruction or skill edits from past execution traces and applies them at specific decision points to improve future performance. Experimental results demonstrate significant improvements in long tool-use environments by effectively transferring learned conventions across tasks without requiring benchmark-specific onboarding.

## Key Takeaways
- EvoCUE addresses the limitation of global prompts and memories by treating experience reuse as a localized control problem, using an explicit state-machine representation where nodes correspond to model or tool calls and edges define transitions; this structure allows each update to specify exactly what changes, where it acts, and when it applies within the workflow.
- The framework extracts candidate edits from completed trajectories using residual goals and observed execution traces, then rigorously evaluates each edit by resuming both parent and edited controllers from the same checkpoint to

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34988v1)
