---
title: Reasoning Error from Known Fact: Step-Level Self-Consistency Group Relative Policy Optimization for LLM
published: 2026-07-21T09:56:58Z
authors: Xiaomeng Hu, Jiaqi Hu, Hao Chen, Qi Zhang, Zhanming Shen, Wentao Ye, Junbo Zhao
url: http://arxiv.org/abs/2607.18915v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reasoning Error from Known Fact: Step-Level Self-Consistency Group Relative Policy Optimization for LLM

## Abstract
With the rapid advancement of large language models (LLMs), modern systems not only possess strong foundational capabilities and extensive knowledge, but can also solve complex problems via long, multi-step reasoning. However, as reasoning traces become longer, LLMs may produce a substantial amount of hallucinated content during the reasoning process, which is often difficult to detect. In this work, we conduct a fine-grained analysis of hallucinations arising in LLM reasoning and find that the reasoning traces are particularly prone to Context-Sensitive Factual Hallucinations: cases where the model actually has the relevant knowledge, yet makes factual errors due to contextual interference during reasoning. To address this issue, we propose Step-level Self-Consistency Group Relative Policy Optimization (SSC-GRPO), which assigns step-level rewards to reasoning traces by computing self-consistency scores of individual steps across multiple rollouts. Compared with prior methods, SSC-GRPO achieves state-of-the-art performance on both mathematical reasoning benchmarks and hallucination leaderboards. Our results offer a new perspective for detecting and mitigating hallucinations in the reasoning process of large language models.

## Metadata
- **Published**: 2026-07-21T09:56:58Z
- **Authors**: Xiaomeng Hu, Jiaqi Hu, Hao Chen, Qi Zhang, Zhanming Shen, Wentao Ye, Junbo Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18915v1)