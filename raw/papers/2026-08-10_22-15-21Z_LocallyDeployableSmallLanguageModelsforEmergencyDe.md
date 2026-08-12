---
title: Locally Deployable Small Language Models for Emergency Department Decision Support: A Systematic Benchmark of Fine-Tuning Strategies
published: 2026-08-10T22:15:21Z
authors: Qingfeng Zhang, Yuanxiong Guo, Yanmin Gong
url: http://arxiv.org/abs/2608.10273v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Locally Deployable Small Language Models for Emergency Department Decision Support: A Systematic Benchmark of Fine-Tuning Strategies

## Abstract
Deploying large language models (LLMs) for decision support in emergency departments (EDs) faces two major challenges: privacy risks of transmitting patient data to closed-source commercial LLMs and the lack of systematic evaluation of fine-tuning strategies for locally deployable open-source small language models (SLMs). We benchmarked eight open-source SLMs using zero-shot prompting, prefix tuning, Low-Rank Adaptation (LoRA), and full fine-tuning on three ED tasks: triage level prediction, specialist referral recommendation, and diagnosis prediction. Using 2,083 MIMIC-IV-ED cases and Claude Haiku 4.5 and Claude Sonnet 4.5 as baselines, we found that LoRA fine-tuned open-source SLMs outperform commercial baselines on triage level prediction and specialist referral recommendation, while diagnosis prediction remains challenging for open-source SLMs. Confusion matrix analysis further shows that fine-tuned open-source SLMs can detect highest-severity patients missed by the commercial baselines. These results demonstrate that locally deployable SLMs can achieve clinically competitive performance for ED decision support.

## Metadata
- **Published**: 2026-08-10T22:15:21Z
- **Authors**: Qingfeng Zhang, Yuanxiong Guo, Yanmin Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10273v1)