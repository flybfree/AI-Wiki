---
title: Don't Repeat Yourself: Stopping Verbatim Loops at Sampling Time
published: 2026-08-24T03:33:39Z
authors: Philipp Emanuel Weidmann, Allen Roush, Judah Goldfeder, Sanjay Basu, Ravid Shwartz-Ziv
url: http://arxiv.org/abs/2608.22761v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Don't Repeat Yourself: Stopping Verbatim Loops at Sampling Time

## Abstract
Large Language Models generate text autoregressively, but open-ended generation is prone to verbatim looping, in which models repeat spans already present in context. Standard defenses such as repetition, presence, and frequency penalties and n-gram blocking act on token recurrence rather than the sequential structure of a loop, and often suppress looping only at strengths that also degrade formatting or fluency. We propose Don't Repeat Yourself (DRY), a sampling-time logit adjustment that penalizes a candidate token only when generating it would extend the current suffix into an exact continuation of a span seen earlier in the context. Sequence breakers protect chat templates and formatting tokens. Across models from 1.5B to 120B parameters, nine prompt families, and a 600-pair human study, DRY reduces suffix-extension rate by 47% while improving lexical diversity. An intervention-matched placebo produces no comparable reduction, identifying suffix matching as the operative mechanism. On AWQ-quantized 70B and 120B models, DRY reduces loop rate by roughly half while preserving MT-Bench, MMLU, and GSM8K performance, whereas standard alternatives lose measurable ground. DRY has been adopted by popular open-source LLM inference frameworks including llama.cpp, ExLlamaV2, and text-generation-webui, highlighting its practical impact on text generation.

## Metadata
- **Published**: 2026-08-24T03:33:39Z
- **Authors**: Philipp Emanuel Weidmann, Allen Roush, Judah Goldfeder, Sanjay Basu, Ravid Shwartz-Ziv
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22761v1)