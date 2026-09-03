---
title: How Do Prompt Variations Affect Energy Consumption in On-Device LLMs?
published: 2026-09-01T19:08:04Z
authors: Wei Hu, Xiaolong Tu, Dawei Chen, Yitao Chen, Kyungtae Han, Haoxin Wang
url: http://arxiv.org/abs/2609.01798v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Do Prompt Variations Affect Energy Consumption in On-Device LLMs?

## Abstract
Large language models (LLMs) are increasingly deployed on mobile devices, making energy efficiency a key deployment constraint, yet the energy impact of prompt design remains underexplored. This paper aims to understand how two prompt properties, cognitive load and phrasing pattern, shape the energy behavior of on-device LLM inference. We conduct a broad empirical study covering prompt properties, datasets, models, and devices, with phase-level profiling that separates prefill and decode energy. We find that cognitive load primarily affects the energy cost per token, while phrasing pattern affects energy largely through token usage. Our energy-quality analysis further shows that prompt design reshapes the attainable frontier differently across models, highlighting the need for model-aware prompt design in energy-efficient on-device LLM inference. Code, datasets, and scripts are available at https://amai-gsu.github.io/PromptProperty/.

## Metadata
- **Published**: 2026-09-01T19:08:04Z
- **Authors**: Wei Hu, Xiaolong Tu, Dawei Chen, Yitao Chen, Kyungtae Han, Haoxin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01798v1)