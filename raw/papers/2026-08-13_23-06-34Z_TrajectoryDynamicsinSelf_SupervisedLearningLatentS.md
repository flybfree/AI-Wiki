---
title: Trajectory Dynamics in Self-Supervised Learning Latent Space for Audio Deepfake Detection
published: 2026-08-13T23:06:34Z
authors: Tomás Andrade Weber
url: http://arxiv.org/abs/2608.13817v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trajectory Dynamics in Self-Supervised Learning Latent Space for Audio Deepfake Detection

## Abstract
Human speech production is constrained by physiology, giving rise to characteristic temporal structure on acoustic signals. We hypothesise that these constraints manifest as structured trajectory dynamics in the latent space of Self-Supervised Learning (SSL) models, and that synthetic speech violates them detectably. To test this hypothesis, we train a causal Long Short-Term Memory (LSTM) next-frame predictor on bonafide speech only (Stage 1), using the deepfake-specialised SSL backbone Wav2Vec2-Large-AntiDeepfake, and compare against a static global-average-pooling baseline using identical features, thus isolating the contribution of temporal modelling. A supervised Stage 2, which trains a Multi-Layer Perceptron on the frozen LSTM internal states using labelled data, is included to characterise the role of spoof supervision. Our system achieves competitive or state-of-the-art performance across six benchmarks: ASVspoof 2019/2021, Codecfake, In-the-Wild, MLAAD-EN, and Deepfake-Eval-2024, including best published EER on ASVspoof 2021 (0.75\%) and, notably, Stage 1 trained on bonafide speech only surpasses the published supervised baseline from the same backbone on DE2024 (30.35\%). On near-domain benchmarks, static and dynamic approaches perform comparably. On harder cross-corpus benchmarks with diverse synthesis methods, trajectory dynamics provide substantial gains, confirming that temporal physiological constraints carry detection signal beyond utterance-level statistics.

## Metadata
- **Published**: 2026-08-13T23:06:34Z
- **Authors**: Tomás Andrade Weber
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13817v1)