---
title: AuEmoChat: Authentic Emotion Understanding and Rendering for Conversational Speech Synthesis
published: 2026-07-17T08:47:58Z
authors: Zhenqi Jia, Yuan Zhao,  Aruukhan, Rui Liu, Haizhou Li
url: http://arxiv.org/abs/2607.15755v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AuEmoChat: Authentic Emotion Understanding and Rendering for Conversational Speech Synthesis

## Abstract
Conversational Speech Synthesis (CSS) aims to synthesize speech with human-like emotional expression and contextual consistency in user-agent interactions. Existing CSS methods struggle to render authentic human emotions due to limited predefined emotion label spaces (e.g., seven emotion categories), while redundant multimodal tokens in multi-turn dialogue history interfere with context understanding. To address these issues, we propose AuEmoChat, a CSS framework for authentic emotion understanding and rendering. First, we develop AuEmoCodec, which learns a discrete authentic emotion token space from large-scale emotional speech via finite scalar quantization, enabling a more authentic emotion representation than limited basic emotion categories. We further propose AuEmoToMe, an authentic-emotion-guided token merging algorithm that merges redundant tokens in multimodal dialogue history while preserving emotion-relevant context. We integrate it into an autoregressive text-speech model to predict the target authentic emotion token and speech tokens. Finally, we propose Authentic Emotion Flow Matching, which renders speech by jointly conditioning on merged dialogue context, target authentic emotion, and acoustic priors. Extensive experiments on the NCSSD-EmCap dataset demonstrate that AuEmoChat outperforms state-of-the-art CSS baselines and generates more expressive and authentic emotional speech.

## Metadata
- **Published**: 2026-07-17T08:47:58Z
- **Authors**: Zhenqi Jia, Yuan Zhao,  Aruukhan, Rui Liu, Haizhou Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.15755v1)