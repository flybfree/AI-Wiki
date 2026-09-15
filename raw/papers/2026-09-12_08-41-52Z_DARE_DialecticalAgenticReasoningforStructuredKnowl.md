---
title: DARE: Dialectical Agentic Reasoning for Structured Knowledge Fact Checking
published: 2026-09-12T08:41:52Z
authors: Yifei Li, Xiaohan Zheng, Wentao Qian, Liansheng Zhuang
url: http://arxiv.org/abs/2609.13808v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DARE: Dialectical Agentic Reasoning for Structured Knowledge Fact Checking

## Abstract
Structured knowledge fact checking aims to determine the truthfulness of natural language claims by reasoning over structured evidence. Recent program-generation approaches leverage large language models (LLMs) to generate executable graph reasoning programs, achieving strong performance on structured knowledge fact checking benchmarks. However, these methods remain limited by invalid relation generation, single-path reasoning that lacks self-correction, and biased evidence assessment that tends to overestimate supporting signals. We propose Dialectical Agentic Reasoning (DARE), a multi-agent framework that formulates structured knowledge fact checking as an iterative retrieve-reason-reflect process. DARE integrates relation-grounded evidence retrieval to constrain reasoning to valid structures, dialectical bidirectional verification to evaluate evidence from both supporting and refuting perspectives, and confidence-driven meta-reflection to dynamically determine whether additional evidence exploration is necessary. Extensive experiments demonstrate the effectiveness of DARE in structured knowledge fact checking, with an 8B backbone achieving 88.12% accuracy and matching or surpassing GPT-4o-based program-generation baselines, which attests to the efficacy of dialectical agentic reasoning in eliciting the latent reasoning capabilities of LLMs.

## Metadata
- **Published**: 2026-09-12T08:41:52Z
- **Authors**: Yifei Li, Xiaohan Zheng, Wentao Qian, Liansheng Zhuang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13808v1)