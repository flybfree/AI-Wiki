---
title: MUPA$^{2}$E: Multimodal Unified Perception with Asymmetric Attention for Emotion Assessment
url: http://arxiv.org/abs/2608.15999v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_01-26-47Z_MUPA___2__E_MultimodalUnifiedPerceptionwithAsymmet.md
generated_at: 2026-08-17 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MUPA$^{2}$E, a unified perception framework that jointly processes facial video and electroencephalography (EEG) using a single asymmetric‑attention backbone. The study evaluates this approach on the DMER dataset under a subject‑independent protocol, comparing unimodal and fused configurations and finding that merged fusion at stride~30 yields the highest validation performance with a test accuracy of 70.07 %. It also notes that uneven recording durations across affective classes create a zero‑padding pattern that can act as a classification cue.

## Key Takeaways
- The fused video–EEG model reaches peak performance when EEG is projected into the spatial domain and fusion occurs at stride~30, achieving 70.07 % test accuracy.  
- Zero‑padding introduced by varying trial lengths may serve as an inadvertent cue for affective classification, suggesting a need to control this artifact.  
- When all recordings are cropped to a common 20‑second duration, the test accuracy drops to 62.71 %, indicating that duration uniformity is essential for a fair evaluation.

## Context
Multimodal emotion assessment remains challenging because visual and neural signals often require separate feature pipelines before fusion. Recent advances in shared attention mechanisms aim to overcome this fragmentation, but dataset artifacts such as uneven recording lengths can bias results if not addressed. This work contributes by demonstrating that a compact unified architecture can handle structurally disparate inputs while highlighting the importance of preprocessing for fairness.

## Implications
For practitioners, controlling duration‑related cues is crucial when training models on affective datasets to avoid overfitting to non‑emotional artifacts. In industry, this insight supports more reliable emotion detection systems that rely on both video and EEG data without compromising performance due to dataset inconsistencies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15999v1)
