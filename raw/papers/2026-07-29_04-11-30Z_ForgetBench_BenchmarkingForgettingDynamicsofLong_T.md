---
title: ForgetBench: Benchmarking Forgetting Dynamics of Long-Term Parametric Memory in Language Models
published: 2026-07-29T04:11:30Z
authors: Ruxi Gu, Zhenliang Zhang, Wei Wang
url: http://arxiv.org/abs/2607.26455v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ForgetBench: Benchmarking Forgetting Dynamics of Long-Term Parametric Memory in Language Models

## Abstract
Large language models (LLMs) have demonstrated strong capabilities in knowledge acquisition and reasoning, yet their ability to retain previously acquired knowledge under repeated updates remains insufficiently understood. Existing evaluation paradigms primarily focus on single-step reasoning or static knowledge editing, which fail to capture the temporal dynamics of knowledge retention and degradation during continual model modification. In this work, we propose ForgetBench, a benchmark designed to systematically characterize forgetting behavior in LLMs under continual knowledge editing. ForgetBench introduces two complementary evaluation paradigms, namely concept-based QA and scenario-based QA, to disentangle isolated factual retention from structured relational knowledge preservation. Building upon a sequential editing framework, we construct temporally ordered knowledge streams and evaluate model behavior across multiple editing stages. To quantitatively analyze long-term retention dynamics, we further introduce a unified evaluation framework that models knowledge evolution over time, enabling the measurement of temporal decay, retention strength, and cross-instance stability. Extensive experiments across diverse models and editing methods demonstrate that existing approaches fail to strike a balance between long-term retention and generalization quality. Our findings highlight the need for more robust memory mechanisms that can effectively acquire, update, and preserve knowledge over time in future LLMs. Code will be released upon acceptance.

## Metadata
- **Published**: 2026-07-29T04:11:30Z
- **Authors**: Ruxi Gu, Zhenliang Zhang, Wei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26455v1)