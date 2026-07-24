---
title: Addressing Limited Data in Auditory Attention Decoding with Diffusion Generative Models
published: 2026-07-20T07:47:20Z
authors: David Rannaleet, Victor Gunnarsson, Bo Bernhardsson, Martin A. Skoglund, Emina Alickovic
url: http://arxiv.org/abs/2607.18345v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Addressing Limited Data in Auditory Attention Decoding with Diffusion Generative Models

## Abstract
Limited training data constrains deep learning models for Auditory Attention Decoding (AAD) in hearing aids (HAs). AAD uses electroencephalogram (EEG) data to decode listener's attention, enabling real-time tracking of specific sound sources. However, achieving high AAD performance with short time windows typical in HAs (<=1s) is challenging due to the scarcity of real-world speech-evoked EEG data. To address this issue, we investigate diffusion probabilistic models (DPMs) for generating synthetic speech-evoked EEG data. DPMs learn the underlying complex data structure through a denoising process and can generate realistic samples suitable for data augmentation. We evaluate the use of synthetic EEG data for augmenting datasets in locus-of-attention (LoA) classification tasks. Our experiments demonstrate that DPMs can generate realistic EEG signals and that incorporating synthetic data significantly improves AAD performance compared to models trained solely on measured EEG data (p<0.05). These results highlight the potential of diffusion-based data augmentation to mitigate training data limitations and improve the robustness of short-window AAD models in HA applications.

## Metadata
- **Published**: 2026-07-20T07:47:20Z
- **Authors**: David Rannaleet, Victor Gunnarsson, Bo Bernhardsson, Martin A. Skoglund, Emina Alickovic
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18345v1)