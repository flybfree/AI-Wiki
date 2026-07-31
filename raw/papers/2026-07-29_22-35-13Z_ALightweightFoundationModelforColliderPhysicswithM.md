---
title: A Lightweight Foundation Model for Collider Physics with Multi-Domain Adaptation
published: 2026-07-29T22:35:13Z
authors: Liangyu Wu, Qibin Liu, Alexander Yue, Julia Gonski
url: http://arxiv.org/abs/2607.27501v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Lightweight Foundation Model for Collider Physics with Multi-Domain Adaptation

## Abstract
We present a lightweight approach to foundation modeling (\textbf{NEXUS}) that leverages pre-trained learning from collider physics data towards out-of-domain tasks in other scientific datasets, using a fully connected autoencoder model with approximately 3 million parameters. The model pre-trains with no supervision over a large-scale collision dataset from the Large Hadron Collider modeled by charged particle track features. Downstream tasks for collider analyses, such as kinematic regression and event classification, are developed on pre-trained model weights and achieve improved accuracy with only small labeled datasets when compared to equivalent architectures trained from scratch. The benefits of pre-training are additionally investigated through latent space interpretation and application to other domains, including gravitational waves, flood forecasting, and neural activity. Furthermore, the relative computational simplicity of NEXUS is demonstrated compared to transformer approaches at comparable scale, opening the door to power-efficient inference and real-time or edge applications of foundation models in scientific experiments.

## Metadata
- **Published**: 2026-07-29T22:35:13Z
- **Authors**: Liangyu Wu, Qibin Liu, Alexander Yue, Julia Gonski
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27501v1)