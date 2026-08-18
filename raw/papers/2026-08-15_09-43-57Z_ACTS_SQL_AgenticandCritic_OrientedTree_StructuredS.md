---
title: ACTS-SQL: Agentic and Critic-Oriented Tree-Structured SQL Correctness with Large Language Models
published: 2026-08-15T09:43:57Z
authors: Xinmei Huang, Jie Song, Peng Li, Fuxin Jiang, Jing Zhang, Tieying Zhang, Jianjun Chen, Chenming Liu, Tao Yang, Maoyin Liu, Wenda Li, Hong Chen, Cuiping Li
url: http://arxiv.org/abs/2608.15145v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ACTS-SQL: Agentic and Critic-Oriented Tree-Structured SQL Correctness with Large Language Models

## Abstract
Large Language Models (LLMs) have been increasingly adopted in Text-to-SQL systems, yet SQL errors remain a major obstacle in real-world Text-to-SQL inference pipelines. Existing SQL correction approaches either rely on large-scale, high-quality training data with substantial overhead, or adopt single-path agentic workflows that are brittle to early mistakes and prone to error propagation.   To develop a practical SQL correctness system for industrial scenarios, we present a training-free framework that formulates SQL correction as a plan-guided, tree-structured debugging process. By maintaining multiple correction strategies and enabling backtracking, the framework mitigates error accumulation during iterative refinement. We further integrate execution-based verification and clause-level diagnostic tools to support strategy pruning and precise error localization.   We evaluate the system on the BIRD-Critic benchmark and observe consistent accuracy gains over strong LLM backbones and representative agent-based baselines, achieving a 9.42% improvement over the previous state-of-the-art method. The framework is also deployed in the Torch Log Service (TLS) of Volcano Engine to support an online Text-to-TLS API. In production, it improves execution accuracy from 36.77% to 53.61% on real user queries with a representative strong LLM backbone (GPT-5). These results demonstrate the effectiveness and stability of our approach in real-world deployments.

## Metadata
- **Published**: 2026-08-15T09:43:57Z
- **Authors**: Xinmei Huang, Jie Song, Peng Li, Fuxin Jiang, Jing Zhang, Tieying Zhang, Jianjun Chen, Chenming Liu, Tao Yang, Maoyin Liu, Wenda Li, Hong Chen, Cuiping Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15145v1)