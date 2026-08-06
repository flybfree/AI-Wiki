---
title: GUARD: Grounding Uncertainty and Ablation-Based Risk Detection for Diffusion-Based VLAs
url: http://arxiv.org/abs/2608.04510v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_06-48-15Z_GUARD_GroundingUncertaintyandAblation_BasedRiskDet.md
generated_at: 2026-08-05 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GUARD, a test-time failure detection method for diffusion-based vision-language-action policies that quantifies how well generated actions are grounded in visual and language evidence without altering the model. By measuring the impact of key-value cache entries on denoising responses after ablation, GUARD produces diagnostic metrics such as sensitivity, attention entropy, modality bias, and grounding efficiency. The method achieves a 5.73 percentage‑point improvement in unseen‑task ROC‑AUC over existing runtime monitors.

## Key Takeaways
- GUARD estimates the influence of token‑indexed entries in the final vision‑language model key‑value cache by constructing counterfactual caches that remove salient KV entries and comparing their denoising responses to the original conditioning.  
- The diagnostic stream includes sensitivity, attention entropy, modality bias, and grounding efficiency, which are calibrated online and fed to a lightweight temporal classifier for real‑time failure detection.  
- GUARD improves the average unseen‑task ROC‑AUC by 5.73 points compared with the strongest competing runtime monitor while staying within 0.19 points of the best seen‑task performance.

## Context
Current diffusion‑based VLA policies generate plausible actions but often lack reliable grounding in multimodal evidence, leading to failures that are hard to diagnose at inference time. Existing runtime monitors typically rely on coarse error signals and do not directly probe the dependency between action heads and visual‑language inputs across tasks or domains.

## Implications
GUARD provides a transferable failure signal that can be applied across policies, tasks, embodiments, and domains without retraining, enabling more robust deployment of diffusion VLA systems. Practitioners can integrate these lightweight diagnostics to catch grounding failures early, improving safety and reliability in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04510v1)
