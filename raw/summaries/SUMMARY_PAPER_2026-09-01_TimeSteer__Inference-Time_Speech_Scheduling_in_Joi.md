---
title: TimeSteer: Inference-Time Speech Scheduling in Joint Audio-Visual Diffusion Models
url: http://arxiv.org/abs/2609.01277v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-12-57Z_TimeSteer_Inference_TimeSpeechSchedulinginJointAud.md
generated_at: 2026-09-01 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TimeSteer, a training‑free method for inference‑time speech scheduling in joint audio‑visual diffusion models. It enables users to place speech and visual cues within custom intervals without retraining the model. Experiments show improved interval controllability while preserving generation quality.

## Key Takeaways
- The model uses a timing‑sensitive text‑to‑audio cross‑attention head that reveals each utterance's source span on the latent timeline, allowing precise placement of audio‑visual content.
- Predicted clean latents already organize speech and visual articulation, so temporal editing can be done without regenerating full content.
- TimeSteer transfers the associated audio‑visual latent from its original interval to a target interval via region‑aware remapping, providing interval‑level control.

## Context
Joint audio‑visual diffusion models generate synchronized media but lack explicit timing controls. This limitation hampers applications where precise speech placement is required such as interactive storytelling or user‑driven video generation. The paper addresses this gap by decoupling content from its temporal position during inference.

## Implications
For developers, TimeSteer offers a practical way to fine‑tune the experience without model updates, reducing deployment complexity. In industry, it can enable dynamic adverts where speech timing aligns with visual cues, enhancing user engagement and personalization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01277v1)
