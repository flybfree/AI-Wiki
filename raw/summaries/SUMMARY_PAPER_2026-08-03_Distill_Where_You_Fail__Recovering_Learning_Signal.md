---
title: Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups from Adaptive Teacher Guidance
url: http://arxiv.org/abs/2608.00782v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_17-29-14Z_DistillWhereYouFail_RecoveringLearningSignalsofNeg.md
generated_at: 2026-08-03 20:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces RSTG, a method that recovers learning signals in reinforcement learning with verifiable rewards by applying teacher guidance selectively to negative zero‑variance prompts and high‑entropy tokens. Experiments show RSTG improves math performance by 4.02% and code performance by 3.05% compared with naive GRPO+OPD, demonstrating that targeted distillation can mitigate sparse reward issues.

## Key Takeaways
- OPD applied to all samples dilutes gradients because many responses receive identical rewards, so RSTG restricts it to negative zero‑variance prompts and weights them by the teacher’s confidence.  
- Rapid fitting to the teacher can kill exploration; RSTG limits updates to tokens with high student entropy or large divergence to preserve exploratory capacity.  
- Naive GRPO+OPD suffers from asymmetric token coverage, whereas RSTG focuses only on informative tokens, yielding better overall learning.

## Context
RLVR frameworks rely on group‑relative optimization and teacher distillation to guide large language model training, yet sparse rewards limit gradient flow. This work addresses the gap by making distillation adaptive rather than blanket, preserving exploration while injecting positive signals where RL provides none.

## Implications
For practitioners, RSTG offers a practical way to enhance RL training without sacrificing sample efficiency. In industry, adopting such targeted guidance could accelerate fine‑tuning of LLM agents for complex tasks like math and code generation, delivering measurable performance gains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00782v1)
