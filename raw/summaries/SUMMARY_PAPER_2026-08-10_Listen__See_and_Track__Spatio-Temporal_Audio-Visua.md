---
title: Listen, See and Track: Spatio-Temporal Audio-Visual Sound Event Reasoning for Omni-Modal Language Models
url: http://arxiv.org/abs/2608.09435v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_11-06-28Z_Listen_SeeandTrack_Spatio_TemporalAudio_VisualSoun.md
generated_at: 2026-08-10 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ST-OmniQA, a benchmark for spatio‑temporal audio‑visual reasoning, and its model ST‑Omni‑R1 that learns to identify sound sources, their locations, and trajectories from panoramic videos paired with first‑order Ambisonics. The model reaches an average semantic accuracy of 77.83 % across four difficulty levels, surpassing the best baseline at 37.28 %.

## Key Takeaways
- ST-OmniQA provides a large‑scale dataset (40K videos, 400K QA pairs) organized into four capability levels covering sound‑event recognition, direction of arrival, source distance, motion trajectories and temporally grounded reasoning.
- ST‑Omni‑R1 integrates FOA‑derived semantic and trajectory representations with panoramic visual context using progressive curriculum learning and reasoning‑tree reinforcement learning to improve performance on all levels.
- The model’s learned spatial and motion representations transfer beyond the benchmark to three public spatial‑audio datasets, demonstrating broader utility.

## Context
This work tackles a gap in multimodal models that treat audio as isolated events without spatial cues. By fusing FOA audio with panoramic visuals, it advances embodied reasoning toward more realistic perception tasks.

## Implications
The results suggest that integrating spatial audio with vision can significantly boost performance for robotics, augmented reality and other real‑world applications. Practitioners may adopt similar curriculum learning strategies to enhance model generalization across multimodal challenges.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09435v1)
