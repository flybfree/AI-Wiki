---
title: Act More, Decide Less: Skill-Guided Adaptive Action Chunking for Long-Horizon LLM Agents
url: http://arxiv.org/abs/2609.02042v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_03-17-11Z_ActMore_DecideLess_Skill_GuidedAdaptiveActionChunk.md
generated_at: 2026-09-02 20:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SPACE, a method for training LLM agents to emit variable‑length action chunks instead of single primitives in long‑horizon tasks. Experiments on ALFWorld and ScienceWorld show that SPACE boosts success rates by 7%–31% over the strongest baseline while cutting average decision rounds by up to 79%.

## Key Takeaways
- Naively training chunk‑emitting policies with standard reinforcement learning fails because agents either collapse into single‑action behavior or produce excessively long sequences.  
- Both failures stem from the inability of the agent to learn appropriate chunk boundaries.  
- SPACE solves this by distilling chunk‑boundary supervision from trajectory‑induced programmatic skills and using hybrid on/off‑policy optimization with chunk‑aware credit assignment.

## Context
Long‑horizon interactive tasks require agents that can plan efficiently over many rounds, but the ReAct style of issuing one primitive per round leads to unnecessary replanning. Variable‑length action chunks could reduce computational load, yet existing RL approaches cannot reliably learn where a chunk should end. This work bridges that gap by leveraging programmatic skill extraction from successful trajectories.

## Implications
The results demonstrate that skill‑guided adaptive chunking can make LLM agents more effective and resource‑efficient for long tasks. Practitioners can adopt SPACE to lower latency, improve task success, and scale deployment without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02042v1)
