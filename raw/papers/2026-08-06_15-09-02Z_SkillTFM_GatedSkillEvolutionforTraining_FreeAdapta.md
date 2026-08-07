---
title: SkillTFM: Gated Skill Evolution for Training-Free Adaptation of Tabular Foundation Models
published: 2026-08-06T15:09:02Z
authors: Yi He, Zhengkang Guan, Anpeng Wu, Peng Cui, Fei Wu, Kun Kuang
url: http://arxiv.org/abs/2608.06137v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillTFM: Gated Skill Evolution for Training-Free Adaptation of Tabular Foundation Models

## Abstract
Tabular data are ubiquitous in real-world applications and are crucial for data-driven prediction and decision-making across science, industry, finance, healthcare, and public services. Tabular foundation models (TFMs) have emerged as a promising paradigm for general-purpose tabular learning, offering reusable predictors across diverse datasets and substantially reducing the need for task-specific training, tuning, and model development. However, their practical deployment remains constrained by distribution shifts, heterogeneous feature semantics, and task-specific patterns that are difficult to capture without costly fine-tuning or additional labeled data.   To this end, we propose SkillTFM, a training-free system that shifts TFM adaptation from parameter updates to the gated evolution of agentic skills. The core of SkillTFM is a verifiable and extensible skill bank that couples boundary evidence identification with gated skill evolution: the former characterizes task structure and base-model failure patterns, whereas the latter retrieves and extends reusable skills subject to explicit validation. Across simulated boundary settings and real-world electricity-price forecasting, SkillTFM improves AUC by 0.128--0.142, raises nonlinear-boundary AUC from 0.699 to 0.898. Furthermore, experiments across TFM backbones demonstrate the effectiveness and generality of SkillTFM.

## Metadata
- **Published**: 2026-08-06T15:09:02Z
- **Authors**: Yi He, Zhengkang Guan, Anpeng Wu, Peng Cui, Fei Wu, Kun Kuang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06137v1)