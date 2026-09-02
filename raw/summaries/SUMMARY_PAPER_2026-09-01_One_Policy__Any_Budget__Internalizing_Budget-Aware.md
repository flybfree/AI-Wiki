---
title: One Policy, Any Budget: Internalizing Budget-Aware Search via Reinforcement Learning
url: http://arxiv.org/abs/2609.00813v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_07-12-32Z_OnePolicy_AnyBudget_InternalizingBudget_AwareSearc.md
generated_at: 2026-09-01 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AnySearch, a reinforcement learning framework that lets a single policy handle search under any budget constraint by first training with explicit budget state injection and structured prompts, then removing the scaffold for autonomous operation. Experiments on seven QA benchmarks show the method outperforms baselines across all budgets, generalizes to unseen constraints, and maintains high tool productivity while minimizing token overhead.

## Key Takeaways
- The framework uses a curriculum reinforcement learning approach that first trains with budget state injection and structured reasoning prompts under linearly decaying budgets.
- A composite reward couples answer accuracy with budget efficiency using adaptive weights that amplify efficiency for high‑accuracy queries and attenuate it for low‑accuracy ones.
- The method generalizes to unseen budget constraints beyond the training range, achieving superior tool productivity without excessive token overhead.

## Context
Current LLM search agents rely on fixed budgets during training, limiting their ability to adapt when real‑world constraints vary. This work addresses that limitation by designing a flexible policy that can operate under any budget without retraining, reflecting broader trends toward adaptive and resource‑aware AI systems.

## Implications
For practitioners, AnySearch provides a deployable solution that reduces token waste while maintaining accuracy across diverse query budgets, potentially lowering costs in large‑scale applications. In industry, it enables scalable search agents that can be customized to different budget scenarios without additional engineering effort.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00813v1)
