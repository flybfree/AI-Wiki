---
title: When and Where to Look: Adaptive Visual Evidence Scheduling for Efficient Long Video Understanding
url: http://arxiv.org/abs/2608.03918v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_16-49-53Z_WhenandWheretoLook_AdaptiveVisualEvidenceSchedulin.md
generated_at: 2026-08-05 01:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EcoFrame, a training-free framework that schedules sparse visual evidence for long video understanding by using VLM inference feedback to decide when to increase frame budget and where to search candidates. It combines entropy-gated budget scheduling with attention-guided candidate proposal to adaptively select frames without costly multi-round reasoning. Experiments show EcoFrame achieves higher accuracy-efficiency trade‑off than existing methods, delivering a 1.85× speedup over AKS/BOLT on Qwen2.5-VL.

## Key Takeaways
- EcoFrame uses output uncertainty (entropy) to stop early when evidence is sufficient or expand budget otherwise.
- Attention from the VLM is converted into a temporal prior, allowing dense local search while maintaining global coverage.
- The framework provides significant speedup compared with agent‑based schedulers like A.I.R., matching accuracy with up to 13.5× faster inference.

## Context
Long video understanding remains challenging as VLMs must process many frames yet need efficient evidence selection. Current approaches either use static budgets or require expensive interactive reasoning, limiting scalability and real‑world deployment.

## Implications
This work enables practical, low‑overhead scheduling for large language‑vision models, reducing latency without sacrificing performance. Practitioners can integrate EcoFrame into existing pipelines to accelerate video analysis tasks such as action detection and scene understanding.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03918v1)
