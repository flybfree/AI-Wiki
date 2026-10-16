---
title: DocPilot: Interactive Agent Orchestration and Training for Long Visual Document Understanding
published: 2026-10-15T06:16:43Z
authors: Zhuowen Liang, Xiaotian Lin, Yuyu Luo, Haixun Wang, Nan Tang
url: http://arxiv.org/abs/2610.21327v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DocPilot: Interactive Agent Orchestration and Training for Long Visual Document Understanding

## Abstract
Multimodal long-document question answering requires models to seek sparse evidence across pages and modalities, understand heterogeneous document content, and reason over the collected evidence. Even advanced vision-language models (VLMs) can overlook sparse evidence and struggle with cross-modal reasoning in a single pass. Existing document agents further introduce multi-step interaction, but some still rely on predefined workflows or coarse-grained actions, limiting the flexibility and granularity of document reasoning. We introduce DocPilot, an agentic document framework that supports expressive orchestration and makes complex document solving learnable by small language models (SLMs). DocPilot orchestrates evidence seeking through page-level navigation and fine-grained evidence localization, and integrates local visual inspection, code-based numerical reasoning, and cross-modal reasoning for multimodal understanding. To transfer these capabilities to small models, we propose curriculum-based agentic training that progresses from single-ability learning to adaptive orchestration through supervision from data-grounded reasoning traces and executable interaction trajectories. Across MMLongBench-Doc, DocBench, FinRAGBench-V, and MADQA, DocPilot achieves strong gains with frontier VLM backbones, while DocPilot-4B delivers competitive performance against substantially larger models, demonstrating strong effectiveness and generalization across diverse long-document reasoning settings. The code is available at https://github.com/HKUSTDial/DocPilot.

## Metadata
- **Published**: 2026-10-15T06:16:43Z
- **Authors**: Zhuowen Liang, Xiaotian Lin, Yuyu Luo, Haixun Wang, Nan Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21327v1)