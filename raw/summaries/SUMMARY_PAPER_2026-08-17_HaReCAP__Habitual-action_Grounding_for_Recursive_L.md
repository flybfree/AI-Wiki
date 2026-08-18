---
title: HaReCAP: Habitual-action Grounding for Recursive Large Language Model Agents
url: http://arxiv.org/abs/2608.16447v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_11-47-03Z_HaReCAP_Habitual_actionGroundingforRecursiveLargeL.md
generated_at: 2026-08-17 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces HaReCAP a low‑intrusion extension of ReCAP that reduces the repetitive leaf‑level grounding calls in recursive large language model agents. By reusing frequent decisions as offline rules, HaReCAP cuts token usage and LLM call overhead on long‑horizon tasks.

## Key Takeaways
- The final grounding step in ReCAP is called last‑mile redundancy which inflates token consumption during extended planning.
- HaReCAP builds auditable one‑step leaf‑reflex rules from successful trajectories to skip the LLM when a rule uniquely determines an action.
- Evaluation on Robotouille and ALFWorld shows reductions of 14.67%, 17.93% and 20.08% in token consumption respectively.

## Context
Recursive planning frameworks like ReCAP improve stability but suffer from high LLM call costs as they repeatedly ask the model to ground atomic subtasks. This overhead limits scalability for long‑horizon embodied AI agents.

## Implications
The reduction in token usage translates into lower compute costs and faster iteration cycles, encouraging broader adoption of recursive planning in industry‑grade robotics and autonomous systems where efficiency is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16447v1)
