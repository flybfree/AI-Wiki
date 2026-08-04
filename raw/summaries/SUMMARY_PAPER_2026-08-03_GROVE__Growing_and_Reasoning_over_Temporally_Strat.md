---
title: GROVE: Growing and Reasoning over Temporally Stratified Memory from Streaming Video Experience
url: http://arxiv.org/abs/2608.02392v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_15-35-28Z_GROVE_GrowingandReasoningoverTemporallyStratifiedM.md
generated_at: 2026-08-03 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
GROVE is a training-free framework that enables a wearable assistant to both recall visual information from streaming video and recognize when such memory is relevant. It grows a single causal memory into multiple temporal strata, each paired with retrieval skills for locating observations, replaying activities, or tracing long‑range patterns. Across benchmarks it outperforms existing methods in both reactive QA and proactive assistance.

## Key Takeaways
- GROVE maintains fine‑grained perceptual evidence while incrementally consolidating it into time‑stamped episodes and cross‑day recurring patterns.
- Each stratum is equipped with a scale‑native retrieval skill that can be triggered either by a user query or by the current situation, allowing reactive and proactive use of the same memory interface.
- Ablations demonstrate that temporal strata and their access skills are complementary, and that benefits are greatest when evidence spans multiple days.

## Context
The paper addresses the challenge of integrating long‑term visual memory with real‑time decision making in wearable AI systems. By unifying recall and proactive generation within one causal memory structure, GROVE moves beyond isolated question‑conditioned retrieval to a holistic approach that respects temporal continuity and user intent.

## Implications
GROVE provides a blueprint for future assistants that need persistent visual context without costly retraining. Practitioners can leverage its modular strata design to balance storage efficiency with rich recall capabilities, fostering more natural and reliable human‑AI interaction in daily life.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02392v1)
