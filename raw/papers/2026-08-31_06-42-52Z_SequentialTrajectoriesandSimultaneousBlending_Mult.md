---
title: Sequential Trajectories and Simultaneous Blending: Multi-Emotion Modeling for Instruction-Following TTS
published: 2026-08-31T06:42:52Z
authors: Yan Zhou, Yun Hong, Yang Feng
url: http://arxiv.org/abs/2608.30325v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sequential Trajectories and Simultaneous Blending: Multi-Emotion Modeling for Instruction-Following TTS

## Abstract
Natural-language instructions enable flexible control of synthesized speech, yet emotional TTS systems primarily model a single utterance-level affect, leaving multi-emotion control underexplored. We study two complementary multi-emotion TTS tasks: emotion trajectory, which spans several ordered affective stages, and emotion blending, in which multiple emotions coexist throughout an utterance. These tasks expose a supervision mismatch: supervised fine-tuning (SFT) does not explicitly evaluate emotion features, while single-emotion rewards provide neither structure-aware feedback for trajectory completion nor pair-aware feedback for blending. We introduce HybridEmo, a post-training framework that initializes both tasks with SFT and then aligns the speech-token policy through Group Relative Policy Optimization using a sample-aware hybrid reward. For trajectory samples, segment-aligned consistency combines average and weakest-stage evidence to preserve the correctness and completeness of prescribed stages. For blending samples, a GMM-based reward combines frame-level support from the union of target-emotion anchors in an offline emotion space with an utterance-level weaker-target margin. Both branches share an ASR reward and are routed within a unified policy. On MultiEmo-Test, HybridEmo significantly improves trajectory correctness and blending intensity, without a noticeable degradation in speaker similarity. Human evaluation prefers HybridEmo to CosyVoice 3 and EmoVoice-0.5B, with nearly balanced preferences against Qwen3-TTS.

## Metadata
- **Published**: 2026-08-31T06:42:52Z
- **Authors**: Yan Zhou, Yun Hong, Yang Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30325v1)