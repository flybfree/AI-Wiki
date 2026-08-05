---
title: FLARE: Few-shot Learning-based Adaptive Reflective Engine
published: 2026-08-03T22:13:12Z
authors: Dhanasekar Sundararaman, Bharat Gandhi, Aashna Garg, Minjie Li
url: http://arxiv.org/abs/2608.02919v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FLARE: Few-shot Learning-based Adaptive Reflective Engine

## Abstract
Large language models (LLMs) are increasingly deployed in complex, compound AI systems where performance hinges on the quality of prompts. Recent state-of-the-art optimizers like GEPA (Genetic-Pareto) have argued that reflective instruction evolution can outperform traditional reinforcement learning and few-shot optimization. In this work, we challenge this shift by introducing FLARE (Few-shot Learning-based Adaptive Reflective Engine), a framework that leverages advanced reflective mechanisms and a small set of few-shot reference examples to optimize instructions. We evaluate our method across a diverse suite of benchmarks -- spanning retrieval-augmented reasoning (HotPotQA, MedQA, 2WikiMultiHopQA), tool calling, and multi-label emotion classification (GoEmotions) -- using the GPT-5 series of models. Our results demonstrate that FLARE consistently outperforms GEPA, winning on every task-model pair: it achieves gains of up to +14.2 points on HotPotQA (52.2 vs. GEPA's 42.2 with GPT-5-Chat), reaches 87.0% on tool calling (vs. 81.0% for GEPA), and lifts GoEmotions micro-F1 to 52.7% (+15.3) with GPT-5.1 on the full 5408-example test split, more than doubling GEPA's +5.7 gain. Beyond raw accuracy, FLARE is also strikingly data-efficient: on GoEmotions it reaches its peak performance using as few as 100 validation examples, while remaining markedly more stable across random seeds than GEPA. Our findings suggest that while reflective instructions are powerful, the strategic optimization of few-shot learning remains a critical frontier for maximizing the potential of next-generation LLMs.

## Metadata
- **Published**: 2026-08-03T22:13:12Z
- **Authors**: Dhanasekar Sundararaman, Bharat Gandhi, Aashna Garg, Minjie Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02919v1)