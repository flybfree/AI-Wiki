---
title: Zing: Social Mind for LLMs
url: http://arxiv.org/abs/2607.23740v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_16-25-45Z_Zing_SocialMindforLLMs.md
generated_at: 2026-07-27 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Zhijing, a framework that measures social intelligence in large language models and demonstrates how to internalize it with Zing training and deploy grounding via Actio. Evaluation on SoMBench shows modest performance gaps but significant room for improvement across dimensions. The full harness improves most model‑benchmark pairs.

## Key Takeaways
- SoMBench provides a psychology‑grounded benchmark covering 71 task paradigms, revealing that no secondary dimension exceeds 90% accuracy even with the best models.
- Zing training combines supervised fine‑tuning, on‑policy distillation, and rubric‑based reinforcement learning to boost social cognition across five benchmarks.
- The Actio harness routes four supports—PRISM, Starling, SAGE, gated RAG—to reasoning, improving 14 of 15 model‑benchmark pairs.

## Context
Social intelligence is a critical capability for LLMs moving from isolated tasks to long‑term human interaction. Existing benchmarks lack depth and few methods address deployment‑time grounding, highlighting a gap in current research.

## Implications
These findings suggest that evaluating social cognition must be systematic and that training pipelines should integrate reinforcement learning with external knowledge sources. Practitioners can adopt the Actio harness to achieve measurable gains without sacrificing model size.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23740v1)
