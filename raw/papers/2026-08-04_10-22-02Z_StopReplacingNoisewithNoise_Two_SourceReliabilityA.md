---
title: Stop Replacing Noise with Noise: Two-Source Reliability Assessment for Label Correction and Sample Reweighting in Label-Noise Learning
published: 2026-08-04T10:22:02Z
authors: Wenxiao Fan, Kan Li
url: http://arxiv.org/abs/2608.03432v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stop Replacing Noise with Noise: Two-Source Reliability Assessment for Label Correction and Sample Reweighting in Label-Noise Learning

## Abstract
Refurbishment-based noisy-label learning mixes an observed label with a model-derived pseudo target, typically using one sample-wise cleanliness score to control both branches. This creates a hidden coupling: reducing trust in the observed label automatically increases trust in the pseudo target. We show that this complementarity can replace one unreliable signal with another because a pseudo target learned from corrupted supervision may reproduce the noise it is meant to correct. Our representation diagnostics provide a consistent account of this mismatch: noisy supervision redirects deeper layers more strongly, whereas shallower relations remain comparatively stable and provide information beyond the loss posterior. We therefore propose TRACE, a Two-Source Reliability Assessment framework for Label Correction and Sample Reweighting. TRACE assesses the observed label using loss fit, shallow relation stability, and prediction agreement, while separately assessing the pseudo target using model confidence. Its source-specific scores control target correction and supervision strength without assuming complementary reliability. Across synthetic and real-world noisy benchmarks, TRACE improves representative refurbishment baselines and yields more reliable pseudo supervision.

## Metadata
- **Published**: 2026-08-04T10:22:02Z
- **Authors**: Wenxiao Fan, Kan Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03432v1)