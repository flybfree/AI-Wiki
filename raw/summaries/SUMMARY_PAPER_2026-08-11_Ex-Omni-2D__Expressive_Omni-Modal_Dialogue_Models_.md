---
title: Ex-Omni-2D: Expressive Omni-Modal Dialogue Models with Native Visual Presence
url: http://arxiv.org/abs/2608.10720v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_09-37-11Z_Ex_Omni_2D_ExpressiveOmni_ModalDialogueModelswithN.md
generated_at: 2026-08-11 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Ex-Omni-2D, an omni-modal dialogue system that generates a coordinated response of text, personalized speech, and reference-conditioned video from multimodal inputs. It achieves this by producing a Visual Thought Plan (VTP) that encodes scene, emotion, and motion, then outputs structured text and multi-codebook speech units aligned with video frames. The method uses a full-sequence Video Generator as teacher and a distilled Streaming Student for efficient inference.

## Key Takeaways
- The model creates a Visual Thought Plan (VTP) to guide the generation of scene, emotion, and motion components in the response.
- It produces native multi-codebook speech units that are decoded into speech and aligned online with video frames, forming a shared acoustic-temporal interface.
- A four-step pipeline on four GPUs yields an end-to-end real-time factor (RTF) of 1.293 at 400×720 resolution, balancing quality and efficiency.

## Context
Current omni-modal dialogue models excel at understanding multimodal inputs but produce visually disembodied responses lacking natural presence. This work addresses the need for embodied, synchronized visual outputs that align speech and video in real time.

## Implications
The integration of a shared acoustic-temporal interface enables more natural avatar interactions without requiring massive query-text-speech-video supervision. Practitioners can deploy this framework on four GPUs with low latency, opening possibilities for real-time conversational avatars in immersive applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10720v1)
