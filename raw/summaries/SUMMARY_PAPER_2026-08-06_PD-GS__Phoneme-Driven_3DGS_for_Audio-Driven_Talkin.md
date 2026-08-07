---
title: PD-GS: Phoneme-Driven 3DGS for Audio-Driven Talking Heads
url: http://arxiv.org/abs/2608.05218v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_10-31-42Z_PD_GS_Phoneme_Driven3DGSforAudio_DrivenTalkingHead.md
generated_at: 2026-08-06 21:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Phoneme-Driven Gaussian Splatting (PD-GS) to improve talking-head rendering by aligning phoneme tokens with audio cues, reducing mouth closure violations. On the HDTF benchmark it achieves the best lip geometry among compared baselines and qualitatively improves articulation fidelity.

## Key Takeaways
- The model uses time-aligned phoneme tokens from ASR to guide discrete articulatory events, preventing over-smoothed mouth motion.
- A learned gate in the Linguistic Fusion Module balances continuous audio dynamics with sharp phoneme guidance during critical segments.
- PD-GS reduces closure violations on challenging phoneme sequences and outperforms LMD 2.66 on HDTF.

## Context
Current talking-head synthesis relies heavily on audio-driven motion, which often fails to respect precise speech articulation constraints leading to unnatural lip movements.

## Implications
This approach enables more linguistically faithful neural avatars for applications such as virtual assistants and immersive media where accurate speech representation is essential.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05218v1)
