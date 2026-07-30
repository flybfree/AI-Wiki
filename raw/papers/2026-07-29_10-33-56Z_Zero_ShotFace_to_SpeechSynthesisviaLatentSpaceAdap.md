---
title: Zero-Shot Face-to-Speech Synthesis via Latent Space Adaptation of a Style-Diffusion TTS Model
published: 2026-07-29T10:33:56Z
authors: Carlos Muñoz-Romero, Jose A. Gonzalez-Lopez
url: http://arxiv.org/abs/2607.26742v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Zero-Shot Face-to-Speech Synthesis via Latent Space Adaptation of a Style-Diffusion TTS Model

## Abstract
Zero-shot text-to-speech (TTS) clones a voice from a short audio prompt, but this reliance on reference audio is a barrier when only visual information is available, e.g. for historical figures or video-game characters. In this work, we propose a Face-to-Speech (F2S) framework that predicts a plausible voice from a static facial image. A lightweight Face Adapter, together with soft-tuning of the face encoder's upper blocks, aligns face-recognition features with the style space of a frozen StyleTTS 2 model, kept frozen during training. We evaluate on held-out identities from LRS3, a large-scale audiovisual corpus of English TED-talk videos. The synthesized speech is highly natural (UTMOS 3.7-4.0, matching or exceeding the 3.61 of ground truth), face-to-voice retrieval is consistently above chance, and the generated voice is consistent with the target speaker. Without any retraining, an English-trained adapter also produces fluent Spanish speech, indicating that the face-to-style mapping is largely language-agnostic.

## Metadata
- **Published**: 2026-07-29T10:33:56Z
- **Authors**: Carlos Muñoz-Romero, Jose A. Gonzalez-Lopez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26742v1)