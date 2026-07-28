---
title: Traceable LLM Reasoning for Fake-Order Fraud Detection
published: 2026-07-25T06:51:02Z
authors: Siqi You, Bingsong Xu, Zhixian Zheng, Xinjian Peng, Yang Xie, Ying Wang, Jiarong Xu
url: http://arxiv.org/abs/2607.23075v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Traceable LLM Reasoning for Fake-Order Fraud Detection

## Abstract
Detecting fake-order fraud at scale remains a critical challenge for large online-to-offline (O2O) service platforms, as existing approaches often rely on expert-designed features, produce black-box decisions, and provide limited interpretability. To address these limitations, we propose DeepScrub, a reinforcement learning framework built upon large language models (LLMs) for fake-order fraud detection with traceable reasoning. DeepScrub introduces three innovations. First, a semantic unification module converts heterogeneous risk signals into textual descriptions that LLMs can understand. Second, continued pre-training on risk-control corpora injects domain knowledge, and task rewards jointly evaluate prediction correctness and reasoning quality. Third, the SUggest-REflect (SURE) mechanism incorporates expert feedback and model self-checking to iteratively refine reasoning paths. On a real-world fake-order fraud detection dataset, DeepScrub achieves a macro-F1 score of 85.3%, outperforming the best baseline by 2.7 percentage points. Our task-optimized 8B model further surpasses a 32B model, showing that domain adaptation can matter more than model scale in this setting. In a four-week live pilot, DeepScrub achieved 91.8% precision and 88.5% recall, improving over first-stage human reviewers by 16.6 and 38.8 percentage points. It reduced first-stage manual review workload by 94% and saved nearly one million RMB annually. These results show that DeepScrub improves fraud review accuracy, reduces first-stage review workload, and provides traceable evidence for production risk-review workflows.

## Metadata
- **Published**: 2026-07-25T06:51:02Z
- **Authors**: Siqi You, Bingsong Xu, Zhixian Zheng, Xinjian Peng, Yang Xie, Ying Wang, Jiarong Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23075v1)