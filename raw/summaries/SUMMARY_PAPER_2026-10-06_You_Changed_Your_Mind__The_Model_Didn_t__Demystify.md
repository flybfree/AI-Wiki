---
title: You Changed Your Mind, The Model Didn't: Demystifying Intent in Multi-Turn Dialogue
url: http://arxiv.org/abs/2610.06496v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-05_15-16-03Z_YouChangedYourMind_TheModelDidn_t_DemystifyingInte.md
generated_at: 2026-10-06 00:03
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper investigates how large language models handle evolving user intent in multi-turn dialogue, showing that merely mentioning a proposed change that is later rejected can still corrupt task execution. It introduces Intent-Eval, a controlled benchmark across tool actions, code, databases, and mathematics, and proposes Intent-OPSD, a decision-conditioned on-policy self-distillation method that trains models to follow only active requirements.

## Key Takeaways
- The central failure is "mentioned-as-in-effect" confusion: models treat conversational content as active requirements even after the user rejects or replaces it, causing accuracy degradation in tasks where the final intent is unchanged.
- Intent-Eval systematically evaluates this behavior across diverse domains, including tool actions, code, databases, and mathematics, revealing that models are vulnerable both to rejected proposals and to superseded requirements.
- Intent-OPSD addresses the problem by using a frozen Teacher initialized from the same model to provide active-intent supervision from the complete task matching the user's decision, while the Student is trained on the full dialogue to follow the requirements that remain in effect.

## Context
Multi-turn dialogue systems increasingly need to maintain stateful task execution as users revise, abandon, or replace instructions. This paper matters because it isolates a subtle but important failure mode: language models may over-attend to recent conversational mentions rather than reconstructing the user's current active intent.

## Implications
For practitioners, the findings suggest that dialogue agents, coding assistants, database tools, and mathematical solvers need explicit intent tracking rather than relying on surface conversational cues. The proposed self-distillation approach points toward training methods that can help models distinguish rejected or superseded statements from requirements that remain operative, improving reliability in long-running interactive workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06496v1)
