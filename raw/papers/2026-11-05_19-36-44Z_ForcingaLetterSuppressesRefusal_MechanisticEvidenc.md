---
title: Forcing a Letter Suppresses Refusal: Mechanistic Evidence from WMDP
published: 2026-11-05T19:36:44Z
authors: Stepan Epifantsev, Anna Antipova, Oleg Chernikov, Leon Strelkov, Alexey Dontsov
url: http://arxiv.org/abs/2611.08639v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Forcing a Letter Suppresses Refusal: Mechanistic Evidence from WMDP

## Abstract
Safety benchmarks for large language models (LLMs) commonly use multiple-choice question (MCQ) format. However, prior studies documented that MCQ format reduces refusal rates, which may significantly affect the safety behavior of the model. We provide a first mechanistic explanation of this effect on the Weapons of Mass Destruction Proxy (WMDP) dataset across two models - Llama-3.1-8B and Qwen3-8B. First, we use the tuned lens technique to show that when processing MCQ the model commits to an answer-letter token very quickly, which is in contrast to the gradual refusal build-up in open-ended formats. Additionally, we observe that activations on the MCQ format lie roughly 3x further from the refusal direction, compared with their open-ended counterparts. Moreover, ablating the attention heads that carry the MCQ format answer increases the refusal, which is a direct evidence that the MCQ answer-selection competes with refusal. These findings indicate that MCQ safety scores primarily measure knowledge capabilities and do not assess the safety-mechanisms.

## Metadata
- **Published**: 2026-11-05T19:36:44Z
- **Authors**: Stepan Epifantsev, Anna Antipova, Oleg Chernikov, Leon Strelkov, Alexey Dontsov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.08639v1)