---
title: SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation
published: 2026-08-06T12:46:13Z
authors: Changyuan Wang, Chubin Zhang, Zhenyu Wu, Runhao Li, Angyuan Ma, Ke Chao, Yinan Liang, Xiuwei Xu, Ziwei Wang, Yansong Tang, Jiwen Lu
url: http://arxiv.org/abs/2608.05970v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation

## Abstract
Embodied visuomotor models, including Diffusion Policy (DP) and Vision-Language-Action (VLA) models, have demonstrated promising performance on robotic manipulation benchmarks. However, their potential remains fundamentally constrained by the scarcity of large-scale embodied trajectory datasets, leading to insufficient compositional generalization in out-of-distribution (OOD) scenarios with limited capability to capture reusable skill structures. To address this limitation, we propose Skill-Based Memory (SkillMemo) framework that implicitly decomposes long-horizon demonstrations into latent atomic skills and integrates skill-level features into a dynamic episodic memory bank for solving compositional tasks. Specifically, we first introduce an expert-guided trajectory segmentation module built upon a Mixture-of-Experts (MoE) architecture, which implicitly partitions trajectories into distinct skill primitives represented by learned gating coefficients. We further design a skill-level episodic memory architecture that stores compact skill representations as retrievable key-value pairs. During inference, the memory bank retrieves the most relevant skill primitives which are subsequently fused with the model's current gating distribution, providing a robust contextual prior to refine action predictions. Extensive experiments on the simulation benchmark and real-world manipulation tasks demonstrate that SkillMemo consistently enhances both DP and VLA backbones, achieving state-of-the-art performance and outperforming $π_{0.5}$, while exhibiting strong compositional generalization to unseen task configurations.

## Metadata
- **Published**: 2026-08-06T12:46:13Z
- **Authors**: Changyuan Wang, Chubin Zhang, Zhenyu Wu, Runhao Li, Angyuan Ma, Ke Chao, Yinan Liang, Xiuwei Xu, Ziwei Wang, Yansong Tang, Jiwen Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05970v1)