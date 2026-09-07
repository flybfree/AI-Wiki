---
title: ReCAST: Restoration-aware Cascaded Stage-wise Training for Obfuscated SMS Risk Classification
published: 2026-09-04T08:36:21Z
authors: Jieyun Huang, Yi Shen, Kaikai Zhao, Jiangze Yan, Wenjing Zhang, Ping Chen, Ning Wang, Zhaoxiang Liu, Kai Wang, Shiguo Lian
url: http://arxiv.org/abs/2609.04878v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReCAST: Restoration-aware Cascaded Stage-wise Training for Obfuscated SMS Risk Classification

## Abstract
Fraudulent messages sent via Short Message Service (SMS) are increasingly obfuscated to evade cost-conscious classifiers in production systems. In Chinese SMS, attackers can exploit a wide range of carefully crafted obfuscation strategies to hide risk-bearing phrases while preserving human readability, making direct classification brittle under real-world latency and throughput constraints. We propose ReCAST, a Restoration-aware Cascaded Stage-wise Training framework for robust obfuscated Chinese SMS classification. ReCAST distills a large teacher model's de-obfuscation ability into a smaller deployable student model by supervising obfuscated span detection, obfuscation type prediction, and text restoration, and then uses the restoration-aware student for downstream risk classification. Experiments on an internally constructed real-world Chinese SMS benchmark show that ReCAST substantially improves classification performance over directly trained baselines under obfuscation. The results suggest that restoration-aware distillation offers a practical path toward robust SMS risk classification with smaller deployable models under production-oriented constraints.

## Metadata
- **Published**: 2026-09-04T08:36:21Z
- **Authors**: Jieyun Huang, Yi Shen, Kaikai Zhao, Jiangze Yan, Wenjing Zhang, Ping Chen, Ning Wang, Zhaoxiang Liu, Kai Wang, Shiguo Lian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04878v1)