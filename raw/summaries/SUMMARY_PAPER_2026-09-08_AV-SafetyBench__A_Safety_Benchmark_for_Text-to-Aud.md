---
title: AV-SafetyBench: A Safety Benchmark for Text-to-Audio-Video Generation
url: http://arxiv.org/abs/2609.06991v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_03-32-30Z_AV_SafetyBench_ASafetyBenchmarkforText_to_Audio_Vi.md
generated_at: 2026-09-08 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
AV-SafetyBench is a new benchmark for evaluating safety in text-to-audio-video generation. It introduces a four‑axis taxonomy and 5,200 prompts, assessing outputs under full AV, video‑only, and audio‑only views.

## Key Takeaways
- The benchmark identifies unsafe content that can appear only when visual and audio are combined, showing up to 48% of missed risks in video‑only evaluations.  
- Audio‑only judgments flag a large portion of Full‑AV unsafe cases, accounting for 41.6–48.3% of those not caught by video‑only checks.  
- In the Cross‑Modal Harm Emergence category, AV‑Joint risk sources cause 87.5% of assigned unsafe outputs.

## Context
Current safety evaluations often treat video and audio separately, missing interactions that create harmful content. This work bridges that gap with a unified framework for multimodal generation.

## Implications
Researchers can use AV-SafetyBench to detect hidden hazards in T2AV systems before deployment. Industry practitioners will benefit from quantifying risk sources to prioritize mitigation efforts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.06991v1)
