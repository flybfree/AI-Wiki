---
title: Long Listening Thoughts: Eliciting Open Auditory Reasoning with Deliberative Perception and Cognitive Refinement
published: 2026-10-17T03:20:36Z
authors: Jaeyeon Kim, Chao-Han Huck Yang, Luoyi Zhang, Chan-Jan Hsu, Fernando Ruiloba Portilla, Jinchuan Tian, Shinji Watanabe, Carlos Busso
url: http://arxiv.org/abs/2610.24409v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Long Listening Thoughts: Eliciting Open Auditory Reasoning with Deliberative Perception and Cognitive Refinement

## Abstract
We introduce Long Listening Thoughts (LLT), a framework for constructing post-training datasets that improves audio reasoning by pairing deliberate perceptual grounding with explicit cognitive behaviors. On audio understanding and reasoning benchmarks, large audio-language models (LALMs) are limited primarily by perceptual errors, yet existing post-training datasets rely on audio descriptions of limited diversity. Through a four-stage pipeline, LLT (1) builds multi-aspect dense audio descriptions spanning semantic, acoustic, and temporal information, (2) generates more challenging questions, (3) synthesizes incorrect reasoning traces, and (4) extends short reasoning traces into long ones via a thought-continuation strategy that elicits cognitive behaviors such as verification and backtracking. Using LLT, we synthesize 1.6M reasoning traces and train Qwen2.5-Omni-7B with a two-stage pipeline of supervised fine-tuning (SFT) followed by direct preference optimization (DPO). This improves accuracy on MMAU Test-mini (71.5 to 78.2), MMAR (56.7 to 63.7), and MMSU (60.6 to 66.0).

## Metadata
- **Published**: 2026-10-17T03:20:36Z
- **Authors**: Jaeyeon Kim, Chao-Han Huck Yang, Luoyi Zhang, Chan-Jan Hsu, Fernando Ruiloba Portilla, Jinchuan Tian, Shinji Watanabe, Carlos Busso
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24409v1)