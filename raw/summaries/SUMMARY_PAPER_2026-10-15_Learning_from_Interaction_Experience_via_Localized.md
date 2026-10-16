---
title: Learning from Interaction Experience via Localized Context Distillation
url: http://arxiv.org/abs/2610.21427v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_07-39-09Z_LearningfromInteractionExperienceviaLocalizedConte.md
generated_at: 2026-10-15 22:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Localized Context Distillation (LoCD), a method for enabling large language models to learn from interaction experience during deployment by addressing the fundamental limitations of existing context distillation approaches. LoCD works by identifying critical spans within a student model's own trajectory that require correction, having a teacher regenerate only those specific segments from the student's prefix, and then training the student on these targeted regenerated segments. The approach consistently outperforms strong baselines across math reasoning, code generation, and agent tasks while achieving more stable training with smaller and sparser parameter updates.

## Key Takeaways
- Existing context distillation methods suffer from a fundamental dilemma: off-policy context distillation trains the student on teacher-generated trajectories, introducing exposure bias where the student encounters states it would never produce on its own, while on-policy context distillation trains on the student's own rollouts, whose states are often uninformative and fail to convey behaviors the student cannot yet produce. LoCD resolves this dilemma by hybridizing both approaches in a targeted way.
- LoCD's core mechanism involves three steps: first, localizing the critical spans of a student trajectory that require revision; second, having the teacher regenerate only these spans conditioned on the student's own prefix; and third, training the student on the regenerated segments. This concentrates learning on the most informative states while keeping exposure bias low, effectively targeting the student's actual failure modes rather than distilling from arbitrary teacher behavior.
- Extensive experiments across math reasoning, code generation, and agent tasks demonstrate that LoCD consistently outperforms strong baselines and achieves more stable training with smaller and sparser parameter updates, suggesting that targeted, localized distillation is more parameter-efficient and training-stable than full-trajectory distillation approaches.

## Context
Continual learning from deployment experience is a critical frontier for large language models, as static training data cannot capture the full range of interactions a model encounters in production. Context distillation has emerged as a promising paradigm for transferring privileged information from a teacher to a student model, but the field has been hampered by the tradeoff between exposure bias in off-policy methods and the informativeness gap in on-policy methods. This paper addresses a core methodological gap in the continual learning and knowledge distillation literature by proposing a principled middle ground that preserves the student's own distributional context while injecting targeted corrective signals.

## Implications
For practitioners deploying LLMs in production environments, LoCD offers a more practical and stable pathway for post-deployment improvement without requiring full retraining or access to privileged information at inference time. The finding that localized, span-level distillation yields smaller and sparser parameter updates suggests that future continual learning pipelines can be made significantly more compute-efficient and less prone to catastrophic forgetting. For the broader AI research community, this work reframes how distillation signals should be constructed—shifting the focus from whole-trajectory imitation to targeted intervention at the student's actual failure points, which may influence how agent training, self-improvement loops, and online fine-tuning systems are designed going forward.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21427v1)
