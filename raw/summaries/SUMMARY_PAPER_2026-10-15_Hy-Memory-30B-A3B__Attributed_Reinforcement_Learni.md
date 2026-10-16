---
title: Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing
url: http://arxiv.org/abs/2610.22196v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_16-46-47Z_Hy_Memory_30B_A3B_AttributedReinforcementLearningf.md
generated_at: 2026-10-15 23:06
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Hy-Memory-30B-A3B introduces a compact 30-billion-parameter language model (with approximately 3 billion active parameters) purpose-trained to serve as a long-term memory writer across multiple external-memory frameworks, including Mem0, MemOS, and Hy-Memory. The model is trained using a two-stage pipeline—Memory On-Policy Distillation followed by Memory Reinforcement Learning with attributed cross-chunk rewards and chunk-level GRPO—and achieves a 55.49% macro average on fixed 20% benchmark subsamples, surpassing Claude Opus 5's 54.62% across all four evaluated harnesses, including a held-out framework (EverMemOS) not seen during training.

## Key Takeaways
- The paper identifies a critical bottleneck in external-memory systems: the "write path," where a model must decide what information to retain, how precisely to encode it, and how new evidence should update persistent memory state. Existing approaches rely on general-purpose LLMs behind framework-specific prompts, which inflates serving costs and prevents transfer across protocols. Hy-Memory-30B-A3B addresses this by training a single specialized writer that operates across established memory frameworks without per-framework prompt engineering.
- The training methodology combines Memory On-Policy Distillation, which teaches framework-specific write protocols on student-generated states, with Memory RL that optimizes downstream answerability through dense per-chunk probes, attributed cross-chunk rewards, over-storage controls, and chunk-level GRPO. Carrying policy-written memory banks across training windows ensures the model's behavior during training matches its deployment-time behavior, reducing distribution shift.
- Despite being a compact model, Hy-Memory-30B-A3B ranks first on all four evaluated harnesses, including the held-out EverMemOS benchmark, demonstrating that specialized training on memory-writing tasks can outperform much larger general-purpose models like Claude Opus 5 on memory-specific evaluation metrics.

## Context
External-memory augmentation has become a central strategy for extending large language models beyond their fixed context windows, enabling applications in long-horizon reasoning, personalization, and multi-session dialogue. However, the field has largely treated the memory-writing component as a downstream task delegated to a general-purpose LLM with hand-crafted prompts, creating a fragmented ecosystem where each framework (Mem0, MemOS, Hy-Memory) requires its own prompt engineering and incurs high inference costs. This paper represents a shift toward training dedicated, compact memory-writing models that can generalize across frameworks, a direction that had been described as "largely unexplored" prior to this work.

## Implications
For practitioners deploying memory-augmented LLM systems, a specialized 30B model that outperforms frontier general-purpose models on memory-writing benchmarks suggests a path toward significantly lower serving costs and reduced latency in production memory pipelines. The cross-framework generalization demonstrated on held-out benchmarks indicates that such specialized writers could reduce the maintenance burden of maintaining separate prompt templates for each memory framework. For the broader research community, the attributed cross-chunk reward design and chunk-level GRPO approach offer a template for training models on structured, multi-step memory operations rather than single-turn generation, potentially informing future work on agentic memory management and long-context reasoning systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22196v1)
