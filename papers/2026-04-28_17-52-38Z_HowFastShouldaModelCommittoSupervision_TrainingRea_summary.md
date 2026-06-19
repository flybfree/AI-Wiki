---
title: "2026 04 28 17 52 38Z Howfastshouldamodelcommittosupervision Trainingrea Summary"
date: 2026-04-28
tags: ['paper', 'research', 'ai']
---
# How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum


**Source**: [Original Paper](http://arxiv.org/abs/2604.25907v1)
Saved: 2026-05-08 03:29
Source: 2026-04-28_17-52-38Z_HowFastShouldaModelCommittoSupervision_TrainingRea.md

---

## Summary
Introduces a Tsallis q-loss continuum that interpolates between RL from verifiable rewards and log-marginal-likelihood training for reasoning models. The paper derives GARL and PAFT estimators, showing how q trades off cold-start speed and noise, and reports that the methods can outperform GRPO depending on task and regime.

## Key Takeaways
- Frames supervision as a continuum between exploitation and density estimation.
- Explains cold-start stalling through the scaling of gradient flow.
- Provides two Monte Carlo estimators with different bias-variance tradeoffs.

## Context
The work targets post-training of reasoning models when initial success probability is low.

## Implications
Choosing the right q may improve early learning dynamics and training stability.

## Original Reference
- Title: How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum
- Authors: Chu-Cheng Lin, Eugene Ie
- Published: 2026-04-28T17:52:38Z
- URL: http://arxiv.org/abs/2604.25907v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-04-28_17-52-38Z_HowFastShouldaModelCommittoSupervision_TrainingRea.md
