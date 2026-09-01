---
title: EmoLASP: Emotion Recognition with Language Models and Answer Set Programming
published: 2026-08-29T04:02:32Z
authors: Thao Le, Michael Thielscher
url: http://arxiv.org/abs/2608.29035v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EmoLASP: Emotion Recognition with Language Models and Answer Set Programming

## Abstract
Emotion recognition in conversations is increasingly tackled with language models, but these models can be unstable and expensive to fine-tune or to prompt with long dialogue histories. We propose EmoLASP, a framework that combines a language model with declarative reasoning via Answer Set Programming (ASP) to predict VAD scores (Valence-Arousal-Dominance) in conversations. Experiments on a widely used benchmark dataset (IEMOCAP) across six open-source LLMs (3B-120B) and two PLMs (BERT, RoBERTa) show that EmoLASP improves prediction performance compared to using the language model alone, even when the LLMs/PLMs are given no dialogue history in their prompts or input vectors. The gains are largest for prompt-only LLMs, which EmoLASP uses without any fine-tuning. However, for fine-tuned PLMs, the reasoner adds little once dialogue history is available. EmoLASP's LLM pipeline demonstrates the potential advantages of using a reasoning approach to ensure emotion prediction consistency and to reduce both the cost of fine-tuning and the cost of prompting with long dialogue histories.

## Metadata
- **Published**: 2026-08-29T04:02:32Z
- **Authors**: Thao Le, Michael Thielscher
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29035v1)