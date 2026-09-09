---
title: To Adapt or Not to Adapt? Selective Adaptation for Vision-Language Models
url: http://arxiv.org/abs/2609.08367v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-08_07-35-45Z_ToAdaptorNottoAdapt_SelectiveAdaptationforVision_L.md
generated_at: 2026-09-09 00:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces selective adaptation for vision-language models to avoid unnecessary or harmful test-time adaptations. It proposes Cross-Augmentation Similarity (CAS) which skips adaptation when augmented views show high similarity, preserving accuracy while skipping 85% of the process. The baseline improves overall accuracy compared to full adaptation.

## Key Takeaways
- Adaptations can be negligible, leaving predictions unchanged, or harmful, flipping correct answers to wrong ones.
- CAS identifies low similarity across augmented views as a trigger for adaptation, otherwise skips it, reducing unnecessary computation.
- Skipping nearly 85% of the adaptation process still yields improved accuracy.

## Context
Vision-language models face distribution shifts at inference time, prompting test-time adaptation strategies. Existing methods often apply uniform adaptation, which may degrade performance or waste resources. Selective adaptation addresses these inefficiencies by making adaptation decisions per sample.

## Implications
Practitioners can reduce latency and computational cost without sacrificing accuracy in deployment pipelines. The approach encourages research into dynamic adaptation frameworks that adapt only when needed, aligning with efficient AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08367v1)
