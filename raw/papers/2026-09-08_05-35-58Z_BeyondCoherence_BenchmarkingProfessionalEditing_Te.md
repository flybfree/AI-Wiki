---
title: Beyond Coherence: Benchmarking Professional Editing-Technique Execution in Multi-Shot Audio-Video Generation
published: 2026-09-08T05:35:58Z
authors: Tianyi Zeng, Junchao Liao, Yujie Wei, Ziying Zhang, Litao Li, Tianyi Wang, Zhichao Wei, Shuyao Xu, Wenwen Qiang, Siyu Zhu, Zhenghao Zhang, Long Qin
url: http://arxiv.org/abs/2609.08275v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Coherence: Benchmarking Professional Editing-Technique Execution in Multi-Shot Audio-Video Generation

## Abstract
Recent multi-shot audio-video generators can produce increasingly coherent and cinematic outputs, but coherence does not imply the ability to execute editing techniques. Professional editing depends on shot structure, transition grammar, audio-video cut relations, and montage, yet existing benchmarks largely rely on proxies such as content quality, synchronization, or physical plausibility, systematically missing whether such editing instructions are actually executed. We introduce CutCraft, the first benchmark for editing-technique execution in multi-shot audio-video generation. CutCraft extends structured multi-shot prompts with explicit editing specifications and is paired with a hierarchical hybrid evaluation framework that combines shot-structure alignment, expert-model metrics, tool-grounded multimodal judgment, and rubric-based question answering. Beyond evaluation, we design an agentic editing baseline that decomposes generation into planning, shot-level synthesis, and post-hoc composition, explicitly realizing editing semantics such as J-cuts, L-cuts, and transition timing. Across 13 state-of-the-art closed- and open-source models, CutCraft reveals a consistent gap between coherence and editing-technique execution: current systems often produce plausible multi-shot videos yet fail to execute editorial instructions reliably. We find unstable shot structures, weak control of transition execution, and sharp degradation on higher-order montage, while aesthetic quality is only weakly correlated with editing-technique compliance. The benchmark and metrics, and the editing agent baseline are available at https://github.com/AlibabaResearch/cut-craft-bench.

## Metadata
- **Published**: 2026-09-08T05:35:58Z
- **Authors**: Tianyi Zeng, Junchao Liao, Yujie Wei, Ziying Zhang, Litao Li, Tianyi Wang, Zhichao Wei, Shuyao Xu, Wenwen Qiang, Siyu Zhu, Zhenghao Zhang, Long Qin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08275v1)