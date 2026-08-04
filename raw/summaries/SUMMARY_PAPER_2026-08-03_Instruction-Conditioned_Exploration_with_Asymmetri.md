---
title: Instruction-Conditioned Exploration with Asymmetric Reinforcement Learning and Self-Distillation
url: http://arxiv.org/abs/2608.02087v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_11-47-52Z_Instruction_ConditionedExplorationwithAsymmetricRe.md
generated_at: 2026-08-03 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Instruction-Conditioned Exploration (ICE) and Asymmetric-RL/SD to improve LLM training by adding diverse instruction prompts during reinforcement learning. It achieves a 5% pass@1 gain on Qwen3-1.7B at 4K response length for math reasoning, with benefits extending to 8K context.

## Key Takeaways
- ICE augments task prompts with multiple instructions to broaden behavioural coverage in RL training.
- Asymmetric-RL/SD combines reinforcement learning with self-distillation to transfer learned behaviours to the unconditioned test-time policy.
- The method yields a consistent 5% improvement on held-out tasks, demonstrating that instruction conditioning and distillation can boost LLM reasoning performance.

## Context
Current LLMs rely heavily on pre-trained knowledge but struggle to explore new task spaces effectively. Classical RL assumes discrete action spaces, which does not map well to the continuous prompt space of language models. This work addresses the gap by designing a training regime that explicitly conditions exploration on instruction prompts.

## Implications
The results suggest that integrating instruction conditioning with self-distillation can be a scalable way to enhance LLM capabilities without retraining from scratch. Practitioners may adopt this framework to improve performance in downstream reasoning tasks, especially where long-context handling is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02087v1)
