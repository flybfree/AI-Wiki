---
title: HALO: A Heterogeneity-Aware Language-Aligned IMU Foundation Model for Open-Set Human Activity Recognition
published: 2026-08-27T15:17:12Z
authors: Zihan Ding, Liyu Zhang, Xiaomin Ouyang
url: http://arxiv.org/abs/2608.27233v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HALO: A Heterogeneity-Aware Language-Aligned IMU Foundation Model for Open-Set Human Activity Recognition

## Abstract
Human Activity Recognition (HAR) using inertial measurement units (IMUs) enables a wide range of applications, yet the field still lacks a unified model that can generalize across diverse subjects, devices, and activities. Training such a model is difficult due to two key challenges: sensing heterogeneity -- differences in sampling rates, channel configurations, and sensor placements -- and poor generalization to unseen activities and label vocabularies. We introduce HALO (Heterogeneity-Aware Language-aligned Open-set model), a domain-specific IMU foundation model that addresses both challenges through a two-stage training framework. Stage 1 pretrains the IMU encoder with heterogeneity-aware self-supervised learning, including adaptive-pooling tokenization, channel-independent feature extraction, and contextualized sensor conditioning that injects natural-language sensor descriptions into each channel embedding. Stage 2 aligns this IMU encoder with text embeddings via synonym-aware soft contrastive learning, enabling open-set recognition via cosine-similarity retrieval without per-dataset classifiers. Trained on 10 public HAR datasets and evaluated on 7 held-out datasets, HALO outperforms five state-of-the-art baselines on all 8 aggregate metrics, and still leads on 3 of 4 settings under baseline-matched inputs. Despite using only ~35M trainable parameters -- 10x fewer than the latest foundation model MOMENT (341.2M) -- HALO improves zero-shot open-set accuracy, measured over all 87 training labels, by 13.7 percentage points. On two further datasets with severe distribution shift, every model including HALO collapses zero-shot. A video demonstration of HALO's performance in real world is available at https://youtu.be/rooVKragtFU

## Metadata
- **Published**: 2026-08-27T15:17:12Z
- **Authors**: Zihan Ding, Liyu Zhang, Xiaomin Ouyang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27233v1)