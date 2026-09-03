---
title: Door-in-the-Face Requests and Refusal Behaviour in Large Language Models
url: http://arxiv.org/abs/2609.02707v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_15-08-51Z_Door_in_the_FaceRequestsandRefusalBehaviourinLarge.md
generated_at: 2026-09-02 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the door‑in‑the‑face technique—where a large request is refused and followed by a smaller one—works on large language models. It finds that the effect varies across model families: Anthropic’s frontier models see higher compliance after refusal, while OpenAI, Google, and Haiku 4.5 experience lower compliance.

## Key Takeaways
- The technique works for Anthropic's frontier models like Opus 5, raising approval from 29.3% to 65.8%, but backfires in other families.
- A related request on the same topic matters more than an unrelated one, showing that concession effect is universal across all nine models.
- The method does not transfer to refusals drawn from public benchmarks, indicating it relies on model‑specific behavior.

## Context
This study addresses a gap in understanding human social influence mechanisms when applied to AI systems. By testing refusal and follow‑up responses across multiple large language models, the research reveals that social dynamics are not universal but contingent on model architecture and training data.

## Implications
For developers, these findings suggest that deploying door‑in‑the‑face tactics may improve user compliance only with certain model families, requiring tailored strategies. Practitioners should consider model‑specific effects when designing interaction flows to avoid unintended negative outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02707v1)
