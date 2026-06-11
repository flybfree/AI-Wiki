---
title: System Report for CCL25-Eval Task 5: New Dataset and LoRA-Fine-Tuned Qwen2.5
published: 2026-06-10T17:54:32Z
authors: Haotao Xie
url: http://arxiv.org/abs/2606.12392v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# System Report for CCL25-Eval Task 5: New Dataset and LoRA-Fine-Tuned Qwen2.5

## Abstract
Recently, large language models (LLMs) have achieved promising progress in the fields of classical Chinese translation and the generation of classical poetry. However, domain-specific research on precise translation and affective-semantic understanding of classical poetry remains limited. The main challenge is that most studies treat the poetic appreciation task as a general-domain problem, neglecting the distinctive features of poetic appreciation, while high-quality and domain-specific datasets are extremely limited. To address this limitation, we decompose the task into three subtasks: term interpretation, semantic interpretation, and emotional inference. Based on multiple open-source datasets, we perform data cleansing and alignment to construct the Classical Chinese Poetry Instruction Pair Dataset (CCPoetry-49K), which comprises 49,404 high-quality instruction-response pairs explicitly optimized for this domain. We then propose a domain-specialized LLM, called PoetryQwen, by applying Low-Rank Adaptation (LoRA) to fine-tune the Qwen2.5-14B model. Experimental results on the CCL25-Eval Task 5 benchmark demonstrate that PoetryQwen achieves a score of 0.757, representing a 9.7% improvement over the Qwen2.5-14B-Instruct baseline (0.690). These findings clearly indicate that PoetryQwen significantly enhances performance in precise translation and emotional understanding of classical poetry. We present new dataset and methodological considerations intended to support the domain-specific optimization of LLMs.

## Metadata
- **Published**: 2026-06-10T17:54:32Z
- **Authors**: Haotao Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.12392v1)