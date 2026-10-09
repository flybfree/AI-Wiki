---
title: How Narrative Wrapping Affects LLM Refusal: A Cross-Language Benchmark and Defense
published: 2026-10-07T23:40:25Z
authors: Zhankai Ye, Yanning Wang, Yukai Jin, Bo Mei, Fangyi Li, Wei Wang, Shangqian Gao, Xin Liu
url: http://arxiv.org/abs/2610.11005v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Narrative Wrapping Affects LLM Refusal: A Cross-Language Benchmark and Defense

## Abstract
Safety-aligned language models often refuse a harmful request stated directly but answer the same request inside a role-play or narrative wrapper. We measure this vulnerability across languages and registers: attack success on Qwen3-1.7B is already 89.4% in English and 93.0% in modern Chinese, and reaches 95.7% in Classical Chinese. We build GUISE, a benchmark for systematically studying this vulnerability. It includes parallel requests in English, modern Chinese, and Classical Chinese, matched harmful and benign pairs, wrapper types held out for evaluation, and a stricter criterion that counts warn-then-answer responses as attack successes. Representation analysis shows that language and register move harmful-request representations only slightly away from the model's refusal direction, whereas narrative wrappers move them much farther away. We propose AXIS, which combines preference optimisation with a rotation objective that aligns harmful-request representations with the refusal direction and a commitment objective that trains the model to refuse completely rather than produce a warn-then-answer response. Across Qwen3-1.7B, Qwen3-4B and GLM-4-9B, AXIS achieves the highest combined safety and usability score among the compared methods.

## Metadata
- **Published**: 2026-10-07T23:40:25Z
- **Authors**: Zhankai Ye, Yanning Wang, Yukai Jin, Bo Mei, Fangyi Li, Wei Wang, Shangqian Gao, Xin Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11005v1)