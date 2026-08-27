---
title: From Passive Response to Proactive Correction: Enhancing LLM Robustness Against Input Fact Perturbations
published: 2026-08-26T15:13:50Z
authors: Ping Wang, Xiangguo Sun, Bingbing Xu, Guocong Li, Xiaofeng Meng
url: http://arxiv.org/abs/2608.25894v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Passive Response to Proactive Correction: Enhancing LLM Robustness Against Input Fact Perturbations

## Abstract
Large language models (LLMs) frequently produce confident yet factually incorrect responses when user inputs contain misleading premises, a phenomenon we attribute to fact perturbations in the input. Existing approaches to hallucination mitigation typically assume reliable user inputs, overlooking how such factual errors can actively mislead model reasoning. To address this vulnerability, we propose DEDUCE, a three-stage framework that transforms LLMs from passive responders into proactive error correctors. DEDUCE operates in three stages: (1) detect errors through fine-grained fact extraction and verification; (2) devise correction strategies via multi perspective deliberation; and (3) correct misconceptions while delivering reliable answers. We also present MisFactQA, a dataset containing factual errors of varying degrees, and propose new metrics for evaluating model robustness. Experiments on TruthfulQA, FalseQA, and our MisFactQA benchmark demonstrate that DEDUCE significantly improves both accuracy and error correction capability. Consistent gains across Qwen, LLaMA, and Gemma families confirm its effectiveness and scalability.

## Metadata
- **Published**: 2026-08-26T15:13:50Z
- **Authors**: Ping Wang, Xiangguo Sun, Bingbing Xu, Guocong Li, Xiaofeng Meng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25894v1)