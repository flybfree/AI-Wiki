---
title: Learning to Follow In-Context Watermark Instructions via Self-Distillation
url: http://arxiv.org/abs/2608.29030v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_03-42-28Z_LearningtoFollowIn_ContextWatermarkInstructionsvia.md
generated_at: 2026-08-31 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ICWBench to evaluate how well large language models follow in-context watermark instructions while preserving answer quality. It finds that none of the tested LLMs meet both criteria across three instruction families and proposes a self-distillation method that improves performance without external supervision.

## Key Takeaways
- The benchmark shows current LLMs have low detection rates for watermarks, averaging around 0.1 to 0.34, indicating poor compliance with ICW instructions.
- Self-distillation using logits perturbation enables the model to learn instruction-following behavior from its own output distribution without needing a stronger teacher.
- Reinforcement learning with an automatic verifier as reward boosts detection rates to near 0.97 while keeping response quality high.

## Context
In-context watermarking aims to embed detectable signals in AI responses for provenance tracking, yet current models often prioritize answer quality over instruction adherence. This work addresses the gap by providing a training protocol that enhances compliance without sacrificing performance, aligning with broader goals of transparent and trustworthy AI.

## Implications
For industry practitioners, the method offers a scalable way to embed watermarks into LLM outputs, improving verification reliability for content provenance. Practitioners can adopt this self-contained approach to meet regulatory or ethical standards requiring detectable model behavior without compromising user experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29030v1)
