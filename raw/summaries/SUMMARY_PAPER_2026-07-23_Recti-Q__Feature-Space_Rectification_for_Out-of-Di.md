---
title: Recti-Q: Feature-Space Rectification for Out-of-Distribution-Robust Quantized Perception in Edge Robotics
url: http://arxiv.org/abs/2607.18540v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_22-14-04Z_Recti_Q_Feature_SpaceRectificationforOut_of_Distri.md
generated_at: 2026-07-23 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Recti-Q, a lightweight feature-space rectification method that mitigates robustness loss caused by post‑training quantization on edge robots. Experiments show that 4‑bit PTQ models suffer large degradation in out‑of‑distribution performance while keeping in‑distribution accuracy stable. Recti‑Q recovers much of the lost robustness with minimal overhead.

## Key Takeaways
- 4‑bit PTQ models lose significant robustness under sensor noise, severe weather, and novel environments even though ID accuracy is unchanged.
- Recti‑Q trains a small LoRA classifier head on source data to rectify quantized feature space, restoring much of the degraded performance without retraining the backbone.
- The adapter adds only 6 KB of parameters (≈1% overhead) and incurs negligible compute cost while preserving over 99% of PTQ memory savings.

## Context
Edge robotics must run large vision models with strict power and bandwidth limits, making quantization essential. However, quantization often introduces hidden vulnerabilities that become critical when robots operate in unpredictable real‑world conditions, highlighting a gap between theoretical efficiency gains and practical reliability.

## Implications
For industry, Recti‑Q provides a practical solution to embed robustness into quantized perception pipelines without sacrificing memory efficiency. Practitioners can deploy resilient patches over the air, ensuring continued performance across diverse operating scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18540v1)
