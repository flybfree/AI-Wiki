---
title: Multimodal Prompt Learning with Irregular EHRs for Robust Monitoring of Critical Care Patients
published: 2026-08-22T12:49:01Z
authors: Yixin Yang, Yueyang Sun, Weichen Liu, Xianbing Zhao, Sicen Liu
url: http://arxiv.org/abs/2608.21941v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multimodal Prompt Learning with Irregular EHRs for Robust Monitoring of Critical Care Patients

## Abstract
Accurate assessment of patients in intensive care units (ICUs) is essential for timely clinical intervention and improved patient outcomes. Multimodal electronic health records (EHRs), including structured physiological time series and longitudinal clinical notes, provide complementary information for critical care prediction. However, in real-world clinical settings, individual modalities may be partially observed or entirely unavailable, resulting in substantial performance degradation for existing multimodal models. To address this challenge, we propose a multimodal prompt-learning framework for robust clinical prediction under diverse missing-modality scenarios. The proposed framework introduces four complementary types of prompts: generative prompts, missing-signal prompts, missing-type prompts, and temporal prompts. Generative prompts construct surrogate latent representations for unavailable modalities, while missing-signal prompts distinguish observed representations from generated ones. Missing-type prompts condition the model on different modality-availability configurations, whereas temporal prompts perform condition-specific aggregation over temporally encoded clinical sequences. Together, these prompts enable the model to capture missingness-aware intramodal dependencies and cross-modal interactions within a unified architecture. Extensive experiments demonstrate that our method outperforms existing approaches across evaluation metrics on two missingness settings. Ablation and robustness analyses further verify the complementary contributions of the four prompt types and the effectiveness of the proposed framework for clinical prediction from incomplete multimodal EHR data.

## Metadata
- **Published**: 2026-08-22T12:49:01Z
- **Authors**: Yixin Yang, Yueyang Sun, Weichen Liu, Xianbing Zhao, Sicen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21941v1)