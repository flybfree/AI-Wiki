---
title: On-Policy Distillation Meets Off-Policy GRPO: Training Compact Instruction-Following Rerankers
url: http://arxiv.org/abs/2609.01947v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_23-36-19Z_On_PolicyDistillationMeetsOff_PolicyGRPO_TrainingC.md
generated_at: 2026-09-02 20:54
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a two‑stage reinforcement learning framework that combines off‑policy teacher optimization with on‑policy student distillation for instruction‑following rerankers. The method trains a compact 1B student to generate rankings, then uses soft rewards from a larger 4B teacher evaluated by an LLM judge, achieving higher nDCG@6 and MRR@6 than offline methods.

## Key Takeaways
- Off‑policy GRPO strengthens the teacher using LLM‑judged feedback on 88K examples, enabling better ranking knowledge.  
- The student samples its own rankings and receives soft teacher rewards, coupling exploration with transfer.  
- On MAIR‑11 the student reaches 0.7670 nDCG@6, surpassing offline KD by four points.

## Context
The work addresses a key challenge in deploying large language models: producing compact yet high‑quality ranking outputs efficiently. By integrating RL into distillation pipelines, it moves beyond static imitation learning toward adaptive, on‑policy improvement.

## Implications
For practitioners, this approach offers a scalable way to fine‑tune smaller rerankers without sacrificing performance, especially under distribution shift. It could lower costs for real‑time applications while maintaining competitive quality scores across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01947v1)
