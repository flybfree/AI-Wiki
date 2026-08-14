---
title: I-SDPO: Instance-Level Adaptive Self-Distillation Policy Optimization
url: http://arxiv.org/abs/2608.12957v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_08-37-24Z_I_SDPO_Instance_LevelAdaptiveSelf_DistillationPoli.md
generated_at: 2026-08-13 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces I‑SDPO, an instance‑level adaptive self‑distillation policy optimization method that addresses the limitation of GRPO when all sampled responses are incorrect. By routing teacher reliance to groups with uninformative relative rewards and reducing it as success probability rises, I‑SDPO improves performance on scientific QA tasks, raising average mean@16 accuracy from 56.67% to 70.31%.

## Key Takeaways
- Teacher reliance is made capability dependent: only groups where all responses are wrong trigger privileged self‑distillation, providing a dense token supervision signal when relative rewards are absent.
- The routing rule automatically lowers the distillation weight as success probability increases, preventing a biased surrogate from overriding reward‑improving updates and avoiding an optimization bias floor.
- I‑SDPO achieves the best results across all four scientific domains on SciKnowEval, delivering an 18.24‑point gain in mean@16 accuracy compared with GRPO.

## Context
Self‑distillation is a powerful technique for improving reinforcement learning policies by leveraging teacher models to generate high‑quality examples. However, when the teacher’s influence remains constant regardless of success rates, it can create undesirable bias and hinder policy updates. I‑SDPO’s adaptive routing offers a principled way to align distillation with actual capability, aligning with broader efforts toward more robust and sample‑efficient RL.

## Implications
For practitioners developing scientific or domain‑specific AI agents, I‑SDPO demonstrates that teacher guidance should be conditional on performance, not fixed throughout training. This approach can reduce overfitting to a biased surrogate and lead to higher generalization, offering a practical improvement for industry applications where reliable, high‑accuracy responses are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12957v1)
