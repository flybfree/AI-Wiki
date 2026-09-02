---
title: CaRL-EM: Cost-Aware Reinforcement Learning for Entity Matching with LLMs
published: 2026-09-01T13:05:47Z
authors: Chaohui Guo, Michel Klein, Zhisheng Huang
url: http://arxiv.org/abs/2609.01195v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CaRL-EM: Cost-Aware Reinforcement Learning for Entity Matching with LLMs

## Abstract
Entity matching (EM) requires fine-grained contextual understanding and domain knowledge. Recent work shows that large language models (LLMs) can serve as strong matchers across domains, but most methods either make independent pairwise decisions or rely on manually designed composite pipelines, thus lacking flexibility in realistic multi-candidate settings. At the same time, they typically ignore inference cost at scale. We formulate LLM-based EM with candidates as a cost-aware sequential decision problem and propose CaRL-EM, a reinforcement learning controller that manages LLM operations. Given the state of an anchor record, its candidate set, and the cost, CaRL-EM adaptively chooses among different operators (Match/Compare/Select/Decide) and model capacities to maximize a quality-cost objective. The policy interacts with abstract operators, allowing the same controller to be reused with different underlying LLM backends at inference time without retraining. Experiments on 7 benchmarks show that CaRL-EM (i) learns to dynamically plan the usage of inexpensive and expensive operators based on task complexity, (ii) achieves robust zero-shot transfer across diverse datasets and domains, and (iii) consistently achieves a better quality-cost trade-off than strong LLM-based baselines and manually designed pipelines, yielding a lower inference cost at comparable or higher quality.

## Metadata
- **Published**: 2026-09-01T13:05:47Z
- **Authors**: Chaohui Guo, Michel Klein, Zhisheng Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01195v1)