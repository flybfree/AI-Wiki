---
title: Interpreting and Steering for Safe and Correct Code Generation
published: 2026-08-30T20:30:14Z
authors: Hao Yan, Ziyu Yao
url: http://arxiv.org/abs/2608.30025v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Interpreting and Steering for Safe and Correct Code Generation

## Abstract
Large language models (LLMs) frequently generate source code containing vulnerabilities, yet little work studies the internal mechanisms that distinguish safe from vulnerable generation in them. In this work, we systematically perform a mechanistic interpretation of LLMs, aiming at both understanding how code safety-vs-vulnerability is represented or driven by components in an LM and turning the insights into actionable steering strategies to encourage safer code generation. To this end, we introduce CodeSec-Pairs, a dataset of 9,342 Python safe-and-vulnerable contrastive code pairs, sampled from Llama-3.1-8B-Instruct. Utilizing the dataset, we explore approaches to localize layers and attention heads that relate to code safety, and further experiment with different steering strategies for inference-time vulnerability reduction. In particular, we propose DuoSteer, a double-steering approach that simultaneously applies safety and code-correctness steering to attention heads. In experiments over five vulnerability types, DuoSteer leads to an average of -26.9% vulnerability rate reduction and +7.5% functional correctness improvement, which outperforms not only other steering variants but also prompting and supervised fine-tuning baselines. The advantage also replicates on Qwen-2.5-Coder-7B-Instruct with another 2,500 contrastive pairs sampled from that model.

## Metadata
- **Published**: 2026-08-30T20:30:14Z
- **Authors**: Hao Yan, Ziyu Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30025v1)