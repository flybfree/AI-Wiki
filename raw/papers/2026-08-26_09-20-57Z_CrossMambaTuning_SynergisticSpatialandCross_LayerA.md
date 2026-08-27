---
title: CrossMambaTuning: Synergistic Spatial and Cross-Layer Adaptation for Machine Vision Compression
published: 2026-08-26T09:20:57Z
authors: Haobo Xiong, Shaobo Liu, Kai Liu, Chongyang Ding
url: http://arxiv.org/abs/2608.25568v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CrossMambaTuning: Synergistic Spatial and Cross-Layer Adaptation for Machine Vision Compression

## Abstract
To reduce deployment cost and retraining overhead, adapting pretrained learned image compression (LIC) models to downstream machine vision tasks has attracted growing attention. However, existing methods typically insert fine-tuning modules independently into frozen backbones, lacking explicit mechanisms for cross-layer coordination. To address this limitation, we propose a novel framework named CrossMambaTuning, which integrates State Space Models with cross-layer interaction mechanisms for parameter-efficient fine-tuning. Specifically, we design an efficient Mamba adapter equipped with task-specific prompts and multi-scale branching to precisely capture both local features and global dependencies. Furthermore, we introduce a Scale-Invariant Cross-Layer Adapter (SICA) utilizing a parameter-sharing strategy to fuse task information across different scales and reduce redundancy. Extensive experiments demonstrate that CrossMambaTuning achieves state-of-the-art (SOTA) performance on multiple machine vision tasks, reducing parameter overhead by 72\% compared to SOTA methods. Code is available at https://github.com/rsr1123/CrossMambaTuning.

## Metadata
- **Published**: 2026-08-26T09:20:57Z
- **Authors**: Haobo Xiong, Shaobo Liu, Kai Liu, Chongyang Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25568v1)