---
title: PRISM-Bench: An Audio-Centric Diagnostic Benchmark for Text-to-Audio-Video Generation
published: 2026-09-04T08:27:10Z
authors: Yuchen Sun, Qian Yang, Jun Wang, Detai Xin, Guoqiao Yu, Guanglu Wan, Qi Jia
url: http://arxiv.org/abs/2609.04867v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PRISM-Bench: An Audio-Centric Diagnostic Benchmark for Text-to-Audio-Video Generation

## Abstract
Text-to-audio-video (T2AV) generation has advanced rapidly, but its evaluation still underestimates the audio modality. Existing benchmarks either treat audio as an auxiliary component of video quality or assess it in isolation from audiovisual grounding, making it difficult to diagnose where current systems truly succeed or fail in audio generation. We present PRISM-Bench, the first audio-centric diagnostic benchmark for T2AV generation. Built from a rigorously curated dataset of 900 human-verified samples, PRISM-Bench factorizes audio evaluation along two orthogonal axes: audio type (Speech, Music, and Sound) and sound-source visibility (On-screen vs. Off-screen). It evaluates generated content across four perceptual dimensions (Audio-Visual Coherence, Audio Quality, Audio Expressiveness, and Prompt Following) with 35 fine-grained criteria. To ensure reliable assessment, we adopt an enhanced MLLM-as-a-Judge protocol based on blind, side-by-side comparison against ground-truth references, demonstrating strong alignment (over 70% mean agreement) with human raters. Our evaluation of recent T2AV systems highlights a significant performance gap between frontier and open-source models. Furthermore, we demonstrate that current generation paradigms overfit to perceptual fidelity while struggling with complex grounding and control tasks, particularly in generating music and synchronized On-screen audio.

## Metadata
- **Published**: 2026-09-04T08:27:10Z
- **Authors**: Yuchen Sun, Qian Yang, Jun Wang, Detai Xin, Guoqiao Yu, Guanglu Wan, Qi Jia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04867v1)