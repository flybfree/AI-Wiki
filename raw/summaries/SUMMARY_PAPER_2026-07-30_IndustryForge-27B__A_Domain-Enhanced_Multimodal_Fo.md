---
title: IndustryForge-27B: A Domain-Enhanced Multimodal Foundation Model for Industrial CAD
url: http://arxiv.org/abs/2607.28050v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_11-28-21Z_IndustryForge_27B_ADomain_EnhancedMultimodalFounda.md
generated_at: 2026-07-30 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces IndustryForge-27B, a domain‑enhanced multimodal foundation model built on Qwen3.5-VL-27B that excels at industrial CAD tasks such as generating parametric scripts and Windows COM API code from engineering drawings and 3D screenshots. Across four CAD benchmarks it improves the base model by an average of 33.65 percentage points and surpasses GPT‑5.4, while maintaining gains in eleven general‑capability tests.

## Key Takeaways
- IndustryForge-27B lifts the base model’s performance on CAD visual QA, parametric code generation, assembly‑level code generation, and COM API tasks by a significant margin, demonstrating strong domain specialization.
- The unified multi‑task SFT recipe preserves general capabilities, showing no catastrophic forgetting and only modest improvement in non‑CAD benchmarks.
- The model outperforms the leading closed‑source GPT‑5.4 on all CAD‑specific evaluations, indicating that targeted fine‑tuning can match or exceed large commercial models.

## Context
The rapid growth of foundation models has enabled many applications, yet few address the specific multimodal demands of industrial design and manufacturing. This work bridges that gap by creating a model that integrates diverse CAD corpora into a single system, offering a practical solution for real‑world engineering workflows.

## Implications
For industry practitioners, IndustryForge-27B provides a reliable starting point for building full‑stack agents that can handle everything from part design to assembly automation. Its performance suggests that domain‑specific fine‑tuning is viable even within large language models, potentially lowering the barrier for custom industrial AI solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28050v1)
