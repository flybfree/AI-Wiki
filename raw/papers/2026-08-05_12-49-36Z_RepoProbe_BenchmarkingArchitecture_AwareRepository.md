---
title: RepoProbe: Benchmarking Architecture-Aware Repository Comprehension with Checklists
published: 2026-08-05T12:49:36Z
authors: Yuexi Yang, Alyssa Wu, Ji Luo, Richeng Xuan, Zhichao Hu, Yuhong Liu, Zhen Qin
url: http://arxiv.org/abs/2608.04783v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RepoProbe: Benchmarking Architecture-Aware Repository Comprehension with Checklists

## Abstract
The integration of Large Language Models (LLMs) into software engineering has shifted the focus from function-level generation to repository-scale assistance. However, existing benchmarks largely rely on bug reports from GitHub Issues, which often allow models to bypass genuine understanding via pattern matching on error logs. This misalignment under-measures Edit Bias, which refers to premature generation, where models prematurely propose code modifications instead of understanding the existing repository architecture. Furthermore, current LLM-as-a-Judge scalar scoring suffers from high variance and low interpretability. This work introduces RepoProbe, a novel benchmark for evaluating repository-level code understanding through open-ended Q&A using GitHub Discussions, which focuses on open-ended architectural inquiries rather than defect reporting. To ensure rigorous evaluation, we propose a Checklist-Based Verification Protocol that decomposes answers into atomic, verifiable facts, thereby replacing subjective ratings with objective verification. Our evaluation of state-of-the-art (SOTA) LLMs reveals a persistent gap between high clarity and evidencegrounded technical correctness. It also quantitatively confirms the prevalence of edit bias, in which models prioritize code generation instead of architectural analysis. Finally, we demonstrate that our verification protocol significantly improves evaluation reliability compared to traditional evaluations with scalar scoring.

## Metadata
- **Published**: 2026-08-05T12:49:36Z
- **Authors**: Yuexi Yang, Alyssa Wu, Ji Luo, Richeng Xuan, Zhichao Hu, Yuhong Liu, Zhen Qin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04783v1)