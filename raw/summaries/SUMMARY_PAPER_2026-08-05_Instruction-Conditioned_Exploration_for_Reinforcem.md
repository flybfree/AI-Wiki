---
title: Instruction-Conditioned Exploration for Reinforcement Learning with Self-Distillation to an Unconditioned Policy
url: http://arxiv.org/abs/2608.02087v2
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_11-47-52Z_Instruction_ConditionedExplorationforReinforcement.md
generated_at: 2026-08-05 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Instruction-Conditioned Exploration (ICE), a method that augments reinforcement learning for large language models by appending a fixed set of instructions to task prompts, thereby broadening the behaviours the model attempts during training. The approach pairs instruction‑conditioned RL with self‑distillation, where correct rollouts are distilled into an unconditioned test‑time policy, improving performance on held‑out tasks such as mathematical reasoning at 4K and 8K response lengths.

## Key Takeaways
- ICE enhances Qwen3-1.7B’s hold‑out pass@1 by 5.0% compared with DAPO training, showing that a small instruction set can significantly broaden exploration coverage.  
- The improvement persists up to an 8K context length, indicating robustness of the method across longer generation tasks.  
- No benefit is observed for Qwen3-4B at 4K responses, suggesting that larger models may already cover diverse behaviours without additional instructions.

## Context
The integration of instruction‑conditioned exploration addresses a gap in RL for LLMs where action spaces are high‑dimensional and opaque. By leveraging the model’s pre‑training knowledge to guide sampling, ICE aligns training with human‑like task diversity, moving beyond standard reward‑maximization strategies that often lead to narrow behavior.

## Implications
For industry practitioners, ICE offers a low‑cost way to improve model reliability on complex reasoning tasks without retraining from scratch. It also provides a template for future work that combines instruction tuning with self‑distillation, potentially enabling more efficient and effective deployment of large language models in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02087v2)
