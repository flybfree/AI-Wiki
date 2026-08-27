---
title: Paint What You See: Benchmarking Dexterous Visual Tool Use in Multimodal Agents
published: 2026-08-26T06:19:28Z
authors: Shudong Liu, Dongyang Chen, Enci Zhang, Jinwei Liang, Zheng Ma, Lewei Lu
url: http://arxiv.org/abs/2608.25417v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Paint What You See: Benchmarking Dexterous Visual Tool Use in Multimodal Agents

## Abstract
Evaluation is shifting from static QA toward agentic settings where models act through external tools. We identify a critical yet underexplored capability within this space - dexterous visual tool use: fine-grained, closed-loop parameterized visual action in which models infer tool parameters from visual evidence, and those parameters directly govern the final result. Existing benchmarks cover web navigation, GUI operation, and software engineering, but rarely target this coupling between visual evidence and execution precision. We propose EASEL, a benchmark evaluating a controlled instance of dexterous visual tool use that adopts reference-guided visual reconstruction as its primary proxy task: the agent incrementally paints a canvas to match a reference image. EASEL additionally includes semantic tasks spanning region annotation, handwriting, and path planning. We further provide EASEL-Data, a 440k-sample two-stage curriculum dataset for trajectory supervision, and EASEL-9B to investigate its effect on this capability. Evaluation of 25 models reveals that current multimodal agents systematically struggle on EASEL. Reconstruction similarity bottlenecks at low levels (0.40-0.54), while trajectory diagnostics expose severe closed-loop instability - models typically saturate early or degrade post-peak. Semantic tasks reveal sharp capability boundaries in precision annotation and path planning. EASEL-9B, trained on EASEL-Data, surpasses the base model by a relative 6.3%, ranking third among all evaluated models.

## Metadata
- **Published**: 2026-08-26T06:19:28Z
- **Authors**: Shudong Liu, Dongyang Chen, Enci Zhang, Jinwei Liang, Zheng Ma, Lewei Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25417v1)