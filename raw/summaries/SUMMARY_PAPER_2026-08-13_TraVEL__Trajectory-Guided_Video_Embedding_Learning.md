---
title: TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval
url: http://arxiv.org/abs/2608.13495v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_17-24-23Z_TraVEL_Trajectory_GuidedVideoEmbeddingLearningforD.md
generated_at: 2026-08-13 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes TraVEL, a trajectory‑guided fine‑tuning method for multimodal video embeddings to retrieve driving clips with motion‑specific accuracy; it shows significant improvements over standard SFT on both small and large models.

## Key Takeaways
- Fine‑tuning Qwen3-VL-Embedding with InfoNCE using nuReasoning reasoning traces yields baseline gains but still lacks fine‑grained motion understanding.
- Introducing TraVEL, which uses ego‑trajectory similarity as a reward in Group Relative Policy Optimization, provides motion‑aware supervision without requiring ego poses or expert rules.
- Experiments demonstrate that TraVEL raises longitudinal and lateral mAP by 9.8 and 4.7 points at the 2B model, with smaller gains at 8B.

## Context
This work addresses the challenge of retrieving relevant driving video clips from massive logs where motion events are critical; it demonstrates how trajectory information can be leveraged within embedding‑centric pipelines to improve retrieval relevance without complex perception components.

## Implications
Practitioners can adopt TraVEL to enhance safety analysis and model training with minimal added infrastructure, offering a scalable solution for autonomous vehicle data curation that bridges deep learning and physical constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13495v1)
