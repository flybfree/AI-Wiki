---
title: From Inaudible Inputs to Model Failures: Low-Frequency Safety Risks in LALMs
url: http://arxiv.org/abs/2608.09158v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_06-09-50Z_FromInaudibleInputstoModelFailures_Low_FrequencySa.md
generated_at: 2026-08-10 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Intermittent Low‑Frequency Lockout (ILL), a red‑team technique that tests how large audio‑language models respond to inaudible low‑frequency signals, and presents Distributional Requery Guard (DRG) as a mitigation strategy. Experiments across six LALMs show up to 67 percentage points accuracy loss with human audibility near 1.33, while DRG restores performance to around 46 % after clean reacquisition.

## Key Takeaways
- ILL can degrade model output by as much as 67 percentage points when exposed to inaudible low‑frequency waveforms that are barely perceptible (rating 1.33).  
- The attack leverages Sentence Attention Scale Estimation and Frequency Confusion Transfer to create a continuous phase waveform aligned with corpus spectral variation, making it effective even though humans rate it as almost invisible.  
- DRG detects distribution shifts caused by low‑frequency interference and triggers a second recording, raising attacked accuracy from 28.5 % to 46.1 %, demonstrating the value of corrective reacquisition.

## Context
Audio‑language models are increasingly integrated into real‑world applications where environmental audio can contain frequencies below human hearing. Understanding how such signals affect model behavior is essential for reliable deployment, yet prior research has largely ignored low‑frequency safety risks in LALMs.

## Implications
Practitioners must incorporate red‑team testing that includes inaudible perturbations to ensure robustness of multimodal systems. The findings suggest a need for guard mechanisms like DRG and broader standards for handling non‑perceptual inputs across AI products.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09158v1)
