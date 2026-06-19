---
title: Judging to Improve: A De-biased VLM-as-3D-Judge Protocol for Single-Image 3D Generation
url: http://arxiv.org/abs/2606.20364v1
type: paper-summary
date: 2026-06-18
source_paper: 2026-06-18_15-25-57Z_JudgingtoImprove_ADe_biasedVLM_as_3D_JudgeProtocol.md
generated_at: 2026-06-18 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a de‑biased vision‑language model as a 3D judge that ranks single‑image to mesh quality and adapts it cheaply to the furniture class using TRELLIS. The study shows that conditioning repair can match the performance of strong public baselines while other methods fail, demonstrating that lightweight PEFT is insufficient.

## Key Takeaways
- The dual‑judge protocol (training Qwen2.5-VL-7B and evaluation InternVL3-8B) eliminates circularity and reduces order‑flip bias to 0.94.
- Conditioning repair on severe image degradation yields a win‑rate of 0.50, matching the base model’s performance.
- Lightweight PEFT alone cannot surpass the strong public baseline; signal must be engineered through quality‑contrastive construction.

## Context
The work advances single‑image to 3D generation by providing an automated, bias‑aware evaluation that can be integrated into training loops without human labels. It highlights a gap between cheap proxies and true geometric fidelity, prompting new research on robust judge design.

## Implications
For practitioners, the protocol offers a reusable framework for evaluating image‑to‑mesh outputs across diverse domains. For industry, it enables rapid quality checks of 3D renders while keeping computational costs low, supporting scalable production pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.20364v1)
