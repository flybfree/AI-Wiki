---
title: FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving
url: http://arxiv.org/abs/2608.12932v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_08-10-54Z_FlashDrive_FlashVision_Language_ActionInferencefor.md
generated_at: 2026-08-13 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FlashDrive a framework that reduces latency of vision-language-action models for autonomous driving from 717ms to 151ms while preserving accuracy. It targets four bottlenecks in VLA inference and uses algorithmic shortcuts combined with system-level optimizations. The result is a ten‑billion‑parameter model running at six point six hertz on a single GPU.

## Key Takeaways
- Temporal overlap enables streaming KV‑cache reuse across frames eliminating redundant visual encoding compute.
- Non‑autoregressive diffusion drafter exploits low per‑token entropy and strong intra‑block correlations to generate speculative reasoning tokens efficiently.
- Adaptive step caching concentrates flow‑matching denoising where the velocity field is steep, reducing unnecessary computation.

## Context
Vision‑language‑action models aim for end‑to‑end reasoning but their inference remains too slow for real‑time control. Recent work focuses on single‑stage optimizations yet FlashDrive shows that co‑design across all stages yields dramatic speedups without accuracy loss.

## Implications
This approach can be applied to larger models in autonomous driving and other multimodal tasks where latency is critical. Practitioners may adopt FlashDrive’s pipeline to push inference toward real‑time performance on edge hardware.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12932v1)
