---
title: JOR-Bench: Japanese Operations Research Benchmarks for Large Language Models
published: 2026-07-18T11:24:10Z
authors: Yuu Jinnai
url: http://arxiv.org/abs/2607.16777v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JOR-Bench: Japanese Operations Research Benchmarks for Large Language Models

## Abstract
We present JOR-Bench, a collection of five Japanese-language benchmarks for evaluating the ability of large language models (LLMs) to formulate and solve operations research (OR) problems. Each benchmark is a Japanese translation of an existing English benchmark: IndustryOR, MAMO Complex LP, NL4OPT, OptiBench, and OptMATH, covering 1,319 problems spanning linear programming, mixed-integer programming, non-linear programming, and combinatorial optimization. JOR-Bench is a solver-independent benchmark that can be used with any solver or programming language, and consists of pairs of Japanese problem statements and expected numerical answers. We evaluate seven LLMs, including multilingual general-purpose models and Japanese-specialized models, on both the original English and the new Japanese versions, and compare performance across languages. For the main evaluation, we standardize execution with the Python interface to OR-Tools to make model outputs comparable and reproducible with open-source software. Our results show that OR formulation ability is largely language-neutral for strong multilingual models; the overall average accuracy difference between English and Japanese is only $-0.3$ pp. Yet error analysis reveals subtle cross-lingual differences, including a pragmatic disambiguation failure in some domains that causes models to output decision-variable values instead of the objective value when the prompt is in Japanese.

## Metadata
- **Published**: 2026-07-18T11:24:10Z
- **Authors**: Yuu Jinnai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16777v1)