---
title: Modular Foundation Models for Time-Series Perception in Digital Twins
published: 2026-07-03T20:02:28Z
authors: Quang Hung Pham, Ryad Zemouri, Martin Gagnon, Luc Vouligny
url: http://arxiv.org/abs/2607.03585v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Modular Foundation Models for Time-Series Perception in Digital Twins

## Abstract
Engineering Digital Twins and Prognostics and Health Management (PHM) systems rely on robust perception modules to extract actionable information from heterogeneous and non-stationary time-series data. However, most existing approaches remain task-specific, data-hungry, and difficult to integrate into scalable monitoring and decision-making pipelines. Moreover, purely data-driven models often lack robustness and transferability across varying operating conditions. To address these challenges, this paper proposes a modular foundation model for time-series perception based on a collection of pretrained representation encoders. The framework leverages self-supervised learning on heterogeneous datasets to learn transferable and task-agnostic representations, which can be reused across multiple PHM tasks. A gating mechanism is introduced to dynamically select relevant encoders for a given target dataset, enabling conditional computation and adaptive model composition. The selected representations are projected into a shared latent space and aggregated using a Transformer-based self-attention module that explicitly models cross-encoder interactions. The resulting architecture supports multiple downstream tasks, including imputation, long-term forecasting, and few-shot learning, through lightweight task-specific heads, while keeping pretrained encoders frozen during adaptation. Extensive ablation studies demonstrate the complementary roles of self-supervised pretraining, encoder selection, representation alignment, and adaptive aggregation. Experimental results on the ETT benchmark show competitive performance across tasks, while a real-world industrial case study on virtual sensing for hydro-generator rotor temperature highlights the practical relevance of the approach.

## Metadata
- **Published**: 2026-07-03T20:02:28Z
- **Authors**: Quang Hung Pham, Ryad Zemouri, Martin Gagnon, Luc Vouligny
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.03585v1)