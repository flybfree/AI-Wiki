---
title: Neonatal Hypoxic-ischaemic Encephalopathy Classification from the EEG and HRV Signals Using a Conformer based Masked Autoencoder
published: 2026-07-26T09:11:03Z
authors: Shuwen Yu, William P Marnane, Geraldine B. Boylan, Gordon Lightbody
url: http://arxiv.org/abs/2607.23554v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neonatal Hypoxic-ischaemic Encephalopathy Classification from the EEG and HRV Signals Using a Conformer based Masked Autoencoder

## Abstract
In this paper, we propose the MAEConformer, a novel self-supervised learning framework that combines the Conformer architecture with the Masked Autoencoder (MAE) paradigm for large-scale representation learning from unlabelled electroencephalography (EEG) and heart rate variability (HRV) signals. By integrating convolutional operations with Transformer-based self-attention, MAEConformer effectively captures both local temporal patterns and long-range contextual dependencies in physiological time series. To enhance reconstruction fidelity and representation quality, a multi-resolution short-time Fourier transform (MR-STFT) loss is incorporated alongside the reconstruction objective, enabling the model to jointly learn temporal and spectral characteristics across multiple scales. Modality-specific EEG and HRV MAEConformer models were pretrained on 6,030h and 4,868h of unlabelled recordings, respectively, and subsequently transferred to expert-annotated downstream tasks. Experimental results demonstrate that the learned representations provide strong transferability and data efficiency. In EEG-based hypoxic ischemic encephalopathy (HIE) severity classification, the pretrained MAE-EEG model achieved test AUCs of 97.19% and 96.56% for binary and four-class classification tasks, respectively, outperforming a range of state-of-the-art supervised and self-supervised baselines. On the HRV-based HIE severity classification task, MAE-HRV achieved a test AUC of 82.42%, surpassing both self-supervised Transformer-based and supervised convolutional baselines. These findings demonstrate the effectiveness of MAEConformer for learning robust and transferable representations across multiple physiological modalities.

## Metadata
- **Published**: 2026-07-26T09:11:03Z
- **Authors**: Shuwen Yu, William P Marnane, Geraldine B. Boylan, Gordon Lightbody
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23554v1)