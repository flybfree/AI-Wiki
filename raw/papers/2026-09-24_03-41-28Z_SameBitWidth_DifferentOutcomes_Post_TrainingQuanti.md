---
title: Same Bit Width, Different Outcomes: Post-Training Quantization of Text-to-Speech Across Architectures
published: 2026-09-24T03:41:28Z
authors: Se Un Park, Yutae Kim, Junyoung Park
url: http://arxiv.org/abs/2609.28974v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Same Bit Width, Different Outcomes: Post-Training Quantization of Text-to-Speech Across Architectures

## Abstract
Post-training quantization (PTQ) reduces the cost of on-device text-to-speech (TTS), but published evaluations cover one system or method. We evaluate PTQ across TTS architectures under one protocol with three core models, weight and activation ablations of eight more, and two held-out models quantized blind. Four-bit per-channel weights reduce UTMOS, a predicted mean opinion score, by 2.8 on Supertonic and 0.07 on Kokoro, and per-tensor scaling can cause severe degradation even at 8 bits. The same bit width yields different outcomes, because the sensitive component is model-specific and not reliably predicted from the model class. A staged ablation procedure identifies it, and per-layer GPTQ can restore it to within 0.1 UTMOS. Real int8 and int4 kernels reproduce the simulated ordering at hardware-dependent cost. On a Mac mini, a 4-bit weight kernel runs Supertonic at 0.60x the fp32 latency while int8 is slower, so each configuration requires validation on the target runtime.

## Metadata
- **Published**: 2026-09-24T03:41:28Z
- **Authors**: Se Un Park, Yutae Kim, Junyoung Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28974v1)