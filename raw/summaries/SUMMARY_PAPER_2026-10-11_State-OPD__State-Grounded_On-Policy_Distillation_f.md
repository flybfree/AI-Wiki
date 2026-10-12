---
title: State-OPD: State-Grounded On-Policy Distillation for Multi-Turn Agents
url: http://arxiv.org/abs/2610.13238v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_08-54-07Z_State_OPD_State_GroundedOn_PolicyDistillationforMu.md
generated_at: 2026-10-11 21:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces State-Grounded On-Policy Distillation (State-OPD), a framework for transferring reasoning capabilities from large frontier models to smaller student models in multi-turn agentic environments. The authors identify that student reasoning trajectories distort teacher supervision and limit action diversity, and propose grounding teacher supervision in interaction states rather than full reasoning traces. State-OPD achieves the highest macro-average success rates across ALFWorld, ScienceWorld, and WebShop benchmarks, with Qwen3-4B surpassing its Qwen3-32B teacher on ALFWorld Seen.

## Key Takeaways
- The authors decompose multi-turn agentic interactions into "interaction states" (the objective task plus executed action-observation records) versus the internal semantic trajectory of student reasoning. They demonstrate that at matched interaction states, removing prior student reasoning improves teacher continuation success and alters the teacher's token-level targets, with larger gains observed at later turns in a task. This reveals that prior reasoning acts as a distortion mechanism on teacher supervision.
- Resampling complete reasoning-action responses at a given state yields substantially greater action diversity than resampling only actions under a fixed reasoning trace. This finding motivates the core design of State-OPD: reallocating the sampling budget to generate multiple complete reasoning-action responses at states exhibiting high response entropy, while retaining full-history student generation for context.
- State-OPD raises Qwen3-4B's macro-average success from 26.07% (strongest baseline) to 31.74%, and notably surpasses its Qwen3-32B teacher on ALFWorld Seen. The method achieves higher task success with fewer supervised turn responses and substantially reduces persistent failed-action repetition, with qualitative traces showing decision revision based on interaction feedback.

## Context
On-Policy Distillation has proven effective for transferring reasoning from large models to smaller ones in single-turn settings, but multi-turn agentic tasks introduce compounding errors, state-dependent reasoning, and feedback loops that break the assumptions of standard OPD. This paper addresses a critical gap in the distillation literature by formalizing how student reasoning interacts with teacher supervision across sequential decision-making steps, bridging knowledge distillation research with the rapidly growing field of autonomous agent training.

## Implications
For practitioners deploying smaller language models as agents in tool-use, web navigation, or embodied task environments, State-OPD offers a principled training recipe that reduces reliance on expensive teacher supervision while improving task success and reducing repetitive failure loops. The finding that a 4B-parameter model can outperform its 32B teacher on specific agentic benchmarks signals that state-grounded training strategies may unlock capabilities that pure scale cannot, potentially reshaping how organizations allocate compute budgets for agent development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13238v1)
