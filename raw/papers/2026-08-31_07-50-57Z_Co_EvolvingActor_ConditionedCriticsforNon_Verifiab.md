---
title: Co-Evolving Actor-Conditioned Critics for Non-Verifiable Generation
published: 2026-08-31T07:50:57Z
authors: Jinyoung Kim, Muhammad Khalifa, Lajanugen Logeswaran, Jaekyeom Kim, Moontae Lee, Honglak Lee, Lu Wang
url: http://arxiv.org/abs/2608.30397v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Co-Evolving Actor-Conditioned Critics for Non-Verifiable Generation

## Abstract
Natural-language critiques provide supervision beyond scalar rewards for non-verifiable generation, which lacks deterministic verifiers. In critique-guided refinement, a critic gives feedback on an initial response and an actor revises it. However, final revision quality does not reveal whether the critique was actually useful: a capable actor may improve without following the feedback, while valid feedback may fail if the actor cannot execute it. We frame critique as actor-conditioned revision guidance, where usefulness depends on whether the feedback helps the target actor address the intended weakness. We introduce TAIScore (Targeted Actionable Improvement Score), a reward that evaluates the instruction, initial response, critique, and revision together, assessing whether the critique targets a real weakness, whether the actor follows it, and whether the intended aspect improves. We use this reward to train an actor-tailored critic with GRPO, and use critique-guided refinements to construct DPO preference pairs for the actor, forming a co-evolving critic-actor loop where the critic adapts to the actor's changing capability. Experiments show that an 8B critic trained with TAIScore outperforms both a zero-shot 120B critic and critics trained with outcome-only or critique-only reward signals. Co-evolving the critic and actor further improves performance, suggesting that effective critique supervision should adapt as the actor changes.

## Metadata
- **Published**: 2026-08-31T07:50:57Z
- **Authors**: Jinyoung Kim, Muhammad Khalifa, Lajanugen Logeswaran, Jaekyeom Kim, Moontae Lee, Honglak Lee, Lu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30397v1)