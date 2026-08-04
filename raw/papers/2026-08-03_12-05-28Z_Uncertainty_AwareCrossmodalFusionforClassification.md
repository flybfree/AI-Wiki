---
title: Uncertainty-Aware Crossmodal Fusion for Classification of Animal Behavior
published: 2026-08-03T12:05:28Z
authors: Ehsan Yaghoubi, Florian Haselbeck
url: http://arxiv.org/abs/2608.02104v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Uncertainty-Aware Crossmodal Fusion for Classification of Animal Behavior

## Abstract
Artificial intelligence offers substantial potential for acoustic monitoring of animals, from welfare assessment in precision livestock farming to wildlife conservation and ecological research, where vocalizations can indicate health, stress, and social states earlier and at lower cost than manual observation. However, recordings in these settings are obtained under uncontrolled conditions, including environmental noise, reverberation, overlapping calls, and sensors that degrade without notice. As a consequence, automated classification of animal vocalizations remains challenging, and the two dominant acoustic representations show complementary limitations: raw waveforms preserve temporal microstructure but degrade under clipping and reverberation, while log-Mel spectrograms capture harmonic organization but lose phase information and are sensitive to broadband noise. To address these challenges, we propose Uncertainty-Aware Fusion (UAF), a dual-stream framework that estimates Gaussian uncertainty for each representation and fuses them via uncertainty weighting. This mechanism assigns greater weight to the more confident representation with no reliability labels required. In a cross-species, identity-based evaluation excluding all individuals seen during training, UAF (mean pooling) achieves 59.4\% accuracy / 39.7\% macro F1 on the 17-class SoundWel pig vocalization benchmark and 73.1\% accuracy / 71.5\% macro F1 on the 3-class DogBark dataset, outperforming static-concatenation fusion by 15.7\% and 20.4\% relative macro F1, respectively. Ablations over four temporal aggregation strategies show that uncertainty fusion, rather than the temporal characteristics of animal calls, is the primary driver of the performance gain.

## Metadata
- **Published**: 2026-08-03T12:05:28Z
- **Authors**: Ehsan Yaghoubi, Florian Haselbeck
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02104v1)