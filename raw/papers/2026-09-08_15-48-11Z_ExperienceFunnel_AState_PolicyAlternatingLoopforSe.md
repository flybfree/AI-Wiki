---
title: Experience Funnel: A State-Policy Alternating Loop for Self-Evolving Agents
published: 2026-09-08T15:48:11Z
authors: Wenbo Gao, Zhaomou Song, Zhiyuan Ji, Renxi Liu, Xing Li, Xianzhi Yu, Xiaoguang Li, James Chung-wai Cheung, Weizhe Lin, Yaoyuan Wang
url: http://arxiv.org/abs/2609.08919v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Experience Funnel: A State-Policy Alternating Loop for Self-Evolving Agents

## Abstract
Autonomous agents powered by large language models (LLMs) continuously accumulate experience through interaction, creating an opportunity to improve future behavior through self-evolution. A fundamental challenge is how to transform abundant, task-specific interaction experience into reusable model competence without sacrificing the ability to adapt rapidly to newly observed evidence. Explicit textual states, such as skills and agent harnesses, provide fast, human-readable and editable adaptation, but incur persistent dependence on external context; parametric policies provide compact and reusable competence, but are substantially slower to update. We present \textit{Experience Funnel}, a self-evolving framework that couples fast state adaptation with slow policy consolidation in an alternating loop. Interaction trajectories are first distilled into an explicit textual state, where newly acquired experience can be rapidly incorporated and validated. The framework then selectively identifies state-enabled behavior that remains useful across state revisions and consolidates it into the policy through transition-aware distillation. The updated state--policy pair subsequently generates new rollouts, providing fresh evidence for the next round of state adaptation and policy consolidation. Experiments across diverse agent benchmarks show that \textit{Experience Funnel} consistently improves agent capability over state-only evolution and policy-internalization approaches, while progressively converting useful explicit experience into autonomous policy competence.

## Metadata
- **Published**: 2026-09-08T15:48:11Z
- **Authors**: Wenbo Gao, Zhaomou Song, Zhiyuan Ji, Renxi Liu, Xing Li, Xianzhi Yu, Xiaoguang Li, James Chung-wai Cheung, Weizhe Lin, Yaoyuan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08919v1)