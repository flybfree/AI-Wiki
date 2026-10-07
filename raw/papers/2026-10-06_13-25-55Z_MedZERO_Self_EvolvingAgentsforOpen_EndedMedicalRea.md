---
title: MedZERO: Self-Evolving Agents for Open-Ended Medical Reasoning Through Controlled Knowledge Accumulation
published: 2026-10-06T13:25:55Z
authors: Xilin Dang, Weilin Ruan, Xue Yang, Jinghao Wang, Xiaowei Hu, Jinpeng Li, Pheng-Ann Heng
url: http://arxiv.org/abs/2610.08327v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MedZERO: Self-Evolving Agents for Open-Ended Medical Reasoning Through Controlled Knowledge Accumulation

## Abstract
Large language models (LLMs) have shown promise in medical question answering and clinical reasoning, yet their improvement remains constrained by static parametric knowledge and costly expert supervision. Self-evolving agents offer a promising alternative by enabling models to improve through iterative task generation and problem-solving. However, most existing self-evolving methods are designed for easily verifiable domains such as mathematics and coding, where solutions can be checked by exact answers or executable programs. Medical reasoning is fundamentally different: it is open-ended, knowledge-intensive, and often only partially verifiable. We present MedZERO, a self-evolving framework for open-ended medical reasoning. MedZERO couples an Examiner that generates frontier medical question-option pairs with a Reasoner that solves them through evidence-grounded multi-turn reasoning with external knowledge tools. To support reliable, continual improvement, MedZERO adopts controlled knowledge accumulation, which maintains temporary exploratory knowledge and curated persistent knowledge in reasoning. We evaluate MedZERO on five public medical reasoning benchmarks using 4B- and 8B-scale base models under open-ended evaluation. Across all settings, MedZERO consistently outperforms the underlying base models and prior self-evolving baselines, achieving up to 13.7 average accuracy-point gains over the next-best self-evolving baseline.

## Metadata
- **Published**: 2026-10-06T13:25:55Z
- **Authors**: Xilin Dang, Weilin Ruan, Xue Yang, Jinghao Wang, Xiaowei Hu, Jinpeng Li, Pheng-Ann Heng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08327v1)