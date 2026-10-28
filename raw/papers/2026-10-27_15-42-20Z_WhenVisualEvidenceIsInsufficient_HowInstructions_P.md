---
title: When Visual Evidence Is Insufficient: How Instructions, Post-Training, and Internal Activations Shape Refusal in Multimodal Language Models
published: 2026-10-27T15:42:20Z
authors: Ananth K Suresh, Aveen Dayal, Gouthaman KV, Aditya Pola, Vineeth N Balasubramanian
url: http://arxiv.org/abs/2610.37430v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Visual Evidence Is Insufficient: How Instructions, Post-Training, and Internal Activations Shape Refusal in Multimodal Language Models

## Abstract
For reliable deployment, multimodal large language models (MLLMs) should recognize when an image provides insufficient evidence to answer a question and withhold unsupported answers. Yet refusal alone is not necessarily evidence of such recognition: models may refuse because of unrelated safety constraints or without identifying the missing evidence. We study how refusal on visually unanswerable questions is shaped by three sources of control: inference-time instructions, post-training, and internal activation interventions. Across three MLLMs on the MoHoBench benchmark, we systematically manipulate the meaning and placement of refusal instructions, compare supervised and preference-based post-training, and intervene on a refusal-related activation direction derived from naturally answered and refused examples. We find that refusal is highly sensitive to both the meaning and placement of instructions, with model-specific changes at the sample level that are obscured by aggregate refusal rates. Evidence-aware and general refusal instructions have stronger effects than an intentionally mismatched safety instruction. Post-training produces larger increases in refusal, but can also induce responses that combine refusal language with attempted answers. In contrast, activation intervention produces smaller yet transferable changes across prompt conditions, without evidence of indiscriminate refusal on tested visually answerable samples. These findings show that refusal is jointly shaped by external instructions, post-training, and internal representations, highlighting the need to disentangle evidence recognition from a model's learned propensity to refuse.

## Metadata
- **Published**: 2026-10-27T15:42:20Z
- **Authors**: Ananth K Suresh, Aveen Dayal, Gouthaman KV, Aditya Pola, Vineeth N Balasubramanian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.37430v1)