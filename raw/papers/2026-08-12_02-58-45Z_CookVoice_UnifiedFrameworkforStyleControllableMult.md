---
title: CookVoice: Unified Framework for Style Controllable Multi-Modal Human Voice Generation
published: 2026-08-12T02:58:45Z
authors: Haowei Lou, Hye-Young Paik, Dai Jia, Kai Li, Lina Yao
url: http://arxiv.org/abs/2608.11590v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CookVoice: Unified Framework for Style Controllable Multi-Modal Human Voice Generation

## Abstract
Human voice generation has made rapid progress in speech generation, singing voice generation, voice cloning, and voice editing. However, most existing systems are designed for specific tasks and often rely on task-dependent architectures, control signals, or autoregressive decoding, limiting fine-grained controllability and inference efficiency. In this paper, we propose CookVoice, a unified framework for multimodal, multi-style, and multi-task human voice generation. CookVoice decomposes the human voice into three key factors: content, prosody, and style, enabling both speech and singing voice generation within a unified model. To achieve precise and flexible controllability, we design a flexible alignment strategy that maps text, style, and prosody control signals onto the frame-level of spectrogram. This design allows CookVoice to support a wide range of tasks, including text-to-speech, text-to-singing voice, style-controllable generation, voice mimicry, voice conversion, and voice editing. Experimental results show that CookVoice achieves generation quality comparable to existing Text-to-Speech and text-to-singing voice baselines, while providing stronger style and prosody controllability. Moreover, CookVoice achieves comparable performance to large-scale baselines with only 43.51 million parameters and efficient inference using as few as 4 ODE steps, making it a practical solution for real-world human voice generation applications. Demo page is available at https://haoweilou.github.io/CookVoice/.

## Metadata
- **Published**: 2026-08-12T02:58:45Z
- **Authors**: Haowei Lou, Hye-Young Paik, Dai Jia, Kai Li, Lina Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11590v1)