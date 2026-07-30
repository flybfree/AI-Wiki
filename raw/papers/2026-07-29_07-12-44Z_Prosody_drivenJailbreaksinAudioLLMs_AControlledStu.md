---
title: Prosody-driven Jailbreaks in Audio LLMs: A Controlled Study and Mechanistic Analysis
published: 2026-07-29T07:12:44Z
authors: Jiachen Qian, Junyu Li
url: http://arxiv.org/abs/2607.26541v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prosody-driven Jailbreaks in Audio LLMs: A Controlled Study and Mechanistic Analysis

## Abstract
Audio-capable foundation models enable end-to-end spoken interaction, but they also introduce safety risks beyond transcript content. It remains unclear how much jailbreak capability can arise from matched-text variation in speech delivery rather than from lexical rewriting or broader style transfer. We study this question by holding transcript content fixed and varying six speech-delivery presets whose acoustic attributes may co-vary. We present PJ-Break, a black-box evaluation protocol with presets targeting arousal, authority, and speaking rate, together with AdvAudio-Prosody, a 600-sample benchmark with acoustically verified attributes. On the exact post-QC Qwen2-Audio panel, the Q=1 Panic (38/95), Anger (35/95), and Fast (32/95) presets are all well above Neutral (4/95). The fixed six-query pool covers 44/95 Qwen2-Audio seeds and 15/95 GPT-4o seeds and exceeds a matched-budget StyleBreak reimplementation (27/95) on Qwen2-Audio. A same-voice pool excluding the confounded Commanding condition still reaches 40/95, and a retained-panel ablation shows emotional-delivery audio alone (44/95) is far more effective than emotional text alone (11/95). Exploratory surrogate diagnostics and pilot mitigation observations are secondary, non-core analyses. Overall, matched-text speech delivery should be treated as a first-class factor in Audio LLM safety evaluation

## Metadata
- **Published**: 2026-07-29T07:12:44Z
- **Authors**: Jiachen Qian, Junyu Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26541v1)