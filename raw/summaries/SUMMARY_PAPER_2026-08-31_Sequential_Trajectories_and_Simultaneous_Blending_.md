---
title: Sequential Trajectories and Simultaneous Blending: Multi-Emotion Modeling for Instruction-Following TTS
url: http://arxiv.org/abs/2608.30325v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_06-42-52Z_SequentialTrajectoriesandSimultaneousBlending_Mult.md
generated_at: 2026-08-31 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the gap between single‑emotion emotional TTS and multi‑emotion control by introducing two tasks: emotion trajectory, where a sequence of affective stages is generated, and emotion blending, where multiple emotions coexist. The authors propose HybridEmo, a post‑training framework that aligns speech‑token policies using Group Relative Policy Optimization with a hybrid reward that combines segment‑aligned consistency for trajectories and GMM‑based frame rewards for blending. On the MultiEmo‑Test benchmark, HybridEmo improves both task metrics while keeping speaker similarity stable.

## Key Takeaways
- The framework introduces a hybrid reward that merges average and weakest stage evidence to ensure trajectory correctness and completeness, addressing supervision mismatch between SFT and single‑emotion rewards.
- For blending, the GMM reward uses frame‑level support from emotion anchors in an offline space alongside an utterance‑level weaker‑target margin, enabling simultaneous multi‑emotion generation without sacrificing speaker identity.
- HybridEmo achieves significant gains on both trajectory correctness and blending intensity while maintaining comparable speaker similarity to state‑of‑the‑art models like CosyVoice 3.

## Context
Emotional TTS remains limited to single affective labels, restricting applications that require nuanced emotional expression. Multi‑emotion control is essential for realistic user interaction where users may want a blend of emotions or a progression through feelings. This work advances the field by providing a unified policy capable of handling both ordered and simultaneous emotion cues.

## Implications
For industry practitioners, HybridEmo offers a practical solution to integrate multi‑emotion capabilities into existing TTS pipelines without retraining from scratch. Practitioners can leverage the framework to deliver richer user experiences in voice assistants, gaming, and accessibility tools where precise emotional control is valued.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30325v1)
