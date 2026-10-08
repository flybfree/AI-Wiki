---
title: Steering Follows Geometry, Not Labels: Emotion Directions in a Full-Duplex Speech Model
published: 2026-10-06T15:29:37Z
authors: Pulak Kuli
url: http://arxiv.org/abs/2610.08887v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Steering Follows Geometry, Not Labels: Emotion Directions in a Full-Duplex Speech Model

## Abstract
Full-duplex voice agents need to modulate emotion and delivery during real-time conversations, when de-escalating a complaint, carrying urgency in dispatch, softening a clinical result. Emotion and delivery control is well studied for TTS and turn based models through prompt-conditioned synthesis, reference-conditioned synthesis and activation steering; PersonaPlex controls identity in a duplex model but not affect.   We study emotion steering in Moshi, a fully open sourced full-duplex speech language model, across four emotions, using mean-difference activation steering, which costs only a few vector additions per frame and no retraining.   We show that emotion is linearly decodable from Moshi's residual stream, but activation steering is only partially achievable, and unevenly so; as happy, angry and surprise steer towards a shared direction while sad is distinctly steerable. We also show that the shared component across the three emotions cannot simply be projected away from all the emotions equally.

## Metadata
- **Published**: 2026-10-06T15:29:37Z
- **Authors**: Pulak Kuli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08887v1)