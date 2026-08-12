---
title: BooST: Bridging Semantics and Motions for Efficient Skill Transfer
published: 2026-08-11T07:35:12Z
authors: Jusuk Lee, Daesol Cho, Jonghun Shin, Seungyeon Yoo, Jonghae Park, Taekbeom Lee, H. Jin Kim
url: http://arxiv.org/abs/2608.10600v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BooST: Bridging Semantics and Motions for Efficient Skill Transfer

## Abstract
Skill abstraction---the process of learning reusable and temporally extended behaviors---has emerged as a key paradigm for improving sample efficiency and generalization in robot learning. For efficient skill transfer to real robots, learned skills must generalize across tasks and domains, remain robust to visual and dynamic perturbations, and be efficient enough for practical deployment. However, existing methods typically satisfy only a subset of these properties, as they capture either high-level semantic intent (what) or low-level motion dynamics (how). This incomplete skill transfer yields weak priors for policy learning, thereby demanding substantial in-domain data for downstream adaptation. To address these challenges, we introduce BooST, a two-stage framework that explicitly bridges semantics and motions to satisfy all three desiderata. BooST first leverages a cross-modal VQ-VAE to capture both semantic intent and motion dynamics, yielding a unified skill representation. It then distills this representation into a lightweight policy for efficient downstream adaptation to new tasks. Extensive experiments across simulation and real-robot settings demonstrate that BooST achieves superior few-shot adaptation, cross-domain skill transfer, and robustness to dynamic visual distractors, while maintaining a lightweight yet expressive design suitable for real-world deployment.

## Metadata
- **Published**: 2026-08-11T07:35:12Z
- **Authors**: Jusuk Lee, Daesol Cho, Jonghun Shin, Seungyeon Yoo, Jonghae Park, Taekbeom Lee, H. Jin Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10600v1)