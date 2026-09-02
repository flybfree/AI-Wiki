---
title: From Rollouts to Recipes: Self-Contained Post-Training for LLMs
url: http://arxiv.org/abs/2609.01422v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_15-36-26Z_FromRolloutstoRecipes_Self_ContainedPost_Trainingf.md
generated_at: 2026-09-01 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Self-Routing, a self-contained post-training method that adapts the optimization recipe for each sample based on rollout correctness and confidence. Experiments show it outperforms uniform GRPO, uniform OPSD, fixed mixtures, and simpler baselines on mathematical reasoning tasks with Qwen3 and Qwen3.5 backbones.

## Key Takeaways
- Self‑Routing routes samples to GRPO, self-distillation, regularization, or skipping depending on their behavior state, eliminating the need for external teachers or annotations.
- The routing distribution changes during training, reducing unnecessary updates on low-signal or already stable samples.
- Consistent improvement is observed across all baselines, indicating that adaptive optimization yields better performance.

## Context
Post-training fine-tuning traditionally applies a single recipe to all data, which can be inefficient and suboptimal. This work demonstrates that leveraging the model’s own rollout signals allows more nuanced training without external resources.

## Implications
Practitioners can implement Self-Routing to improve LLM performance with minimal overhead, supporting scalable fine-tuning pipelines. The approach may become a standard technique for adaptive post‑training in industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01422v1)
