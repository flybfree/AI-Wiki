---
title: A 2-Block Architecture for Real-Time EEG Gait Decoding: A Pilot Study
url: http://arxiv.org/abs/2608.02083v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_11-43-31Z_A2_BlockArchitectureforReal_TimeEEGGaitDecoding_AP.md
generated_at: 2026-08-03 23:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a two‑block BCI architecture that combines real‑time EEG feature extraction with artifact suppression and a decoder using a Polynomial Time‑Varying Layer plus LSTM for four‑state gait classification. The pilot study shows the decoder outperforms all variants with validation MCC 0.435, a gap of 0.187 over the best alternative. Closed‑loop deployment achieved initiation success rates of 55.3 % (Rex‑assisted) and 52.7 % (volitional) within a mean prediction time of 70.5 ms.

## Key Takeaways
- The architecture separates feature extraction from decoding, enabling artifact suppression in real time.
- PolyTVL+LSTM provides four‑state gait classification with higher MCC than previous models.
- Real‑time predictions are achieved under 100 ms latency, confirming feasibility for closed‑loop exoskeleton control.

## Context
Brain‑computer interfaces that rely on EEG often suffer from motion artifacts and limited temporal resolution. This work demonstrates how a modular neural network can integrate preprocessing with deep learning to improve signal quality without sacrificing speed. The approach aligns with broader trends toward lightweight, real‑time AI solutions for wearable medical devices.

## Implications
The findings suggest that modular BCI designs can be more robust than monolithic models in clinical settings. By reducing prediction latency and improving classification accuracy, the technology could enable practical exoskeleton applications for rehabilitation. Practitioners may adopt this architecture to develop low‑cost, high‑performance EEG‑based control systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02083v1)
