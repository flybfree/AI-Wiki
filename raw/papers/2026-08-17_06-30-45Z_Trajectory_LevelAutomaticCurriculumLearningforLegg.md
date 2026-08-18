---
title: Trajectory-Level Automatic Curriculum Learning for Legged Locomotion on Unstructured Terrain
published: 2026-08-17T06:30:45Z
authors: Rocky Liu, Tengyu Liu, Baoxiong Jia, Fangwei Zhong, Xinyi Tong, Hongzhao Xie, Siyuan Huang
url: http://arxiv.org/abs/2608.16164v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trajectory-Level Automatic Curriculum Learning for Legged Locomotion on Unstructured Terrain

## Abstract
Training locomotion policies for complex unstructured terrain requires a curriculum to avoid early exploration failures. However, since unstructured terrain lacks explicit difficulty ordering for curriculum design, existing methods resort to heuristic curricula over parameterized terrains. This abstraction limits generalization, as policies can overadapt to near-fixed perceptual patterns. To address this, we propose \textbf{\ourname{}}, an \textbf{T}rajectory-level \textbf{A}utomatic \textbf{C}urriculum \textbf{L}earning framework that generates training tasks directly from unstructured terrain maps. At each curriculum update, the evaluator learns a difficulty function for the current policy that maps a given trajectory task to a difficulty score. The sampler then proposes new trajectories guided by the learned evaluator as the curriculum for the next policy update. This forms a closed loop in which the curriculum is iteratively matched to the evolving policy. Quantitative and qualitative experiments show that \ourname{} continuously provides effective curricula on unstructured terrain, improving trajectory success rate by \(56.3\%\) over direct training without curriculum. Compared with handcrafted curriculum learning, our method improves success rate by \(18.5\%\) on the hardest terrain tasks and by up to \(39.74\%\) when evaluating traversal from diverse approach directions on the same obstacle type.

## Metadata
- **Published**: 2026-08-17T06:30:45Z
- **Authors**: Rocky Liu, Tengyu Liu, Baoxiong Jia, Fangwei Zhong, Xinyi Tong, Hongzhao Xie, Siyuan Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16164v1)