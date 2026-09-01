---
title: OCR-MetaReasoning Benchmark: Evaluating the Meta-Reasoning Ability of MLLMs in Text-Rich Image Understanding
published: 2026-08-31T12:20:05Z
authors: Gengxu Li, Yuan Wu, Yi Chang
url: http://arxiv.org/abs/2608.30678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OCR-MetaReasoning Benchmark: Evaluating the Meta-Reasoning Ability of MLLMs in Text-Rich Image Understanding

## Abstract
Text-rich image understanding requires multimodal large language models (MLLMs) to organize OCR (Optical Character Recognition)-grounded evidence across words, layout, fields, charts, and visual correspondences. Existing evaluations often conflate extraction with reasoning and rarely test whether models follow the required reasoning direction: applying visible rules, abstracting hidden regularities, or recovering missing premises. We introduce OCR-MetaReasoning, a controlled single-image benchmark that treats deduction, induction, and abduction as distinct directions and separates final-answer correctness from reasoning-process compliance. The benchmark contains 1,500 verified samples in a balanced \(3\times5\) taxonomy crossing three reasoning types with five OCR-object categories, along with reference reasoning steps, automatic answer scoring, the Meta-Reasoning Macro Score (MRMS), and the Reasoning Process Compliance Score (RPCS). Experiments with representative closed-source and open-source MLLMs show that OCR-grounded meta-reasoning remains far from saturated: models struggle with visible-rule application and layout-sensitive inference, while process-compliant rationales can accompany incorrect final answers under exact-match evaluation. The code is available at https://github.com/gengxuli/OCR-MetaReasoning.

## Metadata
- **Published**: 2026-08-31T12:20:05Z
- **Authors**: Gengxu Li, Yuan Wu, Yi Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30678v1)