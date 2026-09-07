---
title: IPGeoAI: Transformer-Based Geolocation with LLM Semantic Fusion
published: 2026-09-03T23:29:15Z
authors: Avinash Kadimisetty, Andy Jinqing Yu, Philip Favaloro, Wenlong Liu, Xiaolu Xiong
url: http://arxiv.org/abs/2609.04559v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IPGeoAI: Transformer-Based Geolocation with LLM Semantic Fusion

## Abstract
Accurate city-level IP Geolocation is an important enabler for the modern digital ecosystem, underpinning services ranging from local content delivery and targeting to digital rights enforcement. However, traditional heuristic and database-driven methods often struggle to resolve the complex, non-linear allocation patterns of modern network infrastructures, particularly within the exploding IPv6 address space and transient mobile networks. In this paper, we introduce IPGeoAI, a novel deep learning model architecture that reframes geolocation from a static lookup problem to a sequential modeling task. Our approach utilizes the Transformer Encoder to capture hierarchical dependencies inherent in IP subnet structures. We propose a method to resolve geographic ambiguity by integrating unstructured semantic context via a Zero-Shot LLM Feature Extraction pipeline. We utilize Large Language Models to transform raw, noisy Autonomous Systems (AS) descriptions into structured, domain-specific metadata (such as 'University' vs. 'ISP' or 'Global' vs. 'Local') via an offline pre-computation process. By fusing these semantic signals into the network via a Multi-Head Cross-Attention module, we bridge the gap between numerical network topology and real-world semantic identity. Extensive offline evaluation on a proprietary dataset spanning 200,000 cities demonstrates that IPGeoAI significantly outperforms a leading external vendor in city-level granularity. By adopting a hierarchical inference strategy that refines coarse-grained country signals, our model achieves a 6% improvement in city-level accuracy while extending coverage to 100% of the traffic. Furthermore, in large-scale online production tests, the model drove a statistically significant +0.35% improvement in our 1st-tier downstream use cases metric.

## Metadata
- **Published**: 2026-09-03T23:29:15Z
- **Authors**: Avinash Kadimisetty, Andy Jinqing Yu, Philip Favaloro, Wenlong Liu, Xiaolu Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04559v1)