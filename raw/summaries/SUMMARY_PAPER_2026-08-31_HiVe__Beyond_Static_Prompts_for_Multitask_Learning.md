---
title: HiVe: Beyond Static Prompts for Multitask Learning via Hierarchy-based Vertical Mixture-of-Experts
url: http://arxiv.org/abs/2608.29790v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_13-35-42Z_HiVe_BeyondStaticPromptsforMultitaskLearningviaHie.md
generated_at: 2026-08-31 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
HiVe introduces a prompt‑tuning framework that models prompts at multiple hierarchical levels and uses a vertical mixture‑of‑experts mechanism to compose input‑specific prompts during inference. Experiments show HiVe outperforms existing prompt‑tuning baselines across diverse tasks, demonstrating its effectiveness in parameter‑efficient fine‑tuning.

## Key Takeaways
- HiVe builds a dynamic prompt hierarchy that adapts specialization based on task relationships learned during training.
- The vertical mixture‑of‑experts (V‑MoE) selects the most appropriate level of prompt composition at inference, enabling input‑dependent optimization.
- The framework consistently achieves higher performance than flat or fixed hierarchical prompt methods across multiple tasks.

## Context
Large language models face challenges in fine‑tuning without full parameter updates, making prompt tuning a popular yet limited solution. Traditional approaches either use static prompts or rigid hierarchies that cannot specialize per input. HiVe addresses these gaps by introducing adaptable, hierarchy‑based prompting.

## Implications
This work provides a scalable method for deploying specialized language models with minimal compute cost, encouraging industry adoption of efficient fine‑tuning pipelines. Practitioners can leverage hierarchical prompt design to improve task performance without retraining large parameter sets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29790v1)
