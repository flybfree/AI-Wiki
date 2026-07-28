---
title: Chamaileon: Cross-Context Binder Design with Contextualized Modeling and Mixed Sampling
published: 2026-07-26T07:35:10Z
authors: Hengyuan Cao, Shizhuo Cheng, Mingxuan Liu, Weicheng Huang, Yunhong Lu, Chenxi Cai, Yan Zhang, Min Zhang
url: http://arxiv.org/abs/2607.23518v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Chamaileon: Cross-Context Binder Design with Contextualized Modeling and Mixed Sampling

## Abstract
The rapid evolution of generative models has unlocked new potentials in protein binder design, a pivotal task in structural biology, by facilitating end-to-end generation via joint sequence-structure modeling or hallucination. However, existing approaches are predominantly implemented under a single-target, single-state assumption, limiting their ability to model multi-target or multi-state interactions required for advanced function-oriented protein design. Here, we introduce Chamaileon, which unifies multi-target and multi-state binder design by formulating the problem as cross-context binding landscape modeling. The framework is underpinned by a training paradigm termed In-Context Complex Co-Design (I3CD) for context-aware sequence-structure co-modeling. During inference, we employ Mixture-of-Paths Sampling (MoPS), a scalable strategy that optimizes a single sequence across contexts while alleviating the scarcity of high-quality multi-conformational paired data. Extensive evaluation on our newly constructed benchmark, CROSS, demonstrates that Chamaileon effectively generates sequences adaptable to diverse conformational landscapes and multi-target requirements. The code is available on https://github.com/caohengyuan/Chamaileon.

## Metadata
- **Published**: 2026-07-26T07:35:10Z
- **Authors**: Hengyuan Cao, Shizhuo Cheng, Mingxuan Liu, Weicheng Huang, Yunhong Lu, Chenxi Cai, Yan Zhang, Min Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23518v1)