---
title: CM-MAE: A Physics-Guided Cross-Modal Self-Supervised Learning Framework for Vision-Wireless Applications
published: 2026-08-16T23:55:03Z
authors: Yubo Zhang, Yiyao Liu
url: http://arxiv.org/abs/2608.15972v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CM-MAE: A Physics-Guided Cross-Modal Self-Supervised Learning Framework for Vision-Wireless Applications

## Abstract
Synchronized camera and wireless measurements observe the same scene through different physical channels. The central difficulty is that a representation learned in one deployment can fail when viewpoint, traffic, illumination, and propagation geometry change. This paper presents CM-MAE, a self-supervised vision--wireless pretraining framework for cross-scenario representation transfer. The evaluated real-data model uses only RGB frames and the measured 64-beam received-power vector available in DeepSense 6G; it does not use ray-traced paths, calibrated depth, or beam-index labels during pretraining. Its central pretraining term is a \emph{soft contrastive alignment loss}. Instead of making the synchronized image--wireless pair the only positive pair, this loss builds a target distribution from similarities between measured beam-power profiles, so nonidentical samples with similar directional responses are not forced apart as false negatives. A masked joint decoder provides the complementary local objective by reconstructing hidden visual patches and wireless angular clusters under modality dropout. After pretraining, a differential-rate fine-tuning rule lets a new fusion head adapt quickly while the encoders move slowly. Under a sequence-disjoint DeepSense 6G protocol, adding the soft alignment loss improves a matched linear-probe transfer average from 24.88\% to 29.49\%. Mild fusion fine-tuning reaches 77.38\% Top-1 accuracy on unseen Scenarios 6--8, and optional transductive normalization adaptation reaches 78.69\%. Since the fusion setting uses the contemporaneous 64-beam power vector at inference, these results should be read as representation-transfer diagnostics, not as proactive beam-prediction or reduced-sweeping claims.

## Metadata
- **Published**: 2026-08-16T23:55:03Z
- **Authors**: Yubo Zhang, Yiyao Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15972v1)