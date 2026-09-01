---
title: Autoregressive Mosaics: Probing 2D Spatial Reasoning in Text-Only Language Models
url: http://arxiv.org/abs/2608.30751v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_13-18-03Z_AutoregressiveMosaics_Probing2DSpatialReasoninginT.md
generated_at: 2026-08-31 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Autoregressive Mosaics (AM‑Bench) as a benchmark that tests whether text‑only language models generate 2D images from spatial descriptions or merely translate those descriptions into code. It finds that all models can reliably produce code for fully specified prompts but their ability to create images from vague prompts varies, showing that layout performance is not solely due to coding skill.

## Key Takeaways
- The translation task demonstrates that text‑only models can map detailed geometric specifications to executable code without any spatial reasoning.  
- The layout task reveals substantial differences in image generation quality across models when given underspecified prompts.  
- Replacing procedural code with raw SVG improves layout scores, indicating the output medium influences performance.

## Context
This work addresses a longstanding question about the capabilities of language‑only AI systems regarding visual tasks, which are typically associated with multimodal models. By separating translation from creation, AM‑Bench clarifies what is learned versus what is emergent.

## Implications
For practitioners, the findings suggest that improving 2D spatial reasoning in text models may require richer output formats or architectural changes rather than just better code generation. It also highlights the need for benchmarks that isolate these factors to guide research and deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30751v1)
