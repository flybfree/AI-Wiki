---
title: CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Representation
published: 2026-08-13T08:21:06Z
authors: Hamza Shafiq, Hung Manh Pham, Bin Zhu, Pan Zhou, Jun Hu, Aaqib Saeed
url: http://arxiv.org/abs/2608.12944v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Representation

## Abstract
Electrocardiography (ECG), photoplethysmography (PPG), and phonocardiography (PCG) provide complementary views of the same cardiac cycle, yet existing cardiac foundation models are trained for a single sensing modality, leaving the shared physiology across sensors unexploited. We introduce CardioState-JEPA, a cardiac foundation model to learn a single shared representation jointly across ECG, PPG, and PCG, built on a physiology-aware joint-embedding predictive architecture. The model maps heterogeneous waveforms into a common token space, processes them with a single shared Transformer encoder, and learns by predicting masked latent cardiac states, placing the pretraining target on shared physiology rather than sensor-specific waveform appearance. To handle the temporal offsets between electrical, mechanical, and hemodynamic events, cross-modal prediction uses a learned delay aligner that matches signals at the corresponding cardiac time. Because synchronized multi-sensor recordings are scarce, CardioState-JEPA first learns within-modality structure from abundant unimodal data and then uses paired data to align modalities in latent cardiac time. Evaluated as a frozen encoder across 25 downstream tasks spanning ECG, PPG, and PCG, our encoder improves average PPG classification by 8.2 AUROC points, PCG murmur detection by 18.8 AUROC points, and ECG classification by 15.5 AUROC points over the best self-supervised signal baseline and matches or exceeds cardiac models trained with privileged clinical text or supervised labels on several ECG benchmarks. These results establish that heterogeneous cardiac signals can mutually supervise a single foundation model of cardiac physiology.

## Metadata
- **Published**: 2026-08-13T08:21:06Z
- **Authors**: Hamza Shafiq, Hung Manh Pham, Bin Zhu, Pan Zhou, Jun Hu, Aaqib Saeed
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12944v1)