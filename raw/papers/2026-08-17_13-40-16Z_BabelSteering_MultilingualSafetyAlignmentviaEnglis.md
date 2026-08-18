---
title: BabelSteering: Multilingual Safety Alignment via English Steering Vectors
published: 2026-08-17T13:40:16Z
authors: Emma V. Stein, Dominik Meier, Terry Ruas, Jan Philip Wahle, Bela Gipp
url: http://arxiv.org/abs/2608.16577v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BabelSteering: Multilingual Safety Alignment via English Steering Vectors

## Abstract
Large language models (LLMs) are deployed globally in high-stakes settings, yet most safety research and alignment efforts remain concentrated on English. Thus, users interacting with LLMs in other languages may encounter weaker safeguards despite relying on the same systems for similarly sensitive tasks. In this work, we investigate whether safety signals learned from a high-resource language, like English, can improve multilingual safety. We propose BabelSteering, an activation steering method that acts as a lightweight inference- time intervention, using refusal directions derived from English safety supervision to generalize across languages. Our evaluation includes eight languages and jointly measures refusal of harmful requests, over-refusal, and general task utility. The results show that BabelSteering increases the refusal of harmful requests across languages, with only a marginal to no reduction in task utility but with some increase in refusal of pseudo-harmful prompts. For example, for Gemma 7B, we see an average increase in the refusal of harmful prompts across languages of 11 percentage points (pp), with individual languages like Bengali seeing an increase of 17 pp, with no loss of utility on Global MMLU, while pseudo-harmful refusals increase by 13 pp on average. We also introduce a multilingual translation-and-evaluation pipeline to facilitate future work on cross-lingual safety interventions. Overall, our findings suggest that activation steering may provide a practical, low- cost mechanism for extending English-derived safety signals to other languages. Warning: this paper contains examples with unsafe content

## Metadata
- **Published**: 2026-08-17T13:40:16Z
- **Authors**: Emma V. Stein, Dominik Meier, Terry Ruas, Jan Philip Wahle, Bela Gipp
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16577v1)