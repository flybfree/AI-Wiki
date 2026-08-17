---
title: Removing Temporal Note Redundancy Improves Multimodal Reinforcement Learning for Medicine
published: 2026-08-14T10:11:03Z
authors: Chenran Weng, Joo Seung Lee, Malini Mahendra, Anil Aswani
url: http://arxiv.org/abs/2608.14157v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Removing Temporal Note Redundancy Improves Multimodal Reinforcement Learning for Medicine

## Abstract
Mechanical ventilation is a critical life-support intervention, requiring dynamic adjustments to ventilator settings as a patient's condition evolves. While reinforcement learning (RL) offers a promising framework for optimizing these sequential decisions, standard approaches rely primarily on structured electronic health record (EHR) data, missing crucial clinical context recorded in free-text notes. Integrating longitudinal clinical notes into RL state spaces is challenging because notes are heavily inflated by temporal redundancy, such as copy-forward text, templating, and repetitive documentation, which dilutes time-local updates and degrades state representation quality. To address this, we propose a redundancy-aware multimodal state representation framework that explicitly removes duplicated note text over time before policy learning. We evaluate two computationally efficient temporal decomposition strategies for removing duplicated note text: (1) an embedding-space decomposition using singular value decomposition on local history subspaces, and (2) an interpretable sentence-level diff operation that filters out previously documented sentences before text encoding. Using real-world ICU data, we demonstrate that state representations constructed by stripping temporal note redundancy significantly outperform both structured-only and raw-note baselines across multiple off-policy evaluation methods (Model-Based Rollouts, Fitted Q-Evaluation, Weighted Importance Sampling, and Weighted Doubly Robust Evaluation). Our findings show that explicitly isolating new clinical information from repeated note text yields higher-quality state representations and directly improves RL performance for clinical decision support.

## Metadata
- **Published**: 2026-08-14T10:11:03Z
- **Authors**: Chenran Weng, Joo Seung Lee, Malini Mahendra, Anil Aswani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14157v1)