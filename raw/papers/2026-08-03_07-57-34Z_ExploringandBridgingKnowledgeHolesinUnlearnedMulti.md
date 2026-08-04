---
title: Exploring and Bridging Knowledge Holes in Unlearned Multimodal Large Language Models
published: 2026-08-03T07:57:34Z
authors: Junxiang You, Junkai Chen, Yuhao He, Ruiqi Liu, Zhetao Guo, Shu Wu
url: http://arxiv.org/abs/2608.01849v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exploring and Bridging Knowledge Holes in Unlearned Multimodal Large Language Models

## Abstract
Machine unlearning offers a promising approach to remove unsafe content from Multimodal Large Language Models (MLLMs), yet ensuring the precision of unlearning remains a persistent challenge. One reason is that current MLLM unlearning evaluation paradigms suffer from a critical blind spot: they assess model utility through benchmarks whose representations are distant from the forget set, failing to capture knowledge holes---severe degradation on benign adjacent inputs. To probe knowledge holes in unlearned MLLMs, we construct a benchmark that captures unintended degradation on benign inputs sharing generic patterns with the forget set, and confirm through controlled experiments that they are a systematic consequence of commonly used approaches. Furthermore, to bridge this gap, we propose Selective Protection with Anchored Regularization, which protects generic patterns via anchored activation filtering while reinforcing them through entity-abstracted enhancement. Our experiments on SafeEraser demonstrate that SPAR recovers over 98% of vanilla response quality compared to below 50% for standard baselines---while achieving 0.00% attack success rate and competitive model utility. These results underscore the necessity of more fine-grained evaluation for trustworthy MLLM unlearning.

## Metadata
- **Published**: 2026-08-03T07:57:34Z
- **Authors**: Junxiang You, Junkai Chen, Yuhao He, Ruiqi Liu, Zhetao Guo, Shu Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01849v1)