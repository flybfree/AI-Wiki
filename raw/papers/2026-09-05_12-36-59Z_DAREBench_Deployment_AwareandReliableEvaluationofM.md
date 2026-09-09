---
title: DAREBench: Deployment-Aware and Reliable Evaluation of Models as Agents
published: 2026-09-05T12:36:59Z
authors: Yu Liu, Zhilin Liu, Zhiwei Yang, Shaojie Zhang, Zheyuan Deng, Tingwei Huang, Zhenbo Luo, Lei Jiang, Yanbing Liu, Pei Fu
url: http://arxiv.org/abs/2609.06059v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DAREBench: Deployment-Aware and Reliable Evaluation of Models as Agents

## Abstract
As large language models evolve from question-answering systems into general-purpose agents, evaluation must move beyond static answer correctness to assess multimodal perception, multi-step execution, tool use, and artifact delivery. However, existing benchmarks are often tied to specific task types, execution environments, or scoring protocols, limiting their comparability, interpretability, and reliability for deployment decisions. We introduce DAREBench (Deployment-Aware and Reliable Evaluation of Models as Agents), a benchmark designed to capture workload variation and support reliable agent evaluation. Built on a shared OpenClaw execution environment, DAREBench organizes 233 tasks selected and adapted from 22 source benchmarks into a $2\times3$ workload matrix defined by input modality and execution form, and evaluates them under a unified contract-based protocol with evidence-based score auditing. We evaluate 23 commercial API models and 12 locally deployed open-weight models over 7,587 model--task runs, reporting accuracy and token consumption alongside reference costs for API models. Results show that no single model dominates all workload groups, text and multimodal tasks exhibit distinct accuracy--cost trade-offs, and local open-weight models are competitive in several groups but still trail frontier commercial models overall. These findings suggest that agent deployment and model selection should consider workload profiles, deployment mode, and accuracy--cost trade-offs rather than rely on a single aggregate score.

## Metadata
- **Published**: 2026-09-05T12:36:59Z
- **Authors**: Yu Liu, Zhilin Liu, Zhiwei Yang, Shaojie Zhang, Zheyuan Deng, Tingwei Huang, Zhenbo Luo, Lei Jiang, Yanbing Liu, Pei Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06059v1)