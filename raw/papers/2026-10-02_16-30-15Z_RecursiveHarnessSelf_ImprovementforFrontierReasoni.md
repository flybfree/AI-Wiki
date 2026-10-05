---
title: Recursive Harness Self-Improvement for Frontier Reasoning Data Synthesis
published: 2026-10-02T16:30:15Z
authors: Wenlong Zhang, Zhengbo Jiao, Chenxu Zhang, Lekang Jiang, SiYuan Ma, Qituan Zhang, Guo Chen, Linfeng Zhang
url: http://arxiv.org/abs/2610.03548v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recursive Harness Self-Improvement for Frontier Reasoning Data Synthesis

## Abstract
Generating progressively harder reasoning problems requires synthesis procedures that adapt as the task distribution evolves. Existing task-level recursion reuses generated problems as seeds but leaves the construction harness unchanged. We present task-harness co-evolution, a framework for recursive harness self-improvement (RSI) in reasoning-data synthesis. Online self-improvement converts intermediate solver failures into reusable skills during generation. Post-task self-improvement revises skills, prompts, and workflows after each batch, adopting candidates only when they generate harder valid tasks within a bounded cost increase. Model weights and verification criteria remain fixed. Across mathematics, coding, and science, mean solver accuracy decreases from 100.0% to 54.8% over fourteen evolution rounds. Ablations show that combining both update schedules produces harder tasks than fixed-harness recursion or either schedule alone. The resulting data improves downstream SFT and GRPO performance. In particular, a 27B student fine-tuned on 10K synthesized mathematics examples achieves 62.5% mean-16 accuracy on APEX, competitive with selected frontier-model references. These results support adapting the synthesis harness alongside the tasks to generate increasingly challenging data with downstream training value.

## Metadata
- **Published**: 2026-10-02T16:30:15Z
- **Authors**: Wenlong Zhang, Zhengbo Jiao, Chenxu Zhang, Lekang Jiang, SiYuan Ma, Qituan Zhang, Guo Chen, Linfeng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.03548v1)