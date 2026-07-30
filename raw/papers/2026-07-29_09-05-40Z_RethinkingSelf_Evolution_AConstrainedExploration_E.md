---
title: Rethinking Self-Evolution: A Constrained Exploration-Exploitation Process for Mitigating Skill Overfitting
published: 2026-07-29T09:05:40Z
authors: Hongqiang Lin, Chao Liu, Xiaofan Bai, Xuan Jin, Yuhong Li, Nenggan Zheng, Xipeng Cao
url: http://arxiv.org/abs/2607.26643v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking Self-Evolution: A Constrained Exploration-Exploitation Process for Mitigating Skill Overfitting

## Abstract
Enabling large language model (LLM) agents to accumulate and reuse experience from past interactions remains a central challenge in real-world applications. A promising solution is to treat skills as trainable states and optimize them in the same way as model parameters in neural network training. However, data-driven skill optimization is prone to overfitting to the limited trajectories collected from real environments. Overexploiting these trajectories overfits the current batch, while unconstrained exploration causes regression on previously solved cases. This tension motivates a constrained search view of skill self-evolution, governed by an exploration--exploitation trade-off. We propose SkillBoost, a three-stage framework that mitigates both risks: structured exploitation localizes observed failures to editable skill components, prior-guided exploration draws on prior knowledge in the LLM to generate diverse repair candidates, and verified acceptance commits a candidate only when it improves performance within a regression bound. Experiments across 23 model--benchmark configurations show that SkillBoost achieves state-of-the-art performance while mitigating overfitting, outperforming both human-crafted and LLM-generated skills. Transfer experiments further show that optimized skills can be reused by other agents on similar tasks.

## Metadata
- **Published**: 2026-07-29T09:05:40Z
- **Authors**: Hongqiang Lin, Chao Liu, Xiaofan Bai, Xuan Jin, Yuhong Li, Nenggan Zheng, Xipeng Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26643v1)