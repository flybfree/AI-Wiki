---
title: LongGuard: Mechanistic Analysis and Training-Free Mitigation of Long-Context Failure in Safety Guardrails
published: 2026-08-27T18:07:25Z
authors: Ziyang Chen, Xing Wu, Songlin Hu
url: http://arxiv.org/abs/2608.27580v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LongGuard: Mechanistic Analysis and Training-Free Mitigation of Long-Context Failure in Safety Guardrails

## Abstract
Safety guardrails serve as the last line of defense against harmful inputs and outputs of large language models (LLMs), yet they are trained and evaluated almost exclusively on short text. We present LongGuard, a framework that evaluates, mechanistically analyzes, and mitigates long-context guardrail failure. We formulate the task as Safety Needle-in-a-Haystack (SafetyNIAH) over a 0.25k-32k length grid; across 15 mainstream guardrails, unsafe recall drops monotonically by more than 50% on average, and a paired Benign-Fill vs. Needle-Repeat design attributes the failure to proportional dilution of the unsafe needle rather than to absolute length. A three-layer attention-logit-behavior analysis on six guardrails locates the mechanism: attention mass on the unsafe needle is diluted, the unsafe-over-safe logit margin is compressed in lockstep, and the detection decision collapses accordingly, with this attention->logit->behavior chain remaining consistent after partialling out length. We further isolate a sparse set of guard-specialized retrieval heads that exhibit partial specificity relative to their base models. Building on the analysis, we propose two training-free mitigations - Chunked Detection (CD) and Attention-Head Sharpening (AHS) - and a deployment protocol, Context-Aware Hyperparameter Routing (CAHR), that selects configurations by context length and audit side. Across five benchmarks spanning synthetic data, long-context attacks, and reasoning-model outputs, CAHR-CD and CAHR-AHS improve the six-guardrail average by 22% and 13%, respectively. Code and data are available online.

## Metadata
- **Published**: 2026-08-27T18:07:25Z
- **Authors**: Ziyang Chen, Xing Wu, Songlin Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27580v1)