---
title: Enhancing Multimodal Emotion Recognition via Multi-Feature Encoding and Attention-Based Fusion
published: 2026-09-04T03:40:16Z
authors: Xu Lin, Ke Wang, Hui Kang, Xinying Wang
url: http://arxiv.org/abs/2609.04690v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enhancing Multimodal Emotion Recognition via Multi-Feature Encoding and Attention-Based Fusion

## Abstract
Multimodal emotion recognition has attracted growing interest due to its importance in human-computer interaction, remote education, and healthcare. This paper proposes a novel multimodal emotion recognition framework that integrates rich audio and visual feature extraction with an attention-based fusion strategy. For audio, we extract three complementary feature types: semantic embeddings from Wav2Vec2, MFCC features, and statistical acoustic descriptors such as pitch, energy, and rhythm. These are aligned and fused via a BiLSTM to capture temporal dependencies. For video, we propose a ResNet50-BiLSTM architecture that combines deep residual learning and sequential modeling to extract expressive spatiotemporal features from facial sequences. To enhance multimodal synergy, we introduce a feature-level fusion mechanism based on multi-head attention, allowing the model to adaptively weigh contributions across modalities. Experiments conducted on the MELD and IEMOCAP datasets demonstrate that our model significantly outperforms baselines in both accuracy and robustness. Furthermore, ablation studies show that the attention-based fusion strategy significantly improves performance in unbalanced data settings. Our findings suggest that the proposed framework effectively captures diverse emotional cues from speech and visual expressions, and offers a practical and generalizable approach for real-world multimodal emotion recognition tasks.

## Metadata
- **Published**: 2026-09-04T03:40:16Z
- **Authors**: Xu Lin, Ke Wang, Hui Kang, Xinying Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04690v1)