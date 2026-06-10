---
title: 'FactorizedHMR: A Hybrid Framework for Video Human Mesh Recovery'
published: 2026-05-14T13:59:56Z
authors: Patrick Kwon, Chen Chen
url: http://arxiv.org/abs/2605.14854v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FactorizedHMR: A Hybrid Framework for Video Human Mesh Recovery

## Abstract
Human Mesh Recovery (HMR) is fundamentally ambiguous: under occlusion or weak depth cues, multiple 3D bodies can explain the same image evidence. This ambiguity is not uniform across the body, as torso pose and root structure are often relatively well constrained, whereas distal articulations such as the arms and legs are more uncertain. Building on this observation, we propose FactorizedHMR, a two-stage framework that treats these two regimes differently. A deterministic regression module first recovers a stable torso-root anchor, and a probabilistic flow-matching module then completes the remaining non-torso articulation. To make this completion reliable, we combine a composite target representation with geometry-aware supervision and feature-aware classifier-free guidance, preserving the torso-root anchor while improving single-reference recovery of ambiguity-prone articulation. We also introduce a synthetic data pipeline that provides the paired image-camera-motion supervision under diverse viewpoints. Across camera-space and world-space benchmarks, FactorizedHMR remains competitive with strong baselines, with the clearest gains in occlusion-heavy recovery and drift-sensitive world-space metrics.

## Metadata
- **Published**: 2026-05-14T13:59:56Z
- **Authors**: Patrick Kwon, Chen Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.14854v1)