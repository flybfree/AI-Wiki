---
title: REGEN: Replay-recycling for Expert-to-Generalist distillation with Offline Reinforcement Learning
url: http://arxiv.org/abs/2607.19450v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_13-36-23Z_REGEN_Replay_recyclingforExpert_to_Generalistdisti.md
generated_at: 2026-07-23 22:59
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces REGEN, a method that uses replay memory from expert RL training to train generalist models via offline reinforcement learning, decoupling rollout sampling and backpropagation. It achieves performance comparable to multi-teacher on-policy distillation while reducing computational cost. The approach transforms online RL into data synthesis.

## Key Takeaways
- REGEN recycles the replay memory generated during teacher-specific RL training instead of collecting new experience, eliminating the need for costly online rollouts.
- By using offline reinforcement learning algorithms, REGEN separates sampling from gradient computation, greatly lowering training cost and computational load.
- The method matches MOPD accuracy on tasks like mathematical reasoning, code generation, and instruction following while operating at a fraction of the expense.

## Context
Large-scale RL remains prohibitive due to high compute and data requirements, limiting its use across diverse domains. Existing techniques such as MOPD still rely on online rollouts that strain infrastructure. This work offers a scalable alternative by leveraging existing replay buffers.

## Implications
Practitioners can integrate RL knowledge into post‑training pipelines without heavy resource allocation, enabling more frequent updates and broader task coverage. The shift toward data synthesis could democratize advanced LLM capabilities across industries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19450v1)
