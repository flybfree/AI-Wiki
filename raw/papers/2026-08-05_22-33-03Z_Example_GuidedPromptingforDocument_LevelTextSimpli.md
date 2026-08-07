---
title: Example-Guided Prompting for Document-Level Text Simplification
published: 2026-08-05T22:33:03Z
authors: Marina Litvak, Ariel Perstin, Ilan Shtilman, Michael Färber
url: http://arxiv.org/abs/2608.05447v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Example-Guided Prompting for Document-Level Text Simplification

## Abstract
Document-level text simplification requires large language models (LLMs) to rewrite complex documents while preserving meaning, readability, and discourse coherence. Although prompt-based LLMs have shown promising performance, they often produce inconsistent simplifications because textual instructions alone provide limited guidance for complex document-level transformations. We investigate whether retrieved document-simplification examples can improve document-level generation by augmenting prompts with examples selected from a parallel simplification corpus. This example-guided prompting approach enables LLMs to exploit relevant simplification patterns without task-specific fine-tuning. Experiments on the OneStopEnglish corpus using multiple state-of-the-art LLMs show that incorporating retrieved examples consistently improves simplification quality over prompt-only generation and achieves competitive or superior performance compared with representative supervised (T5) and planning-based (PlanSimp) document simplification systems. Furthermore, we find that the benefits of example-guided prompting vary across LLMs, suggesting that effective use of retrieved examples depends on a model's ability to integrate contextual information during generation.

## Metadata
- **Published**: 2026-08-05T22:33:03Z
- **Authors**: Marina Litvak, Ariel Perstin, Ilan Shtilman, Michael Färber
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05447v1)