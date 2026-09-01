---
title: Learning Where Outcomes Change:Credit-Addressable Reasoning for Multimodal Geometry
url: http://arxiv.org/abs/2608.30457v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_08-44-36Z_LearningWhereOutcomesChange_Credit_AddressableReas.md
generated_at: 2026-08-31 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces credit-addressable reasoning for multimodal geometry, enabling precise visual relation extraction and multi-step deduction by assigning credit to specific semantic units. It demonstrates two methods Code-CoT and CE-GRPO achieving 76.04% average accuracy on nine benchmarks, beating prior models.

## Key Takeaways
- The framework defines where learning compares alternatives as the semantic unit exposed during inference.
- Code-CoT retains diagrams and represents relations as line-addressable executable code organized into typed events.
- CE-GRPO selects event boundaries using structural priors and type-normalized entropy to convert outcome differences into localized advantages.

## Context
This work addresses a longstanding challenge in multimodal reasoning where free-form traces obscure decision pathways. By integrating representation optimization with reinforcement learning, the authors provide a more interpretable and scalable approach for complex geometry tasks.

## Implications
The method could be applied beyond geometry to any domain requiring step-by-step deduction, offering tools that clarify model reasoning and improve performance on long dependency chains. Practitioners may adopt credit-addressable techniques to enhance transparency and efficiency in large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30457v1)
