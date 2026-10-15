---
title: A Graph-Based Analysis of Comparability, Scale, and Attribution in Private Transformer Inference
published: 2026-10-14T05:30:25Z
authors: Souvik Das, Ariful Azad, Nitesh Saxena
url: http://arxiv.org/abs/2610.19607v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Graph-Based Analysis of Comparability, Scale, and Attribution in Private Transformer Inference

## Abstract
Rising privacy concerns around large language models have accelerated research in private Transformer inference (PTI). Synthesizing the empirical claims in this line of research, however, is hindered by multi-dimensional cryptographic progress and inconsistent evaluation contracts. In this work, we systematize the field by constructing an empirical graph of 62 PTI systems, mapping system attributes to node features and evaluation compatibility to edges. A three-tiered analysis of this graph illuminates the state of private inference. Node-level attribution shows that cryptographic progress drives performance gains across most systems, yet always co-occurs with other factors (model fidelity, hardware, cost accounting). Edge-level auditing shows that only 1 of 1891 candidate system pairs is directly comparable under shared assumptions. Finally, graph-level analysis shows that the scaling frontier of private inference has plateaued at 13B parameters and projects the cost of deploying current PTI techniques on production-scale Transformers. Overall, this graph-based framework equips the community to evaluate PTI claims transparently and channel technical speedups into deployment-scale private inference.

## Metadata
- **Published**: 2026-10-14T05:30:25Z
- **Authors**: Souvik Das, Ariful Azad, Nitesh Saxena
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19607v1)