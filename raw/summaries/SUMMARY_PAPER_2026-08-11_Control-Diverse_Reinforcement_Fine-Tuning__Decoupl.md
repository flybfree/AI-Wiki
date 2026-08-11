---
title: Control-Diverse Reinforcement Fine-Tuning: Decoupling the Shared Control Bottleneck of RL Post-Training
url: http://arxiv.org/abs/2608.08224v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_16-44-47Z_Control_DiverseReinforcementFine_Tuning_Decoupling.md
generated_at: 2026-08-11 12:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Control-Diverse Reinforcement Fine-Tuning to decouple shared activation from task-specific control in reinforcement learning post-training of LLMs, showing that a small activation-control gap leads to collapsed capability across tasks and proposing a regularizer to mitigate this.

## Key Takeaways
- The Shared Control Bottleneck measures how much control each component contributes versus activation, revealing that highly shared activations can coexist with task-specific control.
- An Activation-Control Gap indicates loss of task specificity when control collapses onto a single direction.
- CD-RFT regularizes the post-training loss using this bottleneck, achieving large control decoupling and better multi-task performance than matched GRPO.

## Context
Reinforcement learning fine-tuning improves LLM reasoning but often lacks insight into internal changes; understanding whether improvements stem from activation or control is crucial for reliable scaling and task adaptation in large language models.

## Implications
This framework provides a diagnostic tool to detect when RL post-training loses task diversity, guiding safer regularization strategies. Practitioners can use the bottleneck metric to balance capability gains with generalization across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08224v1)
