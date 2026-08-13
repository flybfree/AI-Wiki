---
title: When the API Speaks the Wrong Language: Revisiting Post-Training for Multilingual Tool Use
url: http://arxiv.org/abs/2608.11715v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_06-55-04Z_WhentheAPISpeakstheWrongLanguage_RevisitingPost_Tr.md
generated_at: 2026-08-12 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why Large Language Models sometimes generate API calls with arguments in the wrong language, a problem called Argument Language Mismatch. It compares supervised fine‑tuning and reinforcement learning methods for fixing this issue and finds that SFT gives strong results comparable to or better than RL.

## Key Takeaways
- Supervised fine‑tuning (SFT) significantly improves argument language consistency and overall function call accuracy, providing a reliable baseline for multilingual API grounding.
- Reinforcement learning with structured rewards such as GRPO can boost language consistency but the gains are incremental and mainly affect generalization and trade‑off handling rather than core performance.
- The study shows that most of the improvement in multilingual API grounding can be achieved through careful supervised training, while RL offers targeted enhancements only under specific conditions.

## Context
Multilingual Large Language Models are increasingly used to interact with APIs across languages, but their reliability suffers when argument labels do not match the intended language. This mismatch is overlooked by existing evaluation metrics that focus on semantic correctness rather than operational validity. The paper addresses this gap by introducing a concrete failure mode and evaluating training strategies.

## Implications
For developers deploying multilingual AI agents, prioritizing supervised fine‑tuning can yield immediate reliability gains with minimal complexity. Practitioners should reserve reinforcement learning for scenarios where additional trade‑off management is critical, as its benefits are modest compared to SFT. This guidance helps allocate engineering effort toward the most effective mitigation strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11715v1)
