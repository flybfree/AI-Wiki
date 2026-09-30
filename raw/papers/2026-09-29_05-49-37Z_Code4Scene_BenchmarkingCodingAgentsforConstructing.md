---
title: Code4Scene: Benchmarking Coding Agents for Constructing and Editing 3D Scenes
published: 2026-09-29T05:49:37Z
authors: Xiaokang Ye, Siddhant Hitesh Mantri, Zimeng Chen, Edward Zhang, Zhaoxu Zheng, Yuanheng Li, Yizhao Chen, Tianyang Huang, Lianhui Qin
url: http://arxiv.org/abs/2609.36777v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Code4Scene: Benchmarking Coding Agents for Constructing and Editing 3D Scenes

## Abstract
Frontier coding agents can now write and execute code that authors 3D environments, but whether they reliably understand 3D structure and precisely control scene state remains unclear. The generated 3D scene is a persistent, executable artifact: a convincing render can hide incorrect spatial relations, intersecting objects, or unintended modifications. We introduce Code4Scene, a benchmark of 190 Unreal Engine cases built from human-assembled scenes that evaluates coding agents on two complementary settings under a shared execution interface. Construction tests scene-level spatial reasoning from open-ended language specifications, where many realizations are valid; editing tests precise control of scene state, where the agent must recover the target scene from reference images while preserving everything else. Rather than scoring code or rendered views, Code4Scene evaluates the generated engine-native scene for task fulfillment, artifact integrity, and static physical validity, with edits additionally compared against withheld ground truth. Across 14 coding-agent configurations on the 95-case public set, construction and editing performance are strongly correlated but not interchangeable (Spearman $ρ= 0.78$): Claude Fable 5.1 leads construction, Gemini 3.8 Flash leads editing, and GPT-6 Astra narrowly leads overall. Spatial Composition is the weakest construction category for every agent, while editing remains imprecise: the best Repair F1 is only 0.527, and 35.8% of edits that fully recover the target still introduce unintended changes elsewhere in the scene. These results expose a gap between plausible 3D generation and reliable spatial reasoning and state control.

## Metadata
- **Published**: 2026-09-29T05:49:37Z
- **Authors**: Xiaokang Ye, Siddhant Hitesh Mantri, Zimeng Chen, Edward Zhang, Zhaoxu Zheng, Yuanheng Li, Yizhao Chen, Tianyang Huang, Lianhui Qin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36777v1)