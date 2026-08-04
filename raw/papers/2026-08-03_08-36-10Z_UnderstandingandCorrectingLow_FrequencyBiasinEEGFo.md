---
title: Understanding and Correcting Low-Frequency Bias in EEG Foundation Model
published: 2026-08-03T08:36:10Z
authors: Junjie Yu, Zihan Deng, Jianyu Zhang, Junrong Mu, Jiahui An, Wenxiao Ma, Ziling Lu, Yue Wang, Yan Zhu, Kexin Lou, Quanying Liu
url: http://arxiv.org/abs/2608.01898v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding and Correcting Low-Frequency Bias in EEG Foundation Model

## Abstract
Increasing EEG pretraining data scale or model capacity does not consistently improve downstream performance. We identify a persistent low-frequency bias in representations learned by diverse EEG foundation models, which remains across dataset scales, model capacities, and pretraining objectives. Our analysis links this bias to the interaction between EEG's $1/f^α$-like spectral structure and neural networks' tendency to preferentially learn low-frequency components. In masked autoencoders, the $\ell_2$ reconstruction objective further amplifies this imbalance: under comparable relative reconstruction errors, high-power low-frequency components contribute disproportionately to the loss. To address this issue, we introduce FAME, a frequency-balanced masked autoencoding framework that reconstructs time--frequency activity in predefined EEG bands from masked EEG inputs. FAME independently standardizes the reconstruction targets within each band and assigns equal weight to all band-specific losses, thereby balancing supervision across the EEG spectrum. Evaluated on 41 downstream tasks in OmniEEG-Bench, FAME learns more spectrally balanced representations and achieves state-of-the-art performance on 24 of them. These results underscore the importance of balanced spectral supervision for learning transferable EEG representations.

## Metadata
- **Published**: 2026-08-03T08:36:10Z
- **Authors**: Junjie Yu, Zihan Deng, Jianyu Zhang, Junrong Mu, Jiahui An, Wenxiao Ma, Ziling Lu, Yue Wang, Yan Zhu, Kexin Lou, Quanying Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01898v1)