---
title: Bounding Boxes to Improve Small Language Model Performance on Vision-Based Grading Tasks
url: http://arxiv.org/abs/2607.18767v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_06-49-24Z_BoundingBoxestoImproveSmallLanguageModelPerformanc.md
generated_at: 2026-07-23 23:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper explores whether cropping student responses using bounding boxes can improve the accuracy and computational efficiency of small language models when grading handwritten exams. Experiments on scanned answers from the 2025 Australian Physics Olympiad show that applying bounding boxes boosts grading performance across models from 4B to 72B parameters while also lowering FLOPs. The authors conclude that bounding box preprocessing is essential for deploying SLMs in vision‑based educational assessments.

## Key Takeaways
- Bounding boxes significantly increase grading accuracy by focusing the model’s attention on the relevant handwritten text and reducing visual noise.
- Computational cost drops because the model processes only a cropped region, resulting in fewer FLOPs regardless of model size.
- The improvement holds across both CoT prompting and non‑CoT settings, indicating robustness to prompt style.

## Context
Small language models are increasingly used for privacy‑preserving and low‑cost AI services. Vision tasks remain challenging because full‑page images demand high compute and contain irrelevant content. This work demonstrates that simple geometric preprocessing can mitigate these issues without model retraining.

## Implications
Educational institutions can deploy SLMs on edge devices with modest resources, enabling scalable grading at reduced cost. Practitioners should incorporate bounding box extraction as a standard step in vision‑based assessment pipelines to maximize efficiency and reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18767v1)
