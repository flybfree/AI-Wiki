---
title: Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback
url: http://arxiv.org/abs/2608.17587v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_09-52-48Z_Write_Execute_Refine_FromSkillFollowerstoSkillOpti.md
generated_at: 2026-08-18 22:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces WER, a multi‑phase reinforcement learning framework that trains a Skill Optimizer to generate natural language skills for tool‑using agents, improving performance beyond the baseline of no skill. The optimizer proposes skills, a frozen executor runs them repeatedly, and a verifier scores outcomes; the resulting credit is used to refine future states by matching successful and failed trajectories. On benchmark suites BFCL v4 and tau2‑bench, WER raises Pass@1 by 7.80 and 3.85 points respectively.

## Key Takeaways
- The gap between expert‑written skills and agent‑generated ones stems from the need to learn from execution evidence rather than merely following procedures.  
- Execution feedback is captured through a verifier that assigns relative credit, enabling the optimizer to select mixed‑outcome records for refinement.  
- Training the 4B optimizer yields significantly higher Pass@1 scores and outperforms both no‑skill baselines and non‑optimized backbones.

## Context
The field of AI agents increasingly relies on natural language instructions to operate software tools, yet current methods often fail to translate human expertise into effective agent behavior. This work addresses the limitation that static skill generation does not leverage real‑world execution outcomes, highlighting a need for continual learning mechanisms within reinforcement learning pipelines.

## Implications
For practitioners developing autonomous tool users, WER offers a scalable way to embed expert knowledge and adapt it through feedback loops. The approach could be integrated into larger AI systems to maintain high performance without retraining large models from scratch.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17587v1)
