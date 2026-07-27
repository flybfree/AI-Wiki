---
title: Pretraining EHR Foundation Models with Patient-Aware Sampling
published: 2026-07-24T09:10:43Z
authors: Joshua Placidi, Yuxuan Liu, Jinpei Han, Marek Rei, A. Aldo Faisal
url: http://arxiv.org/abs/2607.22114v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pretraining EHR Foundation Models with Patient-Aware Sampling

## Abstract
Autoregressive foundation models for electronic health records (EHRs) typically inherit pretraining methods from language modeling, where patient trajectories are concatenated into a single token stream and windows are sampled from that stream. In EHR data, this choice is consequential: windows may mix multiple patients, and patients with longer records contribute more optimization updates, potentially introducing bias. We propose Patient Sampling, a pretraining sequence-construction method that allows us to control how training signal is distributed across patients. We compare this method to the standard approach, which we refer to as Global Stream. We show that stochastic Patient Sampling with controllable weighting improves performance on real-world EHR data. Across downstream clinical tasks on MIMIC-IV v2.2 and v3.1, Patient Sampling improves Macro AUROC and AUPRC over the Global Stream baseline. These results identify training and validation sequence construction as important and underexplored design choices for autoregressive EHR foundation models.

## Metadata
- **Published**: 2026-07-24T09:10:43Z
- **Authors**: Joshua Placidi, Yuxuan Liu, Jinpei Han, Marek Rei, A. Aldo Faisal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22114v1)