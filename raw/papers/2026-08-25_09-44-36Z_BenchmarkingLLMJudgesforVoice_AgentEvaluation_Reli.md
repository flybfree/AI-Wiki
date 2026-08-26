---
title: Benchmarking LLM Judges for Voice-Agent Evaluation: Reliability, Calibration, and Human Oversight
published: 2026-08-25T09:44:36Z
authors: Anupam Purwar, Shashank Singh, Kritika Srivastava
url: http://arxiv.org/abs/2608.24314v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking LLM Judges for Voice-Agent Evaluation: Reliability, Calibration, and Human Oversight

## Abstract
Evaluating conversational voice agents at scale re- quires reliable assessment methods that capture both observ- able interaction quality and the contextual judgment typically provided by human evaluators. We investigate LLM-as-a-Judge evaluation by comparing human judgments with GPT-4.1 and GPT-5 on telecom and retail voice-agent conversations, across conversational quality and safety dimensions. The same interac- tions are scored under three evaluation configurations, p0, p1, and p2, to test whether automated judgments are sensitive to the evaluation setup and whether observed patterns generalize across configurations and judge models. Beyond aggregate agreement, we examine metric-level correlations, evaluator consistency, and systematic human-LLM disagreement to identify which conver- sational attributes can be judged reliably by automation and which remain sensitive to interpretation and context. Effective voice-agent evaluation is also shaped by pipeline-level factors such as speech generation, streaming, and error propagation across ASR, reasoning, and tool-calling stages, motivating our focus on comparing how human and LLM judges score the same interactions end to end. Our results show that LLM- based evaluation can serve as an effective component of large- scale voice-agent assessment, but that its reliability is metric- and configuration-dependent rather than uniform. This pro- vides an empirical framework for identifying which metrics suit automated evaluation and supports hybrid pipelines in which LLM judges handle scalable assessment while human evaluators remain engaged for metrics that demand contextual interpretation and higher-confidence judgment.

## Metadata
- **Published**: 2026-08-25T09:44:36Z
- **Authors**: Anupam Purwar, Shashank Singh, Kritika Srivastava
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24314v1)