---
title: ARENA: Automated Red-Teaming for Large Audio Language Models
published: 2026-08-16T07:03:53Z
authors: Jiaming He, Zhicong Huang, Tian Jin, Zhen Sun, Cheng Hong, Yi Yu, Wenbo Jiang, Xudong Jiang
url: http://arxiv.org/abs/2608.15578v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ARENA: Automated Red-Teaming for Large Audio Language Models

## Abstract
Large audio-language models (LALMs) make it possible to interact with language models through speech, music, and environmental sound, but they also introduce a safety surface that is difficult to expose with text-only red-teaming. We study automated audio-grounded red-teaming, where a text query must remain safe in isolation while the joint text-audio input induces harmful target behavior. We propose ARENA, a closed-loop framework that trains a controller on an independent 2,000case text-audio dataset. MD-Judge supplies training rewards and adaptive search feedback, while a separate, non-adaptive Llama Guard 3 evaluator alone labels final outcomes. On 520 held-out AdvBench objectives, ARENA achieves FDR/PSR of 87.9/100.0%, 71.5/96.3%, 68.1/100.0%, and 75.4/98.5% on Audio Flamingo 3, Qwen2-Audio, MiMo-Audio, and GPTAudio, respectively. Ablations show that feedback-based refinement and audio-variant search substantially improve attack discovery.

## Metadata
- **Published**: 2026-08-16T07:03:53Z
- **Authors**: Jiaming He, Zhicong Huang, Tian Jin, Zhen Sun, Cheng Hong, Yi Yu, Wenbo Jiang, Xudong Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15578v1)