---
title: SemPIC: Learning Semantic Position-Independent KV Caches
url: http://arxiv.org/abs/2607.28069v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_11-45-24Z_SemPIC_LearningSemanticPosition_IndependentKVCache.md
generated_at: 2026-07-30 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
SemPIC introduces a method for learning position‑independent KV caches that reuse document information across tasks, improving retrieval performance. The approach trains a lightweight Writer to generate per‑layer KVs while keeping the pretrained Reader unchanged. Across three models and four tasks, SemPIC raises mean micro‑F1 from 0.53 to 0.60, approaching full recompute at 0.62. The method also preserves the standard KV interface, ensuring compatibility with existing decoding frameworks.

## Key Takeaways
- Learned per‑layer KVs are compiled offline using behavioral distillation, allowing reuse without altering the decoder.
- Gradient checkpointing stores cached KVs to cut peak memory while keeping gradients intact during training.
- Micro‑F1 improves from 0.53 to 0.60 across diverse models and tasks, nearing full recompute scores.

## Context
Long‑context retrieval and agentic workloads often require reusing the same documents under varying instructions and orderings. Traditional prefix caching fails to capture this reuse, leaving position‑independent caching unreliable. SemPIC addresses these limitations by adapting document representations rather than just modifying cache structures.

## Implications
The technique reduces memory usage while preserving decoding speed, offering a scalable solution for large language models handling long histories. Practitioners can adopt SemPIC without modifying model architectures or training pipelines, making it practical for industry deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28069v1)
