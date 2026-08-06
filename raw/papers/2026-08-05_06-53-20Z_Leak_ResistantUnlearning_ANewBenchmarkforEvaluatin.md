---
title: Leak-Resistant Unlearning: A New Benchmark for Evaluating Multi-Hop Reasoning Consistency and Recovery Robustness
published: 2026-08-05T06:53:20Z
authors: Haoting Qian, Qingjie Zhang, Zhicong Huang, Cheng Hong, Han Qiu
url: http://arxiv.org/abs/2608.04519v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Leak-Resistant Unlearning: A New Benchmark for Evaluating Multi-Hop Reasoning Consistency and Recovery Robustness

## Abstract
Benchmarking machine unlearning methods is critical to understand whether sensitive knowledge is removed from large language models (LLMs) or not. Current unlearning benchmarks include mainly single-hop questions and a narrow set of multi-hop questions. Although effective, they still face two challenges. (1) Knowledge is not isolated, whereby diverse multi-hop reasoning paths can potentially induce knowledge leakage than normal queries. (2) Unlearning may be fragile: unlearned knowledge can be partially recovered through recovery attacks such as lightweight post-unlearning adaptation, making static evaluation insufficient. Therefore, in this paper, we introduce \unlearning as a novel benchmark to understand robust LLM knowledge removal across diverse reasoning paths and recovery attacks. We experiment with this benchmark on 3 models, 6 unlearning methods, and 2 carefully curated datasets. Results show that existing methods are vulnerable to multi-hop reasoning paths and recovery attacks. We further explore the trade-off among forget quality, robustness, and model utility for LLM unlearning.

## Metadata
- **Published**: 2026-08-05T06:53:20Z
- **Authors**: Haoting Qian, Qingjie Zhang, Zhicong Huang, Cheng Hong, Han Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04519v1)