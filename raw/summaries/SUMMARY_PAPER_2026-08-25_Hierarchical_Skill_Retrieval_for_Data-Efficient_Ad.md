---
title: Hierarchical Skill Retrieval for Data-Efficient Adaptation of Vision-Language-Action Models
url: http://arxiv.org/abs/2608.24042v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_04-04-49Z_HierarchicalSkillRetrievalforData_EfficientAdaptat.md
generated_at: 2026-08-25 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Hierarchical Skill Retrieval (HSR) to improve data-efficient adaptation of vision-language-action models for robot manipulation. It degrades when adapting to new tasks with few demonstrations, so the authors propose a retrieval framework that decomposes tasks into skill sequences and selects plans based on semantic plausibility and reliability. Experiments show HSR raises success rates by 10.3% and 21.3% over baselines.

## Key Takeaways
- The method separates subtask-level language retrieval from behavior-feature reranking to find demonstrations that match both semantics and task compatibility.
- Skill decomposition is evaluated using prior dataset estimates, allowing reuse of reliable skills even when full task matches are absent.
- A two-stage pretraining and finetuning pipeline enables general skill acquisition followed by fine-tuned adaptation.

## Context
Vision-language-action models excel on large robot datasets but struggle with limited new data. Retrieval techniques that ignore hierarchical structure often fail to capture reusable skills across tasks. This work addresses the gap by modeling long-horizon manipulation as composable skills, offering a more structured approach to data efficiency.

## Implications
For industry practitioners, HSR reduces reliance on extensive task-specific datasets, lowering development cost and time. For researchers, it provides a template for hierarchical retrieval in multimodal robotics, encouraging decomposition of complex tasks into reusable components.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24042v1)
