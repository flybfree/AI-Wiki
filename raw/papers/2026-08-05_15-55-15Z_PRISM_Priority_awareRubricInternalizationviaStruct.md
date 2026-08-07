---
title: PRISM: Priority-aware Rubric Internalization via Structured Multimodal Data Synthesis
published: 2026-08-05T15:55:15Z
authors: Xiaomin He, Dongling Xiao, Jiahao Xie, Ruiqi Lu, Qianle Wang, Zhongbin Guo, Wanxuan Sun
url: http://arxiv.org/abs/2608.05249v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PRISM: Priority-aware Rubric Internalization via Structured Multimodal Data Synthesis

## Abstract
Real-world multimodal instructions often bundle multiple requirements with unequal importance, yet most multimodal training data still reduce instruction following to answering one self-contained question. We study this gap through \textbf{rubric comprehension}, which casts the model not as a generator measured against rubrics but as an \textbf{executor} that follows them: given an image and a typed, prioritized rubric, the model must verify each rule before producing an overall judgment. To support this setting, we propose \textbf{PRISM}, a four-stage data synthesis framework that produces persona--task pairs, prefix-guided rule sets, quality-filtered rubrics, and structured verification traces. We further introduce \textbf{PRISM-Eval}, whose Loose and Strict metrics use deterministic matching against fixed labels and therefore require no inference-time judge model. With only 10K synthesized samples, PRISM lifts Qwen3-VL-4B from 9.5\% to 30.1\% Strict accuracy on PRISM-Eval while preserving average performance on general benchmarks, and the gains transfer to four additional open-source MLLMs across dense and MoE architectures, suggesting that structured rubric supervision is a scalable path toward multi-rule, priority-aware multimodal instruction following.

## Metadata
- **Published**: 2026-08-05T15:55:15Z
- **Authors**: Xiaomin He, Dongling Xiao, Jiahao Xie, Ruiqi Lu, Qianle Wang, Zhongbin Guo, Wanxuan Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05249v1)