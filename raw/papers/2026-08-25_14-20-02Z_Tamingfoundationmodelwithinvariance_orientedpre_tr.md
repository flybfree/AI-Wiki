---
title: Taming foundation model with invariance-oriented pre-training for broad-spectrum EEG analysis across signal-level, brain-state, and brain-health tasks
published: 2026-08-25T14:20:02Z
authors: Yulong Dou, Han Wu, Guo Chen, Fangmao Ju, Zhiming Cui, Dinggang Shen
url: http://arxiv.org/abs/2608.24597v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Taming foundation model with invariance-oriented pre-training for broad-spectrum EEG analysis across signal-level, brain-state, and brain-health tasks

## Abstract
Electroencephalography (EEG) is a widely used window into human brain function, but most EEG models remain tied to a one-dataset-one-model supervised paradigm. Recent EEG foundation models offer a route toward reusable representations, but most remain reconstruction-centered, assuming that EEG content predictable from local context is necessarily transferable neural information. Here we present INCEPT, an invariance-oriented EEG foundation model trained on over 11,000 hours of unlabelled clinical EEG. Rather than prioritizing signal recovery alone, INCEPT learns representation-level stability across correlated EEG observations, separating stable neural structure and essential subject-sensitive information from the nuisance variability that dominates scalp recordings while preserving subject-, state- and condition-discriminative information. We evaluate INCEPT on a broad-spectrum benchmark of ten datasets spanning three levels of post-acquisition EEG analysis: signal-level assessment, brain-state decoding, and brain-health evaluation. INCEPT ranks first among recent EEG foundation models on 26 of 30 linear-probing metrics and 24 of 30 fine-tuning metrics, and also surpasses strong task-specific specialist encoders across diverse downstream settings. Objective ablations and representation analyses further show that invariance-oriented pre-training improves transfer and organizes subject-sensitive neural representations beyond reconstruction alone. These results establish invariance learning as a promising principle for building reusable EEG foundation models.

## Metadata
- **Published**: 2026-08-25T14:20:02Z
- **Authors**: Yulong Dou, Han Wu, Guo Chen, Fangmao Ju, Zhiming Cui, Dinggang Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24597v1)