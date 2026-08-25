---
title: Task-Driven 3D Printability Assistance via Geometry- and Knowledge-Grounded LLM Reasoning
published: 2026-08-22T22:56:29Z
authors: Zhaoda Du, Qiaojie Zheng, Xiaoli Zhang
url: http://arxiv.org/abs/2608.22128v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Task-Driven 3D Printability Assistance via Geometry- and Knowledge-Grounded LLM Reasoning

## Abstract
Printability assessment in additive manufacturing is typically conducted at the geometry level before printing to determine whether a computer-aided design (CAD) model or stereolithography (STL) file can be successfully fabricated. Task suitability, in contrast, is usually evaluated after printing to determine whether the fabricated part satisfies the requirements of its intended use. As a result, for non-expert users to print functional parts, unsuitable material or process choices may only be identified after fabrication, leading to repeated printing, material waste, and user frustration. To address this challenge, this paper leverages the reasoning and language-understanding capabilities of large language models (LLMs), while grounding the reasoning with geometry evidence and structured material/printer knowledge to generate reliable pre-print recommendations. Given a stereolithography (STL) model and a natural-language task description, the framework generates a structured recommendation covering printability, material choice, process parameters, design guidance, risks, and explanations. We evaluate the framework on focused STL benchmark scenarios with novice-style task descriptions. The proposed method achieves 75.0% printability over 96 physical validation trials, with 88.9% task suitability among successfully printed samples. It also improves Gemini 2.5 Flash-Lite material-selection accuracy from 37.5% under pure LLM to 90.0%. Expert evaluation further shows improved report quality, while post-print feedback improves recommendations on selected problematic cases. These results suggest that user task intent, geometry evidence, and structured material knowledge are all important for reliable task-driven printability assistance.

## Metadata
- **Published**: 2026-08-22T22:56:29Z
- **Authors**: Zhaoda Du, Qiaojie Zheng, Xiaoli Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22128v1)