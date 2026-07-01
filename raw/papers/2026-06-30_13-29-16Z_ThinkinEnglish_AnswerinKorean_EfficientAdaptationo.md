---
title: Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents
published: 2026-06-30T13:29:16Z
authors: Utsav Garg, Sungjin Hong, Jason Jung, Justin Lee, Shaan Desai, Joon Hee Kim, Anirudh Shrinivason, Edmond Wen, Susie Park
url: http://arxiv.org/abs/2606.31648v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents

## Abstract
We present LuckyStar 111B, a 111B-parameter hybrid reasoning model developed through a collaboration between Cohere and LG CNS for Korean-English enterprise agents under practical memory and serving constraints. The model trains from Cohere's fully post-trained Command A model rather than a new pretraining run, and uses preamble conditioning to switch between concise non-reasoning behavior and longer tool-oriented reasoning. We study four choices for scaling tool-using agents efficiently: multilingual supervised fine-tuning, reinforcement learning with verifiable rewards for multi-step tool-use tasks, language-consistency rewards for Korean user-facing responses, and 4-bit quantization for single-GPU serving. The adapted model improves mathematical reasoning, function calling, and agentic natural-language-to-SQL (NL2SQL) performance while preserving general Korean and English instruction-following quality. These results provide a practical recipe and failure-mode analysis for adapting post-trained multilingual models to verifiable agentic workflows under memory-constrained deployment.

## Metadata
- **Published**: 2026-06-30T13:29:16Z
- **Authors**: Utsav Garg, Sungjin Hong, Jason Jung, Justin Lee, Shaan Desai, Joon Hee Kim, Anirudh Shrinivason, Edmond Wen, Susie Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.31648v1)