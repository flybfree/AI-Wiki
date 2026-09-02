---
title: Can Large Language Models Forecast What Researchers Study Next?
published: 2026-09-01T05:26:37Z
authors: Fenghai Li, Zihan Tang, Haofei Yu, Yining Zhao, Jiaxuan You
url: http://arxiv.org/abs/2609.00747v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Large Language Models Forecast What Researchers Study Next?

## Abstract
Large language models increasingly generate research ideas, yet judging their novelty or feasibility at generation time does not establish whether they anticipate subsequent work. We introduce IdeaForecastBench to evaluate research idea forecasting. Given a community's literature up to a cutoff, a system produces up to five ranked ideas, which are evaluated against later papers. The benchmark comprises 624 rolling episodes across 52 topics, with a fixed retrieve-then-judge protocol and separately reported results from two judges. We compare five history-compression strategies across GPT-4.1, Qwen2.5-7B/14B, and Qwen3.5-9B, together with a learned Mode-Decomposition Forecaster (MDF). Under the primary GPT-4.1-mini judge, Summary improves on Direct in Hit@5 and Precision@5 across all four backbones. Qwen2.5 scores above GPT-4.1, whereas Qwen3.5 scores below it. An outcome-blind assessment finds that Qwen2.5 produces broader forecasts, but does not identify how much breadth contributes to its advantage. Threshold and judge diagnostics further clarify the limits of interpreting realization as precise anticipation. IdeaForecastBench provides a common task for studying which research ideas a community subsequently pursues and how reliably this outcome can be measured.

## Metadata
- **Published**: 2026-09-01T05:26:37Z
- **Authors**: Fenghai Li, Zihan Tang, Haofei Yu, Yining Zhao, Jiaxuan You
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00747v1)