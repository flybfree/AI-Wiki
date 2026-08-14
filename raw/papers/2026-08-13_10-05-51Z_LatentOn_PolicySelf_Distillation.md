---
title: Latent On-Policy Self-Distillation
published: 2026-08-13T10:05:51Z
authors: Guibin Zhang, Jiayang Lyu, Ran Sun, Xinlei Yu, Haoyu Zhao, Qibing Ren, Shuicheng Yan
url: http://arxiv.org/abs/2608.13040v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Latent On-Policy Self-Distillation

## Abstract
Enabling agents to learn from experience and internalize it into their policy has become a central problem in self-evolving AI. On-policy self-distillation (OPSD) offers an effective pathway by using a privileged self-teacher to provide dense supervision on the student's own trajectories; however, existing methods still rely heavily on designer-specified privileged artifacts (e.g., answers, feedback, skills, or trajectories), limiting the end-to-end learnability and scalability required for continual self-improvement. In this work, we introduce Latent On-Policy Self-Distillation (LOPD), which, rather than proposing another hand-crafted OPSD variant with a newly prescribed form of privileged context, makes the teacher's privileged context itself learnable end-to-end from experience. Technically, LOPD retrieves relevant experiences and composes them into continuous latent tokens that condition a self-teacher, while the student generates trajectories from the task and interaction history and receives dense token-level supervision at every visited prefix. We further introduce a privileged-margin objective to stabilize and regulate the learning of latent context. Empirically, LOPD demonstrates (I) strong performance, outperforming RLVR and representative OPSD methods including OPSD, SDPO, and Skill-SD across both agentic tool use and code generation; and (II) high learning efficiency, surpassing GRPO and Skill-SD with less than 30% of their rollout budget. Ablation studies further provide direct evidence that making privileged context learnable is necessary for realizing these gains. Together, these results position LOPD as a step toward a more scalable and self-directed paradigm for agent evolution.

## Metadata
- **Published**: 2026-08-13T10:05:51Z
- **Authors**: Guibin Zhang, Jiayang Lyu, Ran Sun, Xinlei Yu, Haoyu Zhao, Qibing Ren, Shuicheng Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13040v1)