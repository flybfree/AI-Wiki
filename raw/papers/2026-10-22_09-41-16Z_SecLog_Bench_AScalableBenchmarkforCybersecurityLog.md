---
title: SecLog-Bench: A Scalable Benchmark for Cybersecurity Log Reasoning with Scaffolded Evidence
published: 2026-10-22T09:41:16Z
authors: Yifan Wang, Dongliang Xu, Xiaoyong Li, Jing Li, Peter S. Pan, Yue Yao
url: http://arxiv.org/abs/2610.31000v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SecLog-Bench: A Scalable Benchmark for Cybersecurity Log Reasoning with Scaffolded Evidence

## Abstract
Large language models (LLMs) have shown strong potential for cybersecurity, leading to growing interest in LLM-based automated cybersecurity log analysis. However, current datasets (1) are limited in scale; (2) rely mainly on single-source evidence; and (3) have only binary or multi-class attack labels, without dense annotations of the reasoning process. To address these limitations, SecLog-Bench has three key features. First, we build an extensible simulation platform that covers 29 attack scenarios, supports repeated execution and the integration of new scenarios, and enables scalable generation of cybersecurity logs with attack-stage labels. Second, we use multi-source logs, including audit logs, application logs, and network traffic, to jointly analyze cyber attacks. Third, we annotate each sample with the essential context for cybersecurity log reasoning and a structured step-by-step evidence chain. We evaluate eight mainstream LLMs on this benchmark for post-detection attack-progress reasoning. Results show that, when provided with scaffolded evidence, current LLMs exhibit modest capability in attack-progress reasoning, with the best model achieving only 44.44% accuracy and 45.07% Macro-F1. Their reasoning remains unreliable; i.e., the highest Stage Reasoning F1 (SRF1) score is only 54.87%. Moreover, even correct predictions may be accompanied by flawed reasoning, and reasoning quality is often misaligned with prediction accuracy.

## Metadata
- **Published**: 2026-10-22T09:41:16Z
- **Authors**: Yifan Wang, Dongliang Xu, Xiaoyong Li, Jing Li, Peter S. Pan, Yue Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31000v1)