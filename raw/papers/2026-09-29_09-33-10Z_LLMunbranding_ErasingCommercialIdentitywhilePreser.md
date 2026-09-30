---
title: LLM unbranding: Erasing Commercial Identity while Preserving Generic Utility
published: 2026-09-29T09:33:10Z
authors: Kajetan Ożóg, Alicja Wojciechowska, Dawid Malarz, Paweł Batorski, Artur Kasymov, Przemysław Spurek
url: http://arxiv.org/abs/2609.37127v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM unbranding: Erasing Commercial Identity while Preserving Generic Utility

## Abstract
Establishing unbranding as a critical practice to prevent visual logos from acquiring negative connotations is standard in image generation. Large Language Models (LLMs) now face a parallel and emerging challenge. These models frequently generate brand descriptions within diverse contexts. This frequency introduces significant risks, such as trademark dilution, false attribution, and brand defamation. In response, we formally define the novel task of LLM Unbranding. We specifically address the complex challenge of managing trade dress within textual outputs. This involves neutralizing characteristic language, slogans, and stylistic markers that define brand identity. Crucially, these elements are less evident than explicit visual logos. To benchmark this task, we introduce a comprehensive evaluation dataset incorporating prominent brands from multiple commercial domains. We rigorously evaluate existing state-of-the-art machine unlearning models using this benchmark. This evaluation identifies their limitations in selective textual unbranding. Finally, we propose MUTE, a novel inference-time method that effectively neutralizes textual trade dress while preserving the LLM's general capabilities and utility. By leveraging an iterative refinement loop, MUTE systematically optimizes system instructions to safely eliminate brand leakage without requiring fragile parameter updates.   Code and dataset: The evaluation dataset and code for LLM Unbranding are available at https://github.com/KajetanOzog/LLM_unbranding. The implementation of MUTE is available at https://github.com/KajetanOzog/MUTE.

## Metadata
- **Published**: 2026-09-29T09:33:10Z
- **Authors**: Kajetan Ożóg, Alicja Wojciechowska, Dawid Malarz, Paweł Batorski, Artur Kasymov, Przemysław Spurek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37127v1)