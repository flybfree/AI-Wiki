---
title: Lexical Perturbations Disrupt LLM Reasoning: An Empirical Study of Attention Diversion
published: 2026-08-22T23:51:33Z
authors: Jiaqian Zhu, Yang Zhang, Junhua Ding, Xiaowei Yu
url: http://arxiv.org/abs/2608.22140v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lexical Perturbations Disrupt LLM Reasoning: An Empirical Study of Attention Diversion

## Abstract
Large Language Models (LLMs) achieve strong reasoning performance, but their robustness to realistic lexical corruption remains poorly understood. We evaluate four open-weight instruction-tuned models and frontier models across four reasoning benchmarks under keyboard noise, character swaps, and filler insertion. Character-level perturbations substantially degrade accuracy, especially on multi-step reasoning tasks, while filler insertion has little effect. We trace this asymmetry to Attention Diversion: lexical corruption fragments subword tokenization, and the resulting fragments attract disproportionate attention mass, concentrated in middle and final transformer layers. Length-matched controls confirm that fragmentation, not prompt length, drives the loss. A factorial intervention then shows why the damage is hard to undo: fragmentation corrupts token content and attention allocation together, and the two are coupled. Restoring clean attention while the content remains corrupted is actively harmful, restoring content alone is insufficient, and only restoring both recovers a substantial share of the gap. This coupling explains why inference-time strategies, including chain-of-thought prompting, spell-checking, self-repair, and stronger repair models, fail to consistently recover performance: each addresses one channel at a time. Code and data are available at https://github.com/Jiaqian-Janelle/Attention-Diversion

## Metadata
- **Published**: 2026-08-22T23:51:33Z
- **Authors**: Jiaqian Zhu, Yang Zhang, Junhua Ding, Xiaowei Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22140v1)