---
title: Music-Source-Separation-Training (MSST): A Unified Framework for Training and Evaluating Music Demixing Models
published: 2026-07-25T23:43:19Z
authors: Roman Solovyev, Ilya Kiselev, Alexander Stempkovskiy, Tatiana Gabruseva
url: http://arxiv.org/abs/2607.23395v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Music-Source-Separation-Training (MSST): A Unified Framework for Training and Evaluating Music Demixing Models

## Abstract
Music Source Separation (MSS), the task of recovering individual sound components (stems) from a polyphonic mixture, is central to applications ranging from karaoke and remixing to audio restoration and content production. The separation quality depends on engineering decisions across the entire pipeline: model choice, training data preparation and augmentation, loss function and metrics choice, training configuration, validation, and post-processing. This paper presents MSST (Music-Source-Separation-Training) - a universal open-source framework for MSS tasks, which unifies training, validation, and inference for a broad range of modern demixing model families under a single, configuration-driven interface. The framework supports various model architectures, data preprocessing and augmentations, multiple loss functions and evaluation metrics, which helps with fast iterations and ablation studies. Additionally, the framework supports a range of practical techniques that improve separation quality, such as sliding-window inference with cross-fading, test-time augmentation, model ensembling, and fine-tuning via Low-Rank Adaptation (LORA). Our ablation studies demonstrate improvements of MSS using the above techniques. By consolidating these components into a reproducible, YAML-configurable framework, MSST lowers the barrier to systematic experimentation and enables rapid iteration from idea to verifiable result.

## Metadata
- **Published**: 2026-07-25T23:43:19Z
- **Authors**: Roman Solovyev, Ilya Kiselev, Alexander Stempkovskiy, Tatiana Gabruseva
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23395v1)