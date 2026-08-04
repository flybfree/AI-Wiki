---
title: CrossProjection: Geometric Grounding Beyond Viewpoint Change in Architectural Drawings
url: http://arxiv.org/abs/2608.00473v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_06-51-38Z_CrossProjection_GeometricGroundingBeyondViewpointC.md
generated_at: 2026-08-03 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CrossProjection, a diagnostic framework for evaluating whether vision‑language models maintain component identity across different architectural drawing views such as plans, sections, and elevations. Experiments on 23 real drawing sets show GPT‑5.5 outperforms Qwen3‑VL‑32B‑Instruct and GLM‑4.5V in categorical matching tasks, while free geometry localization remains fragile for all models.

## Key Takeaways
- The model’s ability to correctly match components across view types is measured by high accuracy in closed‑candidate selection, yet explicit point or region localization scores are low (e.g., GPT‑5.5 PCK@0.05 54–76% vs. GLM 14–36%).  
- Free‑geometry outputs for lines and regions show minimal performance across all models, indicating that visual grounding is not reliably achieved without candidate support.  
- Human participants trained on architectural drawings achieve markedly higher categorical accuracy (87.3–93.3%) and GT‑region hit rates (76–92%), suggesting the task is feasible but not representative of population performance.

## Context
Vision‑language models are increasingly used to interpret architectural blueprints, yet they often fail to preserve geometric consistency when switching between plan, section, and elevation views. This gap limits their reliability for tasks that require precise spatial reasoning without relying on candidate feedback.

## Implications
For CAD/BIM systems guided by these models, categorical correctness should not be taken as proof of reliable candidate‑free spatial grounding. Implementing reusable on‑sheet anchors and fixed‑denominator scoring can provide an audit trail to detect when explicit geometric localization is missing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00473v1)
