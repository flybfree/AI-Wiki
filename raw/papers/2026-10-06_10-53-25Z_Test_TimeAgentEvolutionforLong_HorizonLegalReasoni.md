---
title: Test-Time Agent Evolution for Long-Horizon Legal Reasoning
published: 2026-10-06T10:53:25Z
authors: Haotian Chen, Shuaicheng Niu, Haocong Rao, Kaisong Song, Jun Lin, Lizhen Cui, Zhiqi Shen, Yonghui Xu
url: http://arxiv.org/abs/2610.08138v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Test-Time Agent Evolution for Long-Horizon Legal Reasoning

## Abstract
Legal intelligence aims to support reliable decision-making across long-horizon legal processes involving evolving case states and multiple roles. However, real-world legal deployment exhibits substantial case heterogeneity in facts, evidence, and procedural contexts, exposing the limitations of static agent strategies. Moreover, legal reasoning is inherently interdependent across roles and procedural stages, making global reliability fundamentally different from isolated role competence. To address these challenges, we study training-free test-time agent adaptation, where agents continuously exploit deployment-time signals from preceding cases and ongoing interactions without updating model parameters. We propose \method, which introduces \emph{Test-Time Memory Evolution} to retrieve reusable experience from previous cases, adapt it to the current factual and procedural context, and consolidate accumulated experience for subsequent decision-making. Further, \emph{Rubric-Aligned Collaboration} verifies and revises role-specific actions according to behavioral and procedural requirements, enabling coordinated decision-making across roles and stages. Extensive experiments on J1-EVAL and LegalWorld across five backbone models demonstrate consistent improvements over representative reasoning and agent baselines with reasonable interaction and computational costs. Ablation and case studies further show that the two components provide complementary benefits in experience adaptation and cross-role coordination, improving the reliability and efficiency of long-horizon legal reasoning.

## Metadata
- **Published**: 2026-10-06T10:53:25Z
- **Authors**: Haotian Chen, Shuaicheng Niu, Haocong Rao, Kaisong Song, Jun Lin, Lizhen Cui, Zhiqi Shen, Yonghui Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08138v1)