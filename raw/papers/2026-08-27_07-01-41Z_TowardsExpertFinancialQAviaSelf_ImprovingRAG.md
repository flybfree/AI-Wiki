---
title: Towards Expert Financial QA via Self-Improving RAG
published: 2026-08-27T07:01:41Z
authors: Junjie Xiong, Shawheen Ghezavat, Aum Hirpara
url: http://arxiv.org/abs/2608.26706v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Expert Financial QA via Self-Improving RAG

## Abstract
Expert-level financial question answering requires both grounded verification to catch numeric hallucinations and audit trails for regulatory compliance, attributes that standard single-pass RAG systems lack. We take a step toward this goal with Self-Improving RAG, a framework that decomposes document QA into three specialized agents (Retrieval, Reasoning, and Judge) coordinated by an orchestrator with feedback-driven self-correction. When the Judge Agent scores an answer below a dynamic threshold, the system triggers retry with escalated strategies: broader retrieval, more careful prompting, and relaxed acceptance criteria. We evaluate on FinanceBench (SEC filing QA), where Self-Improving RAG achieves 86% oracle-guided accuracy (measuring agreement with gold answers) with a 36.4% Lazarus Rate, recovering nearly 4 in 10 initially incorrect answers through targeted retry. A key finding is that a fixed retrieval pipeline with judge-driven retry achieves strong results without dynamic routing, providing full interpretability. Every decision is logged with confidence scores, enabling the audit trails required for regulated financial applications.

## Metadata
- **Published**: 2026-08-27T07:01:41Z
- **Authors**: Junjie Xiong, Shawheen Ghezavat, Aum Hirpara
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26706v1)