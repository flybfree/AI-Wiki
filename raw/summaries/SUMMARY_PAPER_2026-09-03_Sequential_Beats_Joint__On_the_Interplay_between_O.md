---
title: Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR
url: http://arxiv.org/abs/2609.04108v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_17-14-27Z_SequentialBeatsJoint_OntheInterplaybetweenOn_Polic.md
generated_at: 2026-09-03 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the interaction between on-policy distillation and reinforcement learning with verifiable rewards in large language models. The authors demonstrate that a two-stage approach where on-policy distillation is applied first and then followed by RL consistently beats pure methods across reasoning tasks. They also explain why this order works, linking it to coverage of teacher solutions and sharpening within that support.

## Key Takeaways
- OPD expands the student's coverage of teacher-supported solutions before RL begins, providing a richer signal for reward shaping.
- The joint optimization causes interference between OPD and RL signals, so separating them into stages improves performance.
- Using the OPD validation score as a trigger to switch to RL yields a practical recipe that outperforms SFT cold starts.

## Context
The field is moving toward methods that combine dense teacher supervision with sparse reward learning for efficient fine-tuning. This work adds a clear procedural workflow, addressing how two potentially conflicting signals can be sequenced without mutual degradation.

## Implications
Practitioners can adopt OPD-then-RL as a low‑overhead strategy to boost reasoning abilities in LLMs without large compute budgets. The insight that teacher validation guides RL transition may inform future hybrid training pipelines across AI research and industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04108v1)
